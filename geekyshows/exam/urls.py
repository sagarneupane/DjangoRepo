from django.urls import path
from exam import views

urlpatterns = [
    path("learn/",views.learn_django,name="learn_django"),
]