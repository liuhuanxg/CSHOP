from django.db import models
from django.contrib.auth.models import User

class Orders(models.Model):
    class Meta:
        verbose_name='订单总览'
        verbose_name_plural='订单总览'
    order = models.CharField('订单号',max_length=20, unique=True)
    money = models.DecimalField('总金额',max_digits=10,decimal_places=2,default='')  # 小数点后保留两位
    add_time = models.DateTimeField('订单创建时间',auto_now_add=True)
    address = models.CharField('收货地址',max_length=150,default='')
    contacts = models.CharField('收货人姓名',max_length=30,default='')
    phone = models.CharField('收货人电话',max_length=20,default='')
    pay_status = models.BooleanField('支付状态',default=0)
    pay_time = models.CharField('付款时间',default='',max_length=100)
    send_status = models.BooleanField('发货状态',default=0)
    send_time = models.CharField('发货时间',default='',max_length=100)
    receive_status = models.BooleanField('收货状态',default=0)
    receive_time = models.CharField('收货时间',default='',max_length=100)
    comment_status = models.BooleanField('评价状态',default=0)
    seller = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='卖家')
    users = models.ForeignKey('users.User',on_delete=models.CASCADE,verbose_name='买家')
    def __str__(self):
        return self.order

class Order_info(models.Model):
    class Meta:
        verbose_name='订单详情'
        verbose_name_plural='订单详情'
    goods = models.ForeignKey('goods.Detail', default=1,on_delete=models.DO_NOTHING,verbose_name='商品名称')
    number = models.IntegerField(default=1,verbose_name='商品数量')
    price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='价钱')
    order = models.ForeignKey('Orders', default=1, on_delete=models.CASCADE, verbose_name='编号')