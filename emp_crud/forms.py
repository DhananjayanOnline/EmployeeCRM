from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Admin_creation_form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2','is_superuser']

        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "password1": forms.PasswordInput(attrs={"class": "form-control"}),
            "password2": forms.PasswordInput(attrs={"class": "form-control"}),
            "is_superuser": forms.CheckboxInput(attrs={"class": "form-control"}),
        }

class Admin_login_form(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


class Employee_creation_form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'is_staff']

        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "password1": forms.PasswordInput(attrs={"class": "form-control"}),
            "password2": forms.PasswordInput(attrs={"class": "form-control"}),
            "is_staff": forms.CheckboxInput(attrs={"class": "form-control"}),
        }



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


class Exprerience_form(forms.ModelForm):
    class Meta:
        model = Exprerience
        fields = "__all__"

        widgets = {
            "domain": forms.Select(attrs={"class":"form-control"}),
            "skill": forms.Select(attrs={"class":"form-control"}),
            "years_of_expre": forms.NumberInput(attrs={"class":"form-control"}),
            "description": forms.Textarea(attrs={"class":"form-control","rows": 2}),
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['skill'].queryset = Skills.objects.none()

        if 'domain' in self.data:
            try:
                domain_id = int(self.data.get('domain'))
                self.fields['skill'].queryset = Skills.objects.filter(domain=domain_id).all()
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['skill'].queryset = self.instance.domain.skills_set.order_by('name')