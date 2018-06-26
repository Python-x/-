"""test3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from modelvlew import views
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^static/',views.static),
    url(r'^(?P<k1>\d+)/(?P<k2>\d+)/(?P<k3>\d+)',views.show),
    url(r'^ind',views.ind),
    url(r'^get$',views.gettest1),
    url(r'^get2',views.gettest2),
    url(r'^get3',views.gettest3),
    url(r'^pot',views.post),
    url(r'^log',views.log),
]
