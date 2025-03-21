# Generated by Django 5.0.13 on 2025-03-20 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0025_alter_ab_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ab',
            options={'verbose_name_plural': 'Shop by Category'},
        ),
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name_plural': 'سبدهای خرید'},
        ),
        migrations.AlterModelOptions(
            name='cartitem',
            options={'verbose_name_plural': 'آیتم\u200cهای سبد خرید'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name_plural': 'Orders'},
        ),
        migrations.AlterModelOptions(
            name='orderitem',
            options={'verbose_name_plural': 'آیتم\u200cهای سفارش'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'Products'},
        ),
    ]
