from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='myApp'),
    path('about/', views.about, name='myAppAbout'),

]
