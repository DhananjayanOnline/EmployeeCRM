# Generated by Django 4.1.6 on 2023-02-12 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_crud', '0005_remove_employee_position_alter_employee_age_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]