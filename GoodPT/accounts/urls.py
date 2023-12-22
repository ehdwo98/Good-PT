from django.urls import path, include
from . import views

app_name = 'login'

urlpatterns = [
    path('',views.test1),
    path('naver-login',views.test2),
    path('naverCallback',views.test3),
    path('privacy',views.test4)

]