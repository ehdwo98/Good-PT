# 발표 속도
'''
* speech_rate_24 / measure_speech_rate(content, audio_length)
                                            |         |
                                            |          --- speech_to_text_24/audio_length(audio_path)
                                             --- speech_to_text_24/stt(audio_path)

    - measure_speech_rate(content, audio_length): 발표 속도를 측정하는 함수
    - content는 발표 음성을 텍스트로 변환한 것
    - audio_length는 발표 음성의 길이
    - 반환 값: 실수 (발표 속도 비율)
***** 주의 사항 : 음성 파일은 반드시 wav 파일 *****
'''
import numpy as np

def measure_speech_rate(content, audio_length):
    # 음성에서 추출한 텍스트의 글자 수 계산
    word_length = len(content)

    # 발화 속도(글자 수 / 음성 길이(초)) 계산
    speech_rate = word_length / audio_length
    print('word_length:', word_length)
    print('audio_length:', audio_length)
    print(np.round(0.08 * speech_rate, 2))
    return np.round(0.08 * speech_rate, 2)
    
