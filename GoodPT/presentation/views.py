from django.shortcuts import render
import json 
import io
from django.http import JsonResponse
import cv2
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from presentation.preprocessing import extractAudioFromVideo
from presentation.gesture_analysis import gesture_analysis
import os
import sys

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