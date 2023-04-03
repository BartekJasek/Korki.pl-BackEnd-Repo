from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


# Create your models here.


class Tutor(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    experience = models.CharField(max_length=2000)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    facebook_url = models.URLField(max_length=500)

    def __str__(self):
        return self.user


class Subject(models.Model):
    SUBJECTS = (
        ("matematyka", "matematyka"),
        ("j. polski", "j. polski"),
        ("j. angielski", "j. angielski"),
        ("biologia", "biologia"),
        ("chemia", "chemia"),
        ("fizyka", "fizyka"),
        ("historia", "historia"),
        ("geografia", "geografia"),
        ("wiedza o społeczeństwie", "wiedza o społeczeństwie"),
        ("informatyka", "informatyka"),
        ("j. hiszpańśki", "j. hiszpańśki"),
        ("j. rosysjki", "j. rosysjki"),
        ("j. niemiecki", "j. niemiecki"),
    )
    subject = models.IntegerField(choices=SUBJECTS)


class Calendar(models.Model):
    date = models.DateTimeField


class City(models.Model):
    city = models.CharField(max_length=30)
    postcode = models.CharField(max_length=6)

    def __str__(self):
        return self.city


class Publications(models.Model):
    price = models.IntegerField()
    subject = models.ManyToManyField(Subject)
    tutor = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.OneToOneField(City, on_delete=models.CASCADE)
