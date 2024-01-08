from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
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
    question_num = InitialState.questionnum
    answer_list = []
    question_list = InitialState.questionlist
    if request.user.is_authenticated:

        if request.method == 'POST':
            try:
                question_num = InitialState.questionnum
                question_list = InitialState.questionlist
                print(question_list)
                recorded_data = request.FILES.get('recordedData')
                answer_video_path = 'tmp/myAnswer' + str(len(answer_list)) +'.mp4'
                answer_audio_path = 'tmp/myAnswer' + str(len(answer_list)) +'.wav'
                path = default_storage.save(answer_video_path, ContentFile(recorded_data.read()))
                audio_path = extractAudioFromVideo(os.path.join(settings.MEDIA_ROOT,answer_video_path),os.path.join(settings.MEDIA_ROOT,answer_audio_path))
                total_script = stt(audio_path)
                eraseTmpFile()
                answer_list.append(total_script)
                feedbackData = [total_script,question_list[question_num]]
                
                InitialState.questionlist = question_list
                InitialState.questionnum = question_num+1
            
                if InitialState.questionnum >= 5:
                    return JsonResponse({'redirect':'/report'})
                return JsonResponse({'feedbackData':feedbackData})
            except:
                print("stt analays error occured")
                eraseTmpFile()
                return JsonResponse({'error':'음성이 확인되지 않았습니다.'})
        else:
            path = 'media/tmp/myvideo.mp4'
            cap = cv2.VideoCapture(path)
            gesture_analysis(cap)
            audio_path = extractAudioFromVideo("media/tmp/myvideo.mp4","media/tmp/myaudio.wav")
            total_script,content = pt_analysis(audio_path)
            question_list = question_contents(content)
            eraseTmpFile()
            
            InitialState.questionlist = question_list

        return render(request, 'feedback.html',{'question_list':question_list})
    else:
        return redirect('/login')
  
