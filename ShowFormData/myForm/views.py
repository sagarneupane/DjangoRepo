from django.shortcuts import render, redirect,HttpResponse
from .forms import *


# Create your views here.


def index(request):

    if request.method == "POST":
        fm = StudentForm(request.POST)
        if fm.is_valid():
            print("Form Validated")
            print("Name=> ", fm.cleaned_data['full_name'])
            print("Age=> ", fm.cleaned_data['age'])
            print(fm.cleaned_data)
    else:
        fm = StudentForm()
    context = {"form": fm}
    return render(request, "index.html", context)


def showData(request):
    return HttpResponse("Hello World")
