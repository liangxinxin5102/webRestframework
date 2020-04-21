from django.contrib import admin
from django.urls import path
#from app01.views import login,index,logout
from rest_framework.authtoken import views
'''cookie和session
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login.html', login),
    path('index.html', index),
    path('logout.html', logout),
#drf自带的token认证模式
    path('api-token-auth/', views.obtain_auth_token),
]
'''
from app01.views import IndexView
urlpatterns = [
    path('admin/', admin.site.urls),
#drf自带的token认证模式
    path('api-token-auth/', views.obtain_auth_token),
    path('index/',IndexView.as_view(),name='index'),
]
