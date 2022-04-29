from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, 'yourApp/index.html')


def about(request):
    from datetime import datetime
    context = {"date": datetime.now}
    return render(request, 'yourApp/about.html', context)
