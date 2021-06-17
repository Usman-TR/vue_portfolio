from django.urls import  path, include
from allauth.account.views import confirm_email
from .views import UserDetailView, get_userbooks


urlpatterns = [
    path('', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
    path('registration/account-confirm-email/<str:key>', confirm_email, name='account_confirm_email'),
    path('account/', include('allauth.urls')),
    path('<str:username>/', UserDetailView.as_view(), name='get_user'),
    path('<str:username>/books/', get_userbooks, name='get_userbooks'),

]