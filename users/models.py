from django.db import models
from goods.models import Detail
from django.contrib.auth.models import User as Auth_User

class User(models.Model):
    class Meta:
        verbose_name = '买家信息'
        verbose_name_plural = '买家信息'
    username=models.CharField('用户名',max_length=100)
    password=models.CharField('密码',max_length=32)
    sex=models.BooleanField(default=1)
    birthday=models.DateField(null=True)
    is_activate = models.BooleanField('能否登录',default=1)
    def __str__(self):
        return  self.username

class Car(models.Model):
    class Meta:
        verbose_name = '购物车'
        verbose_name_plural = '购物车'
    count=models.IntegerField(verbose_name='数量')
    user=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='买家')
    goods=models.ForeignKey(Detail,on_delete=models.CASCADE,verbose_name='商品')