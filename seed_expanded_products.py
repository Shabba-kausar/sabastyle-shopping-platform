import os
import django
from django.utils.text import slugify

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'saba_kausar_platform.settings')
django.setup()

from shop.models import Category, Product

def seed_products():
    jewellery = Category.objects.get(name__icontains='jewellery')
    western = Category.objects.get(name__icontains='western')
    traditional = Category.objects.get(name__icontains='traditional')
    makeup = Category.objects.get(name__icontains='makeup')
    kids_dresses = Category.objects.get(name__icontains='kids dresses')

    new_products = [
        # Jewellery
        {
            'category': jewellery,
            'name': 'Traditional Silver Nose Pin',
            'description': 'Elegant and traditional silver nose pin for a classic look.',
            'price': 149.00,
            'age_group': 'women',
            'is_featured': True
        },
        {
            'category': jewellery,
            'name': 'Luxury Gold Choker Set',
            'description': 'Exquisite 24K gold plated choker set for weddings and parties.',
            'price': 4999.00,
            'age_group': 'women',
            'is_trending': True
        },
        {
            'category': jewellery,
            'name': 'Elegant Crystal Ring',
            'description': 'Beautiful crystal studded ring in silver finish.',
            'price': 199.00,
            'age_group': 'women',
            'is_new_arrival': True
        },
        
        # Dresses
        {
            'category': traditional,
            'name': 'Cotton Printed Kurti',
            'description': 'Casual and comfortable cotton printed kurti for daily wear.',
            'price': 499.00,
            'age_group': 'women',
            'is_featured': True
        },
        {
            'category': western,
            'name': 'Heavy Embroidered Party Gown',
            'description': 'Stunning heavy embroidered gown for grand celebrations.',
            'price': 6500.00,
            'age_group': 'women',
            'is_best_seller': True
        },
        {
            'category': western,
            'name': 'Summer Floral Crop Top',
            'description': 'Lightweight and stylish floral crop top for summer outings.',
            'price': 399.00,
            'age_group': 'women',
            'is_new_arrival': True
        },
        
        # Makeup
        {
            'category': makeup,
            'name': 'Waterproof Intense Kajal',
            'description': 'Smudge-proof and intense black kajal for 24h wear.',
            'price': 99.00,
            'age_group': 'women',
            'is_featured': True
        },
        {
            'category': makeup,
            'name': 'Pro Eyeshadow Palette',
            'description': 'Professional 12-color eyeshadow palette with shimmer and matte finishes.',
            'price': 299.00,
            'age_group': 'women',
            'is_trending': True
        },
        {
            'category': makeup,
            'name': 'Matte Finish Nail Enamel',
            'description': 'Quick dry matte finish nail polish in trendy shades.',
            'price': 85.00,
            'age_group': 'women',
            'is_new_arrival': True
        },
        
        # Kids
        {
            'category': kids_dresses,
            'name': 'Baby Cotton Frock',
            'description': 'Soft and breathable cotton frock for infants.',
            'price': 450.00,
            'age_group': 'child',
            'is_featured': True
        }
    ]

    for p_data in new_products:
        slug = slugify(p_data['name'])
        # Ensure unique slug
        base_slug = slug
        counter = 1
        while Product.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1
            
        Product.objects.get_or_create(
            slug=slug,
            defaults={
                'category': p_data['category'],
                'name': p_data['name'],
                'description': p_data['description'],
                'price': p_data['price'],
                'age_group': p_data['age_group'],
                'is_featured': p_data.get('is_featured', False),
                'is_trending': p_data.get('is_trending', False),
                'is_best_seller': p_data.get('is_best_seller', False),
                'is_new_arrival': p_data.get('is_new_arrival', True),
                'available': True,
                'image': 'products/placeholder.jpg' # Will update images next
            }
        )
        print(f"Created product: {p_data['name']}")

if __name__ == "__main__":
    seed_products()
