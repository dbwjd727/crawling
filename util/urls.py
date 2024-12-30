# from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("user/", include("user_app.urls")),  # user 앱의 urls.py 연결
]
