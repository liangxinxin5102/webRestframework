from django.db import models
# Create your models here.
class Goods(models.Model):
    """
    商品表
    """
    title=models.CharField(max_length=64,verbose_name='商品名')
    pv=models.IntegerField(default=0,verbose_name='浏览量')
    class Meta:
        verbose_name='商品表'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.title
