from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from .forms import Admin_creation_form, Admin_login_form, Employee_form, Exprerience_form, Employee_creation_form
from django.views.generic import CreateView, FormView, TemplateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.contrib import messages
from django.forms import inlineformset_factory
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from django.http import FileResponse, HttpResponse
from io import BytesIO
from reportlab.pdfgen import canvas

import xlwt

from django.core.paginator import Paginator


# Create your views here.

def signin_required(fn):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, 'invalid session')
            return redirect("signin")
        else:
            return fn(request, *args, **kwargs)
    return wrapper

def super_user(fn):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_superuser:
            messages.error(request, 'Access denied')
            user = Employee.objects.get(user__username=request.user.username)
            emp = user.id
            return redirect('details', emp)
        else:
            return fn(request, *args, **kwargs)
    return wrapper



decs = [signin_required, never_cache]

@method_decorator(decs, name="dispatch")
class Registration_view(CreateView):
    template_name = 'signup.html'
    form_class = Admin_creation_form
    success_url = reverse_lazy('home')
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
                if usr.is_superuser:
                    login(request, usr)
                    return redirect("home")
                else:
                    user = Employee.objects.get(user__username=uname)
                    emp = user.id
                    login(request, usr)
                    return redirect('details', emp)
            else:
                messages.error(self.request,"Invalid Credentials")
                return render(request, self.template_name, {"form":form})


# @method_decorator(decs, name="dispatch")
# class Index_view(CreateView, ListView, UserPassesTestMixin):
#     template_name = 'index.html'
#     form_class = Employee_creation_form
#     success_url = reverse_lazy('home')
#     context_object_name = 'employees'
#     object_list  = Employee.objects.all()
#     queryset = Employee.objects.all()
#     paginate_by = 2
    
#     def form_valid(self, form):
#         username = form.cleaned_data.get('username')
#         password = form.cleaned_data.get('password1')

#         Employee.objects.create(username=username, password=password)

#         user = form.save(commit=False)
#         user.save()
#         return super().form_valid(form)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["emp_count"] = Employee.objects.all().count()
#         context["pro_dept_count"] = Employee.objects.filter(department="Product development").count()
#         context["sales_dept_count"] = Employee.objects.filter(department="Sales and marketing").count()
#         context["salary_sum"] = Employee.get_salary_sum()
#         return context

@login_required(login_url='signin')
@super_user
@never_cache
def index_view(request):

    qs = Employee.objects.all()
    if request.method == 'POST':
        form = Employee_creation_form(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            Employee.objects.create(user=user, username=username, password=password)
    else:
        form = Employee_creation_form()

    # paginatoin
    p = Paginator(Employee.objects.all(), 3)
    page = request.GET.get('page')
    venues = p.get_page(page)


    context = {
        'employees':qs,
        'form':form,
        'venues':venues
    }
    return render(request, 'index.html', context)


    # def test_func(self):
    #     # Check if the user is a superuser or a staff member
    #     return self.request.user.is_superuser

    # def handle_no_permission(self):

    #     # Redirect to the login page if the user doesn't have the required permission
    #     return redirect('details')

    
    

@method_decorator(decs, name="dispatch")
class Update_emp_view(UpdateView):
    template_name = 'update.html'
    form_class = Employee_form
    model = Employee
    success_url = reverse_lazy('home')


@method_decorator(decs, name="dispatch")
class Detail_emp_view(DetailView):
    template_name = 'emp_details.html'
    model = Employee
    context_object_name = 'emp'

    def get_context_data(self, **kwargs):
        user = Employee.objects.get(id=self.request.user.id)
        usr = self.kwargs['pk']
        context = super().get_context_data(**kwargs)
        context["exp_list"] = Exprerience.objects.filter(emp_id=usr)
        return context


@method_decorator(decs, name="dispatch")
class Delete_emp_view(DeleteView):
    template_name = 'emp_confirm_delete.html'
    model = Employee
    success_url = reverse_lazy('home')

def logout_view(request, *args, **kwargs):
    logout(request)
    return redirect('signin')



decs
# def generate_pdf_view(request):
#     # Retrieve the data from your model
#     data = Employee.objects.all()

#     # Create a BytesIO object
#     buffer = BytesIO()

#     # Create the PDF object
#     pdf = canvas.Canvas(buffer)

#     # Write the table header
#     pdf.drawString(10, 800, "Name")
#     pdf.drawString(100, 800, "age")
#     pdf.drawString(200, 800, "department")
#     pdf.drawString(350, 800, "emp_start_date")
#     pdf.drawString(500, 800, "emp_end_date")

#     # Write the table data
#     y = 790
#     for record in data:
#         pdf.drawString(10, y, str(record.name))
#         pdf.drawString(100, y, str(record.age))
#         pdf.drawString(200, y, str(record.department))
#         pdf.drawString(350, y, str(record.emp_start_date))
#         pdf.drawString(500, y, str(record.emp_end_date))
#         y = y - 20

#     # Save the PDF
#     pdf.save()

#     # Create a FileResponse object with the PDF data
#     buffer.seek(0)
#     response = FileResponse(buffer, content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="table.pdf"'

#     return response


def export_users_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users Data') # this will make a sheet named Users Data

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Name', 'Usernme', 'Address', 'Age', 'Department', 'Start Date', 'End Date', 'Salary', 'Status']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column 

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Employee.objects.all().values_list('name', 'username', 'address', 'age', 'department', 'emp_start_date', 'emp_end_date', 'salary', 'status')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)

    return response


def add_exprerience(request, pk):
    EmployeeFormSet = inlineformset_factory(Employee, Exprerience, fields=('domain','skill', 'years_of_expre', 'description'), extra=1, can_delete = False)
    employee = Employee.objects.get(id=pk)
    formset = EmployeeFormSet(queryset=Exprerience.objects.none() ,instance=employee) # initialize formset here

    if request.method == 'POST':
        formset = EmployeeFormSet(request.POST, instance=employee) # update formset with POST data
        if formset.is_valid():
            formset.save()
            return redirect('details',pk)

    context = {'formset': formset}
    return render(request, 'add_exp.html', context)



def add_exprerience_normalForm(request,pk):
    emp = Employee.objects.get(id=pk)

    form = Exprerience_form(initial={'emp_id':emp})

    if request.method == 'POST':
        form = Exprerience_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('details', pk)
    
    context = {'form':form}
    return render(request, 'add_exp.html', context)



class Delete_experience(DeleteView):
    template_name = 'emp_confirm_delete.html'
    model = Exprerience
    success_url = reverse_lazy('home')

class Update_experience_view(UpdateView):
    template_name = 'update.html'
    form_class = Exprerience_form
    model = Exprerience
    success_url = reverse_lazy('home')


def get_user_experience(request, pk):
    
    expre = Exprerience.objects.get(id=pk)
    context = {
        'expre':expre
    }
    return render(request, 'display-exp.html', context)



def load_cities(request):
    domain_id = request.GET.get('domain_id')
    skills = Skills.objects.filter(domain_id=domain_id).all()
    return render(request, 'skill_dropdown_list_options.html', {'skills': skills})


class List_admin(ListView):
    model = User
    queryset = User.objects.filter(is_superuser=True)
    template_name = 'list-admins.html'