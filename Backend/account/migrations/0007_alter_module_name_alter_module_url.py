# Generated by Django 5.0.3 on 2024-04-29 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0006_businessprofile_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="module",
            name="name",
            field=models.CharField(
                choices=[
                    ("product Report", "/product/product-report/"),
                    ("session Report", "/product/product-report/"),
                ],
                max_length=50,
                null=True,
                verbose_name="Page URL",
            ),
        ),
        migrations.AlterField(
            model_name="module",
            name="url",
            field=models.CharField(
                choices=[
                    ("/product/product/", "product"),
                    ("/product/product/", "session"),
                ],
                max_length=150,
                null=True,
                verbose_name="Page Name",
            ),
        ),
    ]
