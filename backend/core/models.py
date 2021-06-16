from django.db import models


class Book(models.Model):
    rating = models.FloatField(default=0.0)
    ISBN = models.CharField(max_length=50)
    numberVoters = models.FloatField(default=0)

    def __str__(self) -> str:
        return self.ISBN


class University(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.title


class Profile(models.Model):
    title = models.CharField(max_length=10)


class Achievement(models.Model):
    title = models.CharField(max_length=10)


class Ratings(models.Model):
    title = models.CharField(max_length=10)
