import json
import os
import sys

EXPECTED_COUNTS = {
    12: 32,
    13: 15,
    14: 35,
    15: 28,
    16: 45,
    17: 36,
    18: 25,
    19: 16
}

BANNED_WORDS = [
    "delve", "foster", "leverage", "utilize", "facilitate", "empower", 
    "streamline", "robust", "cutting-edge", "paradigm shift", "game changer", 
    "tapestry", "realm", "beacon", "multifaceted", "meticulous", "intricate", 
    "paramount", "transformative"
]

def verify_all_classes():
    sm_dir = "Study_Material"
    missing = []
    failed = []
    
    total_slides_verified = 0
    for cid, expected_count in EXPECTED_COUNTS.items():
        fname = os.path.join(sm_dir, f"class_{cid}_slides.json")
        if not os.path.exists(fname):
            missing.append(f"Class {cid} ({fname})")
            continue
            
        with open(fname, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except Exception as e:
                failed.append(f"Class {cid}: JSON parse error: {e}")
                continue
                
        slides = data.get("slides", [])
        if len(slides) != expected_count:
            failed.append(f"Class {cid}: Expected {expected_count} slides, found {len(slides)}")
            continue
            
        for s in slides:
            num = s.get("slide_num")
            for field in ["title", "act", "continuity_bridge", "eli15_takeaway", "mental_model"]:
                val = s.get(field, "")
                if not val or len(val.strip()) < 5:
                    failed.append(f"Class {cid} Slide {num}: Missing or empty '{field}'")
                    break
                    
            facts = s.get("key_facts", [])
            if len(facts) < 2:
                failed.append(f"Class {cid} Slide {num}: Insufficient key_facts (<2)")
                break
                
            cp = s.get("checkpoint", {})
            if not cp.get("question") or len(cp.get("options", [])) < 3 or not cp.get("explanation"):
                failed.append(f"Class {cid} Slide {num}: Invalid checkpoint")
                break
                
            # Slop check
            text = " ".join([
                s.get("title", ""),
                s.get("continuity_bridge", ""),
                s.get("eli15_takeaway", ""),
                " ".join(facts),
                s.get("mental_model", ""),
                cp.get("question", ""),
                cp.get("explanation", "")
            ]).lower()
            
            for bw in BANNED_WORDS:
                if f" {bw} " in f" {text} ":
                    failed.append(f"Class {cid} Slide {num}: Contains banned slop word '{bw}'")
                    break
                    
        total_slides_verified += len(slides)
        
    if missing or failed:
        if missing:
            print("MISSING FILES:", ", ".join(missing))
        if failed:
            print("FAILURES:\n" + "\n".join(failed[:10]))
        sys.exit(1)
        
    print(f"CLASSES_12_TO_19_VERIFIED: ALL_8_CLASSES_MET_WITH_{total_slides_verified}_SLIDES")

if __name__ == "__main__":
    verify_all_classes()
