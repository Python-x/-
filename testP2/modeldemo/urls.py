from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r'^show', views.show,name='show2'),
    url(r'^tes',views.test,name='test3'),
    url(r'^ge',views.get123),
    url(r'index$',views.index,name='index'),
    url(r'login$',views.login,name='login'),
    url(r'loginhanle$',views.login_hanle,name='login_han'),
    url(r'loginout$',views.loginout,name='loginout'),
]