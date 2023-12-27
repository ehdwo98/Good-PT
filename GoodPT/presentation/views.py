from django.shortcuts import render

# Create your views here.

def recording(request):
    if request.method == 'POST':
        print(request.POST)
    return render(request,'presentation.html')