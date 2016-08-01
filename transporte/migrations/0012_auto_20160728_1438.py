# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transporte', '0011_auto_20160728_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='estado',
            field=models.CharField(unique=True, max_length=15),
        ),
        migrations.DeleteModel(
            name='Estado',
        ),
    ]
