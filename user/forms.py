from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username=forms.CharField(max_length=50,
                             widget=forms.TextInput(attrs={
        'class':'w-full  px-6 py-4 rounded-xl',
        'placeholder':'Enter your username'

                             }))
    password=forms.CharField(max_length=65, widget=forms.PasswordInput(attrs={
        'class':'w-full px-6 py-4 rounded-xl',
        'placeholder':'Enter password',
    }))





class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        field=['username','email','password1','password2']
        exclude = ("first_name", "last_name")
    username=forms.CharField(widget=forms.TextInput(attrs={
            'placeholder':'Enter Username',
            'class':'w-full px-6 py-4 rounded-xl',

        }))
    email=forms.EmailField(widget=forms.EmailInput(attrs={
            'placeholder':'Enter email address',
            'class':'w-full px-6 py-4 rounded-xl',
        }))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={
            'placeholder':'Enter Password',
            'class':'w-full px-6 py-4 rounded-xl',
        }))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={
            'placeholder':'Repeat Password',
            'class':'w-full px-6 py-4 rounded-xl'
        }))
