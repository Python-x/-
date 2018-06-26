from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.conf import settings
from .models import *
import os

# Create your views here.
def myException(request):
    # x=10/0
    # int('dasd')
    return HttpResponse('异常')
def uploadPic(request):
    return render(request,'modeldemo/uploaddemo.html')

def uploadHandle(request):
    pic1 = request.FILES.get('pic1')
    picName = os.path.join(settings.MEDIA_ROOT,pic1.name)
    with open(picName,'wb')as pic:
        for c in pic1.chunks():
            pic.write(c)
    return HttpResponse(picName)
def index(request):
    list1 = AreaInfo.objects.filter(aPArea__isnull=True)
    return render(request,'modeldemo/index.html',{'data':list1})

def getArea2(request):
    pid = request.POST['id']
    list1 = AreaInfo.objects.filter(aPArea_id=pid)
    list2 = []
    for a in list1:
        list2.append({'id':a.aid,'title':a.atitle})

    return JsonResponse({'data':list2})