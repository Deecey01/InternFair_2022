# Generated by Django 4.1.4 on 2022-12-30 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recruiter", "0014_auto_20220101_2123"),
    ]

    operations = [
        migrations.AlterField(
            model_name="internapplication",
            name="Status",
            field=models.CharField(
                choices=[
                    ("PENDING", "pending"),
                    ("SHORTLISTED", "shortlisted"),
                    ("REJECTED", "rejected"),
                ],
                default="PENDING",
                max_length=20,
            ),
        ),
    ]
