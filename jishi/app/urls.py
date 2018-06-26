from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^index$',views.index,name='index'),
    url(r'^register$',views.register,name='register'),
    url(r'^login$',views.login,name='login'),
    url(r'^loginHandle$',views.loginHandle,name='loginHandle'),
    url(r'^registerHandle$',views.registerHandle,name='registerHandle'),
    url(r'^liuyan$',views.liuyan,name='liuyan'),
    url(r'^cun$',views.cun,name='cun'),
    url(r'^xiangq/(\d*)$',views.xiangq,name='xiangq'),
]
