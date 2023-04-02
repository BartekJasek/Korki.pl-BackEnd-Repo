from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    experience = forms.CharField(max_length=1280, required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "first_name", "last_name", "experience"]


class Publications(forms.Form):
    price = forms.IntegerField()
