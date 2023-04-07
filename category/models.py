from django.db import models

# Create your models here.


class Category(models.Model):
    categoryName = models.CharField(max_length=64)
    amount = models.CharField(max_length=32)