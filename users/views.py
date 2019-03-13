from django.shortcuts import render
from CSHOP.md5 import encryption
from .models import User_message
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        md5_pwd = encryption(pwd)

    return render(request, 'user/login.html')


def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pwd=request.POST.get('password')
        md5_pwd=encryption(pwd)
        #存入数据库
        userObj=User_message()
        userObj.username=username
        userObj.password=md5_pwd
        userObj.save()
        return HttpResponseRedirect('/users/login')
    return render(request,'user/register.html')