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
from pyaudio import PyAudio
from speech_recognition import Microphone, Recognizer
from django.http import HttpResponse

openai.api_key=''
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
    # GPT-3.5 Turbo에 요청을 보내는 코드
    response = {
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "The 2020 World Series was played in Texas at Globe Life Field in Arlington.",
        "role": "assistant"
      },
    }
  ],
  "created": 1677664795,
  "id": "chatcmpl-7QyqpwdfhqwajicIEznoc6Q47XAyW",
  "model": "gpt-3.5-turbo-0613",
  "object": "chat.completion",
  "usage": {
    "completion_tokens": 17,
    "prompt_tokens": 57,
    "total_tokens": 74
  }
}
    return response.choices.message['content']

def detail(request):
    if request.method == 'POST':
        prompt = request.POST.get('prompt')
        response = get_completion(prompt)
        return render(request, 'feedback.html',{'res':JsonResponse({'response': response})})
    return render(request, 'feedback.html')
  
# def stt(request):
#     pyaudio = PyAudio()
#     audio = pyaudio.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
#     stream = Microphone(audio, chunk_size=1024)

#     recognizer = Recognizer()
#     speech = recognizer.record(stream)

#     transcript = recognizer.recognize_google(speech)

#     return render(request, 'feedback.html',{'stt':transcript})