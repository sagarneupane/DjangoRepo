from django.urls import path
from . import views

urlpatterns = [
    path('', views.insertData, name="insert"),
    path('showValues/', views.index, name="home"),
    path('employee/', views.showEmployee, name="employee"),
]