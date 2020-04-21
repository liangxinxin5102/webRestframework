from django.contrib import admin
from django.urls import path
#引入模糊搜索相关视图类
from app01.views import GetArticleViews
urlpatterns = [
path('admin/', admin.site.urls),
#搜索文章路由
    path('getlist/',GetArticleViews.as_view(),name='getlist'),
]
