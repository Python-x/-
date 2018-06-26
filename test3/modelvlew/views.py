from django.shortcuts import render
from .models import *
from django.template import *
from django.http import *
from modelvlew.static.templatedemo import *
# Create your views here.
def ind(request):
    r = request.GET
    w = r.getlist('us')
    return render(request,'modelvlew/in.html',{'r':w})
def show(request,k1,k2,k3):
    return render(request,'modelvlew/show.html',{'list':[k1,k2,k3]})

def gettest1(request):
    return render(request,'modelvlew/gettest1.html')
def gettest2(request):
    r = request.GET
    return render(request,'modelvlew/gettest2.html',{'r':r})
def gettest3(request):
    r = request.GET
    return render(request,'modelvlew/gettest3.html',{'r':r.getlist('us')})

def log(request):
    return render(request,'modelvlew/login.html')

def post(request):
    r = request.POST
    return render(request,'modelvlew/post.html',{'post':'<h1>haha</h1>'})
def static(request):
    return render(request,'modelvlew/staticdemo.html')