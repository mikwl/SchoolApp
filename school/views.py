from django.shortcuts import render,redirect,HttpResponse
from  django.conf import settings

def index(request):
    return HttpResponse('Hello this is index page   ')


