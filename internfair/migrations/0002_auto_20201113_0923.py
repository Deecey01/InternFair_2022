# Generated by Django 3.1.2 on 2020-11-13 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('internfair', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='startups',
            name='companyName',
        ),
        migrations.RemoveField(
            model_name='students',
            name='department',
        ),
    ]
