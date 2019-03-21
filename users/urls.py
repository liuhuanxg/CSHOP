from django.urls import path
from . import views
app_name ='users'

urlpatterns = [
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('car/',views.car,name='car'),
    path('car_path/',views.car_path,name='car_path'),
    path('truesubmit/',views.truesubmit,name='truesubmit'),
    path('usercenter/',views.usercenter,name='usercenter'),
    path('add_path/',views.add_path,name='add_path'),
]