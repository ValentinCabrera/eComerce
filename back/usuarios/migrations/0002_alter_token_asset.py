# Generated by Django 4.1.2 on 2023-08-17 03:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("usuarios", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="token",
            name="asset",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 8, 18, 3, 54, 21, 783228)
            ),
        ),
    ]
