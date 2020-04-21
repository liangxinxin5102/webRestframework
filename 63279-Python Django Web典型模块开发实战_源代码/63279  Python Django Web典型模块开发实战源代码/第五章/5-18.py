from rest_framework.authtoken import views
urlpatterns = [
    #……
#drf自带的token认证模式
    path('api-token-auth/', views.obtain_auth_token),
]
