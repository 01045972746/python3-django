from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world ~~")

def detail(request, q_id):
    return HttpResponse("Looking at Question %s" %q_id)

def results(request, q_id):
    response = "Looking at Results of Question %s"
    return HttpResponse(response % q_id)

def vote(request, q_id):
    return HttpResponse("Voting on Question %s" %q_id)