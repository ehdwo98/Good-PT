from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
def test1(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            auth_login(request,form.get_user())
            return redirect('/')
    else:
        form = AuthenticationForm()
    context = {'form' : form}
    return render(request,'login.html',context)

def test2(request):
    return render(request,'naver.html')

def test3(request):
    return render(request,'naverCallback.html')

def test4(request):
    return render(request,'privacyPolicy.html')