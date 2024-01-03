
from django.shortcuts import render,redirect, get_object_or_404

from .models import REPORT
def report(request):
    if request.user.is_authenticated:
        try:
            report = REPORT.objects.filter(user=request.user)
            print(report[0].rDatetime)
            return render(request,'report.html')
        except:
            print('error, multiple returns')
            redirect('/')
    return redirect('/')