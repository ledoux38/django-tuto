from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse

from .models import Question, Choice


def index(request: object) -> render:
    lastest_question_list: list = Question.objects.order_by('-pub_date')[:5]
    template: object = loader.get_template('polls/index.html')
    context: dict = {'lastest_question_list': lastest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request: object, question_id: int) -> render:
    question = get_object_or_404(Question, pk=question_id)
    context: dict = {'question': question}
    return render(request, 'polls/detail.html', context)


def results(request: object, question_id: int) -> render:
    question = get_object_or_404(Question, pk=question_id)
    context: dict = {'question': question}
    return render(request, 'polls/results.html', context)


def vote(request: object, question_id: int) -> HttpResponseRedirect:
    question: object = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        responses: dict = dict(question=question, error_message="you didn't select a choice.")
        return render(request, 'polls/detail.html', responses)
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
