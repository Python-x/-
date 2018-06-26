from django.contrib import admin
from booktest.models import *
# Register your models here.
class HeroInfoInline(admin.StackedInline):
    model = Heroinfo
    extra = 10
class HeroInfo(admin.ModelAdmin):

    def gender(self):
        if self.hgender == 1:
            return '男'
        else:
            return '女'
        gender.short_description = '性别'
    list_display = ['hname', gender, 'hcontent', 'hBook']
class BookInfo(admin.ModelAdmin):
    list_display = ['pk','btitle','bpub_date']
    fields = ['bpub_date','btitle']
    list_filter = ['btitle']
    search_fields = ['btitle']
    list_per_page = 1
    # fieldsets = [('basic', {'fields': ['btitle']}),('more', {'fields': ['bpub_date']})]
    inlines = [HeroInfoInline]




admin.site.register(Bookinfo,BookInfo)
admin.site.register(Heroinfo,HeroInfo)