from django.db import models

# Create your models here.
class Mima(models.Model):
    zhanghu=models.CharField(max_length=20)
    mima=models.CharField(max_length=20)