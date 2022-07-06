from django.urls import  path, include
from .views import UserView, get_userbooks, get_userbook, get_achivements, evaluate_knowledge, add_book, request_mark, get_request_marks, get_experts, get_profiles, update_user, get_universities, get_profile_books, get_progress, get_achievements, get_user_achievements, get_popular_books, get_recomendation_books, cancel_mark_request


urlpatterns = [
    path('', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
    path('account/', include('allauth.urls')),
    path('<str:username>/', UserView.as_view(), name='get_user'),
    path('<str:username>/books/', get_userbooks, name='get_userbooks'),
    path('<str:expert>/evaluate/<str:request_id>/<int:rating>', evaluate_knowledge, name='evaluate_knowledge'),
    path('<str:username>/books/add/', add_book, name='add_book'),
    path('<str:username>/books/<int:pk>', get_userbook, name='get_userbook'),
    path('<str:username>/request/<str:expert>/<str:book>', request_mark, name='request_mark'),
    path('<str:username>/cancelrequest/<str:expert>/<str:book>', cancel_mark_request, name='cancel_mark_request'),
    path('<str:username>/requests', get_request_marks, name='get_request_marks'),
    path('<str:username>/achivements/', get_achivements, name='get_achivements'),
    path('experts', get_experts, name='get_experts'),
    path('profiles', get_profiles, name='get_profiles'),
    path('universities', get_universities, name='get_universities'),
    path('<str:username>/update', update_user, name='update_user'),
    path('<str:username>/progress', get_progress, name='get_progress'),
    path('profiles/<str:profile_id>/books', get_profile_books, name='get_profile_books'),
    path('popular', get_popular_books, name='get_popular_books'),
    path('recomendation', get_recomendation_books, name='get_recomendation_books'),
    path('achievements', get_achievements, name='get_achievements'),
    path('<str:username>/achievements', get_user_achievements, name='get_user_achievements')
]