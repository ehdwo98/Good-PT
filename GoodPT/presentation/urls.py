from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'presentation'

urlpatterns = [
    path('',views.recording,name='presentation'),
    path('feedback',views.detail,name='feedback'),

]