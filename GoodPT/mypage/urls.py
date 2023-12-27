from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.views.generic import TemplateView

app_name = 'mypage'

urlpatterns = [
    path('', TemplateView.as_view(template_name='mypage/mypage.html'), name='mypage'  ),
    path("password_change/", views.MyPasswordChangeView.as_view(), name="password_change"),
    path("password_change/done/",auth_views.PasswordChangeDoneView.as_view(),name="password_change_done",),
]
