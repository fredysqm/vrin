# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20140906_2128'),
    ]

    operations = [
        migrations.CreateModel(
            name='asistencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_hora', models.DateTimeField(auto_now=True)),
                ('evento', models.ForeignKey(verbose_name=b'Evento', to='app.cargo')),
                ('participante', models.ForeignKey(verbose_name=b'Participante', to='app.participante')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='evento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=60)),
                ('cerrado', models.BooleanField(default=False)),
                ('fecha_hora', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
