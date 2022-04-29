from .models import *
from django import forms


class ItemForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ("Name", "Description", "image")
