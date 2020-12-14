# Generated by Django 3.1.4 on 2020-12-14 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20201213_1844'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='project_files/')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.project')),
            ],
        ),
    ]
