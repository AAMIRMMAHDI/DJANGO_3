from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import JsonResponse
from django.db.models import Q
import random
from .models import Category, Product, ContactMessage, Cart, CartItem, Order, OrderItem, Profile, ab
from .forms import ContactForm, ProfileForm

# Home and Basic Pages
def home(request):
    categories = Category.objects.all()
    abs = ab.objects.all()
    products = Product.objects.all()

    context = {
        'categories': categories,
        'products': products,
        'abs': abs,
    }
    return render(request, 'root/index.html', context)

def about(request):
    return render(request, "root/about.html")

def x_page(request):
    return render(request, 'root/help.html')

# Contact
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('root:contact')
        else:
            messages.error(request, 'Error sending the message. Please check the fields.')
    else:
        form = ContactForm()

    context = {
        'form': form,
    }
    return render(request, "root/contact.html", context)

# Product Related Views
def product_list(request):
    categories = Category.objects.all()
    selected_category = request.GET.get('category')
    query = request.GET.get('q')

    products = Product.objects.all()
    
    if selected_category:
        products = products.filter(category__id=selected_category)
    
    if query:
        products = products.filter(name__icontains=query)

    context = {
        'categories': categories,
        'products': products,
        'selected_category': selected_category,
        'query': query,
    }
    return render(request, 'root/product_list.html', context)

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'page/product_detail.html', {'product': product})

def search_products(request):
    query = request.GET.get('q', '')
    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query))
    else:
        products = []

    results = [{
        'id': product.id,
        'name': product.name,
        'url': product.get_absolute_url(),
        'image': product.image.url if product.image else '',
    } for product in products]

    return JsonResponse(results, safe=False)

# Cart Related Views
def cart(request):
    if not request.user.is_authenticated:
        return redirect('root:x_page')  # Redirect to x.html if user is not logged in

    cart = Cart.objects.filter(user=request.user).first()
    cart_items = CartItem.objects.filter(cart=cart) if cart else []
    total_price = sum(item.product.price * item.quantity for item in cart_items)

    context = {
        'cart': cart,
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'root/cart.html', context)

def add_to_cart(request, product_id):
    if not request.user.is_authenticated:
        return redirect('root:x_page')  
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not item_created:
        cart_item.quantity += quantity
    else:
        cart_item.quantity = quantity
    cart_item.save()
    return redirect('root:cart')

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
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    cart_item.delete()
    return redirect('root:cart')

# Order Related Views
def checkout(request):
    if not request.user.is_authenticated:
        return redirect('root:x_page')  # Redirect to x.html if user is not logged in

    cart = Cart.objects.filter(user=request.user).first()
    cart_items = CartItem.objects.filter(cart=cart) if cart else []
    total_price = sum(item.product.price * item.quantity for item in cart_items)

    if request.method == 'POST':
        order = Order.objects.create(
            user=request.user,
            total_price=total_price,
            status='pending'
        )

        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )

        cart_items.delete()
        return redirect('root:order_confirmation', order_id=order.id)

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'form/checkout.html', context)

def order_confirmation(request, order_id):
    if not request.user.is_authenticated:
        return redirect('root:x_page')  # Redirect to x.html if user is not logged in

    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'form/order_confirmation.html', {'order': order})

def order_history(request):
    if not request.user.is_authenticated:
        return redirect('root:x_page')  # Redirect to x.html if user is not logged in

    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'form/order_history.html', {'orders': orders})

def order_detail(request, order_id):
    if not request.user.is_authenticated:
        return redirect('root:x_page')  # Redirect to x.html if user is not logged in

    order = get_object_or_404(Order, id=order_id, user=request.user)
    order_items = order.orderitem_set.all()
    return render(request, 'form/order_detail.html', {'order': order, 'order_items': order_items})

# Authentication Related Views
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('root:home')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'form/login.html')

def register_view(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = fullname
        user.save()
        
        messages.success(request, 'Registration successful!')
        return redirect('root:login')
    
    return render(request, 'root/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('root:home')

# Profile Related Views
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
    return render(request, 'page/profile.html', {'form': form})

# Password Reset Related Views
def send_verification_code(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.filter(email=email).first()
        if user:
            verification_code = random.randint(1000, 9999)
            request.session['verification_code'] = verification_code
            request.session['email'] = email

            send_mail(
                'Password Reset Verification Code',
                f'Your verification code is: {verification_code}',
                'your_email@example.com',
                [email],
                fail_silently=False,
            )
            return redirect('root:verify_code')
        else:
            messages.error(request, 'The email does not exist in our system.')
    return render(request, 'page/change_password.html')

def verify_code(request):
    if request.method == 'POST':
        verification_code = request.POST.get('verification_code')
        if verification_code == str(request.session.get('verification_code')):
            return redirect('root:set_new_password')
        else:
            messages.error(request, 'Invalid verification code.')
    return render(request, 'page/verify_code.html')

def set_new_password(request):
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        if new_password == confirm_password:
            email = request.session.get('email')
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                messages.error(request, 'User not found.')
                return redirect('root:set_new_password')
            user.set_password(new_password)
            user.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password has been changed successfully!')
            return redirect('root:login')  
        else:
            messages.error(request, 'Passwords do not match.')
    
    return render(request, 'page/set_new_password.html')