from django.contrib import admin
from django.urls import path
from users.views import BookAPIView1,BookAPIView2
from users.views import BookMixinView1,BookMixinView2
urlpatterns = [
    path('admin/', admin.site.urls),
    path('apibook1/',BookAPIView1.as_view(),name='book1'),
    path('apibook2/',BookAPIView2.as_view(),name='book2'),
    path('apibook3/',BookMixinView1.as_view(),name='book3'),
    path('apibook4/',BookMixinView2.as_view(),name='book4'),
]
