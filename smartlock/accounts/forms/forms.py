from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Required. Please enter a valid e-mail address.')
    email = forms.EmailField(required=True, widget=TextInput(attrs={'class': 'span2', 'placeholder': 'e-mail'}), help_text='Required. Please enter a valid e-mail address.')

    class Meta:
        model = UserCreationFormFields = ('username', 'email', 'password1', 'password2',)


class AuthForm(AuthenticationForm):
    class Meta:
        model = AuthenticationForm
        fields = '__all__'

        def __init__(self, *args, **kwargs):
            super(AuthenticationForm, self).__init__(*args, **kwargs)

            for field in self.fields.values():
                field.error_messages = {'required': '{fieldname} is required'.format(fieldname=field.label)}

    username = forms.CharField(widget=TextInput(attrs={'placeholder': 'nickname'})),
    email = forms.CharField(widget=TextInput(attrs={'placeholder': 'e-mail'})),
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'password'}))