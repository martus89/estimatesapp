# Generated by Django 4.0.5 on 2022-07-08 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_info',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]