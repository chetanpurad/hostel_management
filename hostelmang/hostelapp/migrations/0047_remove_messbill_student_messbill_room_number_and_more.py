# Generated by Django 4.2.4 on 2023-10-03 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "hostelapp",
            "0046_remove_messbill_amount_remove_messbill_uploaded_bill_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="messbill",
            name="student",
        ),
        migrations.AddField(
            model_name="messbill",
            name="room_number",
            field=models.IntegerField(default=1, max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="messbill",
            name="student_name",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]