from django.shortcuts import render
from .models import Goods
from .serializers import GoodsModelSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_extensions.cache.mixins import CacheResponseMixin
# Create your views here.
class GetGoodListView(APIView):
    """
    获取商品列表
    """
    def get(self,request):
        good_list=Goods.objects.all()
        re=GoodsModelSerializer(good_list,many=True)
        return Response(re.data)
