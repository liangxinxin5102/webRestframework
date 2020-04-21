''''
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

'''

from django.shortcuts import render,HttpResponse,redirect
from rbac.models import User,Permission,Role
# Create your views here.

from rbac.service.permission import initial_permission
def login(request):
    if request.method == "POST":
        username=request.POST.get('username')
        pwd=request.POST.get('pwd')
        user=User.objects.filter(name=username,pwd=pwd).first()
        if user:
            #验证身份
            request.session["user_id"]=user.pk
            initial_permission(user,request)
            return HttpResponse('登录成功')
    return render(request, "login.html")
# def login(request):
# #登录函数
#     if request.method == "POST":
#         username=request.POST.get('username')
#         pwd=request.POST.get('pwd')
#         user=User.objects.filter(name=username,pwd=pwd).first()
#         if user:
#             #验证身份
#             request.session["user_id"]=user.pk
#             #查询角色
#             ret=user.role.all()
#             # print(ret)#<QuerySet [<Role: 人力资源总监>]>
#             #查询角色所对应的权限
#             permission_list = []
#             for item1 in ret:
#                 #多对多连表查询
#                 rep =Permission.objects.filter(role__title=item1)
#                 for item2 in rep:
#                     # print(item2.url)#/users/
#                     permission_list.append(item2.url)
#             # print(permission_list)
#             request.session["permission_list"] = permission_list
#             return HttpResponse('登录成功')
#     return render(request, "login.html")

'''写法2：易读
def login(request):
    if request.method == "POST":
        username=request.POST.get('username')
        pwd=request.POST.get('pwd')
        user=User.objects.filter(name=username,pwd=pwd).first()
        if user:
            #验证身份
            request.session["user_id"]=user.pk
            #查询角色
            ret=user.role.all()
            # print(ret)#<QuerySet [<Role: 人力资源总监>]>
            #查询角色所对应的权限
            permission_list = []
            for item1 in ret:
                #多对多连表查询
                rep =Permission.objects.filter(role__title=item1)
                for item2 in rep:
                    # print(item2.url)#/users/
                    permission_list.append(item2.url)
            print(permission_list)
            request.session["permission_list"] = permission_list
           
  return HttpResponse('登录成功')
    return render(request, "login.html")

'''

import re
def user(request):
    #获取session键值，如果不存在不报错，返回None
    permission_list=request.session.get('permission_list',[])
    # print(permission_list)
    path=request.path_info
    # print(path)
    flag=False
    for permission in permission_list:
        permission="^%s$"%permission
        ret=re.match(permission,path)
        if ret:
            flag=True
            break
    # print(flag)
    if not flag:
        return HttpResponse('无访问权限！')
    return HttpResponse('查看用户')
