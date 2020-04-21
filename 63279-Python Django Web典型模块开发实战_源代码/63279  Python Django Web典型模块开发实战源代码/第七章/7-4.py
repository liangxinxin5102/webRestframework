from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
# Create your models here.
class UserProfile(AbstractUser):
    """
    用户表
    """
    user_type_chioces = (
        (1, "普通用户"),
        (2, "版主"),
        (3, "管理员"),
    )
    level = models.IntegerField(choices=user_type_chioces,default=1)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    class Meta:
        verbose_name='用户'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.username
class Article(models.Model):
    """
    文章表
    """
    title=models.CharField(max_length=30,verbose_name='标题')
    content=models.CharField(max_length=5000,verbose_name='文章内容')
    user=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    class Meta:
        verbose_name='文章'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.title
