from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse

from .models import GlobalUser


def login(request):
    return HttpsResponse(200)
def logout(request):

    django_logout(request)
    return HttpResponse(200)

def signup(request):
    retrun HttpsResponse(200)
