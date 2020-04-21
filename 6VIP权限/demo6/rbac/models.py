from django.db import models
# Create your models here.
class Permission(models.Model):
    """
    权限表
    """
    url=models.CharField(max_length=64)
    title=models.CharField(max_length=10)
    class Meta:
        verbose_name='权限表'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.title
class Role(models.Model):
    """
    角色表
    """
    title=models.CharField(max_length=10)
    permission=models.ManyToManyField(Permission,null=True,blank=True)
    class Meta:
        verbose_name='角色表'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.title
class User(models.Model):
    """
    用户表
    """
    name = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)
    role = models.ManyToManyField(Role,null=True,blank=True)
    class Meta:
        verbose_name = '用户表'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name
