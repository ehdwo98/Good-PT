from django.db import models

# Create your models here.

class USER(models.Model):
    uuid = models.IntegerField(max_length=10)
    body = models.TextField()
    test = models.TextField()