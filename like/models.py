from django.db import models

# Create your models here.


class LikeData(models.Model):
    pic = models.CharField(max_length=64)
    bookName = models.CharField(max_length=64)
    author = models.CharField(max_length=32)
