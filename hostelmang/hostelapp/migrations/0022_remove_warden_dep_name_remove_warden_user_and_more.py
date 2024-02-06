# Generated by Django 4.2.4 on 2023-09-13 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hostelapp", "0021_course_type"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="warden",
            name="dep_name",
        ),
        migrations.RemoveField(
            model_name="warden",
            name="user",
        ),
        migrations.AddField(
            model_name="warden",
            name="password",
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]