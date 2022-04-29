from django.urls import path

from results import views


urlpatterns = [
    path("view/",views.result_view)
]