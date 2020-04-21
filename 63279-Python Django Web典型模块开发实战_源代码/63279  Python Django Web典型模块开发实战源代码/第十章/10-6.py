from django.contrib import admin
from django.urls import path
from app01.views import RegisterView,LoginView,ShopView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',RegisterView.as_view(),name='register'),
    path('login/',LoginView.as_view(),name='login'),
    path('shop/',ShopView.as_view(),name='shop'),
]
