# Generated by Django 4.2.6 on 2023-11-16 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metrics', '0004_alter_measurement_description_alter_measurement_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timestamps',
            name='value',
            field=models.CharField(max_length=255),
        ),
    ]
