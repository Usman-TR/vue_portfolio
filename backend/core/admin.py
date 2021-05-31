from django.contrib import admin
from django.db.models.deletion import PROTECT
from .models import Book, University, Profile
# Register your models here.

admin.site.register(Book)
admin.site.register(University)
admin.site.register(Profile)