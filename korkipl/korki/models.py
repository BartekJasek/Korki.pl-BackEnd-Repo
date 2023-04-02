from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


# Create your models here.

SUBJECTS = (
    (1, "matematyka"),
    (2, "j. polski"),
    (3, "j. angielski"),
    (4, "biologia"),
    (5, "chemia"),
    (6, "fizyka"),
    (7, "historia"),
    (8, "geografia"),
    (9, "wiedza o społeczeństwie"),
    (10, "informatyka"),
    (11, "j. hiszpańśki"),
    (12, "j. rosysjki"),
    (13, "j. niemiecki"),
)


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
    subject = models.IntegerField(choices=SUBJECTS)


class Calendar(models.Model):
    date = models.DateTimeField


class City(models.Model):
    city = models.CharField(max_length=30)
    postcode = models.CharField(max_length=6)


class Publications(models.Model):
    price = models.IntegerField()
    subject = models.ManyToManyField(Subject)
    tutor = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.OneToOneField(City, on_delete=models.CASCADE)
