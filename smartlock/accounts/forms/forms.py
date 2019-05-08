from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput


class UserSignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True, widget=TextInput(attrs={'placeholder': 'nickname'})),
    email = forms.EmailField(required=True, widget=TextInput(attrs={'placeholder': 'e-mail'}),
                             help_text='Required. Please enter a valid e-mail address.')
    password = forms.CharField(max_length=100, required=True, widget=TextInput(attrs={'placeholder': 'password'})),

    class Meta:
        model = User
        UserCreationFormFields = ('username', 'email', 'password')
        exclude = []


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'placeholder': 'nickname'})),
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder': 'password'})),

    class Meta:
        model = AuthenticationForm
        fields = ('username', 'password')
        exclude = []

        def __init__(self, *args, **kwargs):
            super(AuthenticationForm, self).__init__(*args, **kwargs)

            for field in self.fields.values():
                field.error_messages = {'required': '{fieldname} is required'.format(fieldname=field.label)}