from django import forms


class NewForm(forms.Form):
    id = forms.HiddenInput()
    # name = forms.CharField()
    name = forms.CharField(initial="sagar",help_text="you can enter 30 characters only")
    email = forms.EmailField()
