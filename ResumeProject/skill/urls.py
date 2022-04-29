from django.urls import path
from . import views


urlpatterns = [
    path('',views.skills,name='skills')
]