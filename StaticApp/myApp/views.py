from django.shortcuts import render

# Create your views here.
def index(request):
    from datetime import datetime
    context = {'myApp':'Django APP',"Date":datetime.now}
    return render(request,'myApp/index.html',context)