from django.urls import  path, include

from .views import UserDetailView, get_userbooks


urlpatterns = [
    path('', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
    path('<str:username>/', UserDetailView.as_view(), name='get_user'),
    path('<str:username>/books/', get_userbooks, name='get_userbooks')
]