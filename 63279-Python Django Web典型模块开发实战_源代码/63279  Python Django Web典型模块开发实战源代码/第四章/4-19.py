class RegisterView(APIView):
    """
    注册类
    """
    def get(self,request):
        username=request.GET.get('username')
        pwd=request.GET.get('pwd')
        phone=request.GET.get('phone')
        email=request.GET.get('email')
        code=request.GET.get('code')
        if username:
            pass
        else:
            msg = '用户名不能为空！'
            result = {"status": "404", "data": {'msg': msg}}
            return HttpResponse(json.dumps(result, ensure_ascii=False),
                                content_type="application/json,charset=utf-8")
        if pwd:
            pass
        else:
            msg = '密码不能为空！'
            result = {"status": "404", "data": {'msg': msg}}
            return HttpResponse(json.dumps(result, ensure_ascii=False),
                                content_type="application/json,charset=utf-8")
        if phone:
            pass
        else:
            msg = '手机号不能为空！'
            result = {"status": "404", "data": {'msg': msg}}
            return HttpResponse(json.dumps(result, ensure_ascii=False),
                                content_type="application/json,charset=utf-8")
        if email:
            pass
        else:
            msg = '邮箱不能为空！'
            result = {"status": "404", "data": {'msg': msg}}
            return HttpResponse(json.dumps(result, ensure_ascii=False),
                                content_type="application/json,charset=utf-8")
        if code:
            pass
        else:
            msg = '验证码不能为空！'
            result = {"status": "404", "data": {'msg': msg}}
            return HttpResponse(json.dumps(result, ensure_ascii=False),
                                content_type="application/json,charset=utf-8")
        #查找对比验证码
        code1=Code.objects.filter(phone=phone).last()
        if code==code1:
            #验证验证码是否已经过期
            end_time=code1.end_time
            end_time=end_time.replace(tzinfo=None)
            if end_time > datetime.datetime.now():
                user = UserProfile()
                user.username = username
                user.password = pwd
                user.phone = phone
                user.email=email
                user.save()
                msg = '注册成功！'
                result = {"status": "200", "data": {'msg': msg}}
                return HttpResponse(json.dumps(result, ensure_ascii=False),
                                    content_type="application/json,charset=utf-8")
            else:
                msg = '验证码已过期！'
                result = {"status": "403", "data": {'msg': msg}}
                return HttpResponse(json.dumps(result, ensure_ascii=False),
                                    content_type="application/json,charset=utf-8")
        else:
            msg = '验证码错误！'
            result = {"status": "403", "data": {'msg': msg}}
            return HttpResponse(json.dumps(result, ensure_ascii=False),
                                content_type="application/json,charset=utf-8")
