from django.shortcuts import render
from django.http import HttpResponse
from booktest.models import *
# Create your views here.
def index(request):
    d = Bookinfo.objects.all()
    return render(request, 'booktest/show.html', {'booklist':d})
def detail(request,id):
    book = Bookinfo.objects.get(pk = id)
    return render(request, 'booktest/declit.html', {'book':book})
