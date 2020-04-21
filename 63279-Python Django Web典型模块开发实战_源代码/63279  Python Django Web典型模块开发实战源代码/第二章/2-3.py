from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class UserProfile(AbstractUser):
    """
    用户
    """
    APIkey=models.CharField(max_length=30,verbose_name='APIkey',default='abcdefghigklmn')
    money=models.IntegerField(default=10,verbose_name='余额')
    class Meta:
        verbose_name='用户'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.username
