from django import forms
from .models import Employee
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Admin_creation_form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'is_superuser']

class Admin_login_form(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


class Employee_form(forms.ModelForm):
    
    class Meta:
        model = Employee
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(attrs={"class":"form-control"}),
            "address": forms.Textarea(attrs={"class":"form-control","rows": 4}),
            "age": forms.NumberInput(attrs={"class":"form-control"}),
            "department": forms.Select(attrs={"class":"form-control"}),
            "emp_start_date": forms.DateInput(attrs={"class":"form-control dateinput"}),
            "emp_end_date": forms.DateInput(attrs={"class":"form-control dateinput"}),
            "salary": forms.NumberInput(attrs={"class":"form-control"}),
            "status": forms.Select(attrs={"class":"form-control"}),
            "photo": forms.FileInput(attrs={"class":"form-control"}),

        }


