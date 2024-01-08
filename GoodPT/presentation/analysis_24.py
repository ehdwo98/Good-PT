# analysis
'''
* analysis / attitude_analysis(attitude)
* analysis / voice_analysis(surplus, speech_rate, gap)
* analysis / script_analysis(content_analysis)
* analysis / total_analysis()

'''
from presentation.surplus_24 import find_surplus
from presentation.speech_rate_24 import measure_speech_rate
from presentation.gap_find_24 import find_silence
from presentation.LLM_gpt_24 import *
    
def script_analysis(a_content_lst):
    result = ""
    for c in a_content_lst:
        result += c
        result += "\n"
    return result

def total_analysis(gesture, gaze, surplus, speech_rate, gap, a_content_lst):
    result = "태도 분석\n"
    result += gesture_analysis(gesture)
    result += gaze_analysis(gaze)
    result += "\n\n"
    result += "음성 분석\n"
    result += surplus_analysis(surplus)
    result += "\n"
    result += speed_analysis(speech_rate)
    result += "\n"
    result += gap_analysis(gap)
    result += "\n\n"
    result += "발표 내용 분석\n"
    result += content_analysis(script_analysis(a_content_lst))
    result += "\n\n"
    return result
