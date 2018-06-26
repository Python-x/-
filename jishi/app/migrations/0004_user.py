# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20180528_0623'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('zhe', models.CharField(unique=True, max_length=20)),
                ('mm', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'User1',
            },
        ),
    ]
