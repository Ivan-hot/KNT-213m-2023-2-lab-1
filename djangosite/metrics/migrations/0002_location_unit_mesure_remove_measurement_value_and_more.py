# Generated by Django 4.2.6 on 2023-10-20 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('metrics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('latitude', models.FloatField()),
                ('logtitude', models.FloatField()),
                ('altitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Unit_Mesure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='measurement',
            name='value',
        ),
        migrations.AddField(
            model_name='measurement',
            name='name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='measurement',
            name='description',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Timestamps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('time', models.DateTimeField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metrics.location')),
                ('measurement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metrics.measurement')),
            ],
        ),
        migrations.AddField(
            model_name='measurement',
            name='unit',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='metrics.unit_mesure'),
            preserve_default=False,
        ),
    ]