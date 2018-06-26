
# Create your views here.
def xiangq(request,id):
    p = Leveo.objects.filter(pk = id)
    return render(request,'app/xiangq.html',{'p':p})
def cun(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    address = request.POST.get('address')
    message = request.POST.get('message')
    n = Leveo()
    n.name = name
    n.email = email
    n.site =address
    n.message = message
    n.save()
    return redirect(reverse('jishi:index'))
def index(request):
    p = Leveo.objects.all()
    return render(request,'app/index.html',{'p':p})
def login(request):
    return render(request,'app/login.html')
def register(request):
    return render(request,'app/register.html')
def registerHandle(request):
    zh = request.POST.get('zh')
    mm1 = request.POST.get('mm')
    mm = doPwd(mm1)
    a = User()
    a.zhe = zh
    a.mm = mm
    a.save()
    return redirect(reverse('jishi:index'))

def liuyan(request):
    return render(request,'app/留言板.html')
def loginHandle(request):
    zh = request.POST.get('zh')
    if zh == '':
        return redirect(reverse('jishi:login'))
    mm1 = request.POST.get('mm')
    mm = doPwd(mm1)
    a = User.objects.get(zhe=zh)
    if a.mm == mm or zh =='':
        return redirect(reverse('jishi:index'))
    else:
        return redirect(reverse('jishi:login'))

def doPwd(pwd):
    '''sha1编码'''
    mysha1 = hashlib.sha1()
    mysha1.update(pwd.encode('utf-8'))
    pwd = mysha1.hexdigest()
    return pwd
