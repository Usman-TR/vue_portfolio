from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=10)


class University(models.Model):
    title = models.CharField(max_length=10)


class Profile(models.Model):
    title = models.CharField(max_length=10)


class Achievement(models.Model):
    title = models.CharField(max_length=10)

class Ratings(models.Model):
    title = models.CharField(max_length=10)