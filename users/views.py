from django.shortcuts import render
from CSHOP.md5 import encryption
from .models import User,Car,Address,Collection
from goods.models import GoodsInfo,Detail
from django.http import HttpResponse,HttpResponseRedirect,Http404,JsonResponse
from django.shortcuts import reverse
from .common import check_user
import json

def login(request):
    if request.method == 'POST':
        pwd = request.POST.get('password')
        username = request.POST.get('username')
        md5_pwd = encryption(pwd)
        print(username,md5_pwd)
        u=User.objects.filter(username=username,password=md5_pwd)
        if u.exists():
            request.session['user']=username
            request.session['id']=u[0].id
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('账号或密码有误。')
    return render(request, 'user/login.html')

def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pwd=request.POST.get('password')
        md5_pwd=encryption(pwd)
        userObj=User()
        userObj.username=username
        userObj.password=md5_pwd
        userObj.save()
        return HttpResponseRedirect('/users/login')
    return render(request,'user/register.html')

@check_user
def logout(request):
    del request.session['user']
    return HttpResponseRedirect('/')

@check_user
def car(request):
    id=request.session.get('id')
    goods_list=Car.objects.filter(user_id=id)
    list=[]
    list1=[]
    for i in goods_list:
        list.append(i.goods_id)
    other_list=GoodsInfo.objects.filter(id__in=list)
    print('other_list:',other_list)
    for j in other_list:
        list1.append(j.type_id)
    print('list1:',list1)
    other_list = GoodsInfo.objects.filter(type_id__in=list1).exclude(id__in=list)
    print('other_list:',other_list)
    return render(request,'user/car.html',{'goods_list':goods_list,'other_list':other_list})

@check_user
def del_car(request,id):
    try:
        c=Car.objects.get(id=id)
        c.delete()
        return HttpResponseRedirect(reverse('users:car'))
    except:
        raise Http404
@check_user
def add_car(request):
    user=request.session.get('id')
    goods_id = request.GET.get('g_id')
    if goods_id:
        goods = Detail.objects.filter(id=goods_id)
        count=1
    else:
        goods_id=request.POST.get('size')
        count=request.POST.get('count')
        goods = Detail.objects.filter(id=goods_id, num__gte=count, goods_count__gte=count)
    if goods.exists():
        c = Car.objects.filter(user_id=user, goods_id=goods_id)
        if c.exists():
            c.update(count=count)
        else:
            c = Car(count=count, user_id=user, goods_id=goods_id)
            c.save()
        return HttpResponseRedirect(reverse('users:car'))
    else:
        return HttpResponse('商品数量有误。')

@check_user
def car_path(request):
    return render(request, 'user/car_path.html')

@check_user
def truesubmit(request):
    return render(request,'user/truesubmit.html')

@check_user
def usercenter(request):
    return render(request,'user/usercenter.html')

@check_user
def add_path(request):
    id=request.session.get('id')
    g_id=request.GET.get('g_id')
    address=False
    if g_id:
        address=Address.objects.filter(id=g_id)
        if address.exists:
            address=address[0]
    address_list=Address.objects.filter(user_id=id)
    return render(request,'user/newPath.html',{'address_list':address_list,'address':address})

@check_user
def modify_address(request,id):
    name = request.POST.get('name')
    address = request.POST.get('address')
    phone = request.POST.get('phone')
    a = Address.objects.filter(id=id)
    if  a.exists():
        a.update(name=name, address=address, phone=phone)
    return HttpResponseRedirect(reverse('users:add_path'))

@check_user
def  del_address(request,id):
    a=Address.objects.filter(id=id)
    if a.exists:
        a=a[0]
        a.delete()
    return HttpResponseRedirect(reverse('users:add_path'))

@check_user
def check_count(request):
    id=request.session.get('id')
    car_list=Car.objects.filter(user_id=id)
    count=car_list.count()
    result={}
    result['status']=1
    result['msg']=count
    return HttpResponse(json.dumps(result))


@check_user
def collect(request):
    id=request.session.get('id')
    g_id=request.GET.get('g_id')
    if g_id:
        c=Collection(goods_id=g_id,user_id=id)
        c.save()
    collect_list=Collection.objects.filter(user_id=id)
    return render(request,'user/collect.html',{'collect_list':collect_list})

@check_user
def del_collect(request,id):
    try:
        c=Collection.objects.get(id=id)
        c.delete()
        return HttpResponseRedirect(reverse('users:collect'))
    except:
        raise Http404
@check_user
def userindex(request):
    return render(request,'user/userindex.html')

#修改个人信息
@check_user
def message(request):
    id=request.session.get('id')
    user=User.objects.get(id=id)
    return render(request, 'user/message.html',{'user':user})

@check_user
def change_message(request):
    id = request.session.get('id')
    username = request.POST.get('username')
    sex=request.POST.get('sex')
    birthday=request.POST.get('birthday')
    u=User.objects.get(id=id)
    u.username=username
    u.sex=sex
    if not u.birthday:
        u.birthday=birthday
    u.save()
    return HttpResponseRedirect(reverse('users:message'))


@check_user
def add_adress(request):
    id=request.session.get('id')
    name=request.POST.get('name')
    address=request.POST.get('address')
    phone=request.POST.get('phone')
    try:
        a=Address.objects.filter(name=name,address=address,phone=phone,user_id=id)
        if not a.exists():
            a=Address(name=name,address=address,phone=phone,user_id=id)
            a.save()
        return HttpResponseRedirect(reverse('users:add_path'))
    except Exception as ex:
        print(ex)
        return HttpResponse('信息提交有误。')

#退货中心
@check_user
def userrefund(request):
    return render(request,'user/userrefund.html')

def test(request):
    return render(request,'user/test.html')