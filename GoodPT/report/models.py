from django.db import models
from accounts.models import USER
from django.conf import settings

# Create your models here.

class CATEGORY(models.Model):
    cID = models.AutoField(primary_key=True)
    cName = models.CharField('카테고리명',max_length=20,unique=True)
    
    def __str__(self):
        return self.cName
    
class REPORT(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    reportID = models.AutoField(primary_key=True)
    category = models.OneToOneField(CATEGORY,on_delete=models.CASCADE,null=True)
    script = models.TextField()
    questions = models.TextField()
    answers = models.TextField()
    voice_analysis = models.TextField()
    attitude_analysis = models.TextField()
    script_analysis = models.TextField()
    total_analysis = models.TextField()
    rDatetime = models.DateTimeField()
    staic = models.FloatField(default=0)
    face_recog = models.FloatField(default=0)
    filler_word = models.FloatField(default=0)
    char_count = models.IntegerField(default=0)
    total_time = models.IntegerField(default=0)
    empty_count = models.IntegerField(default=0)
    
    
    def __str__(self):
        return self.script

