from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User
from django import forms
from .models import User_changes
class RegistrationForm(UserCreationForm):
    email=forms.EmailField()
    phone=forms.IntegerField()
    class Meta:
        model=User_changes
        fields=['username','email','phone','cell','password1','password2']