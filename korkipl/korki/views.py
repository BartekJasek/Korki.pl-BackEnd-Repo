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
            return HttpResponseRedirect('/login/')
    else:
        tutorform = Tutor()
    return render(request, 'register.html', {'tutorform': tutorform})


def tutor(request):
    def get(self, request, tutor_id):
        tutor = get_object_or_404(Tutor, id=tutor_id)
        return render(request, "tutor.html", {"tutor": tutor})

def publications(request):
    context = {}
    return render(request, 'publications.html', context)


def addpublication(request):
    if request.method == 'POST':
        publicationform = Publications(request.POST)
        if publicationform.is_valid():
            return HttpResponseRedirect('/You have been registered!/')
    else:
        publicationform = Tutor()
    return render(request, 'addpublication.html', {'publicationform': publicationform})
