# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transporte', '0002_auto_20160710_1858'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bun',
            name='id_bus',
        ),
        migrations.RemoveField(
            model_name='bun',
            name='id_notificacion',
        ),
        migrations.RemoveField(
            model_name='bun',
            name='id_ubicacion',
        ),
        migrations.RemoveField(
            model_name='busparada',
            name='id_bus',
        ),
        migrations.RemoveField(
            model_name='busparada',
            name='id_parada',
        ),
        migrations.RemoveField(
            model_name='ubicacion',
            name='id_bus',
        ),
        migrations.AlterField(
            model_name='administrador',
            name='apellido',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='administrador',
            name='nombre',
            field=models.CharField(max_length=30),
        ),
        migrations.DeleteModel(
            name='BUN',
        ),
        migrations.DeleteModel(
            name='Bus',
        ),
        migrations.DeleteModel(
            name='BusParada',
        ),
        migrations.DeleteModel(
            name='Notificacion',
        ),
        migrations.DeleteModel(
            name='Parada',
        ),
        migrations.DeleteModel(
            name='Ubicacion',
        ),
    ]
