from django.conf.urls import include, url
from django.contrib import admin
from . import views
urlpatterns = [

    url(r'^index/', views.index, name='index'),
    url(r'^ok/', views.ok,name='ok'),
    url(r'^denglu/', views.denglu,name='denglu'),
    url(r'^hello/', views.hello,name='hello'),
    url(r'^dd/', views.dd,name='dd'),
]
