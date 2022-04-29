from django.shortcuts import render
from django.http import HttpResponse, Http404


# Create your views here.


def app2_view(request):
    return render(request, "app2.html")


def app2_error(request):
    return HttpResponse("No Ome")
