# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transporte', '0010_auto_20160724_2302'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(unique=True, max_length=15)),
            ],
        ),
        migrations.AlterField(
            model_name='conductor',
            name='cedula',
            field=models.CharField(unique=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='conductor',
            name='telefono',
            field=models.CharField(unique=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='establecimiento',
            name='nombre',
            field=models.CharField(unique=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='parada',
            name='order',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='ruta',
            name='nombre',
            field=models.CharField(unique=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='codigo',
            field=models.CharField(unique=True, max_length=4),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='estado',
            field=models.ForeignKey(to='transporte.Estado'),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='numero_gsm',
            field=models.CharField(unique=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='placa',
            field=models.CharField(unique=True, max_length=7),
        ),
    ]
