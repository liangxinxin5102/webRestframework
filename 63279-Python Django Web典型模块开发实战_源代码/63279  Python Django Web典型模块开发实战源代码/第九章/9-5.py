from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer,BrowsableAPIRenderer
# Create your views here.
class BookView(APIView):
    """
     ÈºÆ¡–±Ì
    """
    renderer_classes = [JSONRenderer]  # ‰÷»æ∆˜
    def get(self,request):
        book_list = Book.objects.all()
        re = BookSerializer(book_list, many=True)
        return Response(re.data)
