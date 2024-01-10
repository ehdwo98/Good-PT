from presentation.gesture_analysis import gesture_analysis
from presentation.speech_to_text_24 import stt, audio_length
from presentation.surplus_24 import cleaning_content, find_surplus
from presentation.speech_rate_24 import measure_speech_rate
from presentation.gap_find_24 import find_silence
from presentation.LLM_gpt_24 import *
from presentation.analysis_24 import *

def pt_analysis(gesture, gaze, audio_path="media/tmp/myaudio.wav"):
    content = stt(audio_path)
    audio_len = audio_length(audio_path)
    surplus = find_surplus(content)
    speech_rate = measure_speech_rate(content, audio_len)
    gap = find_silence(audio_path)
    clean_content = cleaning_content(content)
    a_content = content_analysis(clean_content)
    gesture_text = gesture_analysis_return_rate(gesture)
    gaze_text = gaze_analysis(gaze)
    gap_text = gap_analysis(gap)
    surplus_text = surplus_analysis(surplus)
    speed_text = speed_analysis(speech_rate)
    attitude_text = attitude_analysis(gesture_text, gaze_text)      # 태도 분석 텍스트
    voice_text = voice_analysis(surplus_text, speed_text, gap_text) # 음성 분석 텍스트
    script_text = script_analysis(a_content)                        # 발표 내용 분석 텍스트
    total_script = total_analysis(attitude_text, voice_text, script_text)   # 전체 분석 텍스트
    
    # (음성 분석 텍스트, 태도 분석 텍스트, 발표 내용 분석 텍스트, 전체 분석 텍스트, 정적 비율, 정면 응시 비율, 음성 공백 비율, 음성 빠르기 비율, 음성 잉여 비율, **발표 내용**)
    return (voice_text, attitude_text, script_text, total_script, gesture, gaze, gap, speech_rate, surplus, clean_content)