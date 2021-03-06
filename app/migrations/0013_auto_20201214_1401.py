# Generated by Django 3.1.4 on 2020-12-14 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_projectinvoice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectfile',
            name='file',
            field=models.FileField(upload_to='core/static/project_files/'),
        ),
        migrations.AlterField(
            model_name='projectinvoice',
            name='invoice',
            field=models.FileField(upload_to='core/static/invoices/'),
        ),
    ]
