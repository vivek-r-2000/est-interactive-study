import os
import json
import fitz
from PIL import Image
import io

WORKSPACE = r"C:\Users\vivek\EST"
SLIDES_DIR = os.path.join(WORKSPACE, "Lecture_Slides")
METADATA_PATH = os.path.join(WORKSPACE, "Study_Material", "lectures_metadata.json")
DIAG_BASE = os.path.join(WORKSPACE, "Study_Material", "assets", "diagrams")

with open(METADATA_PATH, "r", encoding="utf-8") as f:
    LECS = json.load(f)

extracted_catalog = {}

for lec in LECS:
    lec_id = lec["id"]
    lec_dir = os.path.join(DIAG_BASE, f"lec_{lec_id}")
    os.makedirs(lec_dir, exist_ok=True)
    
    catalog_list = []
    diag_count = 0
    
    for fn in lec["files"]:
        pdf = os.path.join(SLIDES_DIR, fn)
        if not os.path.exists(pdf):
            continue
        doc = fitz.open(pdf)
        for page_idx in range(len(doc)):
            page = doc[page_idx]
            page_text = page.get_text().strip()
            first_line = page_text.split('\n')[0].strip() if page_text else f"Slide {page_idx+1}"
            first_line = first_line[:65]
            
            img_list = page.get_images(full=True)
            for img_info in img_list:
                xref = img_info[0]
                try:
                    base_image = doc.extract_image(xref)
                    img_bytes = base_image["image"]
                    ext = base_image["ext"]
                    
                    # Filter out tiny bullets or logos (< 8 KB or dimensions < 120px)
                    if len(img_bytes) < 8000:
                        continue
                    
                    im = Image.open(io.BytesIO(img_bytes))
                    w, h = im.size
                    if w < 120 or h < 120:
                        continue
                    
                    diag_count += 1
                    diag_filename = f"diagram_{diag_count:02d}.{ext}"
                    out_path = os.path.join(lec_dir, diag_filename)
                    with open(out_path, "wb") as f_out:
                        f_out.write(img_bytes)
                    
                    rel_path = f"assets/diagrams/lec_{lec_id}/{diag_filename}"
                    catalog_list.append({
                        "id": diag_count,
                        "rel_path": rel_path,
                        "width": w,
                        "height": h,
                        "size_kb": round(len(img_bytes) / 1024, 1),
                        "page": page_idx + 1,
                        "source_file": fn,
                        "slide_title": first_line
                    })
                except Exception as e:
                    pass
        doc.close()
    
    print(f"Lec {lec_id}: extracted {len(catalog_list)} distinct diagram image(s).")
    extracted_catalog[lec_id] = catalog_list

out_cat_path = os.path.join(WORKSPACE, "Study_Material", "extracted_diagrams_catalog.json")
with open(out_cat_path, "w", encoding="utf-8") as f:
    json.dump(extracted_catalog, f, indent=2)
print(f"[+] Saved catalog to {out_cat_path}")
