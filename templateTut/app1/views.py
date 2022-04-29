from django.shortcuts import render


# Create your views here.
def render_template(request):
    return render(request, "app1/index.html")

def another_template(request):
    return render(request,"app1/another.html")