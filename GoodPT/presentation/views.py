from django.shortcuts import render
import json 
import io
from django.http import JsonResponse
import cv2
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
# from presentation.preprocessing import extractAudioFromVideo
import os
import sys

# Create your views here.

def recording(request):
    if request.method == 'POST':
        recorded_data = request.FILES.get('recordedData')
        path = default_storage.save('tmp/myvideo.mp4', ContentFile(recorded_data.read()))
        cap = cv2.VideoCapture(path)
        
        while True:
            ret, frame = cap.read()

            if not ret:
                break

            cv2.imshow('Video Playback', frame)

            if cv2.waitKey(30) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
        
        # extractAudioFromVideo()
        if os.path.exists(path):
            os.remove(path)

            
            

    
    return render(request,'presentation.html')