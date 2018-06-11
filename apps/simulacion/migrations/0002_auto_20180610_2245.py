# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simulacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simulador',
            name='numero_Cables',
            field=models.FloatField(null=True),
        ),
    ]
