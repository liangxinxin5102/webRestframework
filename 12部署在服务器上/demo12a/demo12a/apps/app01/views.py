from django.shortcuts import render
from .models import TuWen #引入图文表
from .serializers import TuWenModelSerializer#引入图文表的序列化类
#引入drf的功能组件
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
# Create your views here.
class GetTuWenView(APIView):
    """
    获取图文列表
    """
    renderer_classes = [JSONRenderer]  # 渲染器
    def get(self,request):
        t_list=TuWen.objects.all()
        re=TuWenModelSerializer(t_list,many=True)
        return Response(re.data)
