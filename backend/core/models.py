from statistics import mode
from turtle import title
from django.db import models
from django.db.models.fields import URLField


class Book(models.Model):
    rating = models.FloatField(default=0.0)
    ISBN = models.CharField(max_length=50)
    GoogleId = models.CharField(max_length=150, default='')
    numberVoters = models.FloatField(default=0)
    language = models.CharField(default="", max_length=14)
    publisher = models.CharField(default="",max_length=70)
    publishedDate = models.CharField(default="",max_length=15)
    title = models.CharField(default='no title', max_length=150)
    authors = models.CharField(default='no authors', max_length=300)
    description = models.CharField(default='no description', max_length=4000)
    preview = models.CharField(default='no preview', max_length=300)


    def __str__(self) -> str:
        return f'{self.id} {self.title} {self.ISBN} {self.GoogleId}'


class University(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    url = models.URLField(blank=True)

    def __str__(self) -> str:
        return self.title


class Profile(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    books = models.ManyToManyField('core.Book')

    def __str__(self) -> str:
        return self.title


class Achivement(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='achivements', blank=True)
    books = models.ManyToManyField('core.Book')

    def __str__(self) -> str:
        return self.title


class Ratings(models.Model): # for ecaluationg knowledge
    raiting = models.IntegerField(default=0)
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE)
    user = models.ForeignKey('accounts.CustomUser',
                             on_delete=models.CASCADE)
    expert_id = models.ForeignKey(
        'accounts.CustomUser', on_delete=models.CASCADE , related_name='expert_id')

    def __str__(self) -> str:
        return f'{self.book} {self.raiting} {self.user}'


class MarkRequest(models.Model):
    user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    expert = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE , related_name='expert_markrequest')
    # profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    closed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.user} {self.expert} {self.book} {self.closed}'


class RecomendationBooks(models.Model):
    title = models.CharField(max_length=150)
    books = models.ManyToManyField('core.Book')

    def __str__(self) -> str:
        return self.title
