from django.db import models

# Create your models here.

#用户信息表
class User(models.Model):
    class Meta:
        verbose_name = '买家信息'
        verbose_name_plural = '买家信息'
    username=models.CharField('用户名',max_length=100)
    password=models.CharField('密码',max_length=32)
    is_activate = models.BooleanField('能否登录',default=1)
    def __str__(self):
        return  self.username
