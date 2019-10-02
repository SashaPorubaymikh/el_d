from django.db import models
from django.contrib.auth.models import AbstractUser

class GlobalUser(AbstractUser):
    phone_number = models.CharField(max_length=16, null=True, blank=True)
    age = models.PositiveSmallIntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.username
