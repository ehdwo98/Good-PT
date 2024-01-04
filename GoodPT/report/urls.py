from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'report'

urlpatterns = [
    path('',views.report,name='report'),
    path('<int:no>',views.detail),
]