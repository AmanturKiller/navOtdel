from django import forms
from django.contrib.auth import get_user_model
from .models import *

User = get_user_model()

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name',]

class AuthForm(forms.Form):
    username = forms.CharField(max_length = 150)
    password = forms.CharField(widget = forms.PasswordInput)