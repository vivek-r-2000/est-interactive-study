import json
import os
import sys

def verify_case_studies():
    db_path = os.path.join("Study_Material", "curriculum_database.json")
    if not os.path.exists(db_path):
        print("ERROR: curriculum_database.json not found")
        sys.exit(1)
        
    with open(db_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    cases = data.get("case_studies", [])
    if len(cases) < 12:
        print(f"ERROR: Expected >= 12 case studies, found {len(cases)}")
        sys.exit(1)
        
    required_keywords = [
        "2070", "Easter Island", "Baltic", "Bhopal", "Chernobyl", 
        "Minamata", "Smog", "Aral Sea", "Love Canal", "Movements", 
        "Kalundborg", "Ramsar"
    ]
    
    case_names = " ".join([c.get("name", "") + " " + c.get("id", "") for c in cases])
    for kw in required_keywords:
        if kw.lower() not in case_names.lower():
            print(f"ERROR: Missing expected case study containing '{kw}'")
            sys.exit(1)
            
    for c in cases:
        if not c.get("what_happened") or not c.get("root_cause") or not c.get("takeaway"):
            print(f"ERROR: Case study {c.get('name')} missing required 3-part fields")
            sys.exit(1)
            
    print(f"CASE_STUDIES_VERIFIED: {len(cases)}_MAJOR_INCIDENTS_MAPPED")

if __name__ == "__main__":
    verify_case_studies()
