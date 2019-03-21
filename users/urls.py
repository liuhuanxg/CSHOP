from django.urls import path
from . import views
app_name ='[users]'

urlpatterns = [
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('go/',views.go,name='go'),
    path('refined/',views.refined,name='refined'),
    path('brand/',views.brand,name='brand'),
    path('list/',views.list,name='list'),
    path('car/',views.car,name='car'),
    path('car_path/',views.car_path,name='car_path'),
]