import json
import os
import sys

def verify_class11():
    db_path = os.path.join("Study_Material", "curriculum_database.json")
    if not os.path.exists(db_path):
        print("ERROR: curriculum_database.json not found")
        sys.exit(1)
        
    with open(db_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    c11 = None
    for c in data.get("classes", []):
        if c.get("class_id") == 11:
            c11 = c
            break
            
    if not c11:
        print("ERROR: Class 11 not found in database")
        sys.exit(1)
        
    slides = c11.get("slides", [])
    if len(slides) != 29:
        print(f"ERROR: Expected exactly 29 slides for Class 11, found {len(slides)}")
        sys.exit(1)
        
    banned_words = [
        "delve", "foster", "leverage", "utilize", "facilitate", "empower", 
        "streamline", "robust", "cutting-edge", "paradigm shift", "game changer", 
        "tapestry", "realm", "beacon", "multifaceted", "meticulous", "intricate", 
        "paramount", "transformative"
    ]
    
    required_slide_checks = {
        1: ["Climate Change", "Technology"],
        2: ["Paris", "Afforestation"],
        3: ["Biochar", "pyrolysis"],
        4: ["Blue carbon", "mangrove"],
        5: ["Biomass", "timber"],
        6: ["alkali", "KOH"],
        7: ["weathering", "silicate"],
        8: ["Direct Air Capture", "geologic"],
        9: ["Fuels", "synthetic"],
        10: ["sorbent", "filter"],
        11: ["Bury", "basalt"],
        12: ["Gigaton", "scale"],
        13: ["scuba", "bicarbonate"],
        14: ["Climeworks", "8,000"],
        15: ["Aether", "diamond"],
        16: ["Net Zero Teesside", "North Sea"],
        17: ["beef", "60"],
        18: ["seaweed", "Zelp"],
        19: ["insect", "grasshopper"],
        20: ["cloud brightening", "Flettner"],
        21: ["Remote work", "commute"],
        22: ["datacentre", "cooling"],
        23: ["Hydrogen", "Colombia"],
        24: ["Blockchain", "DolphinGemma"],
        25: ["Vertical Farming", "indoor"],
        26: ["Four", "LED"],
        27: ["AeroFarms", "95%"],
        28: ["Trap cropping", "Marigold"],
        29: ["XPRIZE", "Elon Musk"]
    }
    
    for s in slides:
        num = s.get("slide_num")
        if not num or num < 1 or num > 29:
            print(f"ERROR: Invalid slide_num {num}")
            sys.exit(1)
            
        for field in ["title", "act", "continuity_bridge", "eli15_takeaway", "mental_model"]:
            val = s.get(field, "")
            if not val or len(val.strip()) < 5:
                print(f"ERROR: Slide {num} missing or empty '{field}'")
                sys.exit(1)
                
        facts = s.get("key_facts", [])
        if len(facts) < 2:
            print(f"ERROR: Slide {num} has fewer than 2 key_facts")
            sys.exit(1)
            
        cp = s.get("checkpoint", {})
        if not cp.get("question") or len(cp.get("options", [])) < 3 or not cp.get("explanation"):
            print(f"ERROR: Slide {num} has invalid checkpoint")
            sys.exit(1)
            
        # Check required keywords
        full_text = " ".join([
            s.get("title", ""),
            s.get("continuity_bridge", ""),
            s.get("eli15_takeaway", ""),
            " ".join(facts),
            s.get("mental_model", ""),
            cp.get("question", ""),
            cp.get("explanation", "")
        ]).lower()
        
        req_kws = required_slide_checks.get(num, [])
        for kw in req_kws:
            if kw.lower() not in full_text:
                print(f"ERROR: Slide {num} missing required concept keyword '{kw}'")
                sys.exit(1)
                
        # Unslop check
        for bw in banned_words:
            if f" {bw} " in f" {full_text} ":
                print(f"ERROR: Slide {num} contains banned AI-slop word '{bw}'")
                sys.exit(1)
                
    print("CLASS_11_VERIFIED: ALL_29_SLIDES_COVERED_WITH_NARRATIVE_CONTINUITY")

if __name__ == "__main__":
    verify_class11()
