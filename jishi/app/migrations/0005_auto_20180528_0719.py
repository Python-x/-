# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mm',
            field=models.CharField(max_length=50),
        ),
    ]
