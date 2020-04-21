from django.contrib import admin
from django.urls import path
from app01.views import GetGoodListView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('goodlist/',GetGoodListView.as_view(),name='goodlist')
]
