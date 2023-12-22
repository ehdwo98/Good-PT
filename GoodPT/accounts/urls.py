from django.urls import path, include
from . import views

app_name = 'login'

urlpatterns = [
    path('',views.test1),
    path('naver-login',views.test2),
<<<<<<< HEAD
    path('naverCallback',views.test3),
    path('privacy',views.test4)
=======
    path('naverCallback',views.test3)
>>>>>>> 9d31fda (임시 저장)

]