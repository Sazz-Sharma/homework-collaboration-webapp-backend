# Generated by Django 5.0.3 on 2024-05-15 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mcq", "0003_collections_description_collections_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="collections",
            name="description",
            field=models.TextField(default=None, null=True),
        ),
    ]