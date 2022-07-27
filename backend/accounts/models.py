from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    about_me = models.CharField(max_length=500)
    rating = models.FloatField(default=3.0)
    university = models.ForeignKey('core.University', on_delete=models.CASCADE, blank=True, null=True)
    profile = models.ManyToManyField('core.Profile', blank=True)
    books = models.ManyToManyField('core.Book')
    achivements = models.ManyToManyField('core.Achivement', blank=True)
    expert = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    image = models.ImageField(upload_to='profiles', blank=True)




