# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-29 00:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sensor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlameMsg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wavelength', models.FloatField(null=True)),
                ('pub_time', models.DateField(auto_now_add=True, null=True)),
                ('status', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('flameSensor',),
            },
        ),
        migrations.AlterModelOptions(
            name='flamesensor',
            options={'ordering': ('deviceId',)},
        ),
        migrations.AddField(
            model_name='flamesensor',
            name='create_time',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='flamesensor',
            name='max_wavelength',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='flamesensor',
            name='type',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='temperaturemsg',
            name='temperatureSensor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='temperatureMsgs', to='sensor.TemperatureSensor'),
        ),
        migrations.AddField(
            model_name='flamemsg',
            name='flameSensor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sensor.FlameSensor'),
        ),
    ]
