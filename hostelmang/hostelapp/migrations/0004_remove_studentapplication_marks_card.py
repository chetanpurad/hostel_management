# Generated by Django 4.2.4 on 2023-08-20 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("hostelapp", "0003_alter_studentapplication_table"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="studentapplication",
            name="marks_card",
        ),
    ]
