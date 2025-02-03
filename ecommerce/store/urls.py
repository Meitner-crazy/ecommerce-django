from django.urls import path

#use dot only because they are in the same directory
from . import views

urlpatterns= [

    path('', views.store, name='store'),


    #Individual product
    path('product/<slug:product_slug>/', views.product_info, name='product-info'),

    #Individual category
    path('search/<slug:category_slug>/', views.list_category, name='list-category')


]