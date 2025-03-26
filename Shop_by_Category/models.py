
from django.db import models

class ab(models.Model):
    image = models.ImageField(upload_to='abs/', verbose_name='تصویر')  # اضافه کردن فیلد تصویر

    def __str__(self):
        return self.image.name  # بازگرداندن نام فایل تصویر به عنوان رشته

    class Meta:
        verbose_name_plural = 'Shop by Category'
