# Generated by Django 4.0.5 on 2022-07-02 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0002_remove_service_digital'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]