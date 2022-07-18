# coding: utf8
from fileinput import close
import profile
# from backend.core.models import RecomendationBooks
from core.models import University
from rest_framework import generics
from .models import CustomUser
from .serializers import UserSerializer
from django.http import JsonResponse
from core.models import Ratings, Book, MarkRequest, Profile, Achivement, RecomendationBooks
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
        university_obj = data.get('university', '')
        print('*'*3, profile_id, university_obj)

        if profile_id is not '':
            profile = Profile.objects.filter(id=profile_id)
            user.profile.set(profile)
        if university_obj is not '':
            university = University.objects.filter(id=university_obj).first()
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
    user = CustomUser.objects.filter(username=username).first()
    books = user.books.all()
    marks = Ratings.objects.filter(user=user).all()

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
                }
        }
    )


def get_achievements(request):
    achivements = Achivement.objects.all()
    achivements_books = []

    for achivement in achivements:
        temp_books = []
        for book in achivement.books.all():
            temp_book = {
                    "id": book.id,
                    "rating": book.rating,
                    "ISBN": book.ISBN,
                    "GoogleId": book.GoogleId,
                    "numberVoters": book.numberVoters,
                    "title": book.title
                }
            temp_books.append(temp_book)
        ach_decriptor = {
                    "id": achivement.id,
                    "title": achivement.title,
                    "description": achivement.description,
                    "image": achivement.image.url,
                    "books": temp_books
                    }
        achivements_books.append(ach_decriptor)
    # print('*'*10,achivements_books)

    return JsonResponse(achivements_books, safe=False)
    # return JsonResponse({"status": 'done'})


def get_user_achievements(request, username):
    user = CustomUser.objects.filter(username=username).first()

    marks = Ratings.objects.filter(user=user).all()

    user_books = []

    for m in marks:
        temp_book = {
                    "id": m.book.id,
                    "rating": m.book.rating,
                    "ISBN": m.book.ISBN,
                    "GoogleId": m.book.GoogleId,
                    "numberVoters": m.book.numberVoters,
                    "title": m.book.title
                }
        user_books.append(temp_book)


    achivements = Achivement.objects.all()
    # achievemnts[] => achievemnt => list of ids
    # get all user book ids from marks
    # if all ach id's is in userbooks => give ach

    achivements_books = []
    for achivement in achivements:
        temp_books = []
        for book in achivement.books.all():
            temp_book = {
                    "id": book.id,
                    "rating": book.rating,
                    "ISBN": book.ISBN,
                    "GoogleId": book.GoogleId,
                    "numberVoters": book.numberVoters,
                    "title": book.title
                }
            temp_books.append(temp_book)
        ach_decriptor = {
                    "id": achivement.id,
                    "title": achivement.title,
                    "description": achivement.description,
                    "image": achivement.image.url,
                    "books": temp_books
                    }
        achivements_books.append(ach_decriptor)

        user_achievements = []
        for achivement_books in achivements_books:
            ach_counter = len(achivement_books['books'])
            for book in achivement_books['books']:
                for user_book in user_books:
                    print(book['id'], user_book['id'])
                    if book['id'] == user_book['id']:
                        ach_counter -= 1
                    if ach_counter <= 0:
                        break
            if ach_counter <= 0:
                user_achievements.append(achivement_books)
    return JsonResponse(user_achievements, safe=False)


def add_book(request, username):

    data = json.loads(request.body)
    GoogleId = data.get('GoogleId', '')
    ISBN = data.get('ISBN', '')
    title = data.get('title', '')
    authors = data.get('authors', '')
    description = data.get('description', '')
    preview = data.get('preview', '')
    language = data.get('language', '')
    publisher = data.get('publisher', '')
    publishedDate = data.get('publishedDate', '')


    print('*'*5, GoogleId, ISBN, title)

    user = CustomUser.objects.filter(username=username).first()
    b = Book.objects.filter(GoogleId=GoogleId).first()
    if b is None:
        b = Book(GoogleId=GoogleId, ISBN=ISBN, title=title, authors=authors, description=description, preview=preview, language=language, publishedDate=publishedDate, publisher=publisher)
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

    existing_marks_check = MarkRequest.objects.filter(book=b, user=user).all()
    if len(existing_marks_check) > 0:
        return JsonResponse({"status": 'exists'})

    mark_request = MarkRequest(book=b, user=user, expert=expert_user)
    mark_request.save()
    return JsonResponse({"status": 'done'})

def cancel_mark_request(request, username, expert, book):
    user = CustomUser.objects.filter(username=username).first()
    expert_user = CustomUser.objects.filter(username=expert).first()
    b = Book.objects.filter(GoogleId=book).first()
    print('***',user, expert_user, b, book)
    if not b:
        return JsonResponse({"status": 'error'})

    existing_marks_check = MarkRequest.objects.filter(book=b, user=user).all()
    if len(existing_marks_check) == 0:
        return JsonResponse({"status": 'not exists'})

    MarkRequest.objects.filter(book=b, user=user).all().delete()
    return JsonResponse({"status": 'done'})


def get_request_marks(request, username):
    expert_id = CustomUser.objects.filter(username=username).first().id
    user_requests = MarkRequest.objects.filter(expert=expert_id, closed=False).order_by('user')
    # print('***', username, user_requests[2].book.title, len(user_requests))

    def value_or_def(object, property, default):
        try:
            return getattr(object, property)
        except Exception as e:
            return default


    return JsonResponse(
        {
            "requests": [
                {
                    "id": req.id,
                    "username": req.user.username,
                    "firstName": req.user.first_name,
                    "lastName": req.user.last_name,
                    "image": json.dumps(str(req.user.image)),
					"GoogleId": str(req.book.GoogleId),
                    "bookTitle": str(req.book.title),
                    "bookImage": str(req.book.preview),
                    "bookAuthors": str(req.book.authors),
                    "GoogleId": str(req.book.GoogleId),
                    'profile': value_or_def(req.user.profile.first(), 'title', 'нет'),
                    'university': value_or_def(req.user.university, 'title', 'нет')
                }
                for req in user_requests
            ]
        }
    )


def get_progress(request, username):
    user = CustomUser.objects.filter(username=username).first()
    profile = Profile.objects.filter(id=user.profile.first().id).first()
    marks = Ratings.objects.filter(user=user).all()

    marked_list = []


    my_books = []

    for profile_book in profile.books.all():
        if profile_book in user.books.all():
            my_books.append(profile_book)
    # print('***my_books', my_books)
    # print('***my_books len', len(my_books))

    for m in marks:
        marked_list.append(m.book.id)

    books = profile.books.all()

    progress_counter = 0
    for b in books:
        if b.id in marked_list:
            progress_counter += 1

    total_profile_books = len(books)

    progress = round(progress_counter / total_profile_books, 2)

    # print(progress, total_profile_books, progress_counter)
    # print('***my_books total', progress_counter, len(my_books))

    return JsonResponse({"progress": progress, 'ungraded': len(my_books)/total_profile_books, 'total': total_profile_books, 'total_graded': progress_counter})

def get_progress_all(request, username):
    print('****', username)
    user = CustomUser.objects.filter(username=username).first()
    profiles = Profile.objects.all()
    marks = Ratings.objects.filter(user=user).all()

    marked_list = [] # list of marked book ids
    my_books = {} # dict of lists
    all_profile_books = {}
    progress_counter = {}

    for profile in profiles:
        my_books[profile.id] = []
        all_profile_books[profile.id] = profile.books.all()
        progress_counter[profile.id] = []
        for profile_book in profile.books.all():
            if profile_book in user.books.all():
                my_books[profile.id].append(profile_book)

    for m in marks:
        marked_list.append(m.book.id)

    marked_set = set(marked_list)

    for key in all_profile_books:
        for b in all_profile_books[key]:
            if b.id in marked_set:
                progress_counter[key] += 1

    return JsonResponse(
        {
            "progress": [
                {
                    'id': key,
                    'name': profiles.filter(id=key).first().title,
                    'currentPage0': len(my_books[key]),
                    'allPages': len(all_profile_books[key])
                }
                for key in my_books
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
                    "description": profile.description,
                }
                for profile in profiles
            ]
        }
    )

def get_profile_books(request, profile_id):
    # data = json.loads(request.body)
    # profile_id = data.get('profile', '')
    if profile_id == '':
        raise BadRequest('Profile does not exists')
    profile = Profile.objects.filter(id=profile_id).first()
    return JsonResponse(
        {
            "books": [
                {
                    "id": book.id,
                    "rating": book.rating,
                    "ISBN": book.ISBN,
                    "GoogleId": book.GoogleId,
                    "numberVoters": book.numberVoters,
                    "title": book.title,
                    "description": book.description,
                    "authors": book.authors,
                    "preview": book.preview
                }
                for book in profile.books.all()
            ]
        }
    )

def get_popular_books(request):
    popular_books = Book.objects.order_by('-rating')[:30].all()
    return JsonResponse(
        {
            "books": [
                {
                    "id": book.id,
                    "rating": book.rating,
                    "ISBN": book.ISBN,
                    "GoogleId": book.GoogleId,
                    "numberVoters": book.numberVoters,
                    "title": book.title,
                    "description": book.description,
                    "authors": book.authors,
                    "preview": book.preview,
                    "language": book.language,
                    "publisher": book.publisher,
                    "publishedDate": book.publishedDate
                }
                for book in popular_books
            ]
        }
    )

def get_recomendation_books(request):
    recomendation = RecomendationBooks.objects.order_by('?')[0]
    print('******', len(recomendation.books.all()), recomendation.books.all())
    return JsonResponse(
        {
            'title': recomendation.title,
            "books": [
                {
                    "id": book.id,
                    "rating": book.rating,
                    "ISBN": book.ISBN,
                    "GoogleId": book.GoogleId,
                    "numberVoters": book.numberVoters,
                    "title": book.title,
                    "description": book.description,
                    "authors": book.authors,
                    "preview": book.preview,
                    "language": book.language,
                    "publisher": book.publisher,
                    "publishedDate": book.publishedDate
                }
                for book in recomendation.books.all()
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

