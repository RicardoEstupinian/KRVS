# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Acero',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo_Acero', models.FloatField(null=True)),
                ('normal', models.FloatField(null=True)),
                ('mecanico', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ascensor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('carga_Nominal', models.FloatField(null=True)),
                ('superficie', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CableDeSuspension',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
            name='Polea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('diametro', models.FloatField(null=True)),
                ('peso', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Simulador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero_Cables', models.FloatField(null=True)),
                ('carga_Nominal', models.FloatField(null=True)),
                ('recorrido_Cabina', models.FloatField()),
                ('recorido_Superior_Piston', models.FloatField(null=True)),
                ('cantidad_Pistones', models.IntegerField(null=True)),
                ('cantidad_Cilindros', models.IntegerField(null=True)),
                ('numero_Expanciones', models.IntegerField(null=True)),
                ('velocidad_Cabina', models.FloatField(null=True)),
                ('diametro_Cable', models.FloatField(null=True)),
                ('peso_Ascensor', models.FloatField(null=True)),
                ('diametro_Piston', models.FloatField(null=True)),
                ('masa_Embolo', models.FloatField(null=True)),
                ('usuario', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TipoPiston',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('area_Embolo', models.FloatField(null=True)),
                ('longitud_Embolo', models.FloatField(null=True)),
                ('radio_Giro', models.FloatField(null=True)),
                ('momento_De_Inercia', models.FloatField(null=True)),
                ('aceite', models.FloatField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='ascensor',
            name='Polea',
            field=models.ForeignKey(to='simulacion.Polea', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ascensor',
            name='acero',
            field=models.ForeignKey(to='simulacion.Acero', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ascensor',
            name='cable',
            field=models.ForeignKey(to='simulacion.CableDeSuspension', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ascensor',
            name='piston',
            field=models.ForeignKey(to='simulacion.Piston', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ascensor',
            name='piston_Telescopico',
            field=models.ForeignKey(to='simulacion.PistonTelescopico', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ascensor',
            name='simulador',
            field=models.OneToOneField(to='simulacion.Simulador', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ascensor',
            name='tipoPiston',
            field=models.ForeignKey(to='simulacion.TipoPiston', blank=True, null=True),
        ),
    ]
