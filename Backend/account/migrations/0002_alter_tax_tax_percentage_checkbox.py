# Generated by Django 4.1.13 on 2024-04-26 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tax',
            name='tax_percentage_checkbox',
            field=models.BooleanField(default=True),
        ),
    ]