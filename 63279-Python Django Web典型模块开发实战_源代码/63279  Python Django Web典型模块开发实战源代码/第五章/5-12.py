from django.contrib import admin
from django.urls import path
from app01.views import login,index,logout
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login.html', login),
    path('index.html', index),
    path('logout.html', logout),
]
