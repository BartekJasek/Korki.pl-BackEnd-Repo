from django.test import TestCase

from korki.forms import AddCityForm, TutorForm, PublicationForm, SubjectForm

def addcityform():
    form = AddCityForm(data={"city": "Kielce", "postocode": "25-134"})


def tutorform():
    form2 = TutorForm(data={"user": "testuser", "experience": "Uczeń Coderslab", "phone": "+48510145370",
                           "facebook_url": "https://github.com/BartekJasek/Korki.pl-BackEnd-Repo!"})


def subjectform():
    form3 = SubjectForm(data={"subject": "informatyka"})


def publicationform():
    form4 = PublicationForm(data={"price": "120", "subject": "matematyka", "tutor": "testuser", "city": "Kielce"})
