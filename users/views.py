from django.shortcuts import render
from CSHOP.md5 import encryption
from .models import User,Car,Adress
from goods.models import GoodsInfo,Detail
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.shortcuts import reverse
from .common import check_user

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
    return render(request,'user/car.html',{'goods_list':goods_list})

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
    address_list=Adress.objects.filter(user_id=id)
    return render(request,'user/newPath.html',{'address_list':address_list})

@check_user
def  del_address(request):
    id = request.session.get('id')

@check_user
def collect(request):
    return render(request,'user/collect.html')

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
        a=Adress.objects.filter(name=name,address=address,phone=phone,user_id=id)
        if not a.exists():
            a=Adress(name=name,address=address,phone=phone,user_id=id)
            a.save()
        return HttpResponseRedirect(reverse('users:add_path'))
    except:
        return HttpResponse('信息提交有误。')

#退货中心
@check_user
def userrefund(request):
    return render(request,'user/userrefund.html')

def test(request):
    return render(request,'user/test.html')