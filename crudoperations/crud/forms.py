from django import forms
from .models import Employee, Student,Crops


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ("fullname", "mobile", "emp_code", "position")
        labels = {
            "fullname": "Full Name",
            "emp_code": "Emp. Code",
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"


class DateInput(forms.DateInput):
    input_type = 'date'


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student

        fields = ("studentName", 'studentAddress',"birth_date", "age", "email", "phoneNumber", "course")
        # widgets = {
        #     'birth_date': DateInput()
        # }

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, *kwargs)
        self.fields['course'].empty_label = "Select"


class CropForm(forms.ModelForm):
    class Meta:
        model = Crops
        # image = forms.ImageField()
        fields = ("name","type","image")