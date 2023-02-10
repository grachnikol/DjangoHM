from django.shortcuts import render
from django.http import HttpResponse


def main(request):
    return HttpResponse("Main page")

def article(request):
    return HttpResponse("It's an article")

def archive(request):
    return HttpResponse("It's an archive")

def users(request):
    return HttpResponse(['user1 ', 'user2 ', 'user3 '])

def article_num(request, article_number):
    return HttpResponse(
        (f"This is an article #{article_number}"))

def article_slug(request, article_number, name=''):
    return HttpResponse(
        "This is an article #{}. {}".format(article_number, "Name of this article is {}".format(
            name) if name else "This is unnamed article"))

def users_id(request, user_number):
        if user_number < 4:
            return HttpResponse(f"This is an user #{user_number}")
        else:
            return HttpResponse("We don't have so many users. Only user1, user2, user3")

def regex(request):
    return HttpResponse("it's regexp")

def ukr_number(request, numbers, mob_id):
    return HttpResponse(f"{numbers}")
