from django.db import models
from django.conf import settings
# Create your models here.
from django import forms


class USER(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    userid = models.CharField(max_length=30,null=True)
    birthday = models.DateField(null=True)
    
    def __str__(self):
        return self.userid
    

from django.core.mail import send_mail 
from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in

from django.forms import EmailField

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    email = EmailField()

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user