from django.urls import  path, include
from .views import UserView, get_userbooks, get_userbook, get_achivements, evaluate_knowledge


urlpatterns = [
    path('', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
    path('account/', include('allauth.urls')),
    path('<str:username>/', UserView.as_view(), name='get_user'),
    path('<str:username>/books/', get_userbooks, name='get_userbooks'),
    path('<str:username>/books/<int:book>', evaluate_knowledge, name='evaluate_knowledge'),
    path('<str:username>/books/<int:pk>', get_userbook, name='get_userbook'),
    path('<str:username>/achivements/', get_achivements, name='get_achivements'),

]