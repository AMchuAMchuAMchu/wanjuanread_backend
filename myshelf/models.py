from django.db import models

# Create your models here.


class MyShelfData(models.Model):
    pic = models.CharField(max_length=64)
    bookName = models.CharField(max_length=64)
    author = models.CharField(max_length=32)
