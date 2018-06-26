from django.shortcuts import render, HttpResponse
from app.models import *
from user.models import *


# Create your views here.
def index(request):
    shoes = Shoes.objects.all()
    banners = Banner_shoe.objects.all()
    brank_list = Brank.objects.all()[:6]
    category = Category.objects.all()

    cdx = {
        'banner_list1': banners[0],
        'banner_list2': banners[1:],
        'shoe_list': shoes,
        'brank_list': brank_list,
        'category': category,
    }
    return render(request, '../../xiangmu/templates/index.html', cdx)


brank_list = Brank.objects.all()[:6]
category = Category.objects.all()


def products(request, tid=-1, bid=-1):
    if tid != -1:
        shoe1_list = Shoes.objects.filter(brand=tid)
    elif bid != -1:
        shoe1_list = Shoes.objects.filter(category=bid)
    else:
        shoe1_list = Shoes.objects.all()

    cdx = {
        'shoe_list': shoe1_list,
        'brank_list': brank_list,
        'category': category,
    }
    return render(request, '../../xiangmu/templates/products.html', cdx)


def contact_as(request):
    return render(request, '../../xiangmu/templates/contact.html')


def single(request, sid):
    shoe = Shoes.objects.get(id=sid)
    cdx = {
        'shoe':shoe,
    }
    return render(request, '../../xiangmu/templates/single.html',cdx)
