# Generated by Django 3.1.4 on 2021-01-06 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20210106_1421'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checklist',
            old_name='zsłużebność_przesyłu',
            new_name='służebność_przesyłu',
        ),
    ]
