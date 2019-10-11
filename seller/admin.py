from typing import List, Any
from django.utils import timezone
from django.contrib import admin
from .models import Order_info,Orders,Quarter,Month,Province,City,Month1,Jidu,Order
from django import forms


class Order_infoInline(admin.TabularInline):
	def get_readonly_fields(self, request, obj=None):
		if obj:
			return ['goods','number','price','order']
		else:
			return []
	model = Order_info
	extra = 0

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
	def get_queryset(self, request):
		qs = super(OrdersAdmin, self).get_queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(seller=request.user.id)
	list_display = ('order','pay','send','receive','comment','money')
	list_display_links = ('order','pay','send','receive','comment')
	search_fields = ('order','pay_status','send_status','receive_status','comment_status','money')
	ordering=('pay_status','send_status','receive_status','comment_status','-add_time')
	date_hierarchy = 'add_time'
	list_per_page = 50
	inlines = [Order_infoInline, ]
	exclude = ('seller',)
	def get_readonly_fields(self, request, obj=None):
		if obj:
			if obj.send_status ==0:
				return ['order','pay_status','receive_status','comment_status','money','seller','add_time','contacts','phone','address','send_time','receive_time','users','pay_time']
			else:
				return ['send_status','order', 'pay_status', 'receive_status', 'comment_status', 'money', 'seller', 'add_time', 'contacts', 'phone','address', 'send_time', 'receive_time', 'users','pay_time']
		else:
			return ['send_status']
	def save_model(self, request, obj, form, change):
		obj.send_time = timezone.datetime.now()
		super(OrdersAdmin, self).save_model(request, obj, form, change)

@admin.register(Quarter)
class QuarterAdmin(admin.ModelAdmin):
	list_display = ('name','detail',"all_quarter")
	list_display_links = ('name',)

@admin.register(Province)
class ProviceAdmin(admin.ModelAdmin):
	list_display = ('name', 'detail', "all_quarter")
	list_display_links = ('name',)

@admin.register(Jidu)
class JiduAdmin(admin.ModelAdmin):
	list_display = ('name',"detail")