# Generated by Django 3.1.4 on 2020-12-14 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20201214_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectfile',
            name='file',
            field=models.FileField(upload_to='C:\\Users\\domin\\Documents\\Programowanie\\DjangoDashboard\\staticfiles/project_files/'),
        ),
        migrations.AlterField(
            model_name='projectinvoice',
            name='invoice',
            field=models.FileField(upload_to='C:\\Users\\domin\\Documents\\Programowanie\\DjangoDashboard\\staticfiles/invoices/'),
        ),
    ]
