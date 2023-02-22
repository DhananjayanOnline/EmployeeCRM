from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    age = models.PositiveIntegerField()
    depts = (
        ('Accounts and Finance', 'Accounts and Finance'),
        ('HR', 'HR'),
        ('Sales and marketing', 'Sales and marketing'),
        ('Infrastructures', 'Infrastructures'),
        ('Research and development', 'Research and development'),
        ('IT services', 'IT services'),
        ('Product development', 'Product development'),
        ('Security and transport', 'Security and transport'),
    )
    department = models.CharField(max_length=200, choices=depts, default=None)
    emp_start_date = models.DateField(null=True, blank=True)
    emp_end_date = models.DateField(null=True, blank=True)
    salary = models.PositiveIntegerField()
    photo = models.ImageField(upload_to='media/images')
    options = (
        ('working', 'working'),
        ('resigned', 'resigned')
    )
    status = models.CharField(max_length=100, choices=options, default='working')

    @classmethod
    def get_salary_sum(cls):
        return cls.objects.aggregate(Sum('salary'))['salary__sum']


class Exprerience(models.Model):
    emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    domain = models.CharField(max_length=200)
    years_of_expre = models.IntegerField()
    description = models.TextField(max_length=400)

    def __self__(self):
        return self.emp_id.name