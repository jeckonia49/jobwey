# Generated by Django 4.2.4 on 2023-12-14 15:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0002_accountuser_agree_to_terms"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="banner_photo",
            field=models.ImageField(blank=True, null=True, upload_to="banner/"),
        ),
    ]
