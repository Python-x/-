from django.shortcuts import render
from app.models import *
from user.models import *
# Create your views here.

def login1(request):
    return render(request, 'signup.html')
def register1(request):
    return render(request, 'register.html')
def shop_car(request):
    return render(request, 'checkout.html')