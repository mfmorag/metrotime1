# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transporte', '0003_auto_20160716_1604'),
    ]

    operations = [
        migrations.CreateModel(
            name='Establecimiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Parada',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('latitud', models.CharField(max_length=10)),
                ('longitud', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='RLine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('latitud', models.CharField(max_length=10)),
                ('longitud', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Ruta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('id_est', models.ForeignKey(to='transporte.Establecimiento')),
            ],
        ),
        migrations.CreateModel(
            name='RutaVehiculo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_ruta', models.ForeignKey(to='transporte.Ruta')),
            ],
        ),
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('latitud', models.CharField(max_length=10)),
                ('longitud', models.CharField(max_length=10)),
                ('velocidad', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('placa', models.CharField(max_length=7)),
                ('numero_gsm', models.IntegerField()),
                ('codigo', models.IntegerField()),
                ('id_est', models.ForeignKey(to='transporte.Establecimiento')),
            ],
        ),
        migrations.AddField(
            model_name='ubicacion',
            name='id_vehiculo',
            field=models.ForeignKey(to='transporte.Vehiculo'),
        ),
        migrations.AddField(
            model_name='rutavehiculo',
            name='id_vehiculo',
            field=models.ForeignKey(to='transporte.Vehiculo'),
        ),
        migrations.AddField(
            model_name='rline',
            name='id_ruta',
            field=models.ForeignKey(to='transporte.Ruta'),
        ),
        migrations.AddField(
            model_name='parada',
            name='id_ruta',
            field=models.ForeignKey(to='transporte.Ruta'),
        ),
    ]
