from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("showData/", views.showData, name="showData"),
]


