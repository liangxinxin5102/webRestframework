from rest_framework import serializers
#引入数据表类
from .models import CommonVideo,VIPVideo,SVIPVideo
#将三个数据表类进行序列化 
class CommonVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model=CommonVideo
        fields = "__all__"
class VIPVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model=VIPVideo
        fields = "__all__"
class SVIPVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model=SVIPVideo
        fields = "__all__"
