class Code(models.Model):
    """
    验证码
    """
    phone=models.CharField(max_length=11,verbose_name='手机号')
    code=models.CharField(max_length=4,verbose_name='验证码')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    end_time = models.DateTimeField(default=datetime.now, verbose_name='过期时间')
    class Meta:
        verbose_name='验证码表'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.phone
