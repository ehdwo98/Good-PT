from django.urls import path, include
from . import views

app_name = 'login'

urlpatterns = [
    path('',views.test1),
    path('naver-login',views.test2),
<<<<<<< HEAD
    path('google-login',views.test3),
=======
    path('naverCallback',views.test3)

>>>>>>> 25d4f1d38e7e3743eafa15a1f549e5fbf2f282eb
]