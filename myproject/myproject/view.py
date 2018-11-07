from django.http import HttpResponse
from django.template import loader,Context
from django.shortcuts import render


def hello(request):
    return HttpResponse("Hello world ! ")

def index(request):
    #t=loader.get_template("index.html")
    #c=Context({})
    return render(request, 'index.html')

def home(request):
    return HttpResponse("home ! ")

def blog(request):
    return HttpResponse("my blog ! ")

def study(request):
    return HttpResponse("welcome to learn ui ! ")
