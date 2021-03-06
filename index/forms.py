from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    profile_photo = forms.ImageField()
    email = forms.EmailField(max_length=200,  help_text='Required')
    first_name = forms.CharField(max_length=50, required='false', help_text='First Name')
    last_name = forms.CharField(max_length=50, required='false',help_text='Last Name')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
