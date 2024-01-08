from django.db import models
from django.conf import settings
# Create your models here.
from report.models import REPORT

class Profile(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,verbose_name='사용자')
    intro=models.TextField()
    useremail=models.EmailField(max_length=128,verbose_name='사용자_이메일')
    phone_number = models.CharField(max_length=20,verbose_name='사용자_전화번호')
    address = models.CharField(max_length=50, verbose_name='사용자_주소')
    
    def has_report(self):
        return REPORT.objects.filter(user=self.user).exists()
    
    def __str__(self):
        return self.user
