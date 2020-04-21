from django.shortcuts import render,redirect,HttpResponse
from .models import Administrator
# Create your views here.
#自定义登录函数视图
def login(request):
    message = ""
    if request.method == "POST":
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        c = Administrator.objects.filter(username=user, password=pwd).count()
        if c:
            rep = redirect('index.html')
            rep.set_cookie('username', user)
            rep.set_cookie('password', pwd)
            return rep
        else:
            message = "用户名或密码错误"
    return render(request,'login.html', {'msg': message})
#访问首页视图函数
def index(request):
    # 如果用户已经登录，获取当前登录的用户名
    # 否则，返回登录页面
    username = request.COOKIES.get('username')
    password = request.COOKIES.get('password')
    c = Administrator.objects.filter(username=username, password=password).count()
    if c:
        return render(request, 'index.html', {'username': username})
    else:
        return redirect('/login.html')
