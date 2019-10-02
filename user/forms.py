from django import forms

from .validators import UsernameUniqueValidator


class Login(forms.Form):
    username = forms.CharField(max_length=32, label="Username")
    password = forms.CharField(max_length=128, widget=forms.PasswordInput, label='Password')

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=32, label="Username", validators=[UsernameUniqueValidator])
    password = forms.CharField(max_length=128, widget=forms.PasswordInput, label="Password")
    email = forms.EmailField(max_length=64, label="E-Mail", required=False)
    phone_number = forms.CharField(max_length=16, label='Phone number', required=False)
    age = forms.IntegerField(required=False)