from django.shortcuts import render

# Create your views here.


def homepage(request):
    context = {}
    return render(request, 'homepage.html', context)


def login(request):
    context = {}
    return render(request, 'login.html', context)


def tutor(request):
    context = {}
    return render(request, 'tutor.html', context)

def publications(request):
    context = {}
    return render(request, 'publications.html', context)
