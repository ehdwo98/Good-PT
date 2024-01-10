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
from presentation.feedbackState import InitialState
from presentation.FileErrorHandler import eraseTmpFile
from presentation.speech_to_text_24 import stt
from presentation.surplus_24 import cleaning_content
from report.models import REPORT
from accounts.models import USER
from datetime import datetime

openai.api_key=''
# Create your views here.

def recording(request):
  if request.method == 'POST':
    recorded_data = request.FILES.get('recordedData')
    path = default_storage.save('tmp/myvideo.mp4', ContentFile(recorded_data.read()))
  
  return render(request,'presentation/presentation.html')
      


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
            question_num = InitialState.questionnum
            question_list = InitialState.questionlist
            answer_list = InitialState.answerlist
            print(question_list)
            recorded_data = request.FILES.get('recordedData')
            answer_video_path = 'tmp/myAnswer' + str(len(answer_list)) +'.mp4'
            answer_audio_path = 'tmp/myAnswer' + str(len(answer_list)) +'.wav'
            path = default_storage.save(answer_video_path, ContentFile(recorded_data.read()))
            audio_path = extractAudioFromVideo(os.path.join(settings.MEDIA_ROOT,answer_video_path),os.path.join(settings.MEDIA_ROOT,answer_audio_path))
            total_script = stt(audio_path)
            eraseTmpFile()
            answer_list.append(total_script)
            
            if question_num == 3:
                individual_report = REPORT.objects.filter(user=request.user).latest('rDatetime')
                individual_report.answers = json.dumps(answer_list)
                individual_report.save()
                return JsonResponse({'redirect':'/report'})
              
            feedbackData = [total_script,question_list[question_num]] #출력하는줄
            
            InitialState.questionlist = question_list
            InitialState.answerlist = answer_list #저장하는 줄
            InitialState.questionnum = question_num+1
            return JsonResponse({'feedbackData':feedbackData})
        else:
            # path = 'media/tmp/myvideo.mp4'
            # cap = cv2.VideoCapture(path)
            # gesture, gaze = gesture_analysis(cap)
            # audio_path = extractAudioFromVideo("media/tmp/myvideo.mp4","media/tmp/myaudio.wav")
            # voice_text, attitude_text, script_text, total_script, gesture, gaze, gap, speech_rate, surplus, content = pt_analysis(gesture, gaze, audio_path)
            # question_list = question_contents(content)
            # # DB 저장
            # REPORT(user = request.user,
            #        questions = json.dumps(question_list), 
            #        answers = "", 
            #        voice_analysis = voice_text,
            #        attitude_analysis = attitude_text,
            #        script_analysis = script_text,
            #        total_analysis = total_script,
            #        rDatetime = datetime.now(),
            #        static_rate = gesture,
            #        face_recog_rate = gaze,
            #        gap_rate = gap,
            #        speed_rate = speech_rate,
            #        surplus_rate = surplus).save()
            eraseTmpFile()
            
            # InitialState.questionlist = question_list

        return render(request, 'presentation/feedback.html',{'question_list':question_list})
    else:
        return redirect('/login')
  
