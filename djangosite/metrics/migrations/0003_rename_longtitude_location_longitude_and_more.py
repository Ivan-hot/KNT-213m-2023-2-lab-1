# Generated by Django 4.2.6 on 2023-11-16 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('metrics', '0002_rename_logtitude_location_longtitude'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='longtitude',
            new_name='longitude',
        ),
        migrations.AlterField(
            model_name='measurement',
            name='description',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='unit',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='timestamps',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='metrics.location'),
        ),
        migrations.AlterField(
            model_name='timestamps',
            name='value',
            field=models.DecimalField(decimal_places=8, max_digits=16),
        ),
        migrations.DeleteModel(
            name='Unit_Mesure',
        ),
    ]