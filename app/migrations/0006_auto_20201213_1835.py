# Generated by Django 3.1.4 on 2020-12-13 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20201213_1830'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checklist',
            name='id',
        ),
        migrations.RemoveField(
            model_name='project',
            name='checklist',
        ),
        migrations.AddField(
            model_name='checklist',
            name='project',
            field=models.OneToOneField(default=False, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='app.project'),
            preserve_default=False,
        ),
    ]
