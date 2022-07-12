from django.db import models


class Article(models.Model):
   title = models.CharField(max_length=100)
   year_created = models.CharField(max_length=10)
   description = models.CharField(max_length=10)
   author = models.CharField(max_length=10)