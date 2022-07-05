# Generated by Django 4.0.5 on 2022-07-04 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0009_document_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='name',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='document',
            name='doc_id',
        ),
        migrations.AlterField(
            model_name='document',
            name='date_saved',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='group',
            field=models.CharField(choices=[('Transport', 'Transport'), ('Concrete', 'Concrete'), ('Rental', 'Rental'), ('Paving', 'Paving'), ('Chipping', 'Chipping'), ('Other', 'Other')], default='Other', max_length=15),
        ),
    ]
