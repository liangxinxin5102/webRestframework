from utils import email_send
class SendActiveCodeView(APIView):
    """
    发送激活链接类
    """
    def get(self,request):
        email=request.GET.get('email')
        if email:
            email_send.send_register_email(email)
            msg = '激活链接已发送都您的邮箱，请前往邮箱完成激活！'
            result = {"status": "200", "data": {'msg': msg}}
            return HttpResponse(json.dumps(result, ensure_ascii=False),
                                content_type="application/json,charset=utf-8")
        else:
            msg = '未收到邮箱！'
            result = {"status": "404", "data": {'msg': msg}}
            return HttpResponse(json.dumps(result, ensure_ascii=False),
                                content_type="application/json,charset=utf-8")
from .models import EmailVerifyRecord
class ActiveView(APIView):
    """
    激活认证用户类
    """
    def get(self,request,code):
        item=EmailVerifyRecord.objects.filter(code=code).last()
        if item:
            email=item.email
            user=UserProfile.objects.filter(email=email).first()
            user.is_auther=True
            user.save()
            msg='已认证为开发者，可以创建应用啦。'
            result = {"status": "200", "data": {'msg': msg}}
            return HttpResponse(json.dumps(result, ensure_ascii=False),
                                content_type="application/json,charset=utf-8")
        else:
            msg = '认证失败'
            result = {"status": "403", "data": {'msg': msg}}
            return HttpResponse(json.dumps(result, ensure_ascii=False),
                                content_type="application/json,charset=utf-8")
