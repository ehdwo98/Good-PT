from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from accounts.models import CustomUserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib import messages
import re
from accounts.const import errorDictionary
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
        elif 'register' in request.POST and request.POST['email']:
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                print('register success')
                
                return redirect('/login')
            else:
                print('register failed')
                errors = []
                for field, error_list in form.errors.items():
                    match = re.search(r'<li>(.*?)</li>', str(error_list))
                    errors.append(match.group(1))
                messages.warning(request,errorDictionary[errors[0]])
        elif 'register' in request.POST and request.POST['email'] == '':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                print('register success')
                
                return redirect('/login')
            else:
                print('register failed')
                errors = []
                for field, error_list in form.errors.items():
                    match = re.search(r'<li>(.*?)</li>', str(error_list))
                    errors.append(match.group(1))
                messages.warning(request,errorDictionary[errors[0]])
    
    return render(request,'accounts/login.html')

def test4(request):
    return render(request,'accounts/privacyPolicy.html')