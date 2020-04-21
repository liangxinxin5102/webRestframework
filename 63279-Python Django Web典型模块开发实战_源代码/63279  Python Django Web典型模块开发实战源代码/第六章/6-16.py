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
