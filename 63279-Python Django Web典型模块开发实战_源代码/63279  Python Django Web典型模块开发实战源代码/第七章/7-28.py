from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from .models import UserProfile,Article,Comment,Card
from .serializers import UserProfileSerializer,ArticleSerializer,CommentSerializer,CardSerializer
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer,BrowsableAPIRenderer
# Create your views here.
class GetArticleView(APIView):
    """
    获取所有文章
    """
    renderer_classes = [JSONRenderer]  # 渲染器
    def get(self,request):
        article_list = Article.objects.all()
        re = ArticleSerializer(article_list, many=True)
        return Response(re.data)
class GetCommentView(APIView):
    """
    获取所有评论
    """
    renderer_classes = [JSONRenderer]  # 渲染器
    def get(self,request):
        Comment_list = Comment.objects.all()
        re = CommentSerializer(Comment_list, many=True)
        return Response(re.data)
#只是演示登录视图，并非实项目中可以使用的登录逻辑
class LoginView(APIView):
    """
    演示登录
    """
    renderer_classes = [JSONRenderer]  # 渲染器
    def get(self, request):
        username=request._request.GET.get('username')
        if username:
            user=UserProfile.objects.filter(username=username).first()
            if user:
                re = UserProfileSerializer(user)
                return Response(re.data)
            else:
                return HttpResponse('404')
        else:
            return HttpResponse('404')
class PushArticleView(APIView):
    """
    发表文章类
    """
    renderer_classes = [JSONRenderer]  # 渲染器
    def post(self,request):
        title=request._request.POST.get('title')
        content=request._request.POST.get('content')
        user_id=request._request.POST.get('id')
        # print(title,content)
        if title and content and user_id:
            all_card=Card.objects.all()
            err=[]
            for i in all_card:
                j=title.find(i.word)
                if j!=-1:
                    err.append(i)
                k=content.find(i.word)
                if k!=-1:
                    err.append(i)
            if err:
                re = CardSerializer(err, many=True)
                return Response(re.data)
            article=Article()
            article.title=title
            article.content=content
            user=UserProfile.objects.filter(id=user_id).first()
            article.user=user
            article.save()
            return HttpResponse(200)
        else:
            return HttpResponse(404)
class PushCommentView(APIView):
    """
    发表评论
    """
    renderer_classes = [JSONRenderer]  # 渲染器
    def post(self, request):
        comment = request._request.POST.get('comment')
        user_id = request._request.POST.get('id')
        # print(comment,user_id)
        if comment and user_id:
            all_card = Card.objects.all()
            for i in all_card:
                comment=comment.replace(i.word,"***")
            newcomment=Comment()
            newcomment.content=comment
            user = UserProfile.objects.filter(id=user_id).first()
            newcomment.user=user
            #为了简化与本节知识点无关的内容，给评论的文章一个默认值
            article=Article.objects.filter(id=1).first()
            newcomment.article=article
            newcomment.save()
            return HttpResponse(200)
        else:
            return HttpResponse(404)
