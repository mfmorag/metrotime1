# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transporte', '0009_auto_20160723_0941'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conductor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('cedula', models.IntegerField()),
                ('telefono', models.IntegerField()),
                ('correo', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='vehiculo',
            name='estado',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='conductor',
            name='id_vehiculo',
            field=models.ForeignKey(to='transporte.Vehiculo'),
        ),
    ]
