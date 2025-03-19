from django.shortcuts import render, redirect
from .models import Category, Product, ContactMessage  # اضافه کردن ContactMessage
from .forms import ContactForm
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from .models import Product

from django.shortcuts import render
from .models import Product, Category, ab

def home(request):
    categories = Category.objects.all()  # دریافت تمام دسته‌بندی‌ها
    abs = ab.objects.all()  # دریافت تمام دسته‌بندی‌ها
    products = Product.objects.all()  # دریافت تمام محصولات

    context = {
        'categories': categories,
        'products': products,
        'abs': abs,  # اضافه کردن متغیر abs به context
    }
    return render(request, 'root/index.html', context)


def login(request):
    return render(request, "form/login.html")

def about(request):
    return render(request, "root/about.html")


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





from django.shortcuts import render
from .models import Product, Category

def product_list(request):
    categories = Category.objects.all()  # دریافت تمام دسته‌بندی‌ها
    selected_category = request.GET.get('category')  # دریافت دسته‌بندی انتخاب‌شده از URL

    if selected_category:
        products = Product.objects.filter(category__id=selected_category)  # فیلتر محصولات بر اساس دسته‌بندی
    else:
        products = Product.objects.all()  # نمایش تمام محصولات اگر دسته‌بندی انتخاب نشده باشد

    context = {
        'categories': categories,
        'products': products,
        'selected_category': selected_category,
    }
    return render(request, 'page/product_list.html', context)



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

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required  # اضافه کردن این خط
from .models import Product, Cart, CartItem

# سایر ویوها...

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))  # دریافت مقدار quantity از فرم

    # ایجاد یا دریافت سبد خرید کاربر
    cart, created = Cart.objects.get_or_create(user=request.user)

    # ایجاد یا دریافت آیتم سبد خرید
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not item_created:
        cart_item.quantity += quantity  # افزایش مقدار quantity به جای مقدار ثابت 1
    else:
        cart_item.quantity = quantity  # اگر آیتم جدید است، مقدار quantity را تنظیم کنید

    cart_item.save()  # ذخیره تغییرات

    return redirect('root:cart')  # هدایت به صفحه سبد خرید

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    cart_item.delete()  # حذف آیتم از سبد خرید
    return redirect('root:cart')  # هدایت به صفحه سبد خرید

# سایر ویوها...



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
    return render(request, 'page/profile.html', {'form': form})


from django.contrib.auth import logout

@login_required
def logout_view(request):
    logout(request)
    return redirect('root:home')  # پس از خروج، کاربر به صفحه اصلی هدایت می‌شود











from django.http import JsonResponse
from django.db.models import Q
from .models import Product

from django.http import JsonResponse
from django.db.models import Q
from .models import Product

def search_products(request):
    query = request.GET.get('q', '')  # دریافت عبارت جستجو
    if query:
        # جستجو در نام و توضیحات محصولات
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
    else:
        products = []

    # تبدیل نتایج به فرمت JSON
    results = [{
        'id': product.id,
        'name': product.name,
        'url': product.get_absolute_url(),  # لینک صفحه محصول
        'image': product.image.url if product.image else '',
    } for product in products]

    return JsonResponse(results, safe=False)



































import random
from django.core.mail import send_mail

def send_verification_code(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.filter(email=email).first()
        if user:
            # تولید کد تأیید
            verification_code = random.randint(1000, 9999)
            request.session['verification_code'] = verification_code
            request.session['email'] = email

            # ارسال ایمیل (در کنسول نمایش داده می‌شود)
            send_mail(
                'کد تأیید تغییر رمز عبور',  # موضوع ایمیل
                f'کد تأیید شما: {verification_code}',  # متن ایمیل
                'amirmahdibasiri555@gmail.com',  # ایمیل فرستنده
                [email],  # ایمیل گیرنده
                fail_silently=False,
            )
            return redirect('root:verify_code')
        else:
            messages.error(request, 'ایمیل وارد شده در سیستم وجود ندارد.')
    return render(request, 'page/change_password.html')


from django.contrib.auth import update_session_auth_hash

def verify_code(request):
    if request.method == 'POST':
        verification_code = request.POST.get('verification_code')
        if verification_code == str(request.session.get('verification_code')):
            return redirect('root:set_new_password')
        else:
            messages.error(request, 'کد تأیید نامعتبر است.')
    return render(request, 'page/verify_code.html')

def set_new_password(request):
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        if new_password == confirm_password:
            email = request.session.get('email')
            user = User.objects.get(email=email)
            user.set_password(new_password)
            user.save()
            update_session_auth_hash(request, user)  # به‌روزرسانی session برای جلوگیری از خروج کاربر
            messages.success(request, 'رمز عبور شما با موفقیت تغییر کرد.')
            return redirect('root:profile')
        else:
            messages.error(request, 'رمز عبور و تکرار آن مطابقت ندارند.')
    return render(request, 'page/set_new_password.html')







from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem, Order, OrderItem

@login_required
def checkout(request):
    cart = Cart.objects.filter(user=request.user).first()
    cart_items = CartItem.objects.filter(cart=cart) if cart else []
    total_price = sum(item.product.price * item.quantity for item in cart_items)

    if request.method == 'POST':
        # ایجاد سفارش جدید
        order = Order.objects.create(
            user=request.user,
            total_price=total_price,
            status='pending'
        )

        # افزودن آیتم‌های سبد خرید به سفارش
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )

        # پاک کردن سبد خرید
        cart_items.delete()

        return redirect('root:order_confirmation', order_id=order.id)

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'form/checkout.html', context)

@login_required
def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'form/order_confirmation.html', {'order': order})



@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'form/order_history.html', {'orders': orders})




@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    order_items = order.orderitem_set.all()  # دریافت آیتم‌های سفارش
    return render(request, 'form/order_detail.html', {'order': order, 'order_items': order_items})