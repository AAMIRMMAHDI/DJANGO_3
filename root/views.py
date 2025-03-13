from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from .models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Q
from .models import Category, Product, ContactMessage, Cart, CartItem, Profile, User
from .forms import ContactForm, ProfileForm
import kavenegar
import random

def home(request):
    return render(request, "root/index.html")

def about(request):
    return render(request, "root/about.html")

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'پیام شما با موفقیت ارسال شد')
            return redirect('root:contact')
        else:
            messages.error(request, 'خطا در ارسال پیام')
    else:
        form = ContactForm()

    context = {'form': form}
    return render(request, "root/contact.html", context)

def product_list(request):
    categories = Category.objects.filter(parent__isnull=True)
    products = Product.objects.all()
    return render(request, 'root/Catagori.html', {'categories': categories, 'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'page/product_detail.html', {'product': product})

@login_required
def cart(request):
    cart = Cart.objects.filter(user=request.user).first()
    cart_items = CartItem.objects.filter(cart=cart) if cart else []
    total_price = sum(item.product.price * item.quantity for item in cart_items)

    context = {
        'cart': cart,
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'page/cart.html', context)

@login_required
def update_cart(request):
    if request.method == 'POST':
        for key, value in request.POST.items():
            if key.startswith('quantity_'):
                item_id = key.replace('quantity_', '')
                cart_item = CartItem.objects.get(id=item_id)
                cart_item.quantity = int(value)
                cart_item.save()
    return redirect('root:cart')

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
    
    if not item_created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect('root:cart')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            phone = form.cleaned_data.get('phone')
            password = form.cleaned_data.get('password')
            user = authenticate(request, phone=phone, password=password)
            if user is not None:
                verification_code = send_verification_code(user.phone)
                user.verification_code = verification_code
                user.save()
                messages.success(request, 'کد تایید به شماره شما ارسال شد.')
                return redirect('root:verify', phone=user.phone)
            else:
                messages.error(request, 'شماره موبایل یا رمز عبور اشتباه است.')
        else:
            messages.error(request, 'خطا در ورود')
    else:
        form = LoginForm()

    return render(request, 'root/login.html', {'form': form})
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            verification_code = send_verification_code(user.phone)
            user.verification_code = verification_code
            user.save()
            messages.success(request, 'کد تایید به شماره شما ارسال شد.')
            return redirect('root:verify', phone=user.phone)
        else:
            messages.error(request, 'خطا در ثبت نام')
    else:
        form = RegisterForm()

    return render(request, 'root/register.html', {'form': form})

@login_required
def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('root:profile')
    else:
        form = ProfileForm(instance=profile)
    
    context = {'form': form}
    return render(request, 'page/profile.html', context)

@login_required
def logout_view(request):
    logout(request)
    return redirect('root:home')

def search_products(request):
    query = request.GET.get('q', '')
    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
    else:
        products = []

    results = [{
        'id': product.id,
        'name': product.name,
        'url': product.get_absolute_url(),
        'image': product.image.url if product.image else '',
    } for product in products]

    return JsonResponse(results, safe=False)

def send_verification_code(phone):
    api = kavenegar.KavenegarAPI('YOUR_API_KEY')
    verification_code = random.randint(1000, 9999)
    params = {
        'sender': '10004346',
        'receptor': phone,
        'message': f'کد تایید شما: {verification_code}'
    }
    response = api.sms_send(params)
    return verification_code


def verify_view(request, phone):
    if request.method == 'POST':
        code = request.POST.get('code')
        user = User.objects.filter(phone=phone, verification_code=code).first()
        if user:
            user.is_verified = True
            user.save()
            login(request, user)
            messages.success(request, 'ورود موفقیت‌آمیز بود!')
            return redirect('root:home')
        else:
            messages.error(request, 'کد تایید اشتباه است.')

    return render(request, 'root/verify.html', {'phone': phone})