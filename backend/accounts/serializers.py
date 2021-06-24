from .models import CustomUser

from rest_framework import serializers
from core.serializers import BookSerializer, UniversitySerializer, AchivementSerializer

from core.models import Ratings
class UserSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)
    achivements = AchivementSerializer(many=True)
    university = UniversitySerializer(many=False)
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name',
                  'middle_name', 'about_me', 'rating', 'university', 'books', 'achivements'] #profile

# class RatingSerializer(serializers.ModelSerializer):
#     book = BookSerializer(many=True)
#     user = UserSerializer(many=False)
#     expert = UserSerializer(many=False)

#     class Meta:
#         model = Ratings
#         fields = ['raiting', 'book', 'user', 'expert_id']