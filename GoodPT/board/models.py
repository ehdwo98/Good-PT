from django.db import models
from accounts.models import USER
# Create your models here.

class Board(models.Model):
    postId = models.AutoField(primary_key=True)
    user = models.ForeignKey(USER,on_delete=models.CASCADE)
    title = models.CharField(max_length=400)
    content = models.CharField(max_length=20000)
    isComplete = models.BooleanField()
    datetime = models.DateTimeField()
    
    def __self__(self):
        return self.title
    