from django.shortcuts import render

# Create your views here.


def index(request):
    context = {"home":"active"}
    return render(request, 'core/index.html',context)

def contact(request):
    context = {"contact":"active"}
    return render(request,'core/contact/contact.html',context)