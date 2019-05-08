from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput


class UserSignUpForm(UserCreationForm):
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'nickname'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'e-mail'}))
    password = forms.CharField(max_length=100, required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'password'}))

    class Meta:
        model = User
        UserCreationFormFields = ('username', 'email', 'password')
        exclude = []


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'nickname'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password'}))

    class Meta:
        model = AuthenticationForm
        AuthenticationFormFields = ('username', 'password')