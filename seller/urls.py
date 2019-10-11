from django.urls import path
from . import views
app_name ='seller'

urlpatterns = [
    # path('',views.index),
    path('show_orders/',views.show_orders,name="show_orders"),
    path('orders/api/',views.orders,name='orders/api/'),
    path('zuobiaozhou/',views.zuobiaozhou,name='zuobiaozhou'),
    path('show_evaluation/<int:id>', views.show_evaluation, name="show_evaluation"),
    path('evaluation/<int:id>', views.evaluation, name="evaluation"),
    path('show_quarter/<str:id>', views.show_quarter, name="show_quarter"),
    path('city_volume/<str:id>', views.city_volume, name="city_volume"),
    path('add_order', views.add_order, name="add_order"),
    path('show_order/<str:id>', views.show_order, name="show_order"),
    path('re_order/', views.re_order, name="re_order"),
]