from django.shortcuts import render,HttpResponse,redirect
from django.core.urlresolvers import reverse
from .models import *
# Create your views here.
#首页的
def index(request):
    list1 = Article.objects.filter(isDelete=False)

    return render(request,'modo/index.html',{'list':list1})
#列表的
def detall(request,id):
    article = Article.objects.get(pk = id)
    return render(request, 'modo/detall.html',{'art':article})
#编写的
def edgitpage(request):
    return render(request, 'modo/edgitpage.html')
#编辑提交
#编写的
def edgitpageHandle(request):
    title1 = request.POST.get('title')
    content1 = request.POST.get('content')
    a = Article()
    if title1 == '':
        title1 = '请输入标题'
    a.title = title1
    a.content = content1
    a.read = 0
    a.save()
    return redirect(reverse('blog:ind'))
def revise(request,id):
    r = Article.objects.get(pk =id)
    return render(request,'modo/revise.html',{'dx':r})

def revisehandle(request,id):
    t = request.POST.get('title')
    c = request.POST.get('content')
    a = Article.objects.get(pk = id)
    a.title = t
    a.content = c
    a.save()
    return redirect(reverse('blog:ind'))

def delete(request,id):
    o = Article.objects.get(pk=id)
    o.delete()
    return redirect(reverse('blog:ind'))

