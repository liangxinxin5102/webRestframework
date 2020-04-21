from django.contrib import admin
from django.urls import path
from app01.views import AuthView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/',AuthView.as_view(),name='auth'),
]
