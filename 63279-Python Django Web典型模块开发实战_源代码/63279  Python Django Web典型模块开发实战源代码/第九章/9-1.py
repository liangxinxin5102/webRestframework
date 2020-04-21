from django.db import models
from datetime import datetime
# Create your models here.
class Book(models.Model):
    """
    书籍
    """
    title=models.CharField(max_length=32,verbose_name='书名')
    author=models.CharField(max_length=10,verbose_name='作者名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    class Meta:
        verbose_name='书籍表'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.title
