from django.shortcuts import render, get_object_or_404, redirect
from django.db import models
from .models import Category, Product, Wishlist
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    categories = Category.objects.all()
    featured_products = Product.objects.filter(is_featured=True, available=True)[:4]
    trending_products = Product.objects.filter(is_trending=True, available=True)[:4]
    new_arrivals = Product.objects.filter(is_new_arrival=True, available=True)[:4]
    best_sellers = Product.objects.filter(is_best_seller=True, available=True)[:4]
    return render(request, 'shop/home.html', {
        'categories': categories,
        'featured_products': featured_products,
        'trending_products': trending_products,
        'new_arrivals': new_arrivals,
        'best_sellers': best_sellers,
    })

@login_required
def product_list(request, category_slug=None, age_group=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    
    # Category filter
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    
    # Age group filter
    if age_group:
        products = products.filter(age_group=age_group)
        
    # Search filter
    query = request.GET.get('search')
    if query:
        products = products.filter(
            models.Q(name__icontains=query) | 
            models.Q(description__icontains=query) |
            models.Q(category__name__icontains=query) |
            models.Q(category__search_keywords__icontains=query) |
            models.Q(age_group__icontains=query)
        )
        
    return render(request, 'shop/product/list.html', {
        'category': category,
        'categories': categories,
        'products': products,
        'age_group': age_group,
        'search_query': query
    })

@login_required
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'shop/product/detail.html', {'product': product})

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return render(request, 'shop/contact.html')

@login_required
def wishlist_detail(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'shop/wishlist.html', {'wishlist_items': wishlist_items})

@login_required
def wishlist_add(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Wishlist.objects.get_or_create(user=request.user, product=product)
    return redirect('shop:wishlist_detail')
