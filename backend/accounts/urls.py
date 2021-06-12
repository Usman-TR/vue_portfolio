from django.urls import  path, include

from .views import UserDetailView


urlpatterns = [
    path('api/v1/', include('rest_auth.urls')),
    path('api/v1/registration/', include('rest_auth.registration.urls')),
    path('<str:username>/', UserDetailView.as_view())
    #path('users/<str:username>/books/', get_user_books, name='get_user_books')
]