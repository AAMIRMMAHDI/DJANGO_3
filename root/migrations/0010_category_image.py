# Generated by Django 4.2 on 2025-03-19 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0009_user_alter_product_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default='', upload_to='categories/', verbose_name='تصویر'),
            preserve_default=False,
        ),
    ]
