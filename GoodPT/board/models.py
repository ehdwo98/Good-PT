from django.db import models
from accounts.models import USER

class Question(models.Model):
    postId = models.AutoField(primary_key=True)
    user = models.ForeignKey(USER,on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    isComplete = models.BooleanField()
    create_date = models.DateTimeField()
    
    def __str__(self):
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()