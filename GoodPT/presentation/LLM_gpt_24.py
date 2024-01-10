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
import numpy as np

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
                "content" : "발표 할게. 반드시 질문 3개를 생성해줘!\n" + content
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
    if len(q_content_lst) >= 4:
        q_content_lst = q_content_lst[1:4]
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
                "content" : "내 발표 내용을 분석하고 보완할 점을 평가한 리포트를 한 문단으로 얘기해줘."
            },
            {
                "role" : "user",
                "content" : content
            }
        ]
    )

    # GPT API 호출하여 분석 내용 저장
    a_content = completion.choices[0].message.content

    # 분석 리스트 반환
    return a_content

# 제스처 분석
# gesture: gesture_analysis.py의 gesture_analysis()의 반환 값인 gesture (제스처 비율)
def gesture_analysis_return_rate(gesture):
    # API 연동
    OPENAI_API_KEY = "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"
    client = OpenAI(api_key=OPENAI_API_KEY)
    
    # 제스처 평가 멘트
    gesture_percentage = gesture * 100
    content = f"제스처 비율은 (제스처 동작 시간 / 전체 발표 시간)이야. 제스처 시간 평가 기준은 값이 10%보다 낮으면 많이 정적인 거고 21%보다 높으면 제스처가 너무 많은 거야. 값이 10% 초과 21% 미만이면 적절한 제스처를 하고 있다는 거야. 제스처 비율 값이 10% 이하면 제스처를 사용하라는 식으로 21% 이상이면 제스처를 좀 줄이라는 식으로 평가해야돼. 내 제스처 비율은 {np.round(gesture_percentage)}%이야. 이 제스처 비율에 대해서 발표와 관련하여 평가 리포트를 한 문단으로 만들어 줘."

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
    gesture_content = completion.choices[0].message.content
    
    # 분석 결과 텍스트 반환
    return gesture_content

# 정면 응시 분석
# gaze: gesture_analysis.py의 gesture_analysis()의 반환 값인 gaze (정면 응시 비율)
def gaze_analysis(gaze):
    # API 연동
    OPENAI_API_KEY = "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"
    client = OpenAI(api_key=OPENAI_API_KEY)
    
    gaze_percentage = gaze * 100
    
    if gaze > 0:
        # 정면 응시 평가 멘트
        content = f"발표의 정면 응시 비율은 (정면 응시 프레임의 합 / 전체 프레임의 합)%야. 발표의 정면 응시 비율은 발표 중 정면을 응시하며 발표한 비율을 뜻 해. 발표의 정면 응시 비율이 60% 이상 90% 이하면 발표를 잘하고 있다는 것이고 60%보다 낮으면 정면을 적게 인식하여 청중의 주의가 산만하고 90%보다 높으면 너무 정면만 응시하여 청중의 집중을 이끌지 못해. 내 발표의 정면 응시 비율은 {np.round(gaze_percentage, 2)}%야. 이 비율에 대해서 발표와 관련하여 평가 리포트를 한 문단으로 만들어 줘."
    else:
        gaze_percentage *= -1
        content = f"발표의 정면 응시 비율은 (정면 응시 프레임의 합 / 전체 프레임의 합)%야. 발표의 정면 응시 비율은 발표 중 정면을 응시하며 발표한 비율을 뜻 해. 발표의 정면 응시 비율이 60% 이상 90% 이하면 발표를 잘하고 있다는 것이고 60%보다 낮으면 신체는 정면을 향하지만 시선이 아래를 향하여 청중의 이목을 집중시키지 못하고 90%보다 높으면 너무 정면만 응시하여 청중의 집중을 이끌지 못해. 내 발표의 정면 응시 비율은 {np.round(gaze_percentage, 2)}%야. 이 비율에 대해서 발표와 관련하여 평가 리포트를 한 문단으로 만들어 줘."
        
    # GPT-3.5-TURBO API
    completion = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
            {
                "role" : "system",
                "content" : "안녕 넌 내 발표 자세에 대해 평가하는 역할을 맡았어."
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
    content = f"발표 음성의 공백 비율은 (음성 공백 시간(초) / 전체 발표 시간(초))%야. 발표 음성의 공백은 발표 중 아무 말도 안했다는 것을 뜻해. 발표 음성의 공백 비율이 6.7% 이하면 발표를 매끄럽게 잘하고 있다는 것이고 6.7% 초과면 발표 음성의 공백이 많아 발표가 매끄럽지 않다는 것이야. 내 발표 음성의 공백 비율은 {np.round(gap_percentage, 2)}%야. 이 비율에 대해서 발표와 관련하여 평가 리포트를 한 문단으로 만들어 줘."

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
    content = f"불필요한 단어 언급 비율은 (불필요한 단어 개수 / 전체 단어 개수)%야. 불필요한 단어의 예시는 '아', '어', '음', '그' 야.불필요한 단어 언급 비율 값이 1% 이하면 발표를 잘하고 있다는 것이고 1% 초과면서 3% 이하면 발표를 적절히 하고 있다는 것이고 3%를 초과하면 불필요한 단어를 많이 말하고 있는거야. 내 발표에서 불필요한 단어 언급 비율은 {np.round(surplus_percentage, 2)}%야. 이 비율에 대해서 발표와 관련하여 평가 리포트를 한 문단으로 만들어 줘."

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
    surplus_content = completion.choices[0].message.content

    # 분석 결과 텍스트 반환
    return surplus_content


# 음성 빠르기 분석
# speed: speech_rate.py의 measure_speech_rate의 반환 값 (음성 속도 비율)
def speed_analysis(speed):
    # API 연동
    OPENAI_API_KEY = "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"
    client = OpenAI(api_key=OPENAI_API_KEY)
    
    # 음성 빠르기 평가 멘트
    speed_percentage = speed * 100
    print('speed_percentage:', speed_percentage)
    content = f"발표 속도 평가 기준은 값이 35%보다 낮으면 너무 느린 거고 보다 80%보다 크면 매우 빠른 거야. 발표 속도가 35%보다 크면서 80%보다 작으면 적절한 발표 속도로 평가해야 돼. 내 발표 속도는 {np.round(speed_percentage, 2)}%이야. 이 발표 속도에 대해 발표와 관련하여 평가 리포트를 한 문단으로 만들어 줘."

    # GPT-3.5-TURBO API
    completion = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
            {
                "role" : "system",
                "content" : "안녕 넌 내 발표 속도를 평가하는 역할을 맡았어. 발표 속도는 (0.08 * 발표 글자 수 / 발표 시간(초))%야."
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
