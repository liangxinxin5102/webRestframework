from django.contrib import admin
from django.urls import path
from app01.views import BookView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/',BookView.as_view(),name='book'),
]
