from django.db import models
# Create your models here.
from report.models import REPORT
from django.contrib.auth.models import User
import os
from uuid import uuid4

def get_file_path(instance, filename):
    user_id = instance.user_id
    uuid_name = uuid4().hex
    ext = os.path.splitext(filename)[-1]
    return f'common/profile/{user_id}/{uuid_name}{ext}'

class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    report=models.ForeignKey(REPORT, on_delete=models.CASCADE, related_name='user_report')
    
    def __str__(self):
        return self.user
