from django.db import models

from django.conf import settings

class Lesson(models.Model):
    DAY_CHOICES = [
        (1, "Monday"),
        (2, "Tuesday"),
        (3, "Wednesday"),
        (4, "Thursday"),
        (5, "Friday"),
        (6, "Saturday"),
    ]

    name = models.CharField(max_length=24, null=True, blank=True)
    classroom = models.CharField(max_length=32, blank=True, null=True)
    day = models.IntegerField(choices=DAY_CHOICES, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    number = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.user} {self.name}'

class HomeWork(models.Model):
    homework = models.CharField(max_length=256, blank=True, null=True)
    date = models.DateField(blank=True, null=True) # Date of the lesson for which this homework is set
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    is_done = models.BooleanField(default=False) # True, if user marks the homework as done

    def __str__(self):
        return f'{self.lesson} {self.homework}'