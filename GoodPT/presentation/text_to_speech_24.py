# TTS
'''
* text_to_speech_24/text_to_speech(text, file_path)
                                    |       |
                                    |        --- 예: "GoodPT/tmp/answer.mp3"
                                     --- questions
'''

from gtts import gTTS
import playsound
import os
import speech_recognition as sr

def text_to_speech(text, file_path):
     tts = gTTS(text=text, lang='ko')
     tts.save(file_path)
     playsound.playsound(file_path)
     os.remove(file_path)