from django.db import models
from app.models import Category
# Create your models here.
#
# class User(models.Model):
#
class User(models.Model):
    username = models.CharField(verbose_name='用户名',max_length=30)
    password = models.CharField(verbose_name='密码',max_length=80)
    email = models.EmailField()
    is_login = models.BooleanField(default=False,verbose_name='是否登录')


class Shopcar(models.Model):
    user = models.ForeignKey(User,verbose_name='用户')
    # shoes = models.ForeignKey(Shoes,verbose_name='鞋子')
    count = models.IntegerField(verbose_name='商品数量')
    def __str__(self):
        return self.user+self.id

    class Meta:
        verbose_name = '购物车'
        verbose_name_plural = verbose_name

class History(models.Model):
    user = models.OneToOneField(User, verbose_name='用户')
    shoes = models.CharField(max_length=30, verbose_name='鞋子')
    create_date = models.DateTimeField(verbose_name='创建时间',default=datetime.now)
    last_date = models.DateTimeField(verbose_name='最后一次浏览时间',auto_now = True)

    def __str__(self):
        return self.user + self.id

    class Meta:
        verbose_name = '历史记录'
        verbose_name_plural = verbose_name