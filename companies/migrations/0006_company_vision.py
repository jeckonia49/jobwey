# Generated by Django 4.2.4 on 2023-12-14 12:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("companies", "0005_job_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="company",
            name="vision",
            field=models.CharField(
                default="Digital Marketing Solutions for Tomorrow", max_length=100
            ),
        ),
    ]