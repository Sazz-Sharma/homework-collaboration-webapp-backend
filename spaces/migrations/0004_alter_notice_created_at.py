# Generated by Django 5.0.3 on 2024-04-01 06:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("spaces", "0003_alter_notice_created_at_alter_userspace_space"),
    ]

    operations = [
        migrations.AlterField(
            model_name="notice",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 4, 1, 6, 58, 49, 37507, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]