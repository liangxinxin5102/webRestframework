from django.shortcuts import render,redirect,HttpResponse
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from .utils.mixin_utils import LoginRequiredMixin
from .models import UserProfile
# Create your views here.
class RegisterView(View):
    """
    注册视图
    """
    def get(self, request):
        return render(request, 'register.html')
    def post(self,request):
        user=request.POST.get('username')
        pwd=request.POST.get('pwd')
        print(user,pwd)
        if user and pwd:
            had_reg=UserProfile.objects.filter(username=user)
            if had_reg:
                return HttpResponse('用户名已被注册')
            else:
                new_user=UserProfile()
                new_user.username=user
                new_user.password=make_password(pwd)
                new_user.save()
                return redirect('/login/')
        else:
            return HttpResponse('未收到注册数据')
class LoginView(View):
    """
    登录视图
    """
    def get(self,request):
        return render(request,'login.html')
    def post(self,request):
        user_name = request.POST.get('username', '')
        password = request.POST.get('pwd', '')
        if user_name and password:
            user = authenticate(username=user_name, password=password)
            if user:
                login(request, user)
                return redirect('/shop/')
        return HttpResponse('有错误')
class ShopView(LoginRequiredMixin,View):
    """
    购物视图
    """
    def get(self,request):
        return render(request,'shop.html')
    def post(self,request):
        return HttpResponse('200')
