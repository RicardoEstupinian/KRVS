# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simulacion', '0008_auto_20180616_0804'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acero',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('tipo_Acero', models.FloatField(null=True)),
                ('normal', models.FloatField(null=True)),
                ('mecanico', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoPiston',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('area_Embolo', models.FloatField(null=True)),
                ('longitud_Embolo', models.FloatField(null=True)),
                ('radio_Giro', models.FloatField(null=True)),
                ('momento_De_Inercia', models.FloatField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='ascensor',
            name='acero',
            field=models.ForeignKey(null=True, to='simulacion.Acero', blank=True),
        ),
        migrations.AddField(
            model_name='ascensor',
            name='tipoPiston',
            field=models.ForeignKey(null=True, to='simulacion.TipoPiston', blank=True),
        ),
    ]
