from django import forms
from .models import *


from django import forms
from .models import ContactMessage

from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email address'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control w-100', 'rows': 9, 'placeholder': 'Enter Message'}),
        }


from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']