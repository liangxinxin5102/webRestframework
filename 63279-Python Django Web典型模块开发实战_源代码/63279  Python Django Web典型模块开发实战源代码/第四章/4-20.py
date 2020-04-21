from django.contrib import admin
from django.urls import path
from app01.views import SendCodeView,RegisterView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('sendcode/',SendCodeView.as_view(),name='sendcode'),
    path('register/',RegisterView.as_view(),name='register')
]
