from django.http import HttpResponse
class MyException():
    def process_exception(request,response,exception):
        if isinstance(exception,ZeroDivisionError):
            return HttpResponse('分母不能为0')
        elif isinstance(exception,ValueError):
            return HttpResponse('数值错误')
