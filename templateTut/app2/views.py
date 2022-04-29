from django.shortcuts import render


# Create your views here.

def render_template(request):
    return render(request, "app2/index.html")


def another_template(request):
    return render(request, "app2/another.html")