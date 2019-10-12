from django.contrib import admin
from django.urls import path, include, register_converter

from .diary_view import diary_page
from .edit_lesson_view import add_lesson, delete_lesson, add_homework, mark_as_done
from .lesson_details_view import lesson_details

app_name = 'diary'

class NegativeIntConverter:
    regex = '-?\d+'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return '%d' % value

register_converter(NegativeIntConverter, "negativeInt")

urlpatterns = [
  path('week/<negativeInt:week>/', diary_page, name='diary'),
  path('add_lesson/<negativeInt:week>/', add_lesson, name='add_lesson'),
  path('delete_lesson/<int:id>/<negativeInt:week>/', delete_lesson, name='delete_lesson'),
  path('edit_homework/<negativeInt:week>/<int:id>/', add_homework, name='edit_homework'),
  path('lesson_details/<int:id>/<negativeInt:week>/', lesson_details, name="lesson_details"),
  path('mark_as_done/<int:id>/<negativeInt:week>/', mark_as_done, name="mark_as_done"),
]