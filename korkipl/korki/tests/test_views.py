from django.test import TestCase, Client
from django.urls import reverse
from korki.models import Publications, Tutor, Subject, City
import pytest
from django.contrib.auth.models import User


# django-test that test user register view
@pytest.fixture
def new_user_one(db):
    def create_app_user(
            username: str,
            password: str = None,
            first_name: str = 'firstname',
            last_name: str = 'lastname',
            email: str = 'test@test.com',
            is_superuser: str = False,
            is_active: str = True,
    ):
        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
            is_superuser=is_superuser,
            is_active=is_active
        )
        return user
    return create_app_user


@pytest.fixture
def user_one(db, new_user_one):
    return new_user_one('testuser', 'password', 'somename', 'somelast', 'whatever@test.com', is_superuser='False',
                        is_active='True')


def test_new_user(user_one):
    assert user_one.username == 'testuser'
    # assert user_one.password == 'password'
    assert user_one.first_name == 'somename'
    assert user_one.last_name == 'somelast'
    assert user_one.email == 'whatever@test.com'
    assert user_one.is_superuser
    assert user_one.is_active
