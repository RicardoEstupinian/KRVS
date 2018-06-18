# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simulacion', '0010_tipopiston_aceite'),
    ]

    operations = [
        migrations.AddField(
            model_name='ascensor',
            name='simulador',
            field=models.OneToOneField(blank=True, null=True, to='simulacion.Simulador'),
        ),
    ]
