import os
import glob
import re

base = r"C:\Users\vivek\EST"
index = os.path.join(base, "index.html")
home = os.path.join(base, "Study_Material", "00_home.html")
modules = sorted(glob.glob(os.path.join(base, "Study_Material", "[0-1][0-9]_*.html")))

print(f"index.html: {os.path.exists(index)} ({os.path.getsize(index)} bytes)")
print(f"00_home.html: {os.path.exists(home)} ({os.path.getsize(home)} bytes)")
print(f"Total lecture modules found: {len(modules)}")

broken = 0
total_imgs = 0
for m in modules:
    with open(m, "r", encoding="utf-8") as f:
        txt = f.read()
    imgs = re.findall(r'src=["\']([^"\']+)["\']', txt)
    for img in imgs:
        if not img.startswith("http"):
            total_imgs += 1
            full = os.path.normpath(os.path.join(base, "Study_Material", img))
            if not os.path.exists(full):
                broken += 1
                if broken < 5:
                    print("  [!] Broken image:", os.path.basename(m), img)

print(f"Total internal image references checked: {total_imgs}")
print(f"Broken image paths: {broken}")
