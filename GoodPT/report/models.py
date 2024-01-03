from django.db import models
from accounts.models import USER
from django.conf import settings

# Create your models here.

class REPORT(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    reportID = models.AutoField(primary_key=True)
    questions = models.TextField()
    answers = models.TextField()
    voice_analysis = models.TextField()
    attitude_analysis = models.TextField()
    script_analysis = models.TextField()
    total_analysis = models.TextField()
    rDatetime = models.DateTimeField()
    static_rate = models.FloatField(default = 0)
    face_recog_rate = models.FloatField(default = 0)
    gap_rate = models.FloatField(default = 0)
    speed_rate = models.FloatField(default = 0)
    surplus_rate = models.FloatField(default = 0)
    
    
    def __str__(self):
        return self.voice_analysis

