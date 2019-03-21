from django.shortcuts import render
from CSHOP.md5 import encryption
from .models import User
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

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
        #存入数据库
        userObj=User()
        userObj.username=username
        userObj.password=md5_pwd
        userObj.save()
        return HttpResponseRedirect('/users/login')
    return render(request,'user/register.html')


def car(request):
    return render(request,'user/car.html')

def car_path(request):
    return render(request, 'user/car_path.html')

def truesubmit(request):
    return render(request,'user/truesubmit.html')

def usercenter(request):
    return render(request,'user/usercenter.html')

