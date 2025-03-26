from django import forms
from .models import ContactMessage


# Contact Form
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email address'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control w-100', 'rows': 9, 'placeholder': 'Enter message'}),
        }