from django.shortcuts import render
from django.views.generic.base import View
from .models import Books
# Create your views here.
class BookListView(View):
    """
    获取图书列表
    """
    def get(self,request):
        list=Books.objects.all()
        return render(request,'booklist.html',{'list':list})
class GetBookView(View):
    """
    获取单个图书
    """
    def get(self,request,id):
        book=Books.objects.filter(id=id).first()
        print(book.pv)
        book.pv+=1
        book.save()
        return render(request,'book.html',{'t':book})
