from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def result_view(request):
    return HttpResponse("<h1>Hello From Result</h1>")
