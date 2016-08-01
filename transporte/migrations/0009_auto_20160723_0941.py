# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transporte', '0008_auto_20160722_2122'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pline',
            old_name='id_parada',
            new_name='parada',
        ),
    ]
