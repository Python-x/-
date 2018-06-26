from django.conf.urls import include, url
from . import views

urlpatterns = [
    # 首页
    url(r'^index/$',views.index,name='ind'),
    # 列表页
    url(r'^detall/(\d+)/$',views.detall,name='det'),
    # 编写页
    url(r'^edgitpage/$',views.edgitpage,name='edg'),
    #提交
    url(r'^edgitpageHandle/$',views.edgitpageHandle,name='edgHan'),
    #修改
    url(r'^revise/(\d*)$',views.revise,name='revise'),
    #修改2
    url(r'^reviseHandle(\d*)$',views.revisehandle,name='revisehandle'),
    #删除
    url(r'^delete/(\d*)$',views.delete,name='delete'),

]
