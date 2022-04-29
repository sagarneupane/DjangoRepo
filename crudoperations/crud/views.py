# from django.http import HttpResponse
from django.shortcuts import render, HttpResponse, redirect
from .forms import EmployeeForm, StudentForm, CropForm
from .models import Employee, Student,Crops
from django.contrib import messages


# Create your views here.

def employee_list(request):
    EmployeeVal = Employee.objects.all()
    print(len(EmployeeVal))
    return render(request, "employee_list.html", {"Employee": EmployeeVal})


def employee_edit(request, id=0):
    Title = []
    if request.method == "GET":
        if id == 0:
            Title.append("Add Employee")
            form = EmployeeForm()
        else:
            Title.append("Edit Employee")
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, 'employee_edit.html', {"form": form, "Title": Title})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
            messages.success(request, "Record Inserted Successfully")
        else:
            employee = Employee.objects.get(pk=id)

            messages.success(request, "Record updated Successfully")
            form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
        return redirect("employee_list")


def employee_delete(request, id):
    print(id)
    messages.success(request, "Hello Deleted")
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect("employee_list")


def studentDetails(request):
    students = Student.objects.all()
    return render(request, "students/studentsList.html", {'students': students})


def CreateStudent(request, id=0):
    if request.method == "GET":

        if id == 0:
            form = StudentForm()
            context = {"form": form}
        else:

            student = Student.objects.get(pk=id)
            form = StudentForm(instance=student)

            # form = StudentForm()
        return render(request, "students/studentsForm.html", {'form': form})



    else:
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student Successfully Added")
            return redirect("studentList")
        else:
            messages.info(request, "Something Wrong in the Record")
        students = Student.objects.get(pk=id)
        form = StudentForm(instance=students)
        print("Hekko")
        return render(request, "students/studentsForm.html", {"form": form})


def createCrops(request,id=0):
    if id == 0:
        form = CropForm()
        if request.method=="POST":
            form = CropForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
            messages.info(request,"Crops Insert Success")
    else:
        crop = Crops.objects.get(pk=id)
        form = CropForm(instance=crop)
    return render(request, "students/crops.html", {"form": form})
