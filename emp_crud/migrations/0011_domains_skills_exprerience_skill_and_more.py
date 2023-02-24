# Generated by Django 4.1.6 on 2023-02-24 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emp_crud', '0010_employee_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Domains',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emp_crud.domains')),
            ],
        ),
        migrations.AddField(
            model_name='exprerience',
            name='skill',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='emp_crud.skills'),
        ),
        migrations.AlterField(
            model_name='exprerience',
            name='domain',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emp_crud.domains'),
        ),
    ]