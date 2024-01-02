from django.shortcuts import render
import json 
import io
from django.http import JsonResponse
import cv2
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from presentation.preprocessing import extractAudioFromVideo
from presentation.gesture_analysis import gesture_analysis
from django.shortcuts import render 
from django.http import JsonResponse 
import openai
import os

openai.api_key='s--y'
# Create your views here.

def recording(request):
    if request.method == 'POST':
        recorded_data = request.FILES.get('recordedData')
        path = default_storage.save('tmp/myvideo.mp4', ContentFile(recorded_data.read()))
        cap = cv2.VideoCapture(path)
        
        # 태도 분석
        gesture_analysis(cap)
        
        #음성 파일
        audio_path = extractAudioFromVideo()
        # if os.path.exists(path):
        #     os.remove(path)
        # if os.path.exists(audio_path):
        #     os.remove(audio_path)
    return render(request,'presentation.html')

def get_completion(prompt): 
	print(prompt) 
	query = { 'content': ['안녕하세요','반가워요']}
	response = query['content']
	print(response) 
	return response 

def detail(request):
    if  request.method == 'POST': 
        prompt = request.POST.get('prompt') 
        prompt=str(prompt)
        response = get_completion(prompt)
        return JsonResponse({'response': response})
    return render(request, 'feedback.html') 