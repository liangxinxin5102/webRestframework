from django.db import models
# Create your models here.
class Books(models.Model):
    """
    图书表
    """
    title=models.CharField(max_length=64,verbose_name='书名')
    pv=models.IntegerField(default=0,verbose_name='浏览量')
    class Meta:
        verbose_name='图书表'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.title
