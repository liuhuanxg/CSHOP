from django.db import models
from django.contrib.auth.models import User

#主类
class BigType(models.Model):
    class Meta:
        verbose_name = '商品大类'
        verbose_name_plural = '商品大类'
    name = models.CharField(max_length=50, verbose_name='大类名称')
    create_time=models.DateField('创建时间',auto_now_add=True)
    def __str__(self):
        return self.name
# 商品分类表
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
    goods_oprice= models.FloatField(verbose_name='商品原价')
    goods_xprice = models.FloatField(verbose_name='商品现价')
    goods_count=models.IntegerField(verbose_name='库存',default=0)
    goods_method=models.CharField(verbose_name='存储方法',max_length=100)
    goods_info=models.TextField(verbose_name='商品介绍')
    goods_pic=models.ImageField(verbose_name='商品缩略图',upload_to='media/uploads')
    goods_address=models.CharField(verbose_name='配送地址',max_length=50)
    goods_content=models.TextField(verbose_name='商品内容')
    type=models.ForeignKey(GoodsType,null=True,on_delete=models.DO_NOTHING,verbose_name=('类别'))
    seller=models.ForeignKey(User,default=1,on_delete=models.DO_NOTHING,verbose_name=('卖家'))
    def __str__(self):
        return self.goods_content