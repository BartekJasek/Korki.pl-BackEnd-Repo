from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, PublicationForm, TutorForm, SubjectForm, AddCityForm
from .models import Publications, Tutor, Subject, City, Calendar
from django.contrib.auth.models import User


# Create your views here.


def homepage(request):
    # view of homepage which is empty for now
    return render(request, 'homepage.html')


def register(request):
    # view where new users are saved to database, this view use usercreationform from forms
    if request.method == 'POST':
        registerform = RegisterForm(request.POST)
        if registerform.is_valid():
            user = registerform.save()
            login(request, user)
            return redirect('/')
    else:
        registerform = RegisterForm()
    return render(request, 'registration/sign_up.html', {'registerform': registerform})


def tutor(request, user_id):
    # this view show tutor detail on page
    return render(request, "tutor.html", {"user": get_object_or_404(User, id=user_id)})


def noticeboard(request):
    # noticeboard is view where all publications are showed on the page
    publications = Publications.objects.all()
    return render(request, 'publications.html', {'publications': publications})


@login_required(login_url='/login')
def addpublication(request):
    # add new publications do database, this view can be used only if user is loged in
    # it also create new datetime(now) and add it to publication
    if request.method == 'POST':
        publicationform = PublicationForm(request.POST)
        if publicationform.is_valid():
            price = publicationform.cleaned_data['price']
            subject = publicationform.cleaned_data['subject']
            tutor = publicationform.cleaned_data['tutor']
            city = publicationform.cleaned_data['city']
            create_date = Calendar.objects.create()
            publication = Publications.objects.create(
                price=price, tutor=tutor, city=city, create_date=create_date)
            publication.subject.set(subject)
            return HttpResponseRedirect('/publications/')
    else:
        publicationform = PublicationForm()
    return render(request, 'addpublication.html', {'publicationform': publicationform})


@login_required(login_url='/login')
def addtutorinfo(request):
    # add tutor details, this view can be used only if user is loged in
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


@login_required(login_url='/login')
def addsubject(request):
    # add subject to database from choices, this view can be used only if user is loged in
    if request.method == 'POST':
        subjectform = SubjectForm(request.POST)
        if subjectform.is_valid():
            subject = subjectform.cleaned_data['subject']
            subject = Subject.objects.create(
                subject=subject)
            return HttpResponseRedirect('/addpublication/')
    else:
        subjectform = SubjectForm()
    return render(request, 'addsubject.html', {'subjectform': subjectform})


@login_required(login_url='/login')
def addcity(request):
    # add city to database, this view can be used only if user is loged in
    if request.method == 'POST':
        addcityform = AddCityForm(request.POST)
        if addcityform.is_valid():
            city = addcityform.cleaned_data['city']
            postcode = addcityform.cleaned_data['postcode']
            city = City.objects.create(
                city=city, postcode=postcode)
            return HttpResponseRedirect('/addsubject/')
    else:
        addcityform = AddCityForm()
    return render(request, 'addcity.html', {'addcityform': addcityform})
