from django.contrib import admin
from django.urls import path, include  # include 추가

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("user.urls")),  # 'user' 앱의 urls.py를 포함시킴
]
