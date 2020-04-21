from django.contrib import admin
from django.urls import path
#引入获取文章列表视图类，获取评论视图类
from app01.views import GetArticleView,GetCommentView
#引入获取登录视图类，获取发表文章视图类，发表评论视图类
from app01.views import LoginView,PushArticleView,PushCommentView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',LoginView.as_view(),name='login'),
    path('getarticle/',GetArticleView.as_view(),name='getarticle'),
    path('getcomment/',GetCommentView.as_view(),name='getcomment'),
    path('pusharticle/',PushArticleView.as_view(),name='pusharticle'),
    path('pushcomment/',PushCommentView.as_view(),name='pushcomment')
]
