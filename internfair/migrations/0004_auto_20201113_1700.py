# Generated by Django 3.1.2 on 2020-11-13 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internfair', '0003_auto_20201113_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startups',
            name='contact',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='students',
            name='contact',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='students',
            name='email',
            field=models.EmailField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='students',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='students',
            name='roll_number',
            field=models.CharField(default='', max_length=13),
        ),
    ]
