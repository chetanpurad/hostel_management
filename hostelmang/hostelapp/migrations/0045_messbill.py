# Generated by Django 4.2.4 on 2023-10-03 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("hostelapp", "0044_complaint_complaint_status_complaint_hostel_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="MessBill",
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
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "uploaded_bill",
                    models.FileField(blank=True, null=True, upload_to="mess_bills/"),
                ),
                ("is_paid", models.BooleanField(default=False)),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hostelapp.studentapplication",
                    ),
                ),
            ],
        ),
    ]
