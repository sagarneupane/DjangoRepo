from django.urls import path

from subjects import views


urlpatterns = [
    path("view/",views.view_subjects)
]