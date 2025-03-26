from django.urls import path
from .views import contact

app_name = 'Contact'

urlpatterns = [
    # Contact
    path('contact/', contact, name='contact'),
]