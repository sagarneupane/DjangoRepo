from django import forms


class StudentForm(forms.Form):
    full_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}), label_suffix="-: ", label="Full Name")
    age = forms.IntegerField(label_suffix="-: ", label="Your Age Please",widget=forms.NumberInput(attrs={"class": "form-control"}))

