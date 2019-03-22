from django.urls import path
from . import views
app_name ='users'

urlpatterns = [
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout,name='logout'),
    path('car/',views.car,name='car'),
    path('add_car/',views.add_car,name='add_car'),
    path('car_path/',views.car_path,name='car_path'),
    path('truesubmit/',views.truesubmit,name='truesubmit'),
    path('usercenter/',views.usercenter,name='usercenter'),
    path('add_path/',views.add_path,name='add_path'),
    path('collect/',views.collect,name='collect'),
    path('userindex/',views.userindex,name='userindex'),
    path('change_message/',views.change_message,name='change_message'),
    path('userrefund/',views.userrefund,name='userrefund'),
    path('test/',views.test,name='test'),
]