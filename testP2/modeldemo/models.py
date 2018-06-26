from django.db import models

# Create your models here.
class CoManager(models.Manager):
    def get_queryset(self):
        return super(CoManager, self).get_queryset().all()
    def add_Co(self,name,number,major):
        c = College()
        c.cname = name
        c.cnumber = number
        c.cmajor =major
        c.save()
        return c
    def del_Co(self,name):
        c = College.bm2.get(cname=name)
        c.delete()
    def del_Co2(self,name):
        c = College.bm2.get(cname=name)
        c.isDelete = 1
        c.save()
        return c
    def alter(self,name,newname):
        c = College.bm2.get(cname=name)
        c.cname = newname
        c.save()
        return c
class College(models.Model):
    cname = models.CharField(max_length=30)
    cnumber = models.IntegerField()
    cmajor = models.CharField(max_length=30)
    isDelete = models.BooleanField(default=0)


    def __str__(self):
        return '%s'%self.cname
    class Meta():
        db_table = '学院表'
        ordering = ['id']
    bm1 = models.Manager()
    bm2 = CoManager()
class Student(models.Model):
    sname = models.CharField(max_length=30)
    ssex = models.BooleanField(default=1)
    sdate = models.DateTimeField()
    swj = models.ForeignKey('College')
    isDelete = models.BooleanField(default=0)

    def __str__(self):
        return '%s'%self.sname

    class Meta():
        db_table = '学生表'
        ordering = ['-id']