from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from .models import Question

from django.http import Http404
from django.shortcuts import render

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/dashboard.0.html', context)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
    
def inbox(request):
    return render(request, 'polls/inbox.html')

def contact(request):
    return render(request, 'polls/contact.html')

def calendar(request):
    return render(request, 'polls/calendar.html')

#def index(request):
#    return HttpResponse("This is the first view test")

#hard coded, let's create a templated view instead
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = '<br/> '.join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))