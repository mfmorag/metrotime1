# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transporte', '0014_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='estado',
            field=models.ForeignKey(to='transporte.Estado'),
        ),
    ]
