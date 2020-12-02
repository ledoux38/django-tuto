from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request: object) -> HttpResponse:
    lastest_question_list: list = Question.objects.order_by('-pub_date')[:5]
    template: object = loader.get_template('polls/index.html')
    context: dict = {'lastest_question_list': lastest_question_list}
    return HttpResponse(template.render(context, request))


def detail(question_id) -> HttpResponse:
    return HttpResponse("You're looking at question %s." % question_id)


def result(question_id) -> HttpResponse:
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(question_id) -> HttpResponse:
    return HttpResponse("You're voting on question %s." % question_id)
