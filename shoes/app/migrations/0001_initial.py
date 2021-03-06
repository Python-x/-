# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-26 11:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner_shoe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='鞋子的名字')),
                ('money', models.CharField(max_length=30, verbose_name='鞋子的价格')),
                ('content', models.TextField(verbose_name='产品详情')),
                ('cover', models.ImageField(blank=True, upload_to='static/images/', verbose_name='封面图片')),
            ],
            options={
                'verbose_name': '广告轮播图位',
                'verbose_name_plural': '广告轮播图位',
            },
        ),
        migrations.CreateModel(
            name='Brank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('btitle', models.CharField(max_length=30, verbose_name='品牌名称')),
                ('bcontent', models.TextField(verbose_name='品牌详情')),
            ],
            options={
                'verbose_name': '品牌',
                'verbose_name_plural': '品牌',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ctitle', models.CharField(max_length=30, verbose_name='分类名称')),
            ],
            options={
                'verbose_name': '分类',
                'verbose_name_plural': '分类',
            },
        ),
        migrations.CreateModel(
            name='Detail_pic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(blank=True, upload_to='static/images/', verbose_name='图片')),
            ],
            options={
                'verbose_name': '详情图片',
                'verbose_name_plural': '详情图片',
            },
        ),
        migrations.CreateModel(
            name='Grand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grand', models.IntegerField(verbose_name='评分')),
                ('user', models.CharField(max_length=30, verbose_name='评分用户')),
            ],
            options={
                'verbose_name': '评分',
                'verbose_name_plural': '评分',
            },
        ),
        migrations.CreateModel(
            name='Shoes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='鞋子的名字')),
                ('money', models.CharField(max_length=30, verbose_name='鞋子的价格')),
                ('content', models.TextField(verbose_name='产品详情')),
                ('cover', models.ImageField(blank=True, upload_to='static/images/', verbose_name='封面图片')),
                ('views', models.IntegerField(default=1, verbose_name='浏览量')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Brank', verbose_name='品牌')),
                ('category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app.Category', verbose_name='分类')),
            ],
            options={
                'verbose_name': '鞋子',
                'verbose_name_plural': '鞋子',
            },
        ),
        migrations.AddField(
            model_name='detail_pic',
            name='shoe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Shoes', verbose_name='详情外键图片'),
        ),
        migrations.AddField(
            model_name='banner_shoe',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Brank', verbose_name='品牌'),
        ),
        migrations.AddField(
            model_name='banner_shoe',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app.Category', verbose_name='分类'),
        ),
    ]
