from django.db import models

# Create your models here.
class Bookinfo(models.Model):
    btitle = models.CharField(max_length=30)
    bpub_date = models.DateTimeField()
    def __str__(self):
        return '%s'%self.btitle
class Heroinfo(models.Model):
    hname = models.CharField(max_length=30)
    hgender = models.BooleanField(1)
    hcontent = models.TextField()
    hBook = models.ForeignKey(Bookinfo)

    def __str__(self):
        return '%s'%self.hname