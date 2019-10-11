from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from seller.models import Orders,Quarter,Month,City,Province,Order,Jidu,Month1
from goods.models import BigType,Goods_evaluation
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
# from rest_framework import
@login_required
def show_orders(request):
    return render(request,"seller/orders.html")

@login_required
def orders(request):
    o_list=Orders.objects.all()
    result = {}
    money = []
    for o in o_list:
        money.append(o.money)
    money.sort(key=lambda x:int(x))
    r={k:money.count(k) for k in money}
    if len(money)>0:
        result["flag"]=1   #1代表有数据
        result["money"]=list(r.keys())
        result["count"]=list(r.values())
    else:
        result["flag"] = 0   #0代表没有数据
    return JsonResponse(result)

@login_required
def zuobiaozhou(request):
    return render(request,"seller/zuobiaozhoukedu.html")

@login_required
def show_evaluation(request,id):
    return render(request, "seller/evaluation.html", {"goods_id":id})

#价格——销量柱状图
@login_required
def evaluation(request,id): #传入商品id
    e_list =  Goods_evaluation.objects.filter(goods=id)  #查找商品
    result = {}         #返回的结果
    data = []           #将数据结果存储在列表中
    list1 = [1,2,3,4,5]
    if e_list.exists():
        result['flag'] = 1
        for l in list1:
            dict1 = {}
            count = Goods_evaluation.objects.filter(goods_score=l).count()
            dict1['name'] = l
            dict1['value'] = count
            data.append(dict1)
        result['data']=data
    else:
        result['flag'] = 0
    return JsonResponse(result)

#各季度营业额
def show_quarter(request,id):
    q_id = request.GET.get('q_id',None)
    if q_id != None:
        result = {}
        if q_id != 'all':
            q_list = Quarter.objects.filter(id=q_id)
        else:
            q_list = Quarter.objects.all()
        if q_list.exists():
            month_data = []
            quarter_data=[]
            for q in q_list:
                q_re = {}
                q_re['name'] = q.name
                q_re['value'] = 0
                m_list = Month.objects.filter(quarter=q.id)
                for m in m_list:
                    if m.quarter_id == q.id:
                        q_re['value'] +=m.count
                    r = {}
                    r['name'] = m.name
                    r['value'] = m.count
                    month_data.append(r)
                quarter_data.append(q_re)
            result['flag']=1
            result['data']={"month_data":month_data,"quarter_data":quarter_data}
        else:
            result['flag'] = 0
            result['data'] = "暂无数据"
        return JsonResponse(result)
    return render(request,"seller/quarterly_volume.html",{"q_id":id})

#各省份营业额
def city_volume(request,id):
    c_id = request.GET.get("c_id",None)
    if c_id:
        p_list = Province.objects.filter(id=c_id)
        if p_list.exists():
            # p = p_list[0]
            result = {}
            data = {}
            # c_list = City.objects.filter(province_id=c_id)
            c_list = City.objects.all()  #所有城市信息
            all = 0  #总计
            name_list = ["charts","components"]
            for j in range(len(name_list)):
                data[name_list[j]] = {}
                for c in c_list:
                    if j+1 == c.province_id:
                        data[name_list[j]][c.name] = c.money
                    all += c.money
            data['all'] = all
            result['flag'] = 1
            result['data'] = data
            print(result)
            return JsonResponse(result)
    return render(request,"seller/city_volume.html",{"c_id":id})

import random
def add_order(request):
    month = Month1.objects.all()
    contents = [10000,20000,4000,5000,7000,8000,9000]
    for z in range(10):
        for i in month:
            content = random.choice(contents)
            g = Order(money=content,m_id_id=i.id)
            g.save()
    return HttpResponse("11111")

def show_order(request,id):
    return render(request,"seller/new/demo1.html",{"id":id})

def re_order(request):
    j_id = request.GET.get('j_id')
    j = Jidu.objects.get(id=j_id)
    m_list = Month1.objects.filter(j_id=j)
    result = {'flag':1,"data":{}}  #返回的数据
    month_list = [j.name]
    data2 = {}
    data3 = []
    sum_money = 0
    for m in m_list:
        o_list = Order.objects.filter(m_id_id=m.id)
        for o in o_list:
            sum_money += int(o.money)
        data3.append({"value":sum_money,"name":m.name})
        month_list.append(m.name)
    data2['value']=sum_money
    data2['name']=j.name
    result['data']['data2']=[data2]
    result['data']['data3']=data3
    result['data']['data1']=month_list
    print(result)
    return JsonResponse(result,safe=False)