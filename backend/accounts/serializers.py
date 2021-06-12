from .models import CustomUser

from rest_framework import serializers
from core.serializers import BookSerializer, UniversitySerializer

class UserSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)
    university = UniversitySerializer(many=True)
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name',
                  'middle_name', 'about_me', 'rating', 'university', 'books'] #profile
