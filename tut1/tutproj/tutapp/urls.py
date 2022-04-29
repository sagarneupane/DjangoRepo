from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

                  path('', views.viewItem, name="viewItem"),
                  path('createItem/', views.createItem, name="createItem"),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
