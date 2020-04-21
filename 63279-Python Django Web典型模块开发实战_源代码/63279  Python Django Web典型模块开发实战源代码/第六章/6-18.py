import re
from django.shortcuts import HttpResponse
from django.utils.deprecation import MiddlewareMixin
class ValidPermission(MiddlewareMixin):
    """
    权限验证中间件类
    """
    def process_request(self,request):
        ######################中间件内容start###############
        # 获取session键值，如果不存在不报错，返回[]
        permission_list = request.session.get('permission_list', [])
        # print(permission_list)
        path = request.path_info
        # print(path)
        flag = False
        for permission in permission_list:
            permission = "^%s$" % permission
            ret = re.match(permission, path)
            if ret:
                flag = True
                break
        # print(flag)
        if not flag:
            return HttpResponse('无访问权限！')
        ##################中间件内容end###################
        return None
