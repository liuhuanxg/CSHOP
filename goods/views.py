from django.shortcuts import render
from django.http import HttpResponseRedirect,Http404
from  .models import BigType,GoodsType,GoodsInfo,Detail

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