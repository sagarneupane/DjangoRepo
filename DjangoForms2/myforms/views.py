from django.shortcuts import render
from .forms import MyForm
from .forms1 import *


# Create your views here.
def index(request):
    form = MyForm(auto_id=True)
    context = {"form": form}
    return render(request, 'index.html', context)


def formsView(request):
    mf = NewForm()
    context = {"form": mf}
    return render(request, 'froms.html', context)
