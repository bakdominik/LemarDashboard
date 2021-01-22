# Generated by Django 3.1.4 on 2020-12-14 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20201214_1220'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectInvoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('O', 'Opłacony'), ('D', 'Do opłacenia')], default='D', max_length=1)),
                ('invoice', models.FileField(upload_to='static/invoices/')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.project')),
            ],
        ),
    ]