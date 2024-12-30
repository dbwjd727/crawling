from django.urls import path
from . import views

urlpatterns = [
    path("data/", views.get_stock_data, name="get_stock_data"),
]
