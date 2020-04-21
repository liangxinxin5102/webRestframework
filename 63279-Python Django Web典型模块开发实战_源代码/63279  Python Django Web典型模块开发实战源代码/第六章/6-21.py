def login(request):
#登录函数
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
            # print(permission_list)
            request.session["permission_list"] = permission_list
            return HttpResponse('登录成功')
    return render(request, "login.html")
