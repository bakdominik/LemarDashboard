# Generated by Django 3.1.4 on 2021-01-22 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('W', 'W trakcie'), ('Z', 'Zakończony'), ('P', 'Przerwany')], default='W', max_length=30),
        ),
    ]