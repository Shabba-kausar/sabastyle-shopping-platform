import os
import requests
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'saba_kausar_platform.settings')
django.setup()

from shop.models import Product

# Product Image Data (ID: (URL, filename))
image_data = {
    12: ("https://images.unsplash.com/photo-1764426381179-7aa7bfdb0e32?q=80&w=1080&auto=format&fit=crop", "silver_nose_pin.jpg"),
    13: ("https://images.unsplash.com/photo-1758995115785-d13726ac93f0?q=80&w=1080&auto=format&fit=crop", "gold_choker_set.jpg"),
    14: ("https://images.unsplash.com/photo-1476965805533-564543966f62?q=80&w=1080&auto=format&fit=crop", "crystal_ring.jpg"),
    15: ("https://images.unsplash.com/photo-1769063382706-8156b3b33eac?q=80&w=1080&auto=format&fit=crop", "printed_kurti.jpg"),
    16: ("https://images.unsplash.com/photo-1756483492038-974f2a2ff341?q=80&w=1080&auto=format&fit=crop", "party_gown_heavy.jpg"),
    17: ("https://images.unsplash.com/photo-1759851235367-2eb2282414fa?q=80&w=1080&auto=format&fit=crop", "floral_crop_top.jpg"),
    18: ("https://images.unsplash.com/photo-1668255446079-b15fd061735d?q=80&w=1080&auto=format&fit=crop", "intense_kajal.jpg"),
    19: ("https://images.unsplash.com/photo-1547934659-7fa699ef3ce0?q=80&w=1080&auto=format&fit=crop", "eyeshadow_palette_pro.jpg"),
    20: ("https://images.unsplash.com/photo-1640958903443-1e49d720650d?q=80&w=1080&auto=format&fit=crop", "matte_nail_enamel.jpg"),
    21: ("https://images.unsplash.com/photo-1664918688104-4eb8956f97a2?q=80&w=1080&auto=format&fit=crop", "baby_cotton_frock.jpg"),
}

media_path = os.path.join('media', 'products')
if not os.path.exists(media_path):
    os.makedirs(media_path)

for pid, (url, filename) in image_data.items():
    print(f"Processing Product ID {pid}: {filename}...")
    try:
        response = requests.get(url, stream=True, timeout=15)
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

print("\nExpanded image population complete!")
