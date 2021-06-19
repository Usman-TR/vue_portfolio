from django.db import models
from django.db.models.fields import URLField


class Book(models.Model):
    rating = models.FloatField(default=0.0)
    ISBN = models.CharField(max_length=50)
    numberVoters = models.FloatField(default=0)

    def __str__(self) -> str:
        return self.ISBN


class University(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    url = models.URLField(blank=True)

    def __str__(self) -> str:
        return self.title


class Profile(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.title


class Achivement(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='achivements', blank=True)

    def __str__(self) -> str:
        return self.title


class Ratings(models.Model):
    raiting = models.IntegerField(default=0)
    book = models.ForeignKey(
        Book, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey('accounts.CustomUser',
                             on_delete=models.SET_NULL, null=True, blank=True)
    expert = models.ForeignKey(
        'accounts.CustomUser', on_delete=models.SET_NULL, null=True, blank=True, related_name='expert')

    def __str__(self) -> str:
        return f'{self.book} {self.raiting} {self.user}'
