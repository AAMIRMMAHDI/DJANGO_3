# Generated by Django 5.0.13 on 2025-03-20 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0027_alter_contactmessage_options_alter_order_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={},
        ),
        migrations.AlterModelOptions(
            name='cartitem',
            options={},
        ),
        migrations.AlterModelOptions(
            name='contactmessage',
            options={'verbose_name_plural': 'Call messages'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name_plural': 'Orders'},
        ),
        migrations.AlterModelOptions(
            name='orderitem',
            options={},
        ),
    ]
