# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transporte', '0006_parada_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matriz_Parada',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('valor_time', models.IntegerField(null=True)),
                ('parada1', models.ForeignKey(to='transporte.Parada')),
                ('parada2', models.ForeignKey(related_name='parada2', to='transporte.Parada')),
            ],
        ),
    ]
