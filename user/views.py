from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse

from .forms import Login, RegistrationForm
from .models import GlobalUser

def login(request):
    context = {}
    if request.method == "POST":
        form = Login(request.POST)
        context['form'] = form
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user != None:
                django_login(request, user)
                return HttpResponseRedirect(reverse('diary:diary', args=[0]))
            context['login_error'] = True
            return render(request, 'user/login.html', context=context)
    
    form = Login()
    context['form'] = form
    return render(request, 'user/login.html', context=context)

def logout(request):
    django_logout(request)
    return HttpResponseRedirect(reverse('main_page'))

def signup(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            age = form.cleaned_data['age']
            user = GlobalUser.objects.create_user(username=username, email=email, password=password, age=age, phone_number=phone_number)
            return HttpResponseRedirect(reverse('diary:diary', args=[0]))
        return render(request, 'user/signup.html', {'form' : form})

    form = RegistrationForm()
    return render(request, 'user/signup.html', {'form' : form})