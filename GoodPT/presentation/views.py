from django.shortcuts import render

# Create your views here.

def recording(request):
    return render(request,'presentation.html')