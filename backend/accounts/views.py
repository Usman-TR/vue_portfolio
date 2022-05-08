# coding: utf8
from fileinput import close
import profile
from core.models import University
from rest_framework import generics
from .models import CustomUser
from .serializers import UserSerializer
from django.http import JsonResponse
from core.models import Ratings, Book, MarkRequest, Profile
import json
from django.core.exceptions import BadRequest


class UserView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'

def update_user(request, username):
    try:
        user = CustomUser.objects.filter(username=username).first()
        data = json.loads(request.body)

        profile_id = data.get('profile', '')
        university_id = data.get('university', '')
        print('*'*3, university_id)

        if profile_id is not '':
            profile = Profile.objects.filter(id=profile_id)
            user.profile.set(profile)
        if university_id is not '':
            university = University.objects.filter(id=university_id).first()
            print('*/'*4, university)
            user.university = university
        user.about_me = data.get('about_me', '')
        user.first_name = data.get('first_name', '')
        user.last_name = data.get('last_name', '')
        user.middle_name = data.get('middle_name', '')
        user.save()
        return JsonResponse({"status": 'done'})
    except Exception as e:
        raise BadRequest('Invalid request: ' + str(e))

def get_userbooks(request, username):
    print('username', username)
    user = CustomUser.objects.filter(username=username).first()
    books = user.books.all()
    marks = Ratings.objects.filter(user=user).all()

    # marks[0].expert_id
    # marks[0].raiting
    # marks[0].book

    marked_book_dict = {}
    for m in marks:
        marked_book_dict[m.book.id] = { 'mark': m.raiting, 'expert': m.expert_id }

    export = []

    for book in books:
        book_dict = { 'id': book.id, 'rating': book.rating, 'ISBN': book.ISBN, 'GoogleId': book.GoogleId,
                      'numberVoters': book.numberVoters, 'marked': False, 'mark': -1, 'expert': -1 }
        if book.id in marked_book_dict.keys():
            book_dict['mark'] = marked_book_dict[book.id]['mark']
            book_dict['expert'] = marked_book_dict[book.id]['expert'].username
            book_dict['marked'] = True
        export.append(book_dict)


    return JsonResponse(
        {
            "books": [
                {
                    "id": book['id'],
                    "rating": book['rating'],
                    "ISBN": book['ISBN'],
                    "GoogleId": book['GoogleId'],
                    "numberVoters": book['numberVoters'],
                    "marked": book['marked'],
                    "mark": book['mark'],
                    "expert": book['expert']
                }
                for book in export
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
                    "GoogleId": book.GoogleId,
                    "numberVoters": book.numberVoters,
                    "test": 12
                }
        }
    )

def add_book(request, username):

    data = json.loads(request.body)
    GoogleId = data.get('GoogleId', '')
    ISBN = data.get('ISBN', '')
    title = data.get('title', '')

    print('*'*5, GoogleId, ISBN, title)

    user = CustomUser.objects.filter(username=username).first()
    b = Book.objects.filter(GoogleId=GoogleId).first()
    if b is None:
        b = Book(GoogleId=GoogleId, ISBN=ISBN, title=title)
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
    b = Book.objects.filter(GoogleId=book).first()
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
					"book": str(req.book.GoogleId)
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

def get_profiles(request):
    profiles = Profile.objects.all()
    return JsonResponse(
        {
            "profiles": [
                {
                    "id": profile.id,
                    "title": profile.title,
                    "description": profile.description
                }
                for profile in profiles
            ]
        }
    )

def get_universities(request):
    universities = University.objects.all()
    return JsonResponse(
        {
            "universities": [
                {
                    "id": university.id,
                    "title": university.title,
                    "description": university.description,
                    "url": university.url
                }
                for university in universities
            ]
        }
    )

def get_experts(request):
    experts = CustomUser.objects.filter(expert=True).all()
    return JsonResponse(
        {
            "experts": [
                {
                    "id": expert.id,
                    "username": expert.username,
                    "first_name": expert.first_name,
                    "last_name": expert.last_name,
                    "profile": expert.profile.all()[0].title
                }
                for expert in experts
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
