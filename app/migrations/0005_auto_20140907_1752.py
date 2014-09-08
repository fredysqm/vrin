# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20140907_1738'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='asistencia',
            unique_together=set([('evento', 'participante')]),
        ),
    ]
