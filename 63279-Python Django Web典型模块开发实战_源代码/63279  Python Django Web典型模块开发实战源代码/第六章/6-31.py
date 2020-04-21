from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
#引入所有数据表
from .models import *
引入所有序列化类
from .serializers import *
#引入drf相关模块
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer,BrowsableAPIRenderer
from rest_framework import exceptions
# Create your views here.
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
class CommonVideoView(APIView):
    """
    登录后即可访问的内容资源
    """
    renderer_classes = [JSONRenderer]  # 渲染器
    authentication_classes = [Authtication,]
    def get(self,request):
        # print(request.user,request.auth)#user1 user1
        video_list = CommonVideo.objects.all()
        re = CommonVideoSerializer(video_list, many=True)
        return Response(re.data)
#…………
