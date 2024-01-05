from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import QuestionForm
from ..models import Question, Category


@login_required(login_url='/login')
def question_create(request, category_name):
    category = Category.objects.get(name=category_name)
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            try:
                question.image = request.FILES['image']
            except:
                question.image = None
            question.author = request.user  # author 속성에 로그인 계정 저장
            question.create_date = timezone.now()
            question.category = category
            question.save()
            return redirect(category)
    else:  # request.method == 'GET'
        form = QuestionForm()
    context = {'form': form, 'category': category}
    return render(request, 'board/question_form.html', context)


@login_required(login_url='/login')
def question_modify(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '수정 권한이 없습니다.')
        return redirect(question)

    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            try:
                question.image = request.FILES['image']
            except:
                question.image = None
            question.modify_date = timezone.now()  # 수정일시 저장
            question.save()
            return redirect(question)
    else:
        form = QuestionForm(instance=question)
    context = {'form': form, 'category': question.category}
    return render(request, 'board/question_form.html', context)


@login_required(login_url='/login')
def question_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제 권한이 없습니다.')
        return redirect(question)
    question.delete()
    return redirect(question.category)