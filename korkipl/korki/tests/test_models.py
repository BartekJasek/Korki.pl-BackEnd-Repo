import pytest

from django.contrib.auth.models import User
from korki.models import Publications, Tutor, Subject, City


@pytest.mark.django_db
def user_create():
    User.objects.create_user(username='testuser', email='test@test.com', password1='T3stow3hasl!',
                             password2='T3stow3hasl!', first_name='User', last_name='Test')


@pytest.mark.django_db
def tutor_create():
    Tutor.objects.create(user='testuser', experience='Uczeń Coderslab', phone='+48510145370',
                         facebook_url='https://github.com/BartekJasek/Korki.pl-BackEnd-Repo!')


@pytest.mark.django_db
def subject_create():
    Subject.objects.create(subject='matematyka')


@pytest.mark.django_db
def city_create():
    City.objects.create(city='Kielce', postcode='25-004')
