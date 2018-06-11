# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ascensor',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('carga_Nominal', models.FloatField(null=True)),
                ('superficie', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CableDeSuspension',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('diametro', models.FloatField(null=True)),
                ('diametro_Efectivo', models.FloatField(null=True)),
                ('peso_Cable', models.FloatField(null=True)),
                ('carga_Rotura_Resestencia140', models.FloatField(null=True)),
                ('carga_Rotura_Resestencia160', models.FloatField(null=True)),
                ('carga_Rotura_Resestencia180', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Piston',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('masa_Lineal_Vastago', models.FloatField(null=True)),
                ('diametro_Exterior', models.FloatField(null=True)),
                ('masa_Union_Vastago', models.FloatField(null=True)),
                ('area_Resistente_Embolo', models.FloatField(null=True)),
                ('radio_Giro_Embolo', models.FloatField(null=True)),
                ('resistencia_Traccion_Acero', models.FloatField(null=True)),
                ('momento_Inercia', models.FloatField(null=True)),
                ('factor_Diametro', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PistonTelescopico',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('masa_Embolo', models.FloatField(null=True)),
                ('diametro_Exterior_di', models.FloatField(null=True)),
                ('longitud_Total', models.FloatField(null=True)),
                ('masa_Total', models.FloatField(null=True)),
                ('diametro_Interior_Camisa', models.FloatField(null=True)),
                ('masa_Cabezal', models.FloatField(null=True)),
                ('resistencia_Traccion_Acero', models.FloatField(null=True)),
                ('factor_Diametro_Tu', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Simulador',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('numero_Cables', models.IntegerField(null=True)),
                ('carga_Nominal', models.FloatField(null=True)),
                ('recorrido_Cabina', models.FloatField(null=True)),
                ('recorido_Superior_Piston', models.FloatField(null=True)),
                ('cantidad_Pistones', models.IntegerField(null=True)),
                ('cantidad_Cilindros', models.IntegerField(null=True)),
                ('numero_Expanciones', models.IntegerField(null=True)),
                ('velocidad_Cabina', models.FloatField(null=True)),
                ('diametro_Cable', models.FloatField(null=True)),
                ('usuario', models.ForeignKey(null=True, blank=True, to='log.Usuario')),
            ],
        ),
        migrations.AddField(
            model_name='ascensor',
            name='cable',
            field=models.ForeignKey(null=True, blank=True, to='simulacion.CableDeSuspension'),
        ),
        migrations.AddField(
            model_name='ascensor',
            name='piston',
            field=models.ForeignKey(null=True, blank=True, to='simulacion.Piston'),
        ),
        migrations.AddField(
            model_name='ascensor',
            name='piston_Telescopico',
            field=models.ForeignKey(null=True, blank=True, to='simulacion.PistonTelescopico'),
        ),
    ]
