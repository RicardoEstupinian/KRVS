# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simulacion', '0002_auto_20180610_2245'),
    ]

    operations = [
        migrations.AddField(
            model_name='simulador',
            name='peso_Ascensor',
            field=models.FloatField(null=True),
        ),
    ]
