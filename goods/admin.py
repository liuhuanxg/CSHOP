from typing import List, Any

from django.contrib import admin
from .models import GoodsInfo,GoodsType,BigType,Detail
from django import forms

@admin.register(BigType)
class BigTypeAdmin(admin.ModelAdmin):
	list_display = ('id','name','create_time')
	search_fields = ('name',)
	date_hierarchy = 'create_time'
	list_per_page = 50

@admin.register(GoodsType)
class GoodsTypeAdmin(admin.ModelAdmin):
	list_display = ('id','type_name','type','create_time')
	date_hierarchy = 'create_time'
	search_fields = ('type_name','type')
	ordering = ('-create_time',)
	list_per_page = 50

class DetailInline(admin.TabularInline):
	model = Detail
	extra = 3

@admin.register(GoodsInfo)
class GoodsInfoAdmin(admin.ModelAdmin):
	def get_queryset(self, request):
		qs= super(GoodsInfoAdmin, self).get_queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(seller=request.user.id)
	inlines = [DetailInline,]
	list_display = ('goods_name','xprice','oprice','goods_method','goods_address')
	search_fields = ('goods_name',)
	list_per_page = 50
	exclude = ('seller',)
	fieldsets = (
		("基本信息", {'fields': ['goods_name','goods_method','goods_pic','goods_address','type','oprice','xprice']}),
		("介绍", {'fields': ['goods_info', 'goods_content']})
	)
	def save_model(self, request, obj, form, change):
		obj.seller=request.user
		super(GoodsInfoAdmin, self).save_model(request, obj, form, change)

@admin.register(Detail)
class DetailAdmin(admin.ModelAdmin):
	def get_queryset(self, request):
		qs= super(DetailAdmin, self).get_queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(name__seller=request.user.id)
	list_display = ('name', 'goods_count', 'size','color','goods_oprice','goods_xprice')
	search_fields = ('name','goods_count')
	list_per_page = 50


from django.contrib.auth.models import User,Permission
@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
	list_display = ('id','name', 'codename', )
	ordering=('id',)
	search_fields = ('name', 'codename')

admin.site.site_header='快乐购后台管理'
admin.site.site_title='快乐购后台管理'