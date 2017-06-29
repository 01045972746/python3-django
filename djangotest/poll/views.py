from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader, RequestContext

from poll.models import Question

# Create your views here.
def index(request):
    latest_q_list = Question.objects.order_by('-q_date')[:5]

    context = {'latest_q_list': latest_q_list}
    return render(request, 'poll/hello.html', context)

def detail(request, q_id):
    question = get_object_or_404(Question, pk=q_id)
    return render(request, 'poll/detail.html', {'question': question})

def results(request, q_id):
    response = "Looking at Results of Question %s"
    return HttpResponse(response % q_id)

def vote(request, q_id):
    return HttpResponse("Voting on Question %s" %q_id)