from django.shortcuts import render
from .forms import EmployeeForm


# Create your views here.

def index(request):
    sf = EmployeeForm()
    context = {"form": sf}
    return render(request, "index.html", context)
