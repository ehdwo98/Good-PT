from django.db import models
from accounts.models import USER
# Create your models here.

class CATEGORY(models.Model):
    cID = models.AutoField(primary_key=True)
    cName = models.CharField('카테고리명',max_length=20,unique=True)
    
    def __str__(self):
        return self.cName
    
class REPORT(models.Model):
    user = models.ForeignKey(USER,on_delete=models.CASCADE)
    reportID = models.AutoField(primary_key=True)
    category = models.ManyToManyField(CATEGORY)
    script = models.TextField()
    question1 = models.TextField()
    question2 = models.TextField()
    question3 = models.TextField()
    answer1 = models.TextField()    
    answer2 = models.TextField()    
    answer3 = models.TextField()
    va = models.TextField()
    aa = models.TextField()
    strength = models.TextField()
    weakness = models.TextField()
    suppliment = models.TextField()
    rDatetime = models.DateTimeField()
    
    def __str__(self):
        return self.reportID

