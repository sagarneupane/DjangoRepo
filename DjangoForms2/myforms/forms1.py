from django import forms


class NewForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput())
    # name = forms.CharField()
    name = forms.CharField(initial="sagar", help_text="you can enter 30 characters only")
    email = forms.EmailField()
    # bio = forms.Textarea()
    image = forms.ImageField()