from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام دسته')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name='دسته والد')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


from django.db import models

class ab(models.Model):
    image = models.ImageField(upload_to='abs/', verbose_name='تصویر')  # اضافه کردن فیلد تصویر

    def __str__(self):
        return self.image.name  # بازگرداندن نام فایل تصویر به عنوان رشته

    class Meta:
        verbose_name_plural = 'Shop by Category'

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام محصول')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='دسته‌بندی')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='قیمت')
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='قیمت تخفیف')
    is_new = models.BooleanField(default=False, verbose_name='محصول جدید')
    image = models.ImageField(upload_to='products/', verbose_name='تصویر')
    description = models.TextField(verbose_name='توضیحات')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Products'


from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"

    class Meta:
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"



from django.db import models
from django.contrib.auth.models import User
from .models import Product  # مدل محصولات شما

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='کاربر')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    def __str__(self):
        return f"سبد خرید کاربر {self.user.username}"

    class Meta:
        verbose_name_plural = 'سبدهای خرید'

from django.db import models
from .models import Product, Cart

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name='سبد خرید')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    quantity = models.PositiveIntegerField(default=1, verbose_name='تعداد')

    def __str__(self):
        return f"{self.quantity} عدد {self.product.name} در سبد خرید"

    class Meta:
        verbose_name_plural = 'آیتم‌های سبد خرید'




from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_images/', default='profile_images/default_profile.png')

    def __str__(self):
        return f'{self.user.username} Profile'




from django.db import models

class User(models.Model):
    phone = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=128)
    verification_code = models.CharField(max_length=4, blank=True, null=True)
    is_verified = models.BooleanField(default=False)





from django.db import models
from django.contrib.auth.models import User
from .models import Product

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='جمع کل')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    status = models.CharField(max_length=20, choices=[
        ('pending', 'در حال انتظار'),
        ('completed', 'تکمیل شده'),
        ('canceled', 'لغو شده'),
    ], default='pending', verbose_name='وضعیت')

    # فیلدهای جدید برای اطلاعات فرم پرداخت
    full_name = models.CharField(max_length=255, verbose_name='نام کامل')
    address = models.TextField(verbose_name='آدرس')
    phone = models.CharField(max_length=15, verbose_name='تلفن')

    def __str__(self):
        return f"سفارش #{self.id} توسط {self.user.username}"

    class Meta:
        verbose_name_plural = 'Orders'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='سفارش')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    quantity = models.PositiveIntegerField(verbose_name='تعداد')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='قیمت')

    def __str__(self):
        return f"{self.quantity} عدد {self.product.name} در سفارش #{self.order.id}"

    class Meta:
        verbose_name_plural = 'آیتم‌های سفارش'