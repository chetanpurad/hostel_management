# Generated by Django 4.2.4 on 2023-09-26 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hostelapp", "0034_alter_studentapplication_hostel_choice"),
    ]

    operations = [
        migrations.AddField(
            model_name="studentapplication",
            name="user_id",
            field=models.CharField(default=2, max_length=20, unique=True),
            preserve_default=False,
        ),
    ]
