from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.template import loader

from .models import Question


def index(request: object) -> render:
    lastest_question_list: list = Question.objects.order_by('-pub_date')[:5]
    template: object = loader.get_template('polls/index.html')
    context: dict = {'lastest_question_list': lastest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request: object, question_id: int) -> render:
    question = get_object_or_404(Question, pk=question_id)
    context: dict = {'question': question}
    return render(request, 'polls/detail.html', context)


def result(question_id) -> HttpResponse:
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(question_id) -> HttpResponse:
    return HttpResponse("You're voting on question %s." % question_id)
