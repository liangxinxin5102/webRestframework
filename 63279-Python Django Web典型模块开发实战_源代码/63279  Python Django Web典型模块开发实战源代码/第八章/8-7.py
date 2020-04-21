class IndexView(APIView):
    """
    演示视图
    """
    def get(self,request):
        j=0
        for i in request.META:
            print(i,":",request.META[i])
            j+=1
        print("共",j,"条信息")
        return render(request,'index.html')
