# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transporte', '0012_auto_20160728_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='estado',
            field=models.CharField(max_length=15),
        ),
    ]
