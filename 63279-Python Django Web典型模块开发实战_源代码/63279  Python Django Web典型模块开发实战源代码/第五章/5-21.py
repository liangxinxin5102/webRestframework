from django.contrib import admin
from django.urls import path
from rest_framework.authtoken import views
from app01.views import IndexView
urlpatterns = [
    path('admin/', admin.site.urls),
#drf自带的token认证模式
    path('api-token-auth/', views.obtain_auth_token),
    path('index/',IndexView.as_view(),name='index'),
]
