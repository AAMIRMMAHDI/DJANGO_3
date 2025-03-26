from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

# Contact
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('Contact:contact')
        else:
            messages.error(request, 'Error sending the message. Please check the fields.')
    else:
        form = ContactForm()

    context = {
        'form': form,
    }
    return render(request, "root/contact.html", context)