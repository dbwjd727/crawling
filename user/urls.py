# user/urls.py

from django.urls import path
from . import views  # views.py에서 create_user 함수 가져오기

urlpatterns = [
    path("create/", views.create_user, name="create_user"),  # /create/ URL과 뷰 연결
]
