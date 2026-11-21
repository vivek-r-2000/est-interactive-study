import json
import os
import sys
from pathlib import Path
from build_modern_website import build_website

def sync_and_build():
    db_path = Path("Study_Material/curriculum_database.json")
    if not db_path.exists():
        print("ERROR: curriculum_database.json not found")
        sys.exit(1)
        
    with open(db_path, "r", encoding="utf-8") as f:
        db = json.load(f)
        
    classes_map = {c["class_id"]: c for c in db["classes"] if "class_id" in c}

    # 1. Sync Slides for 11-19
    for cid in range(11, 20):
        slide_file = Path(f"Study_Material/class_{cid}_slides.json")
        if slide_file.exists():
            with open(slide_file, "r", encoding="utf-8") as f:
                sdata = json.load(f)
            slides = sdata.get("slides", [])
            if cid in classes_map:
                classes_map[cid]["slides"] = slides
                classes_map[cid]["total_slides"] = len(slides)
                print(f"[+] Synced {len(slides)} slides for Class {cid}")

    # 2. Sync Cards for Class 11
    c11_cards_file = Path("Study_Material/class_11_cards.json")
    if c11_cards_file.exists():
        with open(c11_cards_file, "r", encoding="utf-8") as f:
            c11_cards = json.load(f)
        if 11 in classes_map:
            classes_map[11]["topic_cards"] = c11_cards
            classes_map[11]["total_topic_cards"] = len(c11_cards)
            print(f"[+] Synced {len(c11_cards)} topic cards for Class 11")

    # 3. Sync Topic Cards for 12-19
    card_group_files = [
        "Study_Material/cards_class_12_13.json",
        "Study_Material/cards_class_14_15.json",
        "Study_Material/cards_class_16_17.json",
        "Study_Material/cards_class_18_19.json"
    ]
    for cgf in card_group_files:
        cg_path = Path(cgf)
        if cg_path.exists():
            with open(cg_path, "r", encoding="utf-8") as f:
                cdata = json.load(f)
            for cid_str, cards in cdata.items():
                cid = int(cid_str)
                if cid in classes_map:
                    classes_map[cid]["topic_cards"] = cards
                    classes_map[cid]["total_topic_cards"] = len(cards)
                    print(f"[+] Synced {len(cards)} topic cards for Class {cid}")

    # Save DB
    with open(db_path, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)
    print("[+] Saved updated curriculum_database.json")

    # Rebuild Website
    build_website()
    print("[+] Rebuilt index.html successfully")

if __name__ == "__main__":
    sync_and_build()
