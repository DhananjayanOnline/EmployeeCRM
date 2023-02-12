from django.shortcuts import render, redirect
from .models import Employee
from .forms import Admin_creation_form, Admin_login_form, Employee_form
from django.views.generic import CreateView, FormView, TemplateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.contrib import messages

from django.http import FileResponse
from io import BytesIO
from reportlab.pdfgen import canvas

# Create your views here.

def signin_required(fn):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, 'invalid session')
            return redirect("signin")
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
                login(request, usr)
                return redirect("home")
            else:
                messages.error(self.request,"Invalid Credentials")
                return render(request, self.template_name, {"form":form})


@method_decorator(decs, name="dispatch")
class Index_view(CreateView, ListView):
    template_name = 'index.html'
    form_class = Employee_form
    model = Employee
    success_url = reverse_lazy('home')
    context_object_name = 'employees'
    object_list  = Employee.objects.all()
    queryset = Employee.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["emp_count"] = Employee.objects.all().count()
        context["pro_dept_count"] = Employee.objects.filter(department="Product development").count()
        context["sales_dept_count"] = Employee.objects.filter(department="Sales and marketing").count()
        context["salary_sum"] = Employee.get_salary_sum()
        return context
    

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


@method_decorator(decs, name="dispatch")
class Delete_emp_view(DeleteView):
    template_name = 'emp_confirm_delete.html'
    model = Employee
    success_url = reverse_lazy('home')

def logout_view(request, *args, **kwargs):
    logout(request)
    return redirect('signin')



decs
def generate_pdf_view(request):
    # Retrieve the data from your model
    data = Employee.objects.all()

    # Create a BytesIO object
    buffer = BytesIO()

    # Create the PDF object
    pdf = canvas.Canvas(buffer)

    # Write the table header
    pdf.drawString(10, 800, "Name")
    pdf.drawString(100, 800, "age")
    pdf.drawString(200, 800, "department")
    pdf.drawString(350, 800, "emp_start_date")
    pdf.drawString(500, 800, "emp_end_date")

    # Write the table data
    y = 790
    for record in data:
        pdf.drawString(10, y, str(record.name))
        pdf.drawString(100, y, str(record.age))
        pdf.drawString(200, y, str(record.department))
        pdf.drawString(350, y, str(record.emp_start_date))
        pdf.drawString(500, y, str(record.emp_end_date))
        y = y - 20

    # Save the PDF
    pdf.save()

    # Create a FileResponse object with the PDF data
    buffer.seek(0)
    response = FileResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="table.pdf"'

    return response
