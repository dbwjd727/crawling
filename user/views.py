# views.py
from django.http import HttpResponse


def create_user(request):
    return HttpResponse("hi")
