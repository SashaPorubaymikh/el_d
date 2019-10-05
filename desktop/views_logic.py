import datetime, textwrap

from diary.models import Lesson, HomeWork

def get_mon_sat(day):
    """Returns the date of Monday and Saturday of the week the day of which was passed to the function"""
    monday = day - datetime.timedelta(days=day.isoweekday() % 7) + datetime.timedelta(days=1)
    saturday = monday + datetime.timedelta(days=5)

    return [monday, saturday]

WEEKDAYS = ['Monday', 'Tuesday', 'Wednesday', "Thursday", "Friday", "Saturday"]

def get_max_number_of_lessons(lessons):
    """Returns the most lessons per week"""

    if lessons:
        return lessons.order_by('-number').first().number
    else:
        return 0

def get_grid_table_context(lessons, homeworks, current_day, week, context):
    """ Returns class schedule and homework for this week """
    if len(lessons) == 0: # If class shedule for the user is empty the program exits the function
        return context

    context['count_of_lessons'] = get_max_number_of_lessons(lessons) # getting the most lessons per week
    context['number_of_days'] = lessons.order_by('-day').first().day # Getting all non empty days

    for day in context['days']:
        for _ in range(1, context['count_of_lessons']+1):
            lesson = lessons.filter(day=current_day.isoweekday(), number=_).first()
            if lesson != None:
                homework = homeworks.filter(lesson=lesson).first()
                if homework != None:
                    day['lessons'].append({
                        'none' : False,
                        'name' : lesson.name,
                        'classroom' : lesson.classroom,
                        'homework' : textwrap.shorten(text=homework.homework, width=25, placeholder='...'),
                        'homework_is_done' : homework.is_done,
                        'details' : homework.id,
                        'delete_id' : lesson.id,
                        'edit_homework' : {'week' : week, 'id' : lesson.id},
                    })
                else:
                    day['lessons'].append({
                        'none' : False,
                        'name' : lesson.name,
                        'classroom' : lesson.classroom,
                        'delete_id' : lesson.id,
                        'details' : 0,
                        'edit_homework' : {'week' : week, 'id' : lesson.id},
                    })
            elif lessons.filter(day=current_day.isoweekday()).exists():
                day['lessons'].append({'none' : True})

        current_day += datetime.timedelta(days=1) # Taking the next day for processing in the next iteration

    context['number_of_lessons'] = context['count_of_lessons'] + 1
    context['count_of_lessons'] = range(1, context['count_of_lessons'] + 1)
    

    return context

def get_vertical_table_context (context, lessons, homeworks, current_day, week):
    for day in context["vertical_grid_days"]:
        for lesson in lessons.filter(day=current_day.isoweekday()):
            homework = homeworks.filter(lesson=lesson).first()
            if homework != None:
                day['lessons'].append(
                    {
                        'number': lesson.number,
                        'name': lesson.name,
                        'classroom': lesson.classroom,
                        'homework' : textwrap.shorten(text=homework.homework, width=25, placeholder='...'),
                        'homework_is_done' : homework.is_done,
                        'details' : homework.id,
                        'delete_id' : lesson.id,
                        'edit_homework' : {'week' : week, 'id' : lesson.id},
                    }
                )
            else:
                day['lessons'].append(
                    {
                        'number': lesson.number,
                        'name' : lesson.name,
                        'classroom' : lesson.classroom,
                        'delete_id' : lesson.id,
                        'details' : 0,
                        'edit_homework' : {'week' : week, 'id' : lesson.id},
                    }
                )
        current_day += datetime.timedelta(days=1)

    return context
    
