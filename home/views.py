from django.shortcuts import render
from goods.models import BigType,GoodsType,GoodsInfo,Detail
# Create your views here.

def index(request):
    big_type_list=BigType.objects.all()
    type_list=GoodsType.objects.all()
    goods_list=GoodsInfo.objects.all()
    return render(request, 'goods/index.html',{'big_type_list':big_type_list,
                                               'type_list':type_list,
                                               'goods_list':goods_list})