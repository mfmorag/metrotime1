# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transporte', '0005_auto_20160718_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='parada',
            name='order',
            field=models.IntegerField(null=True),
        ),
    ]
