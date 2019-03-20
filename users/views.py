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

#精选品牌
def refined(request):
    return render(request,'main/refined.html')

#全球购
def go(request):
    return render(request,'main/go.html')