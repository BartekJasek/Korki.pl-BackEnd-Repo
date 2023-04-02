from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login, logout, authenticate

from .forms import RegisterForm, Publications


# Create your views here.


def homepage(request):
    context = {}
    return render(request, 'homepage.html', context)


def register(request):
    if request.method == 'POST':
        tutorform = RegisterForm(request.POST)
        if tutorform.is_valid():
            user = tutorform.save()
            login(request, user)
            return redirect('/login/')
    else:
        tutorform = RegisterForm()
    return render(request, 'registration/sign_up.html', {'tutorform': tutorform})


def tutor(request):
    def get(self, request, tutor_id):
        tutor = get_object_or_404(Tutor, id=tutor_id)
        return render(request, "tutor.html", {"tutor": tutor})


def publications(request):
    publications = Publications.objects.get.all
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
    return render(request, 'addpublication.html', {'publicationform': publicationform})
