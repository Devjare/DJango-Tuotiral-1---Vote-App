from django.shortcuts import get_object_or_404, render
from django.shortcuts import HttpResponse
from django.http import Http404

from django.template import loader

from polls.models import Question

# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]

    # Old way
    # template = loader.get_template("polls/index.html")
    context = {"latest_question_list": latest_question_list}

    # Old way
    # return HttpResponse(template.render(context, request))
    # Most common way
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    response = f"You are looking at the results of question {question_id}."
    return HttpResponse(response)


def vote(request, question_id):
    return HttpResponse(f"You are votin on question {question_id}.")
