#……
from .utils.auth import VIP,SVIP
# Create your views here.
#……
class VIPVideoView(APIView):
    """
    vip可访问的资源
    """
    renderer_classes = [JSONRenderer]  # 渲染器
    permission_classes = [VIP]
    def get(self,request):
        video_list = VIPVideo.objects.all()
        re = VIPVideoSerializer(video_list, many=True)
        return Response(re.data)
class SVIPVideoView(APIView):
    """
    vip可访问的资源
    """
    renderer_classes = [JSONRenderer]  # 渲染器
    permission_classes = [SVIP]
    def get(self,request):
        video_list = SVIPVideo.objects.all()
        re = SVIPVideoSerializer(video_list, many=True)
        return Response(re.data)
