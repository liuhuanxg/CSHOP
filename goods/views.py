from django.shortcuts import render

# Create your views here.
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
    return render(request, 'goods/list.html')

def goods_detail(request,id):
    return render(request,'goods/goods_detail.html')