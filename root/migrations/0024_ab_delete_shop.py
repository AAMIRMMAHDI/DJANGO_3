# Generated by Django 5.0.13 on 2025-03-20 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0023_shop_delete_shop_by_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='ab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='abs/', verbose_name='تصویر')),
            ],
        ),
        migrations.DeleteModel(
            name='Shop',
        ),
    ]
