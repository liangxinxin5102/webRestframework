def login(request):
    message = ""
    if request.method == "POST":
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        c = Administrator.objects.filter(username=user, password=pwd).count()
        if c:
			#加密
            rep = redirect('index.html')
            rep.set_signed_cookie('username', user)
            rep.set_signed_cookie('password', pwd)
            return rep
        else:
            message = "用户名或密码错误"
    return render(request,'login.html', {'msg': message})
def index(request):
    # 如果用户已经登录，获取当前登录的用户名
    # 否则，返回登录页面
    username = request.get_signed_cookie('username')
    password = request.get_signed_cookie('password')
    c = Administrator.objects.filter(username=username, password=password).count()
    if c:
        return render(request, 'index.html', {'username': username})
    else:
        return redirect('/login.html')
