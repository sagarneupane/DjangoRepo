from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("datetime/", views.dateFilter, name="datefilter"),
    path("tag/", views.TemplatesTag, name="tag"),
    path("loop/", views.loopDTL, name="loop"),
]
