import json
import os
import sys

def verify_pedagogy():
    db_path = os.path.join("Study_Material", "curriculum_database.json")
    if not os.path.exists(db_path):
        print("ERROR: curriculum_database.json not found")
        sys.exit(1)
        
    with open(db_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    classes = data.get("classes", [])
    total_checkpoints = 0
    for c in classes:
        for s in c.get("submodules", []):
            if not s.get("eli15_takeaway"):
                print(f"ERROR: Missing eli15_takeaway in {s.get('id')}")
                sys.exit(1)
            if len(s.get("bullets", [])) < 2:
                print(f"ERROR: Insufficient bullets in {s.get('id')}")
                sys.exit(1)
            if not s.get("mental_model") and not s.get("diagram"):
                print(f"ERROR: Missing mental_model/diagram in {s.get('id')}")
                sys.exit(1)
            cp = s.get("checkpoint")
            if not cp or not cp.get("question") or len(cp.get("options", [])) < 3 or not cp.get("explanation"):
                print(f"ERROR: Invalid checkpoint in {s.get('id')}")
                sys.exit(1)
            total_checkpoints += 1
            
    print(f"PEDAGOGY_VERIFIED: {total_checkpoints} MICRO_LEARNING_CHECKPOINTS_ACTIVE")

if __name__ == "__main__":
    verify_pedagogy()
