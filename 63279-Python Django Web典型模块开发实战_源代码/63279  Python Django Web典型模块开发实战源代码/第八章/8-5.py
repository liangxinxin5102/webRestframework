from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.
class IndexView(APIView):
    """
    —› æ ”Õº
    """
    def get(self,request):
        return render(request,'index.html')
