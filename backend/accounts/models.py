from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    about_me = models.CharField(max_length=500)
    rating = models.FloatField(default=3.0)