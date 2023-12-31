# Generated by Django 3.2.20 on 2023-08-18 07:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("zgw_consumers", "0019_alter_service_uuid"),
    ]

    operations = [
        migrations.CreateModel(
            name="HaalCentraalHRConfig",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "service",
                    models.OneToOneField(
                        limit_choices_to={"api_type": "orc"},
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to="zgw_consumers.service",
                        verbose_name="Haal Centraal HR API",
                    ),
                ),
            ],
            options={
                "verbose_name": "Haal Centraal HR configuration",
            },
        ),
    ]
