# Generated by Django 4.1.13 on 2024-05-01 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0013_remove_outerrepeater_inner_repeater_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Bird",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("common_name", models.CharField(max_length=250)),
                ("scientific_name", models.CharField(max_length=250)),
            ],
        ),
    ]
