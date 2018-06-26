from django.shortcuts import render,redirect
from .models import *
from django.core.urlresolvers import reverse
# Create your views here.
def index(request):
    return render(request,'in/index.html')
def ok(request):
    user=request.POST.get('user','')
    pwd=request.POST.get('pwd','')
    a=Mimi()
    a.user=user
    a.pwd=pwd
    a.save()
    return redirect(reverse('in:index'))
def denglu(request):
    return render(request,'in/denglu.html')
def dd(request):
    c=request.POST.get('user','')
    b=request.POST.get('pwd','')
    print(c)
    a=Mimi.objects.get(user=c)
    if a.pwd == b:
        return render(request,'in/worry.html')
    else:
        return render(request, 'in/welcome.html')
def hello(request):
    return render(request,'in/hello.html')

