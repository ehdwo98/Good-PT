from django.shortcuts import render
import json 
import io
import numpy as np
from django.http import JsonResponse
import cv2
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

# Create your views here.

def recording(request):
    if request.method == 'POST':
        recorded_data = request.FILES.get('recordedData')
        print(type(recorded_data))
        path = default_storage.save('tmp/myvideo.webm', ContentFile(recorded_data.read()))
        print(path)
        
        cap = cv2.VideoCapture(path)
        print(cap)
        
        while True:
            ret, frame = cap.read()

            if not ret:
                print('End of video stream')
                break

            # 디스플레이에 프레임 표시
            cv2.imshow('Video Playback', frame)

            # 'q' 키를 누르면 종료
            if cv2.waitKey(30) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
    
    return render(request,'presentation.html')