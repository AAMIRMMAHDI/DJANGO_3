# Generated by Django 4.2 on 2025-03-11 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0003_contactmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmessage',
            name='is_new',
            field=models.BooleanField(default=False, verbose_name='محصول جدید'),
        ),
    ]
