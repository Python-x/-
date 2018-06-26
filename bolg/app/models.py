from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200,null=False,default='请添加标题')
    content = models.TextField()
    pub_datetime = models.DateTimeField(auto_now=True)
    read = models.IntegerField()
    isDelete = models.BooleanField(default=False)

