from django.contrib import admin
from django.urls import path
from users.views import BookAPIView1
urlpatterns = [
    path('admin/', admin.site.urls),
    path('apibook1/',BookAPIView1.as_view(),name='book1'),
]
