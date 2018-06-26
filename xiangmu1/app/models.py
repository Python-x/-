from django.db import models
from django.utils.timezone import datetime
from user.models import *


# Create your models here.
class Category(models.Model):
    ctitle = models.CharField(verbose_name='分类名称', max_length=30)

    def __str__(self):
        return self.ctitle

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name


class Brank(models.Model):
    btitle = models.CharField(verbose_name='品牌名称', max_length=30)
    bcontent = models.TextField(verbose_name='品牌详情')

    def __str__(self):
        return self.btitle

    class Meta:
        verbose_name = '品牌'
        verbose_name_plural = verbose_name


class Shoes(models.Model):
    name = models.CharField(verbose_name='鞋子的名字', max_length=30)
    money = models.CharField(verbose_name='鞋子的价格', max_length=30)
    brand = models.ForeignKey(Brank, verbose_name='品牌')
    content = models.TextField(verbose_name='产品详情')
    category = models.ForeignKey(Category, verbose_name='分类', blank=True)
    cover = models.ImageField(verbose_name='封面图片', upload_to='static/images/', blank=True)
    views = models.IntegerField(verbose_name='浏览量', default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '鞋子'
        verbose_name_plural = verbose_name


class Detail_pic(models.Model):
    shoe = models.ForeignKey(Shoes, verbose_name='详情外键图片')
    pic = models.ImageField(verbose_name='图片', blank=True, upload_to='static/images/')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = '详情图片'
        verbose_name_plural = verbose_name


class Banner_shoe(models.Model):
    name = models.CharField(verbose_name='鞋子的名字', max_length=30)
    money = models.CharField(verbose_name='鞋子的价格', max_length=30)
    brand = models.ForeignKey(Brank, verbose_name='品牌')
    content = models.TextField(verbose_name='产品详情')
    cover = models.ImageField(verbose_name='封面图片', upload_to='static/images/', blank=True)
    category = models.ForeignKey(Category, verbose_name='分类', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '广告轮播图位'
        verbose_name_plural = verbose_name


class Grand(models.Model):
    grand = models.IntegerField(verbose_name='评分')
    user = models.CharField(verbose_name='评分用户', max_length=30)

    def __str__(self):
        return self.user + self.id

    class Meta:
        verbose_name = '评分'
        verbose_name_plural = verbose_name
