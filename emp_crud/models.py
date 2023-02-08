from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    emp_start_date = models.DateField(auto_now_add=True)
    emp_end_date = models.DateField()
    photo = models.ImageField(upload_to='static/images')
    options = (
        ('working', 'working'),
        ('resigned', 'resigned')
    )
    status = models.CharField(max_length=100, choices=options, default='working')
