from django.contrib import admin
from .models import GoodsInfo,GoodsType,BigType
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


@admin.register(GoodsInfo)
class GoodsInfoAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs= super(GoodsInfoAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(seller=request.user.id)
    list_display = ('goods_name','goods_oprice','goods_xprice','goods_count','goods_address')
    search_fields = ('goods_name',)
    list_per_page = 50
    exclude = ('seller',)
    fieldsets = (
        ("base info", {'fields': ['goods_name', 'goods_oprice', 'goods_xprice','goods_count','goods_method','goods_pic','goods_address','type']}),
        ("Content", {'fields': ['goods_info', 'goods_content']})
    )
    def save_model(self, request, obj, form, change):
        obj.seller=request.user
        super(GoodsInfoAdmin, self).save_model(request, obj, form, change)

admin.site.site_header='快乐购后台管理'
admin.site.site_title='快乐购后台管理'