from django.urls import path
from . import views
from os import name
from django.views.static import serve
from django.conf.urls import url
from django.conf import settings
app_name = "accounts"
urlpatterns = [
    path('', views.home, name="home"),
    #	post	views
    path('index',	views.index,	name='index'),
    path('transfer_money/', views.cust, name='transfermoney'),
    path('customers/transfer_money/', views.cust, name='transfermoney'),
    path('transfer_details/', views.transfer, name='transferdetails'),
    path('customers/transfer_money/transfer_details/',
         views.transfer, name='transferdetails'),
    path('customers/', views.cdetails, name='customers'),
]
