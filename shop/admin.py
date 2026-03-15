from django.contrib import admin
from .models import Category, Product, Wishlist

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'created', 'updated', 'is_trending', 'is_best_seller']
    list_filter = ['available', 'created', 'updated', 'category', 'is_trending', 'is_best_seller']
    list_editable = ['price', 'available', 'is_trending', 'is_best_seller']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'added_at']
