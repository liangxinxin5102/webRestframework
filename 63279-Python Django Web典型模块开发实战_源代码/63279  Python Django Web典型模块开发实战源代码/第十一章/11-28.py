from django.shortcuts import render
from .models import Goods
from .serializers import GoodsModelSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_extensions.cache.mixins import CacheResponseMixin
from rest_framework_extensions.cache.decorators import cache_response
# Create your views here.	
class GetGoodListView(APIView):
    """
    获取商品列表
    """
    @cache_response()
    def get(self,request):
        good_list=Goods.objects.all()
        re=GoodsModelSerializer(good_list,many=True)
        return Response(re.data)
