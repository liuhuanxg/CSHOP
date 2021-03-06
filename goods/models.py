from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html
# from seller.models import Orders

class BigType(models.Model):
    class Meta:
        verbose_name = '商品大类'
        verbose_name_plural = '商品大类'
    name = models.CharField(max_length=50, verbose_name='大类名称')
    create_time=models.DateField('创建时间',auto_now_add=True)
    def __str__(self):
        return self.name

class GoodsType(models.Model):
    class Meta:
        verbose_name='商品小类'
        verbose_name_plural='商品小类'
    type_name=models.CharField(max_length=50,verbose_name='小类名称')
    type=models.ForeignKey(BigType,verbose_name='关联大类',default=1,on_delete=models.DO_NOTHING)
    create_time = models.DateField('创建时间', auto_now_add=True)
    def __str__(self):
        return self.type_name


class GoodsInfo(models.Model):
    class Meta:
        verbose_name = '商品'
        verbose_name_plural = '商品'
    goods_name=models.CharField(verbose_name='商品名称',max_length=200)
    goods_method=models.CharField(verbose_name='注意事项',max_length=100)
    goods_info=models.TextField(verbose_name='商品介绍')
    goods_pic=models.ImageField(verbose_name='商品缩略图',upload_to='media/uploads')
    goods_address=models.CharField(verbose_name='配送地址',max_length=50)
    goods_content=models.TextField(verbose_name='商品内容')
    oprice = models.FloatField(verbose_name='商品原价',default='0')
    xprice = models.FloatField(verbose_name='商品现价',default='0')
    type=models.ForeignKey(GoodsType,null=True,on_delete=models.DO_NOTHING,verbose_name=('类别'))
    seller=models.ForeignKey(User,default=1,on_delete=models.DO_NOTHING,verbose_name=('卖家'))
    def evaluation(self):
        color_code = 'green'
        return format_html(
            '<a style="color:{};" href="/seller/show_evaluation/{}">{}</a>', color_code,self.id,'查看评价',
        )
    evaluation.short_description = u'支付状态'
    def __str__(self):
        return self.goods_name

class Detail(models.Model):
    class Meta:
        verbose_name = '商品细节'
        verbose_name_plural = '商品细节'
    name=models.ForeignKey(GoodsInfo,default=1,on_delete=models.DO_NOTHING,verbose_name='名称')
    size=models.CharField(verbose_name='大小',max_length=500)
    color=models.CharField(verbose_name='颜色',max_length=500)
    goods_oprice = models.FloatField(verbose_name='商品原价')
    goods_xprice = models.FloatField(verbose_name='商品现价')
    goods_count = models.IntegerField(verbose_name='库存', default=0)
    num=models.IntegerField(verbose_name='限购数量',default=3)
    def __str__(self):
        return GoodsInfo.objects.get(id=self.name_id).goods_name

#商品评价表
class Goods_evaluation(models.Model):
    class Meta:
        verbose_name = "商品评价"
        verbose_name_plural = "商品评价"
    order = models.ForeignKey("seller.Orders",default=1,on_delete=models.CASCADE,verbose_name="订单ID")
    goods = models.ForeignKey("GoodsInfo",default=1,on_delete=models.CASCADE,verbose_name="商品ID")
    user = models.ForeignKey("users.User",default=1,on_delete=models.CASCADE,verbose_name="用户ID")
    content = models.CharField(max_length=500,verbose_name="评价内容")
    goods_score = models.IntegerField(verbose_name="商品评分")
    service_score = models.IntegerField(verbose_name="服务评分")

class test(models.Model):
    name = models.CharField(max_length=100)