from django import forms


class StudentFrom(forms.Form):
    full_name = forms.CharField(label="Full Name", error_messages={'required': "Please Enter Your Name"}, widget=forms.TextInput(attrs={'class': "form-control"}))
    address = forms.CharField(label="What Do you Live?", widget=forms.TextInput(attrs={'class':'form-control'}))
    bio_data = forms.CharField(label="Can you Explain More About The You?", widget=forms.Textarea(attrs={'col': 30, 'row': 20, 'class': 'form-control border-danger'}))
    mobile_no = forms.IntegerField(widget=forms.TextInput(attrs={'maxLength': 15, 'class': 'form-control'}))


