from django.db import models

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
    nameandsurname = models.CharField(max_length=64)
    experience = models.CharField
    contact = models.IntegerField(max_length=9)


class Subject(models.Model):
    subject = models.IntegerField(choices=SUBJECTS)


class Calendar(models.Model):
    date = models.DateTimeField


class City(models.Model):
    city = models.CharField(max_length=32)
    zipcode = models.IntegerField(max_length=5)


class Publications(models.Model):
    price = models.IntegerField
    subject = models.ManyToManyField(Subject, through="Przedmiot")
    name = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    city = models.OneToOneField(City, through="Przedmiot", on_delete=models.CASCADE)
