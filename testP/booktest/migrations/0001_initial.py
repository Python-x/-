# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookinfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('btitle', models.CharField(max_length=30)),
                ('bpub_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Heroinfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('hname', models.CharField(max_length=30)),
                ('hgender', models.BooleanField(verbose_name=1)),
                ('hcontent', models.TextField()),
                ('hBook', models.ForeignKey(to='booktest.Bookinfo')),
            ],
        ),
    ]
