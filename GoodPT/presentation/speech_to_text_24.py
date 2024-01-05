# STT
'''
* speech_to_text_24/stt(audio_path)
                            |
                             --- 예: "C://User//users//Desktop//test.wav"

    - stt(audio_path): 발표 음성 파일을 텍스트로 변환하는 함수
    - audio_path는 발표 음성 파일의 경로
    - 반환 값: 문자열 (음성을 텍스트로 변환한 것)

* speech_to_text_24/audio_length(audio_path)
                                    |
                                     --- 예: "C://User//users//Desktop//test.wav"

    - audio_length(audio_path): 발표 음성 파일의 길이를 반환하는 함수
    - audio_path는 발표 음성 파일의 경로
    - 반환 값: 실수 (음성의 길이)
    
***** 주의 사항: 음성 파일은 반드시 wav 파일 *****

'''

import speech_recognition as sr
from pydub import AudioSegment
import numpy as np

def stt(audio_path):
    rec = sr.Recognizer()
    audio_file = sr.AudioFile(audio_path)
    with audio_file as source:
        audio = rec.record(audio_file)
    text = rec.recognize_google(audio_data=audio, language='ko-KR')
    return text

def audio_length(audio_path):
    audio = AudioSegment.from_wav(audio_path)
    audio_length_ms = len(audio) # ms
    return np.round(audio_length_ms / 1000, 2) # s