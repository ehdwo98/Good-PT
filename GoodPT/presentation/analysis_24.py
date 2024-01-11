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

def script_analysis(a_content):
    result = "\t"
    result += a_content
    result += "\n"
    return result

def total_analysis(attitude_text, voice_text, script_text):
    result = "태도 분석\n"
    result += attitude_text
    result += "\n"
    result += "음성 분석\n"
    result += voice_text
    result += "\n"
    result += "발표 내용 분석\n"
    result += script_text
    result += "\n"
    return result

def voice_analysis(surplus_text, speed_text, gap_text):
    result = "\t"
    result += surplus_text
    result += '\n'
    result += ' '
    result += speed_text
    result += '\n'
    result += ' '
    result += gap_text
    result += '\n'
    return result

def attitude_analysis(gesture_text, gaze_text):
    result = "\t"
    result += gesture_text
    result += '\n'
    result += ' '
    result += gaze_text
    result += '\n'
    return result
