
from django.shortcuts import render,HttpResponse
from .models import *

from .forms import *


# Create your views here.


def viewItem(request):
    form = ItemForm
    if request.method == "POST":
        form = ItemForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Saved")
    return render(request, "proj/viewItem.html", {"form": form})


def createItem(request, id=0):
    return render(request, "proj/createItem.html")
