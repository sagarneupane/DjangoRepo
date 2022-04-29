from django import forms


class StudentForm(forms.Form):
    full_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}), label_suffix="-: ",
                                label="Full Name")
    age = forms.IntegerField(label_suffix="-: ", label="Your Age Please",
                             widget=forms.NumberInput(attrs={"class": "form-control"}))


class EmployeeForm(forms.Form):
    emp_name = forms.CharField(label="Employee Name", widget=forms.TextInput(attrs={"class": "form-control"}),
                               label_suffix=":- ")
    emp_email = forms.EmailField(label="Employee Email", widget=forms.EmailInput(attrs={"class": "form-control"}),
                                 label_suffix=":- ")
    emp_password = forms.CharField(label="Your Password", widget=forms.PasswordInput(attrs={"class": "form-control"}),
                                   label_suffix=":- ")
    emp_check_pass = forms.CharField(label="Retype Your Password",
                                     widget=forms.PasswordInput(attrs={"class": "form-control"}), label_suffix=":- ")
