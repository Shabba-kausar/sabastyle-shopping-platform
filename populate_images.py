import os
import requests
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'saba_kausar_platform.settings')
django.setup()

from shop.models import Product

# Product Image Data (ID: (URL, filename))
image_data = {
    2: ("https://images.pexels.com/photos/6069824/pexels-photo-6069824.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2", "chic_denim_skirt.jpg"),
    4: ("https://images.unsplash.com/photo-1769063382706-8156b3b33eac?auto=format&fit=crop&q=80&w=2000", "designer_kurti_set.jpg"),
    6: ("https://images.unsplash.com/photo-1769857879388-df93b4c96bca?auto=format&fit=crop&q=80&w=2000", "diamond_necklace.jpg"),
    8: ("https://images.unsplash.com/photo-1571875257727-256c39da42af?auto=format&fit=crop&q=80&w=2000", "velvet_foundation.jpg"),
    9: ("https://images.unsplash.com/photo-1765947381072-87b78243b759?auto=format&fit=crop&q=80&w=2000", "princess_pink_frock.jpg"),
    10: ("https://images.unsplash.com/photo-1559659133-8781d8f3b673?auto=format&fit=crop&q=80&w=2000", "floral_hair_band.jpg"),
    11: ("https://images.unsplash.com/photo-1766560359395-aa6d7a46ad79?auto=format&fit=crop&q=80&w=2000", "tiny_jewels_bracelet.jpg"),
}

media_path = os.path.join('media', 'products')
if not os.path.exists(media_path):
    os.makedirs(media_path)

for pid, (url, filename) in image_data.items():
    print(f"Processing Product ID {pid}: {filename}...")
    try:
        response = requests.get(url, stream=True, timeout=10)
        if response.status_code == 200:
            file_path = os.path.join(media_path, filename)
            with open(file_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            # Update DB
            product = Product.objects.get(id=pid)
            product.image = f'products/{filename}'
            product.save()
            print(f"  Successfully updated Product ID {pid}")
        else:
            print(f"  Failed to download {url}: Status {response.status_code}")
    except Exception as e:
        print(f"  Error processing Product ID {pid}: {str(e)}")

print("\nImage population complete!")
