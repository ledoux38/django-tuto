from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import loader

from .models import Question


def index(request: object) -> render:
    lastest_question_list: list = Question.objects.order_by('-pub_date')[:5]
    template: object = loader.get_template('polls/index.html')
    context: dict = {'lastest_question_list': lastest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request: object, question_id: int) -> render:
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question des not exist")
    context: dict = {'question': question}
    print(context)
    return render(request, 'polls/detail.html', context)


def result(question_id) -> HttpResponse:
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(question_id) -> HttpResponse:
    return HttpResponse("You're voting on question %s." % question_id)
