from ..models import *
from rest_framework import exceptions
class Authtication(object):
    def authenticate(self,request):
        # 验证是否已经登录,函数名必须为：authenticate
        token = request._request.GET.get('token')
        token_obj=UserToken.objects.filter(token=token).first()
        if not token_obj:
            raise exceptions.AuthenticationFailed('用户认证失败。')
        #在rest_framework内部会将以下两个元素赋值到request，以供后续使用
        return (token_obj.user,token_obj)
    def authenticate_header(self,request):
        #这个函数可以没内容，但是必须要有
        pass
