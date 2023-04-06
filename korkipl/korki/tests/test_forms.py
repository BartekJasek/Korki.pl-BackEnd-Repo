import pytest

from korki.forms import AddCityForm, TutorForm, PublicationForm, SubjectForm


@pytest.fixture
def test_addcityform():
    form = AddCityForm(data={"city": "Kielce", "postocode": "25-134"})


@pytest.fixture
def test_tutorform():
    form2 = TutorForm(data={"user": "testuser", "experience": "Uczeń Coderslab", "phone": "+48510145370",
                           "facebook_url": "https://github.com/BartekJasek/Korki.pl-BackEnd-Repo!"})


@pytest.fixture
def test_subjectform():
    form3 = SubjectForm(data={"subject": "informatyka"})


@pytest.fixture
def test_publicationform():
    form4 = PublicationForm(data={"price": "120", "subject": "matematyka", "tutor": "testuser", "city": "Kielce"})
