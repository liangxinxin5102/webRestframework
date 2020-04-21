from .utils.alipay import AliPay
from demo10.settings import private_key_path,ali_pub_key_path
class ShopView(LoginRequiredMixin,View):
    """
    购物视图
    """
    def get(self,request):
        return render(request,'shop.html',{'user':request.user})
    def post(self,request):
        alipay = AliPay(
            appid="2016091400509946",
            app_notify_url="http://127.0.0.1:8000/shop/",
            app_private_key_path=private_key_path,
            alipay_public_key_path=ali_pub_key_path,  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
            debug=True,  # 默认False,
            return_url="http://127.0.0.1:8000/shop/"
        )
        url = alipay.direct_pay(
            #根据前端进来的数据，确定subject（商品名称），生成不重复的交易号out_trade_no,
            # 根据商品和数量算出总价total_amount
            subject="你的背包",
            out_trade_no="20190316sss1",
            total_amount=100,
            return_url="http://127.0.0.1:8000/alipay/return/"
        )
        re_url = "https://openapi.alipaydev.com/gateway.do?{data}".format(data=url)
        print(re_url)
        return redirect(re_url)
