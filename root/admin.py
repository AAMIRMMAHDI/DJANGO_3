from django.contrib import admin
from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'discount_price', 'is_new')

from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0  # تعداد فرم‌های خالی برای اضافه کردن آیتم‌ها
    readonly_fields = ('product', 'quantity', 'price')  # فیلدهای فقط خواندنی

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_price', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('user__username', 'id')
    inlines = [OrderItemInline]  # نمایش آیتم‌های سفارش در صفحه ویرایش سفارش
    readonly_fields = ('user', 'total_price', 'created_at')  # فیلدهای فقط خواندنی

    # نمایش جزئیات سفارش در صفحه ویرایش
    fieldsets = (
        ('اطلاعات سفارش', {
            'fields': ('user', 'total_price', 'status', 'created_at')
        }),
    )


admin.site.register(ab)
admin.site.register(ContactMessage)

