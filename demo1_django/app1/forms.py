from django import forms
from . import models
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = models.User1
        fields = ('username', 'password', 'first_name', 'email')
