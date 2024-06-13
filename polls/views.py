from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404

from .models import Question

# polls/
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    #entrada sin un template y recorrido para separar las preguntas con una coma
    # output = ", ".join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    
    #entrada con un template y el template lo recorre mediante una lista
    # template = loader.get_template("polls/index.html")
    # context = {
    #     "latest_question_list": latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))
    
    #entrada con un template y el template lo recorre mediante un diccionario
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

#polls/<int:question_id>/
def detail(request, question_id):
    #ingreso con try y except para manejar el error 404
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, "polls/detail.html", {"question": question})
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)