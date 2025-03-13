from django.shortcuts import render, redirect
from .models import Category, Product, ContactMessage  # اضافه کردن ContactMessage
from .forms import ContactForm
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from .models import Product

def home(request):
    return render(request, "root/index.html")

def login(request):
    return render(request, "form/login.html")

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'پیام شما با موفقیت ارسال شد')  # پیام موفقیت
            return redirect('root:contact')  # ریدایرکت به همان صفحه
        else:
            messages.error(request, 'خطا در ارسال پیام ')  # پیام خطا
    else:
        form = ContactForm()

    context = {
        'form': form,
    }
    return render(request, "root/contact.html", context)

def product_list(request):
    categories = Category.objects.filter(parent__isnull=True)
    products = Product.objects.all()
    return render(request, 'root/Catagori.html', {'categories': categories, 'products': products})




def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)  # دریافت محصول بر اساس ID
    return render(request, 'page/product_detail.html', {'product': product})



from django.shortcuts import render
from .models import Cart ,CartItem

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem

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

from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import CartItem

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

from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Cart, CartItem

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
    
    if not item_created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect('root:cart')



from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'ورود موفقیت‌آمیز بود!')
            return redirect('root:home')  # تغییر به صفحه اصلی پس از ورود
        else:
            messages.error(request, 'نام کاربری یا رمز عبور اشتباه است.')
    
    return render(request, 'form/login.html')





from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # ایجاد کاربر جدید
        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = fullname
        user.save()
        
        messages.success(request, 'ثبت نام موفقیت‌آمیز بود!')
        return redirect('root:login')  # تغییر به صفحه ورود پس از ثبت نام
    
    return render(request, 'root/login.html')



from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm

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
    
    context = {
        'form': form,
    }
    return render(request, 'page/profile.html', context)


from django.contrib.auth import logout

@login_required
def logout_view(request):
    logout(request)
    return redirect('root:home')  # پس از خروج، کاربر به صفحه اصلی هدایت می‌شود