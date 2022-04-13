from django import forms

class ApplicationForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=20)
    last_name = forms.CharField(label="Last Name", max_length=10)
    stuid = forms.IntegerField(label="Student Id")