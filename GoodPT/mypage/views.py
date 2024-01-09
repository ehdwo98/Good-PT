
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.
class MyPasswordChangeView(PasswordChangeView) :
    success_url = reverse_lazy('mypage:mypage')
    template_name = 'mypage/password_change_form.html'

    def form_valid(self, form):
        messages.info(self.request, '암호 변경을 완료했습니다!')
        return super().form_valid(form)
    