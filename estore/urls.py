
from django.contrib import admin
from django.urls import path
from .import views



urlpatterns = [
    path('', views.Estore, name='estore'),
    path('<slug:category_slug>/', views.Estore, name='products_by_category'),
    path('<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
]
