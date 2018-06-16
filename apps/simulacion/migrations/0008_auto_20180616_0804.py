# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simulacion', '0007_ascensor_polea'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ascensor',
            old_name='polea',
            new_name='Polea',
        ),
    ]
