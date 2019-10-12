from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from diary.models import Lesson, HomeWork

@login_required
def lesson_details(request, id, week):
    homework = HomeWork.objects.filter(id=id).first()
    if homework != None and homework.lesson.user == request.user:
        lesson = homework.lesson
        context = {
            'name' : lesson.name,
            'classroom' : lesson.classroom,
            'number' : lesson.number,
            'homework' : homework.homework,
            'username' : request.user.username,
            'user_is_authenticated' : True,
            'week': week,
        }
        return render(request, 'desktop/lesson_details.html', context=context)

    return HttpResponseRedirect(reverse('diary:diary', args=[week]))
