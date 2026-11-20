import json
import os
import sys

def merge_classes():
    db_path = os.path.join("Study_Material", "curriculum_database.json")
    if not os.path.exists(db_path):
        print("ERROR: curriculum_database.json not found")
        sys.exit(1)
        
    with open(db_path, "r", encoding="utf-8") as f:
        db = json.load(f)
        
    sm_dir = "Study_Material"
    merged_count = 0
    total_slides = 0
    
    for cid in range(12, 20):
        fname = os.path.join(sm_dir, f"class_{cid}_slides.json")
        if not os.path.exists(fname):
            print(f"[-] Class {cid} slides file not yet present: {fname}")
            continue
            
        with open(fname, "r", encoding="utf-8") as f:
            cdata = json.load(f)
            
        slides = cdata.get("slides", [])
        total_slides += len(slides)
        
        # Find matching class in db
        matched = False
        for c in db.get("classes", []):
            if c.get("class_id") == cid:
                c["slides"] = slides
                c["total_slides"] = len(slides)
                if cdata.get("title"):
                    c["title"] = cdata["title"]
                matched = True
                merged_count += 1
                print(f"[+] Merged Class {cid}: {len(slides)} slides")
                break
                
        if not matched:
            print(f"[-] Warning: Class {cid} not found in curriculum_database.json")
            
    with open(db_path, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully merged {merged_count} classes ({total_slides} slides) into {db_path}!")

if __name__ == "__main__":
    merge_classes()
