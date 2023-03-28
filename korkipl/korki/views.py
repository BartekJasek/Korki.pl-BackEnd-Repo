from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .forms import Tutor, Publications


# Create your views here.


def homepage(request):
    context = {}
    return render(request, 'homepage.html', context)


def login(request):
    context = {}
    return render(request, 'login.html', context)


def register(request):
    if request.method == 'POST':
        tutorform = Tutor(request.POST)
        if tutorform.is_valid():
            name = tutorform.cleaned_data['name']
            surname = tutorform.cleaned_data['surname']
            experience = tutorform.cleaned_data['experience']
            contact = tutorform.cleaned_data['contact']
            tutor = Tutor.objects.create(
                name=name, surname=surname, experience=experience, contact=contact)
            return HttpResponseRedirect('/login/')
    else:
        tutorform = Tutor()
    return render(request, 'register.html', {'tutorform': tutorform})


def tutor(request):
    def get(self, request, tutor_id):
        tutor = get_object_or_404(Tutor, id=tutor_id)
        return render(request, "tutor.html", {"tutor": tutor})


def publications(request):
    publications = get_object_or_404(Publications)
    context = {'publications': publications}
    return render(request, 'publications.html', context)


def addpublication(request):
    if request.method == 'POST':
        publicationform = Publications(request.POST)
        if publicationform.is_valid():
            price = publicationform.cleaned_data['price']
            subject = publicationform.cleaned_data['subject']
            tutor = publicationform.cleaned_data['tutor']
            city = publicationform.cleaned_data['city']
            publication = Publications.objects.create(
                price=price, subject=subject, tutor=tutor, city=city)
            return HttpResponseRedirect('/publications/')
    else:
        publicationform = Publications()
    return render(request, 'register.html', {'publicationform': publicationform})
