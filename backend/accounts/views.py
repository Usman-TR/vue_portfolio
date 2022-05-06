# coding: utf8
from fileinput import close
import profile
from rest_framework import generics
from .models import CustomUser
from .serializers import UserSerializer
from django.http import JsonResponse
from core.models import Ratings, Book, MarkRequest, Profile


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

def add_book(request, username, book):
    #check if book is already in db
    user = CustomUser.objects.filter(username=username).first()
    b = Book.objects.filter(ISBN=book).first()
    if b is None:
        b = Book(ISBN=book)
        b.save()
        user.books.add(b)
        user.save()
        return JsonResponse({"status": 'done'})
    user.books.add(b)
    user.save()
    return JsonResponse({"status": 'done'})

def request_mark(request, username, expert, book):
    user = CustomUser.objects.filter(username=username).first()
    expert_user = CustomUser.objects.filter(username=expert).first()

    b = Book.objects.filter(ISBN=book).first()
    if not b:
        return JsonResponse({"status": 'error'})
    mark_request = MarkRequest(book=b, user=user, expert=expert_user)
    mark_request.save()
    return JsonResponse({"status": 'done'})

def get_request_marks(request, username):
    expert_id = CustomUser.objects.filter(username=username).first().id
    user_requests = MarkRequest.objects.filter(expert=expert_id, closed=False)
    return JsonResponse(
        {
            "requests": [
                {
                    "id": req.id,
                    "username": req.user.username,
					"book": str(req.book.ISBN)
                }
                for req in user_requests
            ]
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

def evaluate_knowledge(request, expert, request_id, rating):
    # rating book user expert
	# update with mark_request object
	mark_request = MarkRequest.objects.filter(id=request_id).first()
	student = mark_request.user
	book = mark_request.book
	expert = mark_request.expert
	mark_row = Ratings(raiting=rating, book=book, user=student, expert_id=expert)
	mark_row.save()
	mark_request.closed = True
	mark_request.save()
	return JsonResponse({"status": 'done'})


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
