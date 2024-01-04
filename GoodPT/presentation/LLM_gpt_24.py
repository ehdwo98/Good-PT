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

    # 질문 리스트 반환
    return q_content_lst

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
