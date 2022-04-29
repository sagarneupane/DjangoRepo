from django.shortcuts import render
from .forms import StudentFrom


# Create your views here.

def index(request):
    sf = StudentFrom()
    context = {"form": sf}
    return render(request, "index.html", context)
