# Generated by Django 4.2.6 on 2023-10-21 08:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("metrics", "0005_timestamps_date_alter_timestamps_time"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="timestamps",
            name="date",
        ),
        migrations.AlterField(
            model_name="timestamps",
            name="time",
            field=models.DateTimeField(),
        ),
    ]