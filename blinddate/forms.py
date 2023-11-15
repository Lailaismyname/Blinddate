from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from .models import *

class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-field'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password','class': 'form-field'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',  'class': 'form-field'}))

    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Emailadress', 'class': 'form-field'}))
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-field'}))
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-field'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email', 'password1', 'password2']