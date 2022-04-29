from django.urls import path
from . import views

urlpatterns = [
    path("", views.render_template),
    path("another/", views.another_template),
]
