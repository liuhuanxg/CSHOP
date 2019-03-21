from django.urls import path
from . import views
app_name ='goods'

urlpatterns = [
    path('global_go/', views.global_go, name='global_go'),
    path('refined/', views.refined, name='refined'),
    path('brand/', views.brand, name='brand'),
    path('list/<int:id>', views.list, name='list'),
    path('goods_detail/<int:id>', views.goods_detail, name='goods_detail'),
]