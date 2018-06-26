# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-24 05:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shoes', models.CharField(max_length=30, verbose_name='鞋子')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.User', verbose_name='用户')),
            ],
            options={
                'verbose_name_plural': '历史记录',
                'verbose_name': '历史记录',
            },
        ),
        migrations.AlterField(
            model_name='shopcar',
            name='shoes',
            field=models.CharField(max_length=30, verbose_name='鞋子'),
        ),
    ]
