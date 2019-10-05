import datetime
import pprint
import textwrap

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from diary.models import Lesson, HomeWork
from . import views_logic


@login_required
def diary_page(request, week):
    '''
    This function displays the schedule for the week, the number of which it receives.
    If the parameter "week" = 0 this function displays shedule for current week,
    else if the parameter "week" parameter = 1 this function diplays shedule for the next week,
    else if the parameter "week" parameter = -1 this function diplays shedule for the previous week.
    '''

    if request.user.is_authenticated:
        context = {"user" : request.user}
        context['username'] = request.user.username
        context["user_is_authenticated"] = True
    
    monday, saturday = views_logic.get_mon_sat(datetime.datetime.today() + datetime.timedelta(weeks=week))
    context['next_week_number'] = week + 1       # To move between weeks we need the next
    context['previous_week_number'] = week -1    # and previous week numbers

    context['days'] = list()
    context['vertical_grid_days'] = list()
    for _ in range(6):
        date = monday + datetime.timedelta(days=_)
        context['days'].append({
            'name' : views_logic.WEEKDAYS[_],
            'date' : f'{date.day}.{date.month}.{str(date.year)}',
            'lessons' : list()
        })

        context['vertical_grid_days'].append({
            'name' : views_logic.WEEKDAYS[_],
            'date' : f'{date.day}.{date.month}.{date.year}',
            'lessons' : list()
        })

    lessons = Lesson.objects.filter(user=request.user)
    homeworks = HomeWork.objects.filter(date__range=[monday, saturday])

    context = views_logic.get_grid_table_context(lessons, homeworks, monday, week, context)
    context = views_logic.get_vertical_table_context(context, lessons, homeworks, monday, week)

    pprint.pprint(context)

    return render(request, 'desktop/diary.html', context)

'''
diary_page() context structure:
context = {
    days : [
        {
            'name' : The name of the weekday we are considering,
            'date' : The date of the day we are considering,
            'lessons' : [
                {
                    'none' : True, if a lesson with this number and weekday does not exist,
                    'name' : The name of the lesson we are considering,
                    'classroom' : The classroom of the lesson,
                    'homewrok' : a string with max length = 25,
                    'homework_is_done' : True, if user mark the homework as done,
                    'details' : Homewrok's id, that we need to show lesson details,
                    'delete_id' : Lesson's id, that wee need to delete the lesson,
                    'edit_homework : {
                        'week' : The week number in which we want to set homework,
                        'id' : ID of the lesson we want to write homework on,
                    }
                },
            ]
        },
    ],
    ...
}
'''
