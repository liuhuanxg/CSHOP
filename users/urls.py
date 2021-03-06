from django.urls import path
from . import views
app_name ='users'

urlpatterns = [
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout,name='logout'),
    path('car/',views.car,name='car'),
    path('check_count/',views.check_count,name='check_count'),
    path('add_car/',views.add_car,name='add_car'),
    path('del_car/<int:id>',views.del_car,name='del_car'),
    path('del_collect/<int:id>',views.del_collect,name='del_collect'),
    path('car_path/',views.car_path,name='car_path'),
    path('change_message/',views.change_message,name='change_message'),
    path('truesubmit/',views.truesubmit,name='truesubmit'),
    path('usercenter/',views.usercenter,name='usercenter'),
    path('add_path/',views.add_path,name='add_path'),
    path('collect/',views.collect,name='collect'),
    path('userindex/',views.userindex,name='userindex'),
    path('message/',views.message,name='message'),
    path('userrefund/',views.userrefund,name='userrefund'),
    path('add_adress/',views.add_adress,name='add_adress'),
    path('del_address/<int:id>',views.del_address,name='del_address'),
    path('receive_goods/<int:id>',views.receive_goods,name='receive_goods'),
    path('modify_address/<int:id>',views.modify_address,name='modify_address'),
    path('pay/',views.pay,name='pay'),
    path('return_url/',views.return_url,name='return_url'),
]