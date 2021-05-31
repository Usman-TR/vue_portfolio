from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    middle_name = models.CharField(max_length=100)
    about_me = models.CharField(max_length=500)
    rating = models.FloatField(default=3.0)
    university = models.ForeignKey('core.University', on_delete=models.SET_NULL) # not delete
    profile = models.ManyToManyField('core.Profile')
    books = models.ManyToManyField('core.Book')