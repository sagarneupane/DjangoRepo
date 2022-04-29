from django import forms


class MyForm(forms.Form):
    first_name = forms.CharField(label_suffix=" ")
    last_name = forms.CharField(label_suffix=" ")
    Are_you_student = forms.BooleanField(label_suffix=" ?")
    # description = forms.TextField()
    bio = forms.Textarea()
    image = forms.ImageField()

    field_order = ("first_name", "bio", "image", "Are_you_student", "last_name")
