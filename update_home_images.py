import urllib.request
import os

def download_image(url, filename):
    headers = {'User-Agent': 'Mozilla/5.0'}
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

# Top 3 Premium Collections Images
replacements = {
    'kurti_1.jpg': 'https://images.unsplash.com/photo-1610030469983-98e550d6193c?q=80&w=1000&auto=format&fit=crop', # Pakistani Kurti
    'saree_1.jpg': 'https://images.unsplash.com/photo-1617627143750-d86bc21e42bb?q=80&w=1000&auto=format&fit=crop', # Luxury Saree
    'trad_1.jpg': 'https://images.unsplash.com/photo-1583391733956-3750e0ff4e8b?q=80&w=1000&auto=format&fit=crop'   # Bridal Wear
}

for filename, url in replacements.items():
    path = os.path.join(img_dir, filename)
    print(f"Replacing {path}...")
    download_image(url, path)

print("Home page category images replacement complete.")
