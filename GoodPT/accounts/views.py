from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def test1(request):
    return render(request,'login.html')

def test2(request):
    return render(request,'naver.html')

def test3(request):
    return render(request,'naverCallback.html')