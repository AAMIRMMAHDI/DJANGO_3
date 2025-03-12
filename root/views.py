from django.shortcuts import render, redirect
from .models import Category, Product, ContactMessage  # اضافه کردن ContactMessage
from .forms import ContactForm
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from .models import Product

def home(request):
    return render(request, "root/index.html")

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
from .models import Cart, CartItem

def cart(request):
    cart = Cart.objects.filter(user=request.user).first()  # دریافت سبد خرید کاربر
    cart_items = CartItem.objects.filter(cart=cart) if cart else []  # دریافت آیتم‌های سبد خرید

    # محاسبه جمع کل سبد خرید
    total_price = sum(item.product.price * item.quantity for item in cart_items)

    context = {
        'cart': cart,
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'page/cart.html', context)


from django.shortcuts import redirect
from .models import CartItem

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
from .models import Product, Cart, CartItem

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)  # اگر کاربر لاگین کرده باشد
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
    
    if not item_created:
        cart_item.quantity += 1  # اگر محصول از قبل در سبد خرید باشد، تعداد آن افزایش می‌یابد
        cart_item.save()
    
    return redirect('root:cart')  # کاربر به صفحه سبد خرید هدایت می‌شود



