import json
import re
import glob
from pathlib import Path

def sanitize_text(text):
    if not isinstance(text, str):
        return text
    
    # 1. Replace $\rightarrow$ and \rightarrow used in text with Unicode arrow →
    # When $\rightarrow$ is standalone:
    text = re.sub(r'\$\s*\\rightarrow\s*\$', '→', text)
    # When \rightarrow is inside words or bullets without proper math:
    text = re.sub(r'\\rightarrow', '→', text)
    
    # 2. Escape literal currency dollar signs ($ followed by digit or number)
    # e.g., $100 -> \$100, $50 -> \$50, $5/t -> \$5/t, $1,000,000 -> \$1,000,000, $1.25 -> \$1.25, $100M -> \$100M
    # Avoid double escaping
    text = re.sub(r'(?<!\\)\$([0-9]+[a-zA-Z0-9,\.\-/]*)', r'\\$\1', text)
    
    # 3. Clean up any weird spaces like double commas or space before punctuation
    text = re.sub(r'\s+([,\.;:\?!])', r'\1', text)
    text = re.sub(r',,+', ',', text)
    
    # 4. Fix any accidental "$\text{Impact} = ...$" where \rightarrow was replaced
    # Ensure real formulas stay valid
    text = text.replace(r'$\rightarrow$', '→')
    
    return text

def sanitize_obj(obj):
    if isinstance(obj, str):
        return sanitize_text(obj)
    elif isinstance(obj, list):
        return [sanitize_obj(x) for x in obj]
    elif isinstance(obj, dict):
        return {k: sanitize_obj(v) for k, v in obj.items()}
    return obj

# 1. Sanitize curriculum_database.json
db_path = Path("Study_Material/curriculum_database.json")
with open(db_path, "r", encoding="utf-8") as f:
    db = json.load(f)

print("Sanitizing curriculum_database.json...")
db = sanitize_obj(db)

with open(db_path, "w", encoding="utf-8") as f:
    json.dump(db, f, indent=2)
print("Saved sanitized curriculum_database.json")

# 2. Sanitize all cards_class_*.json and class_XX_slides.json
json_files = glob.glob("Study_Material/cards_class_*.json")
json_files.extend(glob.glob("Study_Material/class_*_cards.json"))
json_files.extend(glob.glob("Study_Material/class_*_slides.json"))

for jf in json_files:
    p = Path(jf)
    with open(p, "r", encoding="utf-8") as f:
        data = json.load(f)
    print(f"Sanitizing {p.name}...")
    data = sanitize_obj(data)
    with open(p, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

print("All JSON database files sanitized successfully!")
