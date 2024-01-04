# 음성 공백
'''
* gap_find_24 / find_silence(audio_path)
                                |
                                 --- 예: "C:/Users/user/Desktop/test.wav"

    - find_silence(audio_path): 전체 발표 길이 중에서 공백 길이를 측정하는 함수
    - audio_path는 음성 파일 경로
    - 반환 값: 4초 이상의 공백 길이 합 / 전체 발표 길이
                                 
'''

from pydub import AudioSegment
from pydub.silence import detect_silence
import numpy as np
from presentation.speech_to_text_24 import audio_length

def find_silence(audio_path, min_silence_duration=4000, min_db=-40):
    # 오디오 파일 로드
    audio = AudioSegment.from_file(audio_path)

    # 최소 무음 지속 시간과 최소 데시벨 설정
    silence_segments = detect_silence(audio, min_silence_duration, silence_thresh=min_db)

    # 찾은 구간 시간 합
    segment_sum = 0
    for segment in silence_segments:
        segment_sum += (segment[1] - segment[0])
    segment_sum = np.round(segment_sum / 1000, 2) # 초로 변환
    return segment_sum / audio_length(audio_path)
