from django.contrib import admin
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from app01.views import IndexView
urlpatterns = [
    path('admin/', admin.site.urls),
#jwt的认证接口
    path('jwt-token-auth/', obtain_jwt_token),
    path('index/',IndexView.as_view(),name='index')
]
