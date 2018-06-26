from django.contrib import admin
from app.models import *
# from
# Register your models here.
class DetailInfo(admin.StackedInline):
    model = Detail_pic
    extra = 4

class ShoesInfo(admin.ModelAdmin):
    inlines = [DetailInfo]







admin.site.register(Shoes, ShoesInfo)
admin.site.register(Brank)
admin.site.register(Category)
admin.site.register(Banner_shoe)
admin.site.register(Detail_pic)
admin.site.register(Grand)
