# Generated by Django 4.1.13 on 2024-05-01 04:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0012_innerrepeater_outerrepeater"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="outerrepeater",
            name="inner_repeater",
        ),
        migrations.AddField(
            model_name="innerrepeater",
            name="outer_repeater",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="account.outerrepeater",
            ),
            preserve_default=False,
        ),
    ]
