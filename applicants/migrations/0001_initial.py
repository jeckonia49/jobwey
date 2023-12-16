# Generated by Django 4.2.4 on 2023-12-14 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("companies", "0006_company_vision"),
        ("account", "0002_accountuser_agree_to_terms"),
    ]

    operations = [
        migrations.CreateModel(
            name="Applicant",
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
                    "skills",
                    models.CharField(
                        blank=True,
                        help_text="separate multiple skills with a comma",
                        max_length=1000,
                        null=True,
                    ),
                ),
                (
                    "job",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="job_applicant",
                        to="companies.job",
                    ),
                ),
                (
                    "profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profile_applicant",
                        to="account.profile",
                    ),
                ),
            ],
        ),
    ]