from django import forms
from .models import Tutor, Publications, City, Subject
from django.forms import ModelForm


class Tutor(forms.Form):
    name = forms.CharField(max_length=64)
    surname = forms.CharField(max_length=64)
    experience = forms.CharField(max_length=2000)
    contact = forms.IntegerField()


class Publications(forms.Form):
    price = forms.IntegerField
