from django.shortcuts import render
from django.http import JsonResponse


def create_user(request):
    # 기존 Flask의 create.py 로직을 여기에 작성
    return JsonResponse({"message": "User created successfully!"})
