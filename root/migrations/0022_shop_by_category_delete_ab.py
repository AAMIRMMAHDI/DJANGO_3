# Generated by Django 5.0.13 on 2025-03-20 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0021_order_address_order_full_name_order_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop_by_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Shop_by_Categorys/', verbose_name='تصویر')),
            ],
        ),
        migrations.DeleteModel(
            name='ab',
        ),
    ]
