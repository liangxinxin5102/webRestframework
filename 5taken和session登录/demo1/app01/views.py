from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UserInfo

from app01.extensions.auth import JwtQueryParamAuthentication
from app01.utils.jwt_auth import create_token
class ProLoginView(APIView):
    authentication_classes = []
    def post(self, request, *args, **kwargs):
        user = request.data.get('username')
        pwd = request.data.get('password')

        user_object = UserInfo.objects.filter(username = user, password = pwd).first()
        if not user_object:
            return Response("用户名或密码错误")
        token = create_token({"id":user_object.id,'name':user_object.username})
        return Response({'code':1001,'data':token})

class ProOriderView(APIView):
    #authentication_classes = [JwtQueryParamAuthentication,]
    def get(self, request, *args, **kwargs):
        return Response("订单列表")