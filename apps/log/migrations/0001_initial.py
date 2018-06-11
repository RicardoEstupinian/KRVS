# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idUsuario', models.CharField(primary_key=True, serialize=False, max_length=10)),
                ('nombre', models.CharField(max_length=25)),
                ('contraseña', models.CharField(max_length=10)),
            ],
        ),
    ]
