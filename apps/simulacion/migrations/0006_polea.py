# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simulacion', '0005_simulador_masa_embolo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Polea',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('diametro', models.FloatField(null=True)),
                ('peso', models.FloatField(null=True)),
            ],
        ),
    ]
