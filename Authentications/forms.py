# forms.py
from django import forms
from .models import CustomUser

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    Contact = forms.CharField(widget=forms.TextInput(attrs={'autocomplete': 'off'}))

    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','email','Contact']  # Add other fields as needed
class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email Address',}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password','autocomplete': 'off'}))
    
class forget_passwordForm(forms.Form):
    email = forms.EmailField()

class Changepassword(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter New Password', 'auto_complete':'off'}))