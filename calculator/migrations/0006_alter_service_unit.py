# Generated by Django 4.0.5 on 2022-07-02 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0005_alter_service_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='unit',
            field=models.CharField(choices=[('n/a', 'n/a'), ('m2', 'm2'), ('t', 't'), ('h', 'h'), ('km', 'km'), ('m3', 'm3'), ('Item', 'Item')], default='n/a', max_length=15),
        ),
    ]
