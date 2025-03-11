from django.shortcuts import render, redirect
from .models import Category, Product, ContactMessage  # اضافه کردن ContactMessage
from .forms import ContactForm
from django.contrib import messages

def home(request):
    return render(request, "root/index.html")

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'پیام شما با موفقیت ارسال شد')  # پیام موفقیت
            return redirect('root:contact')  # ریدایرکت به همان صفحه
        else:
            messages.error(request, 'خطا در ارسال پیام ')  # پیام خطا
    else:
        form = ContactForm()

    context = {
        'form': form,
    }
    return render(request, "root/contact.html", context)

def product_list(request):
    categories = Category.objects.filter(parent__isnull=True)
    products = Product.objects.all()
    return render(request, 'root/Catagori.html', {'categories': categories, 'products': products})