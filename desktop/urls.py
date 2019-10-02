from django.contrib import admin
from django.urls import path, include, register_converter

from .diary_view import diary_page
from .edit_lesson_view import add_lesson, delete_lesson, add_homework, mark_as_done
from .lesson_details_view import lesson_details


app_name = 'diary'

urlpatterns = [
  path('diary/', diary_page, name='diary'),
]
