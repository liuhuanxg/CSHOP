from django.shortcuts import render,HttpResponse
from django.http import HttpResponseRedirect,Http404
from  .models import BigType,GoodsType,GoodsInfo,Detail
from goods import models
from seller.models import Orders
from users.models import User

#精选品牌
def refined(request):
    return render(request, 'goods/refined.html')

#全球购
def global_go(request):
    return render(request, 'goods/global_go.html')

#品牌馆
def brand(request):
    return render(request, 'goods/brand.html')

def list(request):
    s_id=request.GET.get('s_id')
    goods_list=GoodsInfo.objects.filter(type_id=s_id)
    return render(request, 'goods/list.html',{'goods_list':goods_list})

def goods_detail(request,id):
    goods=GoodsInfo.objects.filter(id=id)
    if goods.exists():
        goods=goods[0]
        detail_list=Detail.objects.filter(name_id=id)
        return render(request,'goods/goods_detail.html',{'goods':goods,'detail_list':detail_list})
    else:
        raise Http404

import random
def add_evaluation(request):
    users = [1,2]       #用户
    goods = [3]     #商品
    score = [1] #评分
    orders = [13,14,15,16,17,19,20,21,22,23] #订单
    contents = ["质量很好。","很耐穿。","很轻便。","价格实惠。","价格公道。","质量好，价格实惠"]
    for z in range(10):
        for i in orders:
            goods_score = random.choice(score)
            service_score = random.choice(score)
            # order = random.choice(orders)
            user = random.choice(users)
            good = random.choice(goods)
            content=random.choice(contents)
            print(goods_score,service_score,i,user,good,content)
            o = Orders.objects.get(id=i)
            g = GoodsInfo.objects.get(id=good)
            u = User.objects.get(id=user)
            g = models.Goods_evaluation(goods_score=goods_score,service_score=service_score,order=o,user=u,goods=g,content=content)
            g.save()
            print(g)
    return HttpResponse("11111")

