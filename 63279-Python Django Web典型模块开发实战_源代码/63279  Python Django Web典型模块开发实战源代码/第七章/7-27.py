from rest_framework import serializers
#引入用户表、文章表、评论表、关键词表
from .models import UserProfile,Article,Comment,Card
class UserProfileSerializer(serializers.ModelSerializer):
	“””
	序列化用户表
	“””
    class Meta:
        model=UserProfile
        fields = "__all__"
class CommentSerializer(serializers.ModelSerializer):
	“””
	序列化评论表
	“””
    class Meta:
        model=Comment
        fields = "__all__"
class ArticleSerializer(serializers.ModelSerializer):
	“””
	序列化文章表
	“””
    class Meta:
        model=Article
        fields = "__all__"
class CardSerializer(serializers.ModelSerializer):
	“””
	序列化违禁词表
	“””
    class Meta:
        model=Card
        fields = "__all__"
