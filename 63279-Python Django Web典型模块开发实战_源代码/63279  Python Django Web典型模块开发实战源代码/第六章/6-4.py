from django.shortcuts import render,HttpResponse,redirect
from .models import Userinfor,Permission
# Create your views here.
def login(request):
    if request.method == "POST":
        username=request.POST.get('username')
        pwd=request.POST.get('pwd')
        user=Userinfor.objects.filter(name=username,pwd=pwd).first()
        if user:
            #验证身份
            request.session["user_id"]=user.pk
            return HttpResponse('登录成功')
    return render(request, "login.html")
def userinfo(request):
    #首先进行身份验证
    pk=request.session.get('user_id')
    if not pk:
        return redirect("/login/")
    #然后进行权限验证
    user=Userinfor.objects.filter(id=pk).first()
    p_list = []
    p_queryset = user.permission.all()
    #获取用户的权限列表
    for p in p_queryset:
        p_list.append(p.url)
    #去重
    p_list=list(set(p_list))
    # print(p_list)
    # 获取URL
    c = request.path_info
    if c in p_list:
        u_queryset=Userinfor.objects.all()
        return render(request,"userinfo.html",{ "u_queryset":u_queryset})
    else:
        return HttpResponse('没有权限访问该页面')
