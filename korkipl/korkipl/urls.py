"""korkipl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from korki import views

urlpatterns = [
    path('', include("django.contrib.auth.urls")),
    path('', views.homepage, name="homepage"),
    path('login/', views.login),
    path('tutor/<int:user_id>', views.tutor, name="tutor"),
    path('publications/', views.noticeboard, name="noticeboard"),
    path('addpublication/', views.addpublication, name="addpublication"),
    path('addsubject/', views.addsubject, name="addsubject"),
    path('addcity/', views.addcity, name="addcity"),
    path('addtutorinfo/', views.addtutorinfo, name="addtutorinfo"),
    path('register/', views.register),
    path('admin/', admin.site.urls),
]
