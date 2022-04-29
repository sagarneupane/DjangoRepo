from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm, EmployeeForm


# Create your views here.
def index(request):
    form = StudentForm()
    stu_obj = Student.objects.all()
    context = {"Students": stu_obj, "form": form}
    return render(request, "myApp/index.html", context)


def insertData(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
        bio = request.POST.get("bio")
        student = Student(name=name, email=email, password=password, address=address, bio_data=bio)
        student.save()
        return redirect("home")
    return render(request, "myApp/insert.html")


def showEmployee(request):
    # emp_form = EmployeeForm(auto_id=False)
    # emp_form = EmployeeForm(auto_id=True)
    emp_form = EmployeeForm(auto_id="sagar_%s",label_suffix=" ", initial={"name": "sagar"})
    # emp_form = EmployeeForm()
    context = {"employee": emp_form}
    return render(request, "myApp/employee.html", context)
