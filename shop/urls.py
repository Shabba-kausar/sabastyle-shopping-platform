from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('products/women/', views.product_list, {'age_group': 'women'}, name='product_list_women'),
    path('products/child/', views.product_list, {'age_group': 'child'}, name='product_list_child'),
    path('products/<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('product/<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('wishlist/add/<int:product_id>/', views.wishlist_add, name='wishlist_add'),
    path('wishlist/', views.wishlist_detail, name='wishlist_detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
