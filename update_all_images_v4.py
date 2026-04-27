import urllib.request
import os

def download_image(url, filename):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            with open(filename, 'wb') as f:
                f.write(response.read())
        print(f"Successfully downloaded {filename}")
    except Exception as e:
        print(f"Error downloading {filename}: {e}")

# Static images directory
img_dir = 'mahek_fashions/static/images'
os.makedirs(img_dir, exist_ok=True)

# 1. Home Page Categories - UPDATED: Using local images provided by user in 'main page' folder
# Pakistani Kurti: mahek_fashions/static/images/main page/kurti.jpeg
# Bridal Lehenga: mahek_fashions/static/images/main page/lahenga.jpeg
# Luxury Sarees: mahek_fashions/static/images/main page/saree.jpeg
home_categories = {} # Removed to avoid overwriting user's local images


for filename, url in home_categories.items():
    download_image(url, os.path.join(img_dir, filename))

# 2. Gallery Images (1-24) to replace male suits and toy cars
# Kurtis (1-8)
# Sarees (9-16)
# Traditional Wear (17-24)
gallery_images = {
    'gallery_1.jpg': 'https://images.unsplash.com/photo-1583391733956-3750e0ff4e8b?q=80&w=1000&auto=format&fit=crop',
    'gallery_2.jpg': 'https://images.unsplash.com/photo-1610030469983-98e550d6193c?q=80&w=1000&auto=format&fit=crop',
    'gallery_3.jpg': 'https://images.unsplash.com/photo-1567113379515-6e85e7168eb1?q=80&w=1000&auto=format&fit=crop',
    'gallery_4.jpg': 'https://images.unsplash.com/photo-1617627143750-d86bc21e42bb?q=80&w=1000&auto=format&fit=crop',
    'gallery_5.jpg': 'https://images.unsplash.com/photo-1608748010899-18f300247112?q=80&w=1000&auto=format&fit=crop',
    'gallery_6.jpg': 'https://images.unsplash.com/photo-1599054802207-91d346adc120?q=80&w=1000&auto=format&fit=crop',
    'gallery_7.jpg': 'https://images.unsplash.com/photo-1567113379515-6e85e7168eb1?q=80&w=1000&auto=format&fit=crop',
    'gallery_8.jpg': 'https://images.unsplash.com/photo-1608748010899-18f300247112?q=80&w=1000&auto=format&fit=crop',
    
    'gallery_9.jpg': 'https://images.unsplash.com/photo-1610030469983-98e550d6193c?q=80&w=1000&auto=format&fit=crop',
    'gallery_10.jpg': 'https://images.unsplash.com/photo-1617627143750-d86bc21e42bb?q=80&w=1000&auto=format&fit=crop',
    'gallery_11.jpg': 'https://images.unsplash.com/photo-1583391733956-3750e0ff4e8b?q=80&w=1000&auto=format&fit=crop',
    'gallery_12.jpg': 'https://images.unsplash.com/photo-1611601322175-ef8ec8c85f01?q=80&w=1000&auto=format&fit=crop',
    'gallery_13.jpg': 'https://images.unsplash.com/photo-1567113379515-6e85e7168eb1?q=80&w=1000&auto=format&fit=crop',
    'gallery_14.jpg': 'https://images.unsplash.com/photo-1610030469983-98e550d6193c?q=80&w=1000&auto=format&fit=crop',
    'gallery_15.jpg': 'https://images.unsplash.com/photo-1611601322175-ef8ec8c85f01?q=80&w=1000&auto=format&fit=crop',
    'gallery_16.jpg': 'https://images.unsplash.com/photo-1617627143750-d86bc21e42bb?q=80&w=1000&auto=format&fit=crop',
    
    'gallery_17.jpg': 'https://images.unsplash.com/photo-1599054802207-91d346adc120?q=80&w=1000&auto=format&fit=crop',
    'gallery_18.jpg': 'https://images.unsplash.com/photo-1583391733956-3750e0ff4e8b?q=80&w=1000&auto=format&fit=crop',
    'gallery_19.jpg': 'https://images.unsplash.com/photo-1610030469983-98e550d6193c?q=80&w=1000&auto=format&fit=crop',
    'gallery_20.jpg': 'https://images.unsplash.com/photo-1617627143750-d86bc21e42bb?q=80&w=1000&auto=format&fit=crop',
    'gallery_21.jpg': 'https://images.unsplash.com/photo-1567113379515-6e85e7168eb1?q=80&w=1000&auto=format&fit=crop',
    'gallery_22.jpg': 'https://images.unsplash.com/photo-1608748010899-18f300247112?q=80&w=1000&auto=format&fit=crop',
    'gallery_23.jpg': 'https://images.unsplash.com/photo-1611601322175-ef8ec8c85f01?q=80&w=1000&auto=format&fit=crop',
    'gallery_24.jpg': 'https://images.unsplash.com/photo-1583391733956-3750e0ff4e8b?q=80&w=1000&auto=format&fit=crop'
}

for filename, url in gallery_images.items():
    download_image(url, os.path.join(img_dir, filename))

print("All images updated locally.")
