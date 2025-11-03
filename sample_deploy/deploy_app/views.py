from django.shortcuts import render
from django.http import HttpResponse,JsonResponse


# Create your views here.
def sample(req):
    return HttpResponse("Hello")