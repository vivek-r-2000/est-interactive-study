import json
import os
import sys

def verify_db():
    db_path = os.path.join("Study_Material", "curriculum_database.json")
    if not os.path.exists(db_path):
        print("ERROR: curriculum_database.json not found")
        sys.exit(1)
        
    with open(db_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    classes = data.get("classes", [])
    if len(classes) != 19:
        print(f"ERROR: Expected 19 classes, found {len(classes)}")
        sys.exit(1)
        
    pillars = set()
    total_submodules = 0
    for c in classes:
        p = c.get("pillar")
        if not p:
            print(f"ERROR: Missing pillar for class {c.get('class_id')}")
            sys.exit(1)
        pillars.add(p)
        subs = c.get("submodules", [])
        if len(subs) < 2:
            print(f"ERROR: Class {c.get('class_id')} has fewer than 2 submodules")
            sys.exit(1)
        total_submodules += len(subs)
        
    if len(pillars) < 5:
        print(f"ERROR: Expected at least 5 pillars, found {len(pillars)}")
        sys.exit(1)
        
    if total_submodules < 50:
        print(f"ERROR: Expected >= 50 total submodules, found {total_submodules}")
        sys.exit(1)
        
    print(f"CURRICULUM_DB_VERIFIED: 19 CLASSES, 5 PILLARS, {total_submodules} SUBMODULES")

if __name__ == "__main__":
    verify_db()
