# Generated by Django 4.2.4 on 2023-09-27 03:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("hostelapp", "0038_remove_warden_dep_id_delete_roomstudentmapping"),
    ]

    operations = [
        migrations.AlterField(
            model_name="studentapplication",
            name="hostel_choice",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="hostelapp.hostels"
            ),
        ),
    ]
