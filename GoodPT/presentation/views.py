from django.shortcuts import render
import json 
import io
# Create your views here.

def recording(request):
    if request.method == 'POST':
        print(request.body)
    return render(request,'presentation.html')