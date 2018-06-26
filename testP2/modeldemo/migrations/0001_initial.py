# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('cname', models.CharField(max_length=30)),
                ('cnumber', models.IntegerField()),
                ('cmajor', models.CharField(max_length=30)),
                ('isDelete', models.BooleanField(default=0)),
            ],
            options={
                'db_table': '学院表',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('sname', models.CharField(max_length=30)),
                ('ssex', models.BooleanField(default=1)),
                ('sdate', models.DateTimeField()),
                ('isDelete', models.BooleanField(default=0)),
                ('swj', models.ForeignKey(to='modeldemo.College')),
            ],
            options={
                'db_table': '学生表',
                'ordering': ['-id'],
            },
        ),
    ]
