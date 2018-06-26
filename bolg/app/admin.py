from django.contrib import admin
from .models import *
# from
# Register your models here.
class Articleinfo(admin.ModelAdmin):
    list_display = ['title','content','pub_datetime','read']
    list_filter = ['title']
    search_fields = ['title']
    list_per_page = 1
admin.site.register(Article,Articleinfo)