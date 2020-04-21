from django.contrib import admin
from django.urls import path
from app01.views import BookListView,GetBookView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('booklist/',BookListView.as_view(),name='booklist'),
    path('book/<id>/',GetBookView.as_view(),name='book')
]
