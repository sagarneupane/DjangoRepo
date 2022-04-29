from django.urls import  path
from . import views


urlpatterns = [
    path("",views.app2_view),
    path("error/",views.app2_error),
]