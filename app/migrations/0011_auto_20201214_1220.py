# Generated by Django 3.1.4 on 2020-12-14 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20201214_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectfile',
            name='file',
            field=models.FileField(upload_to='static/project_files/'),
        ),
    ]
