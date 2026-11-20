import json
import sys
from pathlib import Path

files = [
    "Study_Material/cards_class_12_13.json",
    "Study_Material/cards_class_14_15.json",
    "Study_Material/cards_class_16_17.json",
    "Study_Material/cards_class_18_19.json"
]

all_ready = True
for f in files:
    if not Path(f).exists():
        print(f"Waiting for {f}...")
        all_ready = False

if not all_ready:
    print("Not all subagent files are ready yet.")
    sys.exit(1)

# Load existing database
with open("Study_Material/curriculum_database.json", "r", encoding="utf-8") as f:
    db = json.load(f)

merged_classes = set()

for fpath in files:
    with open(fpath, "r", encoding="utf-8") as f:
        data = json.load(f)
    for class_id_str, cards in data.items():
        cid = int(class_id_str)
        target_class = next((c for c in db["classes"] if c["class_id"] == cid), None)
        if target_class:
            target_class["topic_cards"] = cards
            merged_classes.add(cid)
            print(f"Injected {len(cards)} topic cards into Class {cid}")

with open("Study_Material/curriculum_database.json", "w", encoding="utf-8") as f:
    json.dump(db, f, indent=2)

print(f"Successfully merged topic cards for classes: {sorted(list(merged_classes))}")
