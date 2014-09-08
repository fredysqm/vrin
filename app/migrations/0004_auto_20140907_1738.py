# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_asistencia_evento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asistencia',
            name='evento',
            field=models.ForeignKey(verbose_name=b'Evento', to='app.evento'),
        ),
    ]
