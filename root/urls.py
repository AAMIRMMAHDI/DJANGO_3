from django.urls import path
from .views import home, product_list ,contact 
app_name = 'root' 

urlpatterns = [
    path('', home, name='home'),
    path('Catagori/', product_list, name='product_list'),
    path('contact/', contact, name='contact'),

]