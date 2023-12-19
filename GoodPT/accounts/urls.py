from django.urls import path, include
from . import views

urlpatterns = [
    path('test1/',views.test1)
]