from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def view_subjects(request):
    return HttpResponse("THe List oF the subjects Will be Seen Soon")