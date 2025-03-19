from django.urls import path
from .views import *

app_name = 'root'

urlpatterns = [
    path('', home, name='home'),
    path('Catagori/', product_list, name='product_list'),
    path('contact/', contact, name='contact'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart, name='cart'),
    path('update-cart/', update_cart, name='update_cart'),  
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('profile/', profile, name='profile'),
    path('logout/', logout_view, name='logout'),  # اضافه کردن این خط
    path('about/', about, name='about'),  # اضافه کردن این خط
    path('search/', search_products, name='search_products'),  # اضافه کردن این خط
    path('remove-from-cart/<int:item_id>/', remove_from_cart, name='remove_from_cart'),  # مسیر جدید
    path('change-password/', send_verification_code, name='change_password'),
    path('verify-code/', verify_code, name='verify_code'),
    path('set-new-password/', set_new_password, name='set_new_password'),
    path('checkout/', checkout, name='checkout'),
    path('order-confirmation/<int:order_id>/', order_confirmation, name='order_confirmation'),
    path('order-history/', order_history, name='order_history'),
    path('order-detail/<int:order_id>/', order_detail, name='order_detail'),


]
