# Generated by Django 4.2.4 on 2023-12-13 16:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="accountuser",
            name="agree_to_terms",
            field=models.BooleanField(default=False),
        ),
    ]
