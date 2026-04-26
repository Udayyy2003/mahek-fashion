import urllib.request
import os

# A list of 24 unique and reliable Unsplash IDs for fashion clothing
fashion_ids = [
    "photo-1490481651871-ab68624d5517", "photo-1492707892479-7bc8d5a4ee93", "photo-1495385794356-15371f348c31",
    "photo-1483985988355-763728e1935b", "photo-1496747611176-843222e1e57c", "photo-1509319117193-57bab727e09d",
    "photo-1515886657613-9f3515b0c78f", "photo-1525507119028-ed4c629a60a3", "photo-1539109136881-3be0616acf4b",
    "photo-1554412930-c741e2474067", "photo-1558769132-cb1aea458c5e", "photo-1469334031218-e382a71b716b",
    "photo-1445205170230-053b83016050", "photo-1479064560454-001d91cd7970", "photo-1485230895905-ec40ba36b9bc",
    "photo-1485968579580-b6d095142e6e", "photo-1487222477894-8943e31ef7b2", "photo-1496217590455-aa63a8350eea",
    "photo-1505022610485-0249ba5b3675", "photo-1507680434567-5739c80be1ac", "photo-1512436991641-6745cdb1723f",
    "photo-1523381210434-271e8be1f52b", "photo-1524041255072-7df05f5ed095", "photo-1529139572765-397392ef5a88",
    "photo-1503342217505-b0a15ec3261c", "photo-1503341455253-bfe4c5f173b8", "photo-1503342392335-321c7bad7043",
    "photo-1481350323114-f0e7a246ad92", "photo-1512436991641-6745cdb1723f", "photo-1523381210434-271e8be1f52b",
    "photo-1524041255072-7df05f5ed095", "photo-1529139572765-397392ef5a88", "photo-1537832816519-689ad1631621",
    "photo-1516762689617-e1cffcef479d", "photo-1490114538077-0a7f8cb49891", "photo-1434389677669-e08b4cac3105"
]

# We also need some ethnic wear specific IDs that worked
ethnic_ids = [
    "photo-1589156280159-27698a70f29e", "photo-1594938298603-c8148c4dae35", "photo-1610030469983-98e550d6193c",
    "photo-1583391733956-3750e0ff4e8b", "photo-1605518216938-7c31b7b14ad0", "photo-1617627143750-d86bc21e42bb",
    "photo-1594736797933-d0501ba2fe65"
]

# Combine them, prioritizing ethnic wear, then filling up to 24 with general fashion
all_ids = []
seen = set()
for eid in ethnic_ids:
    if eid not in seen:
        all_ids.append(eid)
        seen.add(eid)

for fid in fashion_ids:
    if len(all_ids) >= 24:
        break
    if fid not in seen:
        all_ids.append(fid)
        seen.add(fid)

os.makedirs("mahek_fashions/static/images", exist_ok=True)
headers = {'User-Agent': 'Mozilla/5.0'}

success_count = 0
for img_id in all_ids:
    if success_count >= 24:
        break
        
    filename = f"gallery_{success_count+1}.jpg"
    
    # Check if already exists
    if os.path.exists(f"mahek_fashions/static/images/{filename}"):
        print(f"Verified {filename}: already exists")
        success_count += 1
        continue

    url = f"https://images.unsplash.com/{img_id}?q=80&w=800"
    print(f"Attempting to download {filename} from {url}...")
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                with open(f"mahek_fashions/static/images/{filename}", 'wb') as out_file:
                    out_file.write(response.read())
                print(f"Successfully downloaded {filename}")
                success_count += 1
            else:
                print(f"Skipping {img_id}: Status {response.status}")
    except Exception as e:
        print(f"Failed to download {img_id}: {e}")

print(f"Finished. Downloaded/Verified {success_count} unique images.")
