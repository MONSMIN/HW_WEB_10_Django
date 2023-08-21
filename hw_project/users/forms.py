from django import forms
from django.forms import ModelForm, CharField, TextInput, EmailField, EmailInput, PasswordInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegisterForm(UserCreationForm):
    username = CharField(max_length=16, required=True,
                         widget=TextInput(attrs={"class": "form-control"}))
    email = CharField(max_length=16, required=True,
                      widget=EmailInput(attrs={"class": "form-control"}))
    password1 = CharField(max_length=16, min_length=6, required=True,
                          widget=PasswordInput(attrs={"class": "form-control"}))
    password2 = CharField(max_length=16, min_length=6, required=True,
                          widget=PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.TextInput(attrs={"class": "form-control"}))

    password = forms.CharField(max_length=20,
                               required=True,
                               widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ['username', 'password']
