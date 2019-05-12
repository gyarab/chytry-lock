from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserSignUpForm(UserCreationForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'nickname'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'e-mail'}))
    password1 = forms.CharField(max_length=100, required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'password'}))
    password2 = forms.CharField(max_length=100, required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'password again'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        exclude = []


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100, widget=forms.widgets.TextInput(attrs={'placeholder': 'nickname'}))
    password = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'password'}))

    class Meta:
        model = AuthenticationForm
        AuthenticationFormFields = ('username', 'password')
        exclude = []