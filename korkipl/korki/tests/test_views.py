from django.test import TestCase, Client
from django.urls import reverse
from korki.models import Publications, Tutor, Subject, City
import pytest
from django.contrib.auth.models import User


@pytest.fixture
def client():
    return Client()


class TestViews(TestCase):

    def test_tutor(self):
        response = self.client.get(reverse('tutor', args=['1']))
        self.assertEqual(response.status_code, 404) or (response.status_code, 200)

    def test_noticeboard(self):
        response = self.client.get(reverse('noticeboard'))
        self.assertEqual(response.status_code, 200)

    def test_homepage(self):
        response = self.client.get(reverse('homepage'))
        self.assertEqual(response.status_code, 200)

    def test_addtutorinfo(self):
        response = self.client.get(reverse('addtutorinfo'))
        self.assertEqual(response.status_code, 302)

    def test_addcity(self):
        response = self.client.get(reverse('addcity'))
        self.assertEqual(response.status_code, 302)

    def test_addsubject(self):
        response = self.client.get(reverse('addsubject'))
        self.assertEqual(response.status_code, 302)

    def test_addpublication(self):
        response = self.client.get(reverse('addsubject'))
        self.assertEqual(response.status_code, 302)
