# @Time    : 18-6-19 下午7:49
# @Author  : panzhiwei
# @Site    :
# @File    : urls.py
# @Software: PyCharm
from django.conf.urls import url, include
from user import views as user_views
urlpatterns = [
    url(r'^register/$', user_views.register1, name='register'),
    url(r'^login/$', user_views.login1, name='login'),
    url(r'^shopcar/$', user_views.shop_car, name='shopcar'),
]
