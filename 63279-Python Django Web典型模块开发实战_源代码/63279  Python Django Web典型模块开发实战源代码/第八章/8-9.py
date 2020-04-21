from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle
# Create your views here.
class IndexView(APIView):
    """
    演示视图
    """
    throttle_classes = (AnonRateThrottle,)
    def get(self,request):
        return Response('本网页代表了所有浏览量高能带来收益的网页。')
