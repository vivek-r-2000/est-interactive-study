import json
import re
import glob
from pathlib import Path

def convert_math_in_str(s):
    if not isinstance(s, str):
        return s
    
    # 1. First, make sure currency like \$100 or $100 is NOT matched as $math$
    # We can protect currency by replacing with a temporary token
    # Matches like $100, $20, $5/t, $1,000,000, $1.25, $100M
    currency_matches = []
    def save_curr(m):
        currency_matches.append(m.group(0))
        return f"__CURR_TOKEN_{len(currency_matches)-1}__"
    
    # Save currency
    s = re.sub(r'(?:\\\$|\$)[0-9]+[a-zA-Z0-9,\.\-/]*(?:\s*(?:per|tCO2|M|billion|million|Cr|ha|yr|t|board-foot))?', save_curr, s)
    
    # 2. Replace any standalone $\rightarrow$ with Unicode →
    s = re.sub(r'\$\s*\\rightarrow\s*\$', '→', s)
    s = re.sub(r'\\rightarrow', '→', s)
    
    # 3. Now find all genuine $...$ math spans
    def repl_math(m):
        inner = m.group(1).strip()
        # If inner starts with $$ it is display math, leave as $$
        if inner.startswith('$') or inner.endswith('$'):
            return m.group(0)
        return f"\\({inner}\\)"

    s = re.sub(r'\$([^\$\n]{1,300}?)\$', repl_math, s)
    
    # 4. Restore currency as clean plain text "$..."
    for i, curr in enumerate(currency_matches):
        clean_curr = curr.replace(r'\$', '$') # clean $
        s = s.replace(f"__CURR_TOKEN_{i}__", clean_curr)
        
    return s

def convert_obj(obj):
    if isinstance(obj, str):
        return convert_math_in_str(obj)
    elif isinstance(obj, list):
        return [convert_obj(x) for x in obj]
    elif isinstance(obj, dict):
        return {k: convert_obj(v) for k, v in obj.items()}
    return obj

# Process curriculum_database.json
db_path = Path("Study_Material/curriculum_database.json")
with open(db_path, "r", encoding="utf-8") as f:
    db = json.load(f)

print("Converting math delimiters in curriculum_database.json...")
db = convert_obj(db)

with open(db_path, "w", encoding="utf-8") as f:
    json.dump(db, f, indent=2)

# Process all cards and slides files
files = glob.glob("Study_Material/cards_class_*.json")
files.extend(glob.glob("Study_Material/class_*_cards.json"))
files.extend(glob.glob("Study_Material/class_*_slides.json"))

for f in files:
    p = Path(f)
    with open(p, "r", encoding="utf-8") as fp:
        data = json.load(fp)
    print(f"Converting math delimiters in {p.name}...")
    data = convert_obj(data)
    with open(p, "w", encoding="utf-8") as fp:
        json.dump(data, fp, indent=2)

print("Conversion complete!")
