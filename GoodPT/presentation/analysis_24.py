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
from presentation.LLM_gpt_24 import content_analysis

def attitude_analysis(attitude):
    result = "정면을 잘 응시하며 발표를 하고 있습니다."
    return result
def voice_analysis(surplus, speech_rate, gap):
    surplus_res = ""
    speed_res = ""
    gap_rate_res = ""

    if surplus >= 0.2:
        surplus_res = "발표 내용에 불필요한 단어를 많이 언급하고 있습니다. "
    else:
        surplus_res = "발표 내용에 대해 자신의 의견을 효과적으로 전달하고 있습니다. "

    if speech_rate < (20 / 8):
        speed_res = "발표 속도가 느린 편입니다. 발표 속도가 느리면 청중들이 발표 내용에 대해 지루함을 느낄 수 있습니다. "
    elif speech_rate > (20 / 4):
        speed_res = "발표 속도가 빠른 편입니다. 발표 속도가 빠르면 청중들에게 의견을 효과적으로 피력하기 어렵습니다. "
    else:
        speed_res = "적절한 발표 속도로 청중들에게 발표하고 있습니다. 적절한 발표 속도는 청중들에게 의견을 전달하기 적합합니다. "

    if gap >= 0.2:
        gap_res = "발표에 공백이 많습니다. 발표 중 정적이 이어진다면 청중들이 집중을 잃고 답답함을 느낄 수 있습니다. "
    else:
        gap_res = "발표를 매끈하게 진행하고 있습니다. 물 흐르듯 자연스러운 발화는 청중들의 집중을 이끌 수 있습니다. "

    result = surplus_res + speed_res + gap_res
    return result
    
def script_analysis(a_content_lst):
    result = ""
    for c in a_content_lst:
        result += c
        result += "\n"
    return result

def total_analysis(attitude, surplus, speech_rate, gap, a_content_lst):
    result = "태도 분석"
    result += attitude_analysis(attitude)
    result += "\n\n"
    result += "음성 분석"
    result += voice_analysis(surplus, speech_rate, gap)
    result += "\n\n"
    result += script_analysis(a_content_lst)
    result += "\n\n"
    return result
