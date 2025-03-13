from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام دسته')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name='دسته والد')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'دسته'
        verbose_name_plural = 'دسته‌ها'

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام محصول')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='دسته')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='قیمت')
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='قیمت تخفیف')
    image = models.ImageField(upload_to='products/', verbose_name='تصویر')
    is_new = models.BooleanField(default=False, verbose_name='محصول جدید')
    description = models.TextField(verbose_name='توضیحات', blank=True, null=True)  

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'



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
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبدهای خرید'

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name='سبد خرید')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    quantity = models.PositiveIntegerField(default=1, verbose_name='تعداد')

    def __str__(self):
        return f"{self.quantity} عدد {self.product.name} در سبد خرید"

    class Meta:
        verbose_name = 'آیتم سبد خرید'
        verbose_name_plural = 'آیتم‌های سبد خرید'




from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='کاربر')
    image = models.ImageField(upload_to='profile_images/', verbose_name='تصویر پروفایل', default='profile_images/default.jpg')

    def __str__(self):
        return f"پروفایل کاربر {self.user.username}"

    class Meta:
        verbose_name = 'پروفایل'
        verbose_name_plural = 'پروفایل‌ها'