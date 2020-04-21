from django.contrib import admin
from django.urls import path
from app01.views import login,userinfo
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login),
    path('userinfo01/', userinfo),
]
