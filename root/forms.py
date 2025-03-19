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



from django import forms

class ChangePasswordForm(forms.Form):
    email = forms.EmailField(label='ایمیل', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    verification_code = forms.CharField(label='کد تأیید', widget=forms.TextInput(attrs={'class': 'form-control'}))
    new_password = forms.CharField(label='رمز عبور جدید', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(label='تکرار رمز عبور جدید', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
