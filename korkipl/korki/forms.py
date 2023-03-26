from django import forms
from .models import Tutor, Publications, City
from django.forms import ModelForm


class Tutor(forms.Form):
    nameandsurname = forms.CharField(max_length=64)
    experience = forms.CharField
    contact = forms.IntegerField(max_length=9)


class Publications(forms.Form):
    price = forms.IntegerField
    subject = forms.ManyToManyField(Subject, through="Przedmiot")
    name = forms.ForeignKey(Tutor, on_delete=forms.CASCADE)
    city = forms.OneToOneField(City, through="Przedmiot", on_delete=forms.CASCADE)
