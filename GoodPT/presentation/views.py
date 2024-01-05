from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from presentation.speech_to_text_24 import stt, audio_length

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
    answer_list = []
    question_list = ['empty1','empty2','empty3']
    if request.method == 'POST':
        recorded_data = request.FILES.get('recordedData')
        
        answer_video_path = 'tmp/myAnswer' + str(len(answer_list)) +'.mp4'
        answer_audio_path = 'tmp/myAnswer' + str(len(answer_list)) +'.wav'
        
        path = default_storage.save(answer_video_path, ContentFile(recorded_data.read()))
        audio_path = extractAudioFromVideo(answer_video_path,answer_audio_path)
        total_script = stt(audio_path)
        print('myVoice TTS : ' + total_script)
        if os.path.exists(path):
            os.remove(path)
        if os.path.exists(audio_path):
            os.remove(audio_path)
        answer_list.append(total_script)
        print(answer_list)
    else:
        path = 'tmp/myvideo.mp4'
        cap = cv2.VideoCapture(path)

        gesture_analysis(cap)

        
        # 태도 분석
        
        #음성 파일
        audio_path = extractAudioFromVideo("tmp/myvideo.mp4","tmp/myaudio.wav")
        
        # 음성 분석
        total_script,content = pt_analysis(audio_path)
        question_list = question_contents(content) # question = ['환영','Q1','Q2','Q3']
        print(question_list)
        if os.path.exists(path):
            os.remove(path)
        if os.path.exists(audio_path):
            os.remove(audio_path)
    return render(request, 'feedback.html',{'question_list':question_list})
  
