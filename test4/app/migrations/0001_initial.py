# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaInfo',
            fields=[
                ('aid', models.IntegerField(primary_key=True, serialize=False)),
                ('atitle', models.CharField(max_length=20)),
                ('aPArea', models.ForeignKey(null=True, to='app.AreaInfo')),
            ],
        ),
    ]
