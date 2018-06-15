# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simulacion', '0003_simulador_peso_ascensor'),
    ]

    operations = [
        migrations.AddField(
            model_name='simulador',
            name='diametro_Piston',
            field=models.FloatField(null=True),
        ),
    ]
