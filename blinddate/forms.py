from django.forms import ModelForm, ImageField, FileInput
from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from .models import Profile, Message


# Form for User Registration
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


# Form for Profile
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        user_img = ImageField(widget=FileInput)
        # fields = ["age","country","city","gender","looking_for_gender","about_me","user_foto"]
        exclude = ['clear']

# Form for Chat Messages
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["message"]
        labels = {"message": " "}