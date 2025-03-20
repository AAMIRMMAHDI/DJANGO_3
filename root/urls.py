from django.urls import path
from .views import *

app_name = 'root'

urlpatterns = [
    # Home and Basic Pages
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('help/', x_page, name='x_page'),

    # Product Related URLs
    path('Catagori/', product_list, name='product_list'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
    path('search/', search_products, name='search_products'),

    # Cart Related URLs
    path('cart/', cart, name='cart'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('update-cart/', update_cart, name='update_cart'),
    path('remove-from-cart/<int:item_id>/', remove_from_cart, name='remove_from_cart'),

    # Order Related URLs
    path('checkout/', checkout, name='checkout'),
    path('order-confirmation/<int:order_id>/', order_confirmation, name='order_confirmation'),
    path('order-history/', order_history, name='order_history'),
    path('order-detail/<int:order_id>/', order_detail, name='order_detail'),

    # Authentication Related URLs
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),

    # Profile Related URLs
    path('profile/', profile, name='profile'),

    # Password Reset Related URLs
    path('change-password/', send_verification_code, name='change_password'),
    path('verify-code/', verify_code, name='verify_code'),
    path('set-new-password/', set_new_password, name='set_new_password'),

    # Contact
    path('contact/', contact, name='contact'),
]