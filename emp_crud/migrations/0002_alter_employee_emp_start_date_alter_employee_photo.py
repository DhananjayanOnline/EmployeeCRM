# Generated by Django 4.1.6 on 2023-02-10 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_crud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_start_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='employee',
            name='photo',
            field=models.ImageField(upload_to='media/images'),
        ),
    ]
