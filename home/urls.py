from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('bag/', views.bag, name='bag'),
    path('checkout/', views.checkout, name='checkout'),
    path('shop/', views.shop, name='shop')
]
