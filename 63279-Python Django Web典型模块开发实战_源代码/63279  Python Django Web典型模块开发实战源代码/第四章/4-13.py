from django.shortcuts import render,HttpResponse
import json
import re
import datetime
import random
from demo4.settings import APIKEY
#引入用户表和验证码表
from .models import Code,UserProfile
#引入对接云片网模块
from utils.yunpian import YunPian
#引入drf功能模块
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
class SendCodeView(APIView):
    """
    获取手机验证码
    """
    def get(self,request):
        phone=request.GET.get('phone')
        if phone:
            #验证是否为有效手机号
            mobile_pat = re.compile('^(13\d|14[5|7]|15\d|166|17\d|18\d)\d{8}$')
            res = re.search(mobile_pat, phone)
            if res:
                #如果手机号合法，查看手机号是否被注册过
                had_register=UserProfile.objects.filter(phone=phone)
                if had_register:
                    msg = '手机号已被注册！'
                    result = {"status": "402", "data": {'msg': msg}}
                    return HttpResponse(json.dumps(result, ensure_ascii=False),
                                        content_type="application/json,charset=utf-8")
                else:
                    #检测是否发送过，如果没发送过则发送验证码，如果发送过则另做处理
                    had_send=Code.objects.filter(phone=phone).last()
                    if had_send:
                        #如果这个号码发送过验证码，查看距离上次发送时间间隔有没有达到一分钟
                        if had_send.add_time.replace(tzinfo=None)>
(datetime.datetime.now()-datetime.timedelta(minutes=1)):
                            msg = '距离上次发送验证码不足1分钟！'
                            result = {"status": "403", "data": {'msg': msg}}
                            return HttpResponse(json.dumps(result,ensure_ascii=False),                                             content_type="application/json,charset=utf-8")
                        else:
                            # 发送验证码
                            code = Code()
                            code.phone = phone
                            # 生成验证码
                            c = random.randint(1000, 9999)
                            code.code = str(c)
                            # 设定验证码的过期时间为20分钟以后
                            code.end_time = 
datetime.datetime.now() + datetime.timedelta(minutes=20)
                            code.save()
                            # 调用发送模块
                            code = Code.objects.filter(phone=phone).last().code
                            yunpian = YunPian(APIKEY)
                            sms_status = yunpian.send_sms(code=code, mobile=phone)
                            msg = sms_status
                            return HttpResponse(msg)
                    else:
                        #发送验证码
                        code = Code()
                        code.phone = phone
                        #生成验证码
                        c = random.randint(1000, 9999)
                        code.code = str(c)
                        #设定验证码的过期时间为20分钟以后
                        code.end_time=datetime.datetime.now()+datetime.timedelta(minutes=20)
                        code.save()
                        #调用发送模块
                        code = Code.objects.filter(phone=phone).last().code
                        yunpian = YunPian(APIKEY)
                        sms_status = yunpian.send_sms(code=code, mobile=phone)
                        msg = sms_status
                        # print(msg)
                        return HttpResponse(msg)
            else:
                msg = '手机号不合法！'
                result = {"status": "403", "data": {'msg': msg}}
                return HttpResponse(json.dumps(result, ensure_ascii=False),
                                    content_type="application/json,charset=utf-8")
        else:
            msg = '手机号为空！'
            result = {"status": "404", "data": {'msg': msg}}
            return HttpResponse(json.dumps(result, ensure_ascii=False),
                                content_type="application/json,charset=utf-8")
