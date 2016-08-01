# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transporte', '0007_matriz_parada'),
    ]

    operations = [
        migrations.CreateModel(
            name='PLine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('latitud', models.CharField(max_length=10)),
                ('longitud', models.CharField(max_length=10)),
                ('id_parada', models.ForeignKey(to='transporte.Parada')),
            ],
        ),
        migrations.RemoveField(
            model_name='matriz_parada',
            name='parada1',
        ),
        migrations.RemoveField(
            model_name='matriz_parada',
            name='parada2',
        ),
        migrations.DeleteModel(
            name='Matriz_Parada',
        ),
    ]
