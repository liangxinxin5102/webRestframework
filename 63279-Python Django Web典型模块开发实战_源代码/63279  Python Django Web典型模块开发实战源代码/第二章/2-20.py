from .serializers import BookModelSerializer
from rest_framework.response import Response
from .models import UserProfile,Book
from rest_framework import viewsets
from rest_framework.permissions import BasePermission
class IsDeveloper(BasePermission):
    message='查无此人啊'
    def has_permission(self,request,view):
        APIKey = request.query_params.get("apikey", 0)
        developer = UserProfile.objects.filter(APIkey=APIKey).first()
        if developer:
            return True
        else:
            print(self.message)
            return False
class EnoughMoney(BasePermission):
    message = "兄弟，又到了需要充钱的时候！好开心啊！"
    def has_permission(self,request,view):
        APIKey = request.query_params.get("apikey", 0)
        developer = UserProfile.objects.filter(APIkey=APIKey).first()
        balance = developer.money
        if balance > 0:
            developer.money -= 1
            developer.save()
            return True
        else:
            return False
class BookModelViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = [IsDeveloper, EnoughMoney]
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
    def get_queryset(self):
        isbn = self.request.query_params.get("isbn", 0)
        books = Book.objects.filter(isbn=int(isbn))
        queryset=books
        return queryset
