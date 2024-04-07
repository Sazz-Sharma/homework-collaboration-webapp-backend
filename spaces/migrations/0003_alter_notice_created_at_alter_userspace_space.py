# Generated by Django 5.0.3 on 2024-03-31 18:35

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("spaces", "0002_alter_notice_noticeid_alter_notice_created_at_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="notice",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 3, 31, 18, 35, 46, 136193, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="userspace",
            name="space",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="spaces.space",
                to_field="spaceId",
            ),
        ),
    ]