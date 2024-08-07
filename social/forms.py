from django import forms
from .models import User
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=250, required=True, widget=forms.TextInput, label='username or phone')
    password = forms.CharField(max_length=250, required=True, widget=forms.PasswordInput)
