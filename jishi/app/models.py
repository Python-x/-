from django.db import models

# Create your models here.
class Leveo(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    site = models.CharField(max_length=100)
    message = models.TextField()
    class Meta():
        db_table = 'Leveo'

class User(models.Model):
    zhe = models.CharField(max_length=20,unique=True)
    mm = models.CharField(max_length=50)
    class Meta():
        db_table = 'User1'