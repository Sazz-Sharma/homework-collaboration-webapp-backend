# Generated by Django 5.0.3 on 2024-05-12 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portal", "0002_remove_portalsubmission_file_path_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="portal",
            name="description",
            field=models.TextField(default=None),
        ),
    ]
