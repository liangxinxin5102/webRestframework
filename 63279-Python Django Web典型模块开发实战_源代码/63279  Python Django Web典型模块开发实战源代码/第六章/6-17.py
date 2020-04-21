from django.contrib import admin
from django.urls import path
from app01.views import login,user
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login),
    path('users/', user),
]
