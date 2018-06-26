# @Time    : 18-6-19 下午7:48
# @Author  : panzhiwei
# @Site    :
# @File    : urls.py
# @Software: PyCharm
from django.conf.urls import url, include
from app import views as app_views
from user import views as user_views

urlpatterns = [
    url(r'^index/$', app_views.index, name='index'),
    url(r'^branch/(?P<tid>\d*)/$', app_views.products,name='branch'),
    url(r'^category/(?P<bid>\d*)/$', app_views.products,name='category'),
    url(r'^single/(?P<sid>\d*)$', app_views.single, name='single'),
    url(r'^contact/$', app_views.contact_as, name='contact'),

]
