from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Publications, Tutor, Subject, City
from localflavor.pl.forms import PLPostalCodeField


class RegisterForm(UserCreationForm):
    # form to create new user
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "first_name", "last_name"]


class TutorForm(ModelForm):
    # form to add tutor details
    class Meta:
        model = Tutor
        fields = ('user', 'experience', 'phone', 'facebook_url')


class PublicationForm(ModelForm):
    # form to add new publications
    class Meta:
        model = Publications
        fields = ('price', 'subject', 'tutor', 'city')


class SubjectForm(ModelForm):
    # form to add new subject
    subject = forms.ChoiceField(choices=Subject.SUBJECTS)

    class Meta:
        model = Subject
        fields = ('subject',)


class AddCityForm(ModelForm):
    # form to add new city
    postcode = PLPostalCodeField()

    class Meta:
        model = City
        fields = ('city', 'postcode')
