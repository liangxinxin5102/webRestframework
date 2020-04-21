class EmailVerifyRecord(models.Model):
    """
    邮箱激活码
    """
    code = models.CharField(max_length=20, verbose_name='激活码')
    email=models.EmailField(max_length=50,verbose_name='邮箱')
    send_time=models.DateTimeField(verbose_name='发送时间',default=datetime.now)
    class Meta:
        verbose_name='邮箱验证码'
        verbose_name_plural=verbose_name
    def __str__(self):
        return '{0}({1})'.format(self.code,self.email)
