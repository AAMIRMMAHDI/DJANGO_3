from django import forms
from .models import  Profile


# Profile Form
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

# Change Password Form
class ChangePasswordForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    verification_code = forms.CharField(
        label='Verification Code',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    new_password = forms.CharField(
        label='New Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    confirm_password = forms.CharField(
        label='Confirm New Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )