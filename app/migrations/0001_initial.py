# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cargo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=60)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='grado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=60)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='participante',
            fields=[
                ('dni', models.CharField(max_length=8, serialize=False, verbose_name=b'DNI', primary_key=True)),
                ('paterno', models.CharField(max_length=80, verbose_name=b'Apellido Paterno')),
                ('materno', models.CharField(max_length=80, verbose_name=b'Apellido Materno')),
                ('nombre', models.CharField(max_length=100, verbose_name=b'Nombre(s)')),
                ('edad', models.SmallIntegerField(verbose_name=b'Edad')),
                ('direccion', models.CharField(max_length=140, verbose_name=b'Direcci\xc3\xb3n')),
                ('email', models.EmailField(max_length=75, verbose_name=b'Email')),
                ('fijo', models.CharField(max_length=12, verbose_name=b'Tel\xc3\xa9fono Fijo')),
                ('movil', models.CharField(max_length=12, verbose_name=b'Tel\xc3\xa9fono Movil')),
                ('facultad', models.CharField(max_length=140, verbose_name=b'Facultad')),
                ('carrera', models.CharField(max_length=140, verbose_name=b'Carrera')),
                ('titulo', models.CharField(max_length=140, verbose_name=b'T\xc3\xadtulo')),
                ('investigacion', models.TextField(verbose_name=b'Trabajos de Investigaci\xc3\xb3n')),
                ('ingreso', models.DateField(auto_now=True)),
                ('cargo', models.ForeignKey(verbose_name=b'Cargo', to='app.cargo')),
                ('grado', models.ForeignKey(verbose_name=b'Grado', to='app.grado')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='universidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=140)),
            ],
            options={
                'verbose_name': 'universidad',
                'verbose_name_plural': 'universidades',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='participante',
            name='universidad',
            field=models.ForeignKey(verbose_name=b'Universidad', to='app.universidad'),
            preserve_default=True,
        ),
    ]
