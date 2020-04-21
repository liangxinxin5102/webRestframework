from rbac.models import User,Permission,Role
def initial_permission(user,request):
    # 查询角色
    ret = user.role.all()
    # print(ret)#<QuerySet [<Role: 人力资源总监>]>
    # 查询角色所对应的权限
    permission_list = []
    for item1 in ret:
        # 多对多连表查询
        rep = Permission.objects.filter(role__title=item1)
        for item2 in rep:
            # print(item2.url)#/users/
            permission_list.append(item2.url)
    # print(permission_list)
    request.session["permission_list"] = permission_list
