import datetime

from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import  reverse

from .forms import AddLesson, AddHomework
from diary.models import Lesson, HomeWork
from .views_logic import get_mon_sat


@login_required
def add_lesson(request):
    '''Creates a new lesson'''

    context = {}
    if request.method == "POST":
        form = AddLesson(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            classroom = form.cleaned_data['classroom']
            day = form.cleaned_data['day']
            number = form.cleaned_data['number']
            if Lesson.objects.filter(day=day, number=number, user=request.user).exists() == False:
                lesson = Lesson.objects.create(name=name, classroom=classroom, day=day, number=number, user=request.user)
                return HttpResponseRedirect(reverse('diary:diary', args=[0]))
            context['addlesson_error'] = "A lesson with this number allready exists"
    
    form = AddLesson()
    context['form'] = form
    return render(request, 'desktop/addlesson.html', context=context)

@login_required
def delete_lesson(request, id):
    '''Deletes lesson with the id'''

    Lesson.objects.filter(id=id, user=request.user).delete()
    return HttpResponseRedirect(reverse('diary:diary', args=[0]))

@login_required
def add_homework(request, week, id):
    '''Creates homework with week and id, passed to function'''

    if request.method == "POST":
        form = AddHomework(request.POST)
        if form.is_valid():
            try: 
                homework = form.cleaned_data['text']
            except: 
                homework = ''
            lesson = Lesson.objects.get(id=id)
            mon, _ = get_mon_sat(datetime.date.today() + datetime.timedelta(weeks=week))
            date = mon + datetime.timedelta(days=lesson.day - 1)
            if HomeWork.objects.filter(date=date, lesson=lesson).exists() == False and homework != '':
                HomeWork.objects.create(homework=homework, date=date, lesson=lesson)
            else:
                hw = HomeWork.objects.get(date=date, lesson=lesson)
                if homework != '':
                    hw.homework = homework
                    hw.is_done = False
                    hw.save()
                else:
                    hw.delete()
            return HttpResponseRedirect(reverse('diary:diary', args=[0]))

    form = AddHomework()
    context = {
        'form' : form,
        'id' : id,
        'week' : week,
    }
    return render(request, 'desktop/add_homework.html', context=context)

def mark_as_done(request, id):
    '''Marks as done homewrok with passed to function homework's id'''
    
    homework = HomeWork.objects.filter(id=id).first()
    homework.is_done = True
    homework.save()
    return HttpResponseRedirect(reverse('diary:diary', args=[0]))