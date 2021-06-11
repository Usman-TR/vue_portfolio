from .models import CustomUser

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    #author = AuthorSerializer(many=False, read_only=True)
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name',
                  'middle_name', 'about_me', 'rating']  # 'university', 'profile', 'books'
