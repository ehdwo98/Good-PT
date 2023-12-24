from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'login'

urlpatterns = [
    path('',views.test1,name='login'),
    path('naver-login',views.test2),
    path('naverCallback',views.test3),
    path('privacy',views.test4)

]