from .models import CustomUser

from rest_framework import serializers
from core.serializers import BookSerializer, UniversitySerializer, AchivementSerializer, ProfileSerializer

class UserSerializer(serializers.ModelSerializer):
    achivements = AchivementSerializer(many=True)
    university = UniversitySerializer(many=False)
    #profile = ProfileSerializer(many=False)
    profile = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name',
                  'middle_name', 'about_me', 'rating', 'university', 'achivements', 'expert', 'profile', 'admin']

    def get_profile(self, obj):
        customer_profile_query = obj.profile
        serializer = ProfileSerializer(customer_profile_query, many=True)
        if len(serializer.data):
            return serializer.data[0]
        return {
            'title': '',
            'description': '',
            'books': []
        }