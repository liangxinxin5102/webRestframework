from rest_framework import serializers
#引入文章表和用户表
from .models import UserProfile,Article
class UserProfileSerializer(serializers.ModelSerializer):
	“””
	序列化用户表
	“””
    class Meta:
        model=UserProfile
        fields = "__all__"
class ArticleSerializer(serializers.ModelSerializer):
	“””
	序列化文章类
	“””
    class Meta:
        model=Article
        fields = "__all__"
