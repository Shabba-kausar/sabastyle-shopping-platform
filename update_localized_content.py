import os
import django
import sys
import shutil

# Set up Django environment
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'saba_kausar_platform.settings')
django.setup()

from shop.models import Category, Product
from django.utils.text import slugify

def update_data():
    # Define local paths for generated images (using placeholder mapping for now)
    # The actual paths from previous tool outputs:
    # western_party_gown: C:\Users\shabb\.gemini\antigravity\brain\656937d3-5660-4627-84d9-9929853a7e29\western_party_gown_1773498369901.png
    # traditional_lehenga: C:\Users\shabb\.gemini\antigravity\brain\656937d3-5660-4627-84d9-9929853a7e29\traditional_lehenga_1773498711584.png
    # gold_necklace_set: C:\Users\shabb\.gemini\antigravity\brain\656937d3-5660-4627-84d9-9929853a7e29\gold_necklace_set_1773498791496.png
    # makeup_kit_premium: C:\Users\shabb\.gemini\antigravity\brain\656937d3-5660-4627-84d9-9929853a7e29\makeup_kit_premium_1773498813330.png

    img_sources = {
        'western': r'C:\Users\shabb\.gemini\antigravity\brain\656937d3-5660-4627-84d9-9929853a7e29\western_party_gown_1773498369901.png',
        'traditional': r'C:\Users\shabb\.gemini\antigravity\brain\656937d3-5660-4627-84d9-9929853a7e29\traditional_lehenga_1773498711584.png',
        'jewellery': r'C:\Users\shabb\.gemini\antigravity\brain\656937d3-5660-4627-84d9-9929853a7e29\gold_necklace_set_1773498791496.png',
        'makeup': r'C:\Users\shabb\.gemini\antigravity\brain\656937d3-5660-4627-84d9-9929853a7e29\makeup_kit_premium_1773498813330.png'
    }

    media_prod_dir = os.path.join('media', 'products')
    if not os.path.exists(media_prod_dir):
        os.makedirs(media_prod_dir)

    # Helper to copy and return relative name
    def deploy_img(src, name):
        if os.path.exists(src):
            dst = os.path.join(media_prod_dir, name)
            shutil.copy(src, dst)
            return f'products/{name}'
        return None

    print("Updating product images and adding new products...")

    # Western
    gown = Product.objects.get(name='Floral Evening Gown')
    gown.image = deploy_img(img_sources['western'], 'gown.png')
    gown.price = 5999
    gown.save()

    # Traditional
    lehenga = Product.objects.get(name='Silk Zari Saree')
    lehenga.image = deploy_img(img_sources['traditional'], 'lehenga.png')
    lehenga.price = 8500
    lehenga.save()

    # Jewellery
    neck = Product.objects.get(name='Gold Plated Earrings')
    neck.image = deploy_img(img_sources['jewellery'], 'necklace.png')
    neck.price = 1200
    neck.save()

    # Makeup
    kit = Product.objects.get(name='Matte Red Lipstick')
    kit.image = deploy_img(img_sources['makeup'], 'makeup.png')
    kit.price = 950
    kit.save()

    print("Localization update complete!")

if __name__ == '__main__':
    update_data()
