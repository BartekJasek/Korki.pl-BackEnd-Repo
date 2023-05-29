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
    path('', views.Homepage.as_view(), name="homepage"),
    path('login/', views.login),
    path('tutor/<int:user_id>', views.Tutor.as_view(), name="tutor"),
    path('publications/', views.Noticeboard.as_view(), name="noticeboard"),
    path('addpublication/', views.AddPublication.as_view(), name="addpublication"),
    path('addsubject/', views.AddSubject.as_view(), name="addsubject"),
    path('addcity/', views.AddCity.as_view(), name="addcity"),
    path('addtutorinfo/', views.AddTutorInfo.as_view(), name="addtutorinfo"),
    path('register/', views.Register.as_view()),
    path('admin/', admin.site.urls),
]
