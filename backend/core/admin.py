from django.contrib import admin
from django.db.models.deletion import PROTECT
from .models import Book, University, Profile, Achievement, Ratings
# Register your models here.

admin.site.register(Book)
admin.site.register(University)
admin.site.register(Profile)
admin.site.register(Achievement)
admin.site.register(Ratings)