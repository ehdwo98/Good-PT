from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from ..models import Question, Answer, Category


def index(request, category_name='qna'):
    '''
    목록 출력
    '''
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    so = request.GET.get('so', 'recent')  # 정렬기준

    category = get_object_or_404(Category, name=category_name)
    # 정렬
    question_list = Question.order_by_so(Question.objects.filter(category=category), so)

    # 검색
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 질문 제목검색
            Q(content__icontains=kw) |  # 질문 내용검색
            Q(answer__content__icontains=kw) |  # 답변 내용검색
            Q(author__username__icontains=kw) |  # 질문 작성자검색
            Q(answer__author__username__icontains=kw)  # 답변 작성자검색
        ).distinct()

    # 페이징처리
    paginator = Paginator(question_list, 10)  # 페이지당 10개식 보여주기
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj, 'page': page, 'kw': kw, 'so': so, 'category': category}
    return render(request, 'board/question_list.html', context)



def detail(request, question_id):
    # 입력파라미터
    page = request.GET.get('page', '1')  # 페이지
    so = request.GET.get('so', 'recommend')  # 정렬기준
    question = get_object_or_404(Question, pk=question_id)

    answer_list = Answer.order_by_so(Answer.objects.filter(question=question), so)

    # 페이징처리
    paginator = Paginator(answer_list, 5)  # 페이지당 5개식 보여주기
    page_obj = paginator.get_page(page)

    context = {'question': question, 'answer_set': page_obj, 'page': page, 'so': so, 'category': question.category}
    return render(request, 'board/question_detail.html', context)