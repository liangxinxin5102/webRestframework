from django.db import models
from datetime import datetime
class TuWen(models.Model):
    """
    图文表
    """
    image = models.ImageField(max_length=200, upload_to='images/',verbose_name='图片')
    title=models.CharField(max_length=200,blank=True,null=True,verbose_name='文本')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    class Meta:
        verbose_name = "图文信息"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.title