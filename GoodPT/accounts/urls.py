from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'login'

urlpatterns = [
    path('',views.test1,name='login'),
    path('privacy',views.test4)

]