from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, PublicationForm, TutorForm
from .models import Publications, Tutor


# Create your views here.


def homepage(request):
    context = {}
    return render(request, 'homepage.html', context)


def register(request):
    if request.method == 'POST':
        registerform = RegisterForm(request.POST)
        if registerform.is_valid():
            user = registerform.save()
            login(request, user)
            return redirect('/login/')
    else:
        tutorform = RegisterForm()
    return render(request, 'registration/sign_up.html', {'registerform': registerform})


def tutor(request):
    def get(tutor_id):
        tutor = get_object_or_404(Tutor, id=tutor_id)
        return render(request, "tutor.html", {"tutor": tutor})


def publications(request):
    publications = Publications.objects.all
    context = {'publications': publications}
    return render(request, 'publications.html', context)


@login_required(login_url='/login')
def addpublication(request):
    if request.method == 'POST':
        publicationform = PublicationForm(request.POST)
        if publicationform.is_valid():
            price = publicationform.cleaned_data['price']
            subject = publicationform.cleaned_data['subject']
            tutor = publicationform.cleaned_data['tutor']
            city = publicationform.cleaned_data['city']
            publication = Publications.objects.create(
                price=price, subject=subject, tutor=tutor, city=city)
            return HttpResponseRedirect('/publications/')
    else:
        publicationform = PublicationForm()
    return render(request, 'addpublication.html', {'publicationform': publicationform})


@login_required(login_url='/login')
def addtutorinfo(request):
    if request.method == 'POST':
        tutorform = TutorForm(request.POST)
        if tutorform.is_valid():
            user = tutorform.cleaned_data['user']
            experience = tutorform.cleaned_data['experience']
            phone = tutorform.cleaned_data['phone']
            facebook_url = tutorform.cleaned_data['facebook_url']
            tutor = Tutor.objects.create(
                user=user, experience=experience, phone=phone, facebook_url=facebook_url)
            return HttpResponseRedirect('/publications/')
    else:
        tutorform = TutorForm()
    return render(request, 'addtutorinfo.html', {'tutorform': tutorform})
