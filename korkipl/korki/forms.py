from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Publications, Tutor, Subject
from localflavor.pl.forms import PLPostalCodeField


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "first_name", "last_name"]


class TutorForm(ModelForm):
    class Meta:
        model = Tutor
        fields = ('user', 'experience', 'phone', 'facebook_url')


class PublicationForm(ModelForm):
    subject = forms.ChoiceField(choices=Subject.SUBJECTS)

    class Meta:
        model = Publications
        fields = ('price', 'subject', 'tutor', 'city')


class CityForm(forms.Form):
    city = forms.CharField(max_length=30)
    postcode = PLPostalCodeField()
