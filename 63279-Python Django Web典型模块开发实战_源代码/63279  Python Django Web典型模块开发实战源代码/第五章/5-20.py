from django.shortcuts import render,redirect,HttpResponse
from rest_framework.views import APIView
# Create your views here.
class IndexView(APIView):
    """
    ��ҳ
    """
    # authentication_classes = []
    # permission_classes = []
    def get(self,request):
        # print(request)
        return HttpResponse('��ҳ')
