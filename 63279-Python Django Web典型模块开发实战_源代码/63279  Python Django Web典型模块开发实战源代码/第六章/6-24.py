from django.db import models
from datetime import datetime
# Create your models here.
class UserInfo(models.Model):
    """
    用户表
    """
    user_type_chioces=(
        (1,"普通用户"),
        (2,"VIP"),
        (3,"SVIP"),
    )
    user_type=models.IntegerField(choices=user_type_chioces)
    username=models.CharField(max_length=32)
    password=models.CharField(max_length=64)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    class Meta:
        verbose_name='用户表'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.username
class UserToken(models.Model):
    """
    token表
    """
    user=models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    token=models.CharField(max_length=64)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    class Meta:
        verbose_name='token表'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.user.username
class CommonVideo(models.Model):
    """
    普通视频
    """
    title=models.CharField(max_length=32)
    url=models.CharField(max_length=200,verbose_name='资源地址')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    class Meta:
        verbose_name='普通视频表'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.title
class VIPVideo(models.Model):
    """
    会员视频
    """
    title=models.CharField(max_length=32)
    url=models.CharField(max_length=200,verbose_name='资源地址')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    class Meta:
        verbose_name='会员视频表'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.title
class SVIPVideo(models.Model):
    """
    超级会员视频
    """
    title=models.CharField(max_length=32)
    url=models.CharField(max_length=200,verbose_name='资源地址')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    class Meta:
        verbose_name='超级会员视频表'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.title
