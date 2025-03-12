from django.contrib import admin
from .models import Category, Product ,ContactMessage ,Cart ,CartItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'discount_price', 'is_new')


admin.site.register(ContactMessage)
admin.site.register(Cart)
admin.site.register(CartItem)

