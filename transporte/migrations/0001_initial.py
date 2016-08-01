# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BUN',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('placa', models.CharField(max_length=7)),
                ('numero_gsm', models.IntegerField()),
                ('codigo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BusParada',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_bus', models.ForeignKey(to='transporte.Bus')),
            ],
        ),
        migrations.CreateModel(
            name='Notificacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('detalle', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Parada',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=7)),
                ('latitud', models.DecimalField(max_digits=15, decimal_places=10)),
                ('longitud', models.DecimalField(max_digits=15, decimal_places=10)),
            ],
        ),
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('latitud', models.DecimalField(max_digits=15, decimal_places=10)),
                ('longitud', models.DecimalField(max_digits=15, decimal_places=10)),
                ('velocidad', models.DecimalField(max_digits=6, decimal_places=3)),
                ('id_bus', models.ForeignKey(to='transporte.Bus')),
            ],
        ),
        migrations.AddField(
            model_name='busparada',
            name='id_parada',
            field=models.ForeignKey(to='transporte.Parada'),
        ),
        migrations.AddField(
            model_name='bun',
            name='id_bus',
            field=models.ForeignKey(to='transporte.Bus'),
        ),
        migrations.AddField(
            model_name='bun',
            name='id_notificacion',
            field=models.ForeignKey(to='transporte.Notificacion'),
        ),
        migrations.AddField(
            model_name='bun',
            name='id_ubicacion',
            field=models.ForeignKey(to='transporte.Ubicacion'),
        ),
    ]
