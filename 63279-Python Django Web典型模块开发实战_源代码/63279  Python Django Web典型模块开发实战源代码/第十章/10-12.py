class ShopView(LoginRequiredMixin,View):
    """
    π∫ŒÔ ”Õº
    """
    def get(self,request):
        return render(request,'shop.html',{'user':request.user})
    def post(self,request):
        return HttpResponse('200')
