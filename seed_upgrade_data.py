import os
import django
import sys

# Set up Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'saba_kausar_platform.settings')
django.setup()

from shop.models import Category, Product
from django.utils.text import slugify

def seed_child_products():
    print("Seeding Child categories and products...")
    
    # Ensure kids categories exist
    kids_dress, _ = Category.objects.get_or_create(name='Kids Dresses', defaults={'slug': 'kids-dresses'})
    kids_acc, _ = Category.objects.get_or_create(name='Kids Accessories', defaults={'slug': 'kids-accessories'})
    
    # Women categories for FEATURED setup
    western = Category.objects.get(name='Western Collection')
    traditional = Category.objects.get(name='Traditional Collection')

    # Update some existing products to be FEATURED, TRENDING etc.
    Product.objects.filter(age_group='women').update(is_featured=False, is_best_seller=False)
    
    featured_w = Product.objects.filter(category=western).first()
    if featured_w:
        featured_w.is_featured = True
        featured_w.save()
        
    best_w = Product.objects.filter(category=traditional).first()
    if best_w:
        best_w.is_best_seller = True
        best_w.save()

    # Add Kids Products
    kids_products = [
        {
            'name': 'Princess Pink Frock',
            'category': kids_dress,
            'price': 1599,
            'description': 'Beautiful pink frock for little princesses. Soft cotton lining.',
            'age_group': 'child'
        },
        {
            'name': 'Floral Hair Band Set',
            'category': kids_acc,
            'price': 299,
            'description': 'Set of 3 comfortable floral hair bands for kids.',
            'age_group': 'child'
        },
        {
            'name': 'Tiny Jewels Bracelet',
            'category': kids_acc,
            'price': 450,
            'description': 'Sparkly little bracelet for girls.',
            'age_group': 'child'
        }
    ]
    
    for p in kids_products:
        p_obj, created = Product.objects.get_or_create(
            name=p['name'],
            defaults={
                'slug': slugify(p['name']),
                'category': p['category'],
                'price': p['price'],
                'description': p['description'],
                'age_group': p['age_group'],
                'is_featured': True,
                'is_new_arrival': True
            }
        )
        if created:
            print(f"Created kid product: {p['name']}")

    print("Seeding complete!")

if __name__ == '__main__':
    seed_child_products()
