from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

import json 
import io
from django.http import JsonResponse
import cv2
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from presentation.preprocessing import extractAudioFromVideo
from presentation.gesture_analysis import gesture_analysis
from presentation.pt_analysis import pt_analysis
from django.shortcuts import render 
from django.http import JsonResponse 
import openai
import os
from pyaudio import PyAudio
from speech_recognition import Microphone, Recognizer
from django.http import HttpResponse
from presentation.LLM_gpt_24 import question_contents

openai.api_key=''
# Create your views here.

def recording(request):
  if request.method == 'POST':
    recorded_data = request.FILES.get('recordedData')
    path = default_storage.save('tmp/myvideo.mp4', ContentFile(recorded_data.read()))
  
  return render(request,'presentation.html')
      


def get_completion(prompt):
    # GPT-3.5 Turbo에 요청을 보내는 코드
    response = "hi"
    return response

def detail(request):
  
    if request.method == 'POST':
      
        prompt = request.POST.get('prompt')
        response = get_completion(prompt)
        return render(request, 'feedback.html',{'response': response})
    else:
        path = 'tmp/myvideo.mp4'
        cap = cv2.VideoCapture(path)

        gesture_analysis(cap)

        
        # 태도 분석
        
        #음성 파일
        audio_path = extractAudioFromVideo()
        
        # 음성 분석
        total_script,content = pt_analysis(audio_path)
        question_list = question_contents(content) # question = ['환영','Q1','Q2','Q3']
        print(question_list)
        if os.path.exists(path):
            os.remove(path)
        if os.path.exists(audio_path):
            os.remove(audio_path)
    return render(request, 'feedback.html')
  
# def stt(request):
#     pyaudio = PyAudio()
#     audio = pyaudio.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
#     stream = Microphone(audio, chunk_size=1024)

#     recognizer = Recognizer()
#     speech = recognizer.record(stream)

#     transcript = recognizer.recognize_google(speech)

#     return render(request, 'feedback.html',{'stt':transcript})