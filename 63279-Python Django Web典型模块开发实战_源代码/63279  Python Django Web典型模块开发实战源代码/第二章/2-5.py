from datetime import datetime
from django.db import models
class Book(models.Model):
    """
    书籍信息
    """
    title=models.CharField(max_length=30,verbose_name='书名',default='')
    isbn=models.CharField(max_length=30,verbose_name='isbn',default='')
    author=models.CharField(max_length=20,verbose_name='作者',default='')
    publish=models.CharField(max_length=30,verbose_name='出版社',default='')
    rate=models.FloatField(default=0,verbose_name='豆瓣评分')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    class Meta:
        verbose_name='书籍信息'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.title
