from django.shortcuts import render
from CSHOP.md5 import encryption
from .models import User,Car,Address,Collection
from goods.models import GoodsInfo,Detail
from django.http import HttpResponse,HttpResponseRedirect,Http404,JsonResponse
from django.shortcuts import reverse
from .common import check_user,page
import json
import time
from seller.models import Orders,Order_info
from PIL import Image,ImageDraw,ImageFont
from django.core.paginator import  Paginator
from django.utils import timezone
# from alipay.aop.api.AlipayClientConfig import AlipayClientConfig
# from alipay.aop.api.DefaultAlipayClient import DefaultAlipayClient
# from alipay.aop.api.domain.AlipayTradePagePayModel import AlipayTradePagePayModel
# from alipay.aop.api.request.AlipayTradePagePayRequest import AlipayTradePagePayRequest

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
	list2=[]
	for i in goods_list:
		list.append(i.goods_id)
	other_list=Detail.objects.filter(id__in=list)
	for j in other_list:
		list1.append(j.name_id)
	other_list = GoodsInfo.objects.filter(id__in=list1)
	for k in other_list:
		list2.append(k.type_id)
	other_list = GoodsInfo.objects.filter(type_id__in=list2).exclude(id__in=list1)
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
		goods = Detail.objects.filter(name=goods_id)
		count=1
	else:
		goods_id=request.POST.get('size')
		count=request.POST.get('count')
		goods = Detail.objects.filter(id=goods_id, num__gte=count, goods_count__gte=count)
	if goods.exists():
		goods_id=goods[0].id
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
	user=request.session.get('id')
	goods_list=Car.objects.filter(user_id=user)
	address_list = Address.objects.filter(user_id=user)
	return render(request, 'user/car_path.html',{'address_list':address_list,'goods_list':goods_list})

@check_user
def truesubmit(request):
	user_id=request.session.get('id')
	address_id=request.POST.get('address')
	goods_list=Car.objects.filter(user_id=user_id)
	money=0
	seller=0
	if not goods_list.exists():
		return HttpResponse('您尚未选择商品。')
	for goods in goods_list:
		g=Detail.objects.get(id=goods.goods_id)
		money += g.goods_xprice * goods.count
		seller=GoodsInfo.objects.get(id=g.name_id).seller_id
		if g.num < goods.count:
			return HttpResponse('商品数量超过了库存，请重新选择。')

	address=Address.objects.filter(id=address_id,user_id=user_id)
	if not address.exists():
		raise Http404
	t = str(time.time()).split('.')
	orders = t[0] + t[1]
	address=address[0]
	o = Orders(order=orders, money=money, address=address.address,contacts=address.name,phone=address.phone,seller_id=seller,users_id=user_id)
	o.save()
	for goods in goods_list:
		g=Detail.objects.get(id=goods.goods_id)
		order=Order_info(number=goods.count,price=g.goods_xprice,goods_id=g.id,order_id=o.id)
		order.save()
		Detail.objects.filter(id=goods.goods_id).update(goods_count=g.goods_count-goods.count)
	goods_list.delete()
	return render(request,'user/truesubmit.html',{'orders':orders,'money':money})

# @check_user
def pay(request):
	order=request.POST.get('orders')
	user=request.session.get('id')
	o=Orders.objects.filter(order=order,users_id=user)
	if not o.exists():
		return HttpResponse('订单不存在。')
	# alipay_client_config = AlipayClientConfig()
	# alipay_client_config.server_url = 'https://openapi.alipaydev.com/gateway.do'
	# alipay_client_config.app_id = '2016092100561600'
	# alipay_client_config.app_private_key = 'MIIEpQIBAAKCAQEAxr2mbz2s8RigfJPxqYFht3hjtbEY9k/7C5BNvATGJRXSpI+9XmSCHG58OnYoZvYLgQoSLKRrE/z7ZeDL8gCVRuLWmEUHRYGEeBQ3IraaHqfHewP39yyoZ3M0Z9gIoK+yRIsgMcK4vdYwQGaw+MRypIEmqIC+AUeWOStYVDzK/TtcJPq8NZN+Gc2hzm94NE4F1fE+OFXVDPmoKJyljRsD2NYRz2iV6nuvRZ4inU31lpy6wNWwgqAZi6tIKMr1ElOFWH59ReCtkTyY0N2u4Z2TopiZgpCnZ3tQAoSEOslyefIH4w/I/dm2zxH3FF7bRuEp5jkueem5gfzmarGRClNp0wIDAQABAoIBABTfaDJ4tMghgQF0fEYEK6IcR8SWU/vSjJg7UJ61laXhc90Kp6XZQnz/8ZYmQLoHj0+/IgeEQSa5RCIACQtimkr2mfkmDsxy/Nmrrdq8eNVNY7r8wLc5/nnW9KMPYmCV81AVmI0BWWu+qhSpdF68Kxox4kCCPPJfdVyNu9olBGCyAtPKp2J/+lD/qCG9uxo7ltT5L4nsoR9gciLqce4B4VImHroUatDcOrDeMniRhNHkNa2YRkV4ddncAHtexAjA8yesTO1bO1D/TyLOHRnNElTBSDJbJaVzifgHM0OmcJUhgdbjJhGEUh+/atMjHLmMiZxEwoUsn4Ctcb8/NT541CECgYEA8Ao8+LIYzydlmaV4ns7GmclkfDXp3ZzVUeoQLCPGQtVeSZjiwIeB4G0bcO3d4JA0c1g5dfYJUA7YhOaOcQzMkkUnJu7oMBX2STYohX2012AdZPUz1/UWnckt5zvZoRYK0KjVQ06zLo2gWuk+dr+KVYQB1XRh777QxLhXK19V8LECgYEA0/RzoZ/+KvMTrFDEFiJep/I3avk6kohx8JUJyJQlus0cxnUdBv3rp3RkElJYCnvvtwhILWRuMovRTKxgUU7fXGIZY3HH7Zw0V3wpsOzPefNsVHCsg9kmpHqIEbabdJKAtnNIginMgEs0l5K2LKPbRK1CETRG3GwRcsoCdFV7A8MCgYEAyWB9eFLJd3jgxr7Ia8qjWL9ZOs9sLMx3Nip8eNtmaAli+bF2gfjs36AJRnt4Cf5Q0newdSL8+xoJUa2u0G7hbNDxILuLNVQnc5Io+pzUS1/KKTmAzetClwsBJJ3UXU0Fs7oAeGAc+LA+WCaXjb3xSv7dHvttclmOAYt5LdzkV3ECgYEAqkr6aH4yaPGZ+dV+ZkZBBPDAA8uwerDz0pb8IFKfKcHIf87yfn6eypDiIjJUmD/Rbp5R116chzH8/Hx2en1DSmdq/JIbTtY026Ffoc3yOIoSnJlWkixzNq1YC9tKdVOL5IslU6cfrmg+HhX7FkykTD5kGYyF7m1Ja4/QfwV6658CgYEAq/YNAIzrLkQxQeyS26bbCf7+FT6jLGmKgxyReODIOPKk7S+vaZWbyHX14AW9cDBeOfsiIQobfkIHMRJtVqe5TC49lHh08zAX610SvXSzIkpeTIMfUVKwhr0xfOqCMSEHKNG6mGbTie0AvhGCHYl2ptAWZot9ugNcgwdTu43Nyag='
	# alipay_client_config.alipay_public_key = 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA8OsmAJsaykPLzLIN//XnymU4s13kPE95EyOvZFq8TMPKJtsQ/f7eQB72wYAi3NarGT7RwebfJoAyeaM0KJsYNFqAodVHwpPRSemj8mwBtzEGGSyOT4Ilbv4KOz+HAsOkaLuQQ2ZGD1m7CCrgZCtxJDVqbd4xigSgMwrTFZYywoT0Sswv0oPV2TMl1tg+F7VUuvQpEvIn6qCQfzXa15eX9/P8OknvP9NSl3jOvDcpMliC2KvbfkNF9Qx9FEgtRlfnZdDItgmUj34VmBph+LUrAyV3lZjLpbFMhKlTBUeAbH72JPUKifXTXKsmbAl0n6cPaJQgb3zd+cfW7equoMhIEQIDAQAB'
	# client = DefaultAlipayClient(alipay_client_config=alipay_client_config)

	o=o[0]
	order_list=Order_info.objects.filter(order_id=o.id)
	name=''
	for i in order_list:
		name = name+' '+Detail.objects.get(id=i.goods_id).name.goods_name

	# model = AlipayTradePagePayModel()
	#
	# model.out_trade_no = o.order
	# model.total_amount = str(o.money)
	# model.subject = "快乐购-" + name
	# model.body = name
	# model.product_code = "FAST_INSTANT_TRADE_PAY"
	# request = AlipayTradePagePayRequest(biz_model=model)
	# request.return_url = 'http://39.105.195.67:80/users/return_url'
	# response = client.page_execute(request, http_method="GET")
	# return HttpResponseRedirect(response)
	return HttpResponse("1111")

@check_user
def return_url(request):
	order = request.GET.get('out_trade_no')
	result = Orders.objects.filter(order=order).update(pay_status=1,pay_time=timezone.datetime.now())
	return HttpResponseRedirect('/')

@check_user
#订单
def usercenter(request):
	user_id=request.session.get('id')
	order_list=Orders.objects.filter(users_id=user_id)

	list=[]
	if not order_list.exists():
		return render(request,'user/usercenter.html',{'order_list':order_list})
	for order in order_list:
		list.append(order.id)
	order_info_list=Order_info.objects.filter(order_id__in=list)
	return page(request, order_list, 5, 'user/usercenter.html',kwargs=order_info_list)
	# return render(request,'user/usercenter.html',{'order_info_list':order_info_list,
	# 											  'order_list': order_list})


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


@check_user
def userindex(request):
	return render(request,'user/userindex.html')

@check_user
def receive_goods(request,id):
	user=request.session.get('id')
	print(id)
	print(user)
	order=Orders.objects.filter(users_id=user,id=id,pay_status=1,send_status=1).update(receive_status=1, receive_time=timezone.datetime.now())
	if order:
		return HttpResponseRedirect(reverse('users:usercenter'))
	else:
		return HttpResponse('订单选择有误。')