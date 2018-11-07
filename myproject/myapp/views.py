from django.shortcuts import render
from django.template import loader,Context
# Create your views here.

from django.http import HttpResponse
 

def baidu(request):
    return HttpResponse(request,"Shotgun Support.html")
