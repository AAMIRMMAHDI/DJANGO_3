# Generated by Django 4.2 on 2025-03-19 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0011_ab'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ab',
            name='image',
            field=models.ImageField(upload_to='abs/', verbose_name='تصویر'),
        ),
    ]
