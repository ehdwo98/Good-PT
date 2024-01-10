# 음성적 잉여
'''
* surplus_24 / find_surplus(content)
                                |
                                 --- speech_to_text_24/stt(audio_path)

    - find_surplus(content): 발표 내용에서 음성적 잉여 비율을 반환하는 함수
    - content는 발표 음성을 텍스트로 변환한 것
    - 음성적 잉여 비율 = 음성적 잉여 단어 개수 / 전체 단어 개수
    - 단어 개수는 띄어쓰기 기준
    - 반환 값: 실수 (음성적 잉여 비율)

* surplus_24 / cleaning_content(content)
                                    |
                                     --- speech_to_text/stt(audio_path)
    - cleaning_content(content): 발표 내용에서 음성적 잉여를 제거하는 함수
    - content는 발표 음성을 텍스트로 변환한 것
    - 반환 값: 문자열 (음성적 잉여를 제거한 발표 내용)
    
***** 음성적 잉여 비율이 높다고 할 기준 선정 필요 *****

'''
import re
import numpy as np

def find_surplus(content):
    # 음성적 잉여 정의 / 현재: (아,어,음)
    pattern = re.compile(r'\b(?:아|어|음|그)\b', re.IGNORECASE)

    # 정규 표현식을 사용하여 음성적 잉여 찾기
    surplus = re.findall(pattern, content)

    # 음성적 잉여 개수 / 전체 단어 개수
    result = np.round(len(surplus) / len(content.split()), 2)
     
    return result

def cleaning_content(content):
    clean_content =re.sub(r"\b(?:아|어|음|그)\b", "", content)
    return clean_content
