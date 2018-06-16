# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simulacion', '0006_polea'),
    ]

    operations = [
        migrations.AddField(
            model_name='ascensor',
            name='polea',
            field=models.ForeignKey(null=True, blank=True, to='simulacion.Polea'),
        ),
    ]
