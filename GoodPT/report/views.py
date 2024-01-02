
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as auth_login

def report(request):
    return render(request,'report.html')