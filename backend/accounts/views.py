from rest_framework import generics
from .models import CustomUser
from .serializers import UserSerializer
from django.http import JsonResponse


class UserView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'


def get_userbooks(request, username):
    books = CustomUser.objects.filter(username=username).first().books.all()
    return JsonResponse(
        {
            "books": [
                {
                    "id": book.id,
                    "rating": book.rating,
                    "ISBN": book.ISBN,
                    "numberVoters": book.numberVoters,
                }
                for book in books
            ]
        }
    )


def get_userbook(request, username, pk):
    book = CustomUser.objects.filter(username=username).first().books.filter(id=pk).first()
    return JsonResponse(
        {
            "book":
                {
                    "id": book.id,
                    "rating": book.rating,
                    "ISBN": book.ISBN,
                    "numberVoters": book.numberVoters,
                }
        }
    )

def get_achivements(request, username):
    achivements = CustomUser.objects.filter(username=username).first().achivements.all()
    return JsonResponse(
        {
            "achivements": [
                {
                    "id": achivement.id,
                    "title": achivement.title,
                    "description": achivement.description,
                    "image": str(achivement.image),
                }
                for achivement in achivements
            ]
        }
    )

def add_rating(request, rating, book, user, expert_id):
    pass


# users = {'admin':
#          {
#              'id': 1,
#              'username': 'admin',
#              'email': 'admin@mail.ru',
#              'description': 'about admin',
#              'rating': 5,
#              'is_expert': True,
#              'university': 'GGNTU',
#              'books': [
#                  {
#                      'id': 1,
#                      'rating': 10,
#                      'ISBN': '022-15-234',
#                      'readed': True,
#                      'my_rating': 10,
#                      'expert_id': 1
#                  },
#                  {
#                      'id': 2,
#                      'rating': 10,
#                      'ISBN': '103-17-324',
#                      'readed': False,
#                      'my_rating': 10,
#                      'expert_id': 1
#                  },
#              ]
#          },
#          'student':
#          {
#              'id': 1,
#              'username': 'student',
#              'email': 'student@mail.ru',
#              'description': 'about student',
#              'rating': 3,
#              'is_expert': False,
#              'university': 'CHGU',
#              'books': [
#                  {
#                      'id': 3,
#                      'rating': 10,
#                      'ISBN': '312-15-709',
#                      'readed': True,
#                      'my_rating': 10,
#                      'expert_id': 1
#                  },
#                  {
#                      'id': 4,
#                      'rating': 10,
#                      'ISBN': '590-11-567',
#                      'readed': False,
#                      'my_rating': 10,
#                      'expert_id': 2
#                  },
#              ]
#          }
#          }
# books = [
#     {
#     'id': 1,
#     'title': 'Python',
#     'year': '2020',
#     'description':'Book about python',
#     'rating': 10,
#     'publisher': 'i.monoteist',
#     'authors': 'Isa Ezerbaev',
#     'ISBN': '022-15-234'
#     }
# ]


# def get_username(request, username):
#     user = users[username]
#     return JsonResponse(user, safe=False, json_dumps_params={'indent': 2})


# def get_user_books(request, username):
#     books = users[username]['books']
#     return JsonResponse(books, safe=False, json_dumps_params={'indent': 2})
