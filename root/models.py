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
    is_new = models.BooleanField(default=False, verbose_name='محصول جدید')


    def __str__(self):
        return f"Message from {self.name} - {self.subject}"

    class Meta:
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"