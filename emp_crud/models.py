from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
# Create your models here.

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=200, default='x')
    password = models.CharField(max_length=200, default='x')
    address = models.CharField(max_length=200, null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
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
    department = models.CharField(max_length=200, choices=depts, default=None, null=True, blank=True)
    emp_start_date = models.DateField(null=True, blank=True)
    emp_end_date = models.DateField(null=True, blank=True)
    salary = models.PositiveIntegerField(null=True, blank=True)
    photo = models.ImageField(upload_to='media/images', null=True, blank=True)
    options = (
        ('working', 'working'),
        ('resigned', 'resigned')
    )
    status = models.CharField(max_length=100, choices=options, default='working', null=True, blank=True)

    @classmethod
    def get_salary_sum(cls):
        return cls.objects.aggregate(Sum('salary'))['salary__sum']

    @property
    def imageURL(self):
        if self.photo:
            return self.photo.url
        else:
            return ""


class Exprerience(models.Model):
    emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    domain = models.CharField(max_length=200)
    years_of_expre = models.IntegerField()
    description = models.TextField(max_length=400)

    def __self__(self):
        return self.emp_id.name