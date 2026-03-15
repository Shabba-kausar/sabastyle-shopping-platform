import os
import django
import sys

# Set up Django environment
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'saba_kausar_platform.settings')
django.setup()

from shop.models import Category, Product
from django.utils.text import slugify

def seed_data():
    print("Seeding categories...")
    categories_data = [
        {'name': 'Western Collection', 'description': 'Tops, jeans, skirts, gowns, party wear'},
        {'name': 'Traditional Collection', 'description': 'Saree, salwar suit, lehenga, kurti'},
        {'name': 'Jewellery', 'description': 'Earrings, Necklaces, Bangles, Rings'},
        {'name': 'Makeup Products', 'description': 'Lipstick, Foundation, Eyeliner, Mascara'},
    ]

    categories = {}
    for cat in categories_data:
        obj, created = Category.objects.get_or_create(
            name=cat['name'],
            defaults={'slug': slugify(cat['name']), 'description': cat['description']}
        )
        categories[cat['name']] = obj

    print("Seeding products...")
    products_data = [
        # Western
        {
            'category': 'Western Collection',
            'name': 'Floral Evening Gown',
            'description': 'A beautiful pink floral gown perfect for evening parties.',
            'price': 89.99,
            'rating': 4.8,
            'is_trending': True,
        },
        {
            'category': 'Western Collection',
            'name': 'Chic Denim Skirt',
            'description': 'Stylish high-waisted denim skirt for casual outings.',
            'price': 34.50,
            'rating': 4.5,
            'is_best_seller': True,
        },
        # Traditional
        {
            'category': 'Traditional Collection',
            'name': 'Silk Zari Saree',
            'description': 'Premium silk saree with intricate zari work.',
            'price': 120.00,
            'rating': 4.9,
            'is_trending': True,
        },
        {
            'category': 'Traditional Collection',
            'name': 'Designer Kurti Set',
            'description': 'Comfortable and elegant kurti set with dupatta.',
            'price': 55.00,
            'rating': 4.6,
        },
        # Jewellery
        {
            'category': 'Jewellery',
            'name': 'Gold Plated Earrings',
            'description': 'Elegant gold plated drop earrings for a royal look.',
            'price': 25.00,
            'rating': 4.7,
            'is_best_seller': True,
        },
        {
            'category': 'Jewellery',
            'name': 'Diamond Studded Necklace',
            'description': 'Beautiful necklace with shimmering stones.',
            'price': 150.00,
            'rating': 5.0,
            'is_trending': True,
        },
        # Makeup
        {
            'category': 'Makeup Products',
            'name': 'Matte Red Lipstick',
            'description': 'Long-lasting matte finish red lipstick.',
            'price': 12.99,
            'rating': 4.4,
            'is_best_seller': True,
        },
        {
            'category': 'Makeup Products',
            'name': 'Velvet Foundation',
            'description': 'Full coverage foundation for a flawless look.',
            'price': 28.00,
            'rating': 4.3,
        }
    ]

    for prod in products_data:
        cat_obj = categories[prod['category']]
        Product.objects.get_or_create(
            name=prod['name'],
            category=cat_obj,
            defaults={
                'slug': slugify(prod['name']),
                'description': prod['description'],
                'price': prod['price'],
                'rating': prod['rating'],
                'is_trending': prod.get('is_trending', False),
                'is_best_seller': prod.get('is_best_seller', False),
                # Note: images are handled separately in real scenarios, 
                # for now we'll just ensure fields are populated
            }
        )
    
    print("Data seeding completed!")

if __name__ == '__main__':
    seed_data()
