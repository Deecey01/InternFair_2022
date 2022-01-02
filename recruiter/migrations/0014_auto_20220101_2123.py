# Generated by Django 3.1.2 on 2022-01-01 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0013_auto_20220101_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intern_form',
            name='FormStatus',
            field=models.CharField(choices=[('DEACTIVE', 'DEACTIVE'), ('ACTIVE', 'ACTIVE')], default='ACTIVE', max_length=10),
        ),
        migrations.AlterField(
            model_name='internapplication',
            name='Status',
            field=models.CharField(choices=[('SHORTLISTED', 'shortlisted'), ('PENDING', 'pending'), ('REJECTED', 'rejected')], default='PENDING', max_length=20),
        ),
    ]
