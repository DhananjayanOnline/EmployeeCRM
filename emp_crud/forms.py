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
