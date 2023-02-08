from django import forms
from .models import Employee
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Admin_creation_form(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'


class Employee_form(forms.MpdelForm):
    
    class Meta:
        model = Employee
        fields = "__all__"
