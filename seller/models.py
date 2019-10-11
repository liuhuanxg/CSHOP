from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html

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
    def pay(self):
        if self.pay_status == 0:
            color_code = 'blue'
            return format_html(
                '<span style="color:{};">{}</span>',color_code,'尚未支付',
            )
        else:
            color_code='green'
            return format_html(
                '<span style="color:{};">{}</span>',color_code,'已经支付',
            )
    pay.short_description = u'支付状态'

    def send(self):
        if self.send_status == 0:
            color_code = 'blue'
            return format_html(
                '<span style="color:{};">{}</span>',color_code,'尚未发货',
            )
        else:
            color_code='green'
            return format_html(
                '<span style="color:{};">{}</span>',color_code,'已经发货',
            )
    send.short_description = u'发货状态'
    def receive(self):
        if self.receive_status == 0:
            color_code = 'blue'
            return format_html(
                '<span style="color:{};">{}</span>',color_code,'尚未收货',
            )
        else:
            color_code='green'
            return format_html(
                '<span style="color:{};">{}</span>',color_code,'已经收货',
            )
    receive.short_description = u'发货状态'
    def comment(self):
        if self.comment_status == 0:
            color_code = 'blue'
            return format_html(
                '<span style="color:{};">{}</span>',color_code,'尚未评价',
            )
        else:
            color_code='green'
            return format_html(
                '<span style="color:{};">{}</span>',color_code,'已经评价',
            )
    comment.short_description = u'评价状态'


class Order_info(models.Model):
    class Meta:
        verbose_name='订单详情'
        verbose_name_plural='订单详情'
    goods = models.ForeignKey('goods.Detail', default=1,on_delete=models.DO_NOTHING,verbose_name='商品名称')
    number = models.IntegerField(default=1,verbose_name='商品数量')
    price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='价钱')
    order = models.ForeignKey('Orders', default=1, on_delete=models.CASCADE, verbose_name='编号')

#季度表
class Quarter(models.Model):
    class Meta:
        verbose_name = '季度营业额'
        verbose_name_plural = '季度营业额'
    name = models.CharField(verbose_name='季度名称',max_length=10)
    def detail(self):
        color_code='green'
        return format_html(
            '<a style="color:{};" href="../../../../seller/show_quarter/{}">{}</a>',color_code,self.id,'当季营业额',
        )
    detail.short_description = u'当季营业额'

    def all_quarter(self):
        color_code = 'green'
        return format_html(
            '<a style="color:{};" href="../../../../seller/show_quarter/all">{}</a>', color_code, '所有季度营业额',
        )

    all_quarter.short_description = u'所有季度营业额'

#月份表
class Month(models.Model):
    class Meta:
        verbose_name = '月份'
        verbose_name_plural = '月份'
    name = models.CharField(verbose_name='月份名称',max_length=40)
    quarter = models.ForeignKey('Quarter',default=1,on_delete=models.DO_NOTHING,verbose_name='季度')
    count = models.IntegerField(verbose_name='数量')

#省份表
class Province(models.Model):
    class Meta:
        verbose_name = '各省营业额'
        verbose_name_plural = '各省营业额'
    name = models.CharField(verbose_name='省份名称',max_length=40)
    def detail(self):
        color_code = 'green'
        return format_html(
            '<a style="color:{};" href="../../../../seller/city_volume/{}">{}</a>', color_code, self.id,'查看营业额',
        )
    detail.short_description = u'营业额'

    def all_quarter(self):
        color_code = 'green'
        return format_html(
            '<a style="color:{};" href="">{}</a>', color_code, '所有省份营业额',
        )
    all_quarter.short_description = u'所有省份营业额'

    def __str__(self):
        return self.name

class City(models.Model):
    class Meta:
        verbose_name = '城市'
        verbose_name_plural = '城市'
    name = models.CharField(verbose_name='城市名称',max_length=40)
    province = models.ForeignKey('Province',default=1,on_delete=models.DO_NOTHING,verbose_name='省份')
    money = models.IntegerField(verbose_name='金额')

class Jidu(models.Model):
    class Meta:
        verbose_name = "季度"
        verbose_name_plural = "季度"
    name = models.CharField(max_length=30,verbose_name="季度名称")

    def detail(self):
        color_code = 'green'
        return format_html(
            '<a style="color:{};" href="../../../../seller/show_order/{}">{}</a>', color_code, self.id, '查看营业额',
        )

    detail.short_description = u'营业额'

class Month1(models.Model):
    class Meta:
        verbose_name = "月份"
        verbose_name_plural = "月份"
    name = models.CharField(max_length=20)
    j_id = models.ForeignKey("Jidu",verbose_name="季度",on_delete=models.DO_NOTHING)

class Order(models.Model):
    class Meta:
        verbose_name = "订单"
        verbose_name_plural = "订单"
    money = models.CharField(max_length=20,verbose_name="金额")
    m_id = models.ForeignKey('Month1',verbose_name="月份",on_delete=models.DO_NOTHING)

