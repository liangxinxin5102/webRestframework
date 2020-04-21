from django.shortcuts import render
#引入APIview
from rest_framework.views import APIView
#引入用户数据表类
from .models import UserProfile,Article
#引入序列化类
from .serializers import UserProfileSerializer,ArticleSerializer
#引入drf功能模块
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer,BrowsableAPIRenderer
#引入Q模块
from django.db.models import Q
# Create your views here.
class GetArticleViews(APIView):
    """
    获取文章列表
    """
    def get(self,request):
        keyword=request._request.GET.get('keyword')
        # print(keyword)
        if keyword:
            article_list = Article.objects.filter(Q(title__icontains=keyword)|Q(content__icontains=keyword))
        else:
            article_list = Article.objects.all()
        re = ArticleSerializer(article_list, many=True)
        return Response(re.data)
