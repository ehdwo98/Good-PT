from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, resolve_url

from ..models import Question, Answer

@login_required(login_url='/login')
def vote_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user == question.author:
        messages.error(request, '본인이 작성한 글을 추천할 수 없습니다.')
    else:
        question.voter.add(request.user)
    return redirect(question)


@login_required(login_url='/login')
def vote_answer(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    page = request.GET.get('page', '1')
    so = request.GET.get('so', 'recommend')

    if request.user == answer.author:
        messages.error(request, '본인이 작성한 글을 추천할 수 없습니다.')
    else:
        answer.voter.add(request.user)
        if so == 'recommend':
            page = answer.get_page(so)

    return redirect(resolve_url(answer.question)+f'?page={page}&so={so}#answer_{answer.id}')