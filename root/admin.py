from django.contrib import admin
from .models import Category, Product, Order, OrderItem

# Category Admin
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')

# Product Admin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'discount_price', 'is_new')

# Order Item Inline
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0  
    readonly_fields = ('product', 'quantity', 'price')  

# Order Admin
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_price', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('user__username', 'id')
    inlines = [OrderItemInline]  
    readonly_fields = ('user', 'total_price', 'created_at')  


    fieldsets = (
        ('Order Information', {
            'fields': ('user', 'total_price', 'status', 'created_at')
        }),
    )

