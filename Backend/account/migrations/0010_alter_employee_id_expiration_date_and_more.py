# Generated by Django 4.1.13 on 2024-04-30 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_alter_sessionschedule_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='id_expiration_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='joining_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='passport_expiration_date',
            field=models.DateField(null=True),
        ),
    ]
