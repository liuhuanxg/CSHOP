from typing import List, Any

from django.contrib import admin
from .models import Order_info,Orders
from django import forms

class Order_infoInline(admin.TabularInline):
	model = Order_info
	extra = 3

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
	def get_queryset(self, request):
		qs = super(OrdersAdmin, self).get_queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(seller=request.user.id)
	list_display = ('order','pay_status','send_status','receive_status','comment_status','money')
	search_fields = ('order','pay_status','send_status','receive_status','comment_status','money')
	ordering=('pay_status','send_status','receive_status','comment_status','-add_time')
	date_hierarchy = 'add_time'
	list_per_page = 50
	inlines = [Order_infoInline, ]
	exclude = ('seller',)
	def get_readonly_fields(self, request, obj=None):
		if obj:
			return ['order','pay_status','receive_status','comment_status','money','seller','add_time','address','contacts','phone']
		else:
			return ['send_status']


@admin.register(Order_info)
class Order_infoAdmin(admin.ModelAdmin):
	list_display = ('goods','number','price','order')
	search_fields = ('goods',)
	list_per_page = 50


