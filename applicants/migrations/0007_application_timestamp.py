# Generated by Django 4.2.4 on 2023-12-16 14:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("applicants", "0006_alter_application_options_testimony"),
    ]

    operations = [
        migrations.AddField(
            model_name="application",
            name="timestamp",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
