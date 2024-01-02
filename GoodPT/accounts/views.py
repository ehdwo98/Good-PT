from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib import messages

def test1(request):
    if request.method == 'POST':
        if 'login' in request.POST:
            form = AuthenticationForm(request,request.POST)
            if form.is_valid():
                print('login success')
                auth_login(request,form.get_user())
                return redirect('/')
            else:
                print(form.errors)
                messages.warning(request,"아이디나 비밀번호가 맞지 않습니다.")
                # print('login failed')
                # return redirect('/login')
        elif 'register' in request.POST:
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                print('register success')
                return redirect('/login')
            else:
                print('register failed')
    
    return render(request,'login.html')

def test4(request):
    return render(request,'privacyPolicy.html')