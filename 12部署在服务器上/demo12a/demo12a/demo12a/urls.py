from django.contrib import admin
from django.urls import path
#配置媒体文件路径
from django.views.static import serve
from demo12a.settings import MEDIA_ROOT
#获取图文信息的视图类
from apps.app01.views import GetTuWenView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('media/<path:path>',serve,{'document_root':MEDIA_ROOT}),
    path('getdata/',GetTuWenView.as_view())
]
