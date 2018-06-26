# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20180528_0609'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user',
            new_name='Leveo',
        ),
        migrations.AlterModelTable(
            name='leveo',
            table='Leveo',
        ),
    ]
