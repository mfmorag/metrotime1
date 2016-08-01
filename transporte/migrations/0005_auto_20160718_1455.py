# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transporte', '0004_auto_20160718_1438'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='administrador',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='Administrador',
        ),
    ]
