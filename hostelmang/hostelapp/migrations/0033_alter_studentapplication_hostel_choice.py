# Generated by Django 4.2.4 on 2023-09-26 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("hostelapp", "0032_alter_studentapplication_hostel_choice"),
    ]

    operations = [
        migrations.AlterField(
            model_name="studentapplication",
            name="hostel_choice",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="StudentApplication",
                to="hostelapp.hostels",
            ),
        ),
    ]
