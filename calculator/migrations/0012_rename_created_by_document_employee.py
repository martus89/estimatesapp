# Generated by Django 4.0.5 on 2022-07-05 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0011_employee_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='created_by',
            new_name='employee',
        ),
    ]