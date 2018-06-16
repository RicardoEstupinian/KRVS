# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simulacion', '0009_auto_20180616_1011'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipopiston',
            name='aceite',
            field=models.FloatField(null=True),
        ),
    ]
