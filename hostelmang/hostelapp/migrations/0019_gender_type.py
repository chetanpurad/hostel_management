# Generated by Django 4.2.4 on 2023-09-03 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hostelapp", "0018_alter_studentapplication_hostel_choice"),
    ]

    operations = [
        migrations.CreateModel(
            name="gender_type",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[("1", "Male"), ("2", "Female")], max_length=10
                    ),
                ),
            ],
        ),
    ]
