from django import forms


class StudentForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()


class EmployeeForm(forms.Form):
    name = forms.CharField()
    address = forms.Textarea()
    email = forms.EmailField()
    image = forms.ImageField()
    qualifications = forms.FileField()
    degree = forms.ChoiceField()
    slug = forms.SlugField()
