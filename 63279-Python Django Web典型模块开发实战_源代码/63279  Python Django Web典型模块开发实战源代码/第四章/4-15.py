from django.contrib import admin
from django.urls import path
from app01.views import SendCodeView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('sendcode/',SendCodeView.as_view(),name='sendcode')
]
