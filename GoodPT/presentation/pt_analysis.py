from presentation.speech_to_text_24 import stt, audio_length
from presentation.surplus_24 import cleaning_content, find_surplus
from presentation.speech_rate_24 import measure_speech_rate
from presentation.gap_find_24 import find_silence
from presentation.LLM_gpt_24 import content_analysis
from presentation.analysis_24 import total_analysis

def pt_analysis(audio_path="GoodPT/tmp/myaudio.wav"):
    attitude = 0.4
    content = stt(audio_path)
    if content == -1:
        return (-1, -1)
    audio_len = audio_length(audio_path)
    surplus = find_surplus(content)
    speech_rate = measure_speech_rate(content, audio_len)
    gap = find_silence(audio_path)
    clean_content = cleaning_content(content)
    a_content_lst = content_analysis(clean_content)
    total_script = total_analysis(attitude, surplus, speech_rate, gap, a_content_lst)
    print(total_script)
    
    return (total_script, content)