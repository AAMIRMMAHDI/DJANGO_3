from django.urls import path
from .views import (
    home, product_list, contact, product_detail, add_to_cart, cart, update_cart,
    login_view, register_view, profile, logout_view, about, search_products
)

app_name = 'root'

urlpatterns = [
    path('', home, name='home'),
    path('Catagori/', product_list, name='product_list'),
    path('contact/', contact, name='contact'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart, name='cart'),
    path('update-cart/', update_cart, name='update_cart'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('verify/<str:phone>/', verify_view, name='verify'),
    path('profile/', profile, name='profile'),
    path('logout/', logout_view, name='logout'),
    path('about/', about, name='about'),
    path('search/', search_products, name='search_products'),
]