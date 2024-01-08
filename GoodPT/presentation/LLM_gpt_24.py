# LLM
'''
* LLM_model_24/question_contents(content)
                                    |
                                     --- speech_to_text_24/cleaning_content(content)

    - question_contents(content): 발표 내용을 받아 질문하는 함수
    - content는 speech_to_text_24 / cleaning_content(content) 의 return 값 (음성적 잉여를 제거한 발표 내용)
    - 반환 값: 질문 리스트 (발표 내용을 바탕으로 질문 구성)

* LLM_model_24/content_analysis(content)
                                    |
                                     --- speech_to_text_24/cleaninig_content(content)

    - content_analysis(content): 발표 내용을 분석하는 함수
    - content는 speech_to_text_24 / cleaning_content(content) 의 return 값 (음성적 잉여를 제거한 발표 내용)
    - 반환 값: 분석 리스트 (발표 내용을 바탕으로 분석한 것들을 번호 매긴 리스트)

***** API_KEY 외부 유출 절대 금지 *****
'''

from openai import OpenAI
import re

def question_contents(content):
    # API 연동
    OPENAI_API_KEY = "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"
    client = OpenAI(api_key=OPENAI_API_KEY)

    # GPT-3.5-TURBO API
    completion = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
            {
                "role" : "system",
                "content" : "내가 발표 내용을 보여줄게. 너는 발표를 들은 청중이야. 내 발표를 듣고 발표 내용에 대해 3개의 질문을 해줘."
            },
            {
                "role" : "user",
                "content" : content
            }
        ]
    )

    # GPT API 호출하여 질문 저장
    q_content = completion.choices[0].message.content

    # 질문 내용에서 '1.', '2.', '3.' 제거
    q_content = re.sub(r"1. |2. |3. ", "", q_content)

    # 질문 분할하여 리스트로 구성
    q_content_lst = q_content.split('\n\n')
    q_content_lst = q_content.split('\n')
    q_content_lst = [i for i in q_content_lst if i != '']

    # 질문 리스트 반환
    return q_content_lst

# 발표 내용 분석
def content_analysis(content):
    # API 연동
    OPENAI_API_KEY = "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"
    client = OpenAI(api_key=OPENAI_API_KEY)

    # GPT-3.5-TURBO API
    completion = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
            {
                "role" : "system",
                "content" : "내 발표 내용을 분석하고 보완할 점을 번호 붙여서 얘기해줘."
            },
            {
                "role" : "user",
                "content" : content
            }
        ]
    )

    # GPT API 호출하여 분석 내용 저장
    a_content = completion.choices[0].message.content

    # 분석 내용 자르기
    a_content_lst = a_content.split('\n')
    a_content_lst = [c for c in a_content_lst if c != '']

    # 분석 리스트 반환
    return a_content_lst

# 제스처 분석
# gesture: gesture_analysis.py의 gesture_analysis()의 반환 값인 gesture (제스처 비율)
def gesture_analysis_return_rate(gesture):
    # API 연동
    OPENAI_API_KEY = "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"
    client = OpenAI(api_key=OPENAI_API_KEY)
    
    # 정면 응시 평가 멘트
    gesture_percentage = gesture * 100
    content = f"제스처 비율은 (제스처 동작 시간 / 전체 발표 시간)이야. 제스처 시간 평가 기준은 값이 10%보다 낮으면 많이 정적인 거고 21%보다 높으면 제스처가 너무 많은 거야. 값이 10% 초과 21% 미만이면 적절한 제스처를 하고 있다는 거야. 제스처 비율 값이 10% 이하면 제스처를 사용하라는 식으로 21% 이상이면 제스처를 좀 줄이라는 식으로 평가해야돼. 내 제스처 비율은 {gesture_percentage}%이야. 이 제스처 비율에 대해서 '{gesture_percentage}%'는 빼고 발표와 관련하여 평가해줘."

    # GPT-3.5-TURBO API
    completion = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
            {
                "role" : "system",
                "content" : "넌 내 발표의 제스처 시간에 대해 평가하는 역할을 맡았어."
            },
            {
                "role" : "user",
                "content" : content
            }
        ]
    )

    # GPT API 호출하여 분석 내용 저장
    gaze_content = completion.choices[0].message.content
    
    # 분석 결과 텍스트 반환
    return gaze_content

# 정면 응시 분석
# gaze: gesture_analysis.py의 gesture_analysis()의 반환 값인 gaze (정면 응시 비율)
def gaze_analysis(gaze):
    # API 연동
    OPENAI_API_KEY = "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"
    client = OpenAI(api_key=OPENAI_API_KEY)
    
    # 정면 응시 평가 멘트
    gaze_percentage = gaze * 100
    content = f"내가 발표를 했는데 전체 발표 중에서 정면 응시 비율이 {gaze_percentage}%야. '{gaze_percentage}%'라는 말은 쓰지 말고 이것을 평가해줘."

    # GPT-3.5-TURBO API
    completion = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
            {
                "role" : "system",
                "content" : "안녕 넌 내 발표 음성에 대해 평가하는 역할을 맡았어."
            },
            {
                "role" : "user",
                "content" : content
            }
        ]
    )

    # GPT API 호출하여 분석 내용 저장
    gaze_content = completion.choices[0].message.content

    # 분석 결과 텍스트 반환
    return gaze_content

# 음성 공백 분석
# gap: gap_find_24의 find_silence()의 반환 값인 음성 공백 비율
def gap_analysis(gap):
    # API 연동
    OPENAI_API_KEY = "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"
    client = OpenAI(api_key=OPENAI_API_KEY)
    
    # 음성 공백 평가 멘트
    gap_percentage = gap * 100
    content = f"내가 발표를 했는데 전체 발표 중에서 음성의 공백이 {gap_percentage}%야. '{gap_percentage}%'라는 말은 쓰지 말고 이것을 평가해줘."

    # GPT-3.5-TURBO API
    completion = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
            {
                "role" : "system",
                "content" : "안녕 넌 내 발표 음성에 대해 평가하는 역할을 맡았어."
            },
            {
                "role" : "user",
                "content" : content
            }
        ]
    )

    # GPT API 호출하여 분석 내용 저장
    gap_content = completion.choices[0].message.content

    # 분석 결과 텍스트 반환
    return gap_content

# 음성적 잉여 분석
# surplus: surplus_24의 find_surplus()의 반환 값인 음성적 잉여 비율
def surplus_analysis(surplus):
    # API 연동
    OPENAI_API_KEY = "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"
    client = OpenAI(api_key=OPENAI_API_KEY)
    
    # 음성적 잉여 평가 멘트
    surplus_percentage = surplus * 100
    content = f"불필요한 단어 언급 비율은 (불필요한 단어 개수 / 전체 단어 개수)야. 불필요한 단어의 예시는 '아', '어', '음', '그' 야. 내 발표에서 불필요한 단어 언급 비율은 20%야. 이 비율에 대해서 '20%'는 빼고 발표와 관련하여 평가해줘."

    # GPT-3.5-TURBO API
    completion = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
            {
                "role" : "system",
                "content" : "안녕 넌 내 발표 음성에 대해 평가하는 역할을 맡았어."
            },
            {
                "role" : "user",
                "content" : content
            }
        ]
    )

    # GPT API 호출하여 분석 내용 저장
    a_content = completion.choices[0].message.content

    # 분석 결과 텍스트 반환
    return a_content


# 음성 빠르기 분석
# speed: speech_rate.py의 measure_speech_rate의 반환 값 (음성 속도 비율)
def speed_analysis(speed):
    # API 연동
    OPENAI_API_KEY = "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"
    client = OpenAI(api_key=OPENAI_API_KEY)
    
    # 음성 빠르기 평가 멘트
    speed_percentage = speed * 100
    content = f"표 속도 = (발표 글자 수  / 발표 시간(초))이야. 내 발표 속도는 {speed_percentage}%이야. '{speed_percentage}%' 단어는 빼고 내 발표 속도가 빠른지, 적절한지, 느린지 평가해줘."

    # GPT-3.5-TURBO API
    completion = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
            {
                "role" : "system",
                "content" : "안녕 넌 내 발표 속도를 평가하는 역할을 맡았어. 발표 속도는 (발표 글자 수 / 발표 시간(초))야."
            },
            {
                "role" : "user",
                "content" : content
            }
        ]
    )

    # GPT API 호출하여 분석 내용 저장
    speed_content = completion.choices[0].message.content

    # 분석 결과 텍스트 반환
    return speed_content
