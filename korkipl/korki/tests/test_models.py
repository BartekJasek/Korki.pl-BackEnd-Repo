import pytest

from django.contrib.auth.models import User
from korki.models import Publications, Tutor, Subject, City


@pytest.mark.django_db
def test_user_create():
    User.objects.create_user(username='testuser', email='test@test.com', first_name='User', last_name='Test')


@pytest.mark.django_db
def test_tutor_create():
    testuser = User.objects.create(username='test', email='test@test.pl', first_name='test', last_name='test')
    Tutor.objects.create(user=testuser, experience='Uczeń Coderslab', phone='+48510145370',
                         facebook_url='https://github.com/BartekJasek/Korki.pl-BackEnd-Repo!')


@pytest.mark.django_db
def test_subject_create():
    Subject.objects.create(subject='matematyka')


@pytest.mark.django_db
def test_city_create():
    City.objects.create(city='Kielce', postcode='25-004')


@pytest.mark.django_db
def test_publication_create():
    testuser = User.objects.create(username='test', email='test@test.pl', first_name='test', last_name='test')
    testcity = City.objects.create(city='Kielce', postcode='25-004')
    testsubject = Subject.objects.create(subject='biologia')
    publication = Publications.objects.create(price='120', tutor=testuser, city=testcity)
    publication.subject.set([testsubject])
