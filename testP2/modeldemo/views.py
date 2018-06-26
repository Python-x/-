from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.core.urlresolvers import reverse
from datetime import *
from django.db.models import *

# Create your views here.
def get123(request):
    b=get_object_or_404(College,pk = 999)
    return redirect('/show')
def show(request):
    list1 = College.bm2.all()
    return render(request,'modeldemo/show.html',{'list':list1})

def test(request):
    # stu = Student.objects.filter(swj__cname=)
    return render(request,'modeldemo/test.html',{'li':0})

def index(request):
    pass
def login(request):
    pass
def login_hanle(request):
    pass
def loginout(request):
    pass

