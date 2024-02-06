# Generated by Django 4.2.4 on 2023-09-26 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("hostelapp", "0030_studentapplication_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="studentapplication",
            name="user",
        ),
        migrations.AlterField(
            model_name="studentapplication",
            name="hostel_choice",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="hostelapp.hostels",
            ),
        ),
    ]
