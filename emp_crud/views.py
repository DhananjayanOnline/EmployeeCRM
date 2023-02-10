from django.shortcuts import render, redirect
from .models import Employee
from .forms import Admin_creation_form, Admin_login_form, Employee_form
from django.views.generic import CreateView, FormView, TemplateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout

# Create your views here.

class Registration_view(CreateView):
    template_name = 'signup.html'
    form_class = Admin_creation_form
    success_url = reverse_lazy('signin')
    context_object_name = 'form'


class Login_view(FormView):
    template_name = 'signin.html'
    form_class = Admin_login_form

    def post(self, request, *args, **kwargs):
        form = Admin_login_form(request.POST)
        if form.is_valid():
            uname = form.cleaned_data.get("username")
            pword = form.cleaned_data.get("password")
            usr = authenticate(request, username=uname, password=pword)
            if usr:
                login(request, usr)
                return redirect("home")
            else:
                return render(request, self.template_name, {"form":form})



class Index_view(CreateView, ListView):
    template_name = 'index.html'
    form_class = Employee_form
    model = Employee
    success_url = reverse_lazy('home')
    context_object_name = 'employees'

class Update_emp_view(UpdateView):
    template_name = 'index.html'
    form_class = Employee_form
    model = Employee
    success_url = reverse_lazy('home')

class Detail_emp_view(DetailView):
    template_name = 'emp_details.html'
    model = Employee
    context_object_name = 'emp'

class Delete_emp_view(DeleteView):
    template_name = 'emp_confirm_delete.html'
    model = Employee
    success_url = reverse_lazy('home')

