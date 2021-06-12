from rest_framework import generics
from .models import CustomUser
from .serializers import UserSerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'

