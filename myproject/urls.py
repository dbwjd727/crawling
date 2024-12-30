from django.contrib import admin
from django.urls import path, include  # include 추가

urlpatterns = [
    path("admin/", admin.site.urls),
    path("user/", include("user.urls")),  # 'user' 앱의 urls.py를 포함시킴
    path("crawling/", include("crawling.urls")),  # 'crawling' 앱의 urls.py를 포함시킴
]
