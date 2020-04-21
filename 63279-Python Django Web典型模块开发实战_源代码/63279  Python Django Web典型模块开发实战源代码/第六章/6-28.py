from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from .models import *
# Create your views here.
def md5(user):
    import hashlib
    import time
    ctime=str(time.time())
    m=hashlib.md5(bytes(user,encoding='utf-8'))
    m.update(bytes(ctime,encoding='utf-8'))
    return m.hexdigest()
class AuthView(APIView):
    """
    登录
    """
    def post(self,request):
        ret={'code':1000,'msg':'登录成功！'}
        try:
            user=request._request.POST.get('username')
            pwd=request._request.POST.get('password')
            obj=UserInfo.objects.filter(username=user,password=pwd).first()
            if not obj:
                ret['code']=1001
                ret['msg']='用户名或密码错误'
                return JsonResponse(ret)
            #为登录用户创建token
            token=md5(user)
            #存在则更新，不存在的创建
            UserToken.objects.update_or_create(user=obj,defaults={'token':token})
            ret['token']=token
        except Exception as e:
            ret['code']=1002
            ret['msg']='请求异常'
        return JsonResponse(ret)
