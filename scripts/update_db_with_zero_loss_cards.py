import json

with open("Study_Material/class_11_cards.json", "r", encoding="utf-8") as f:
    cards = json.load(f)

with open("Study_Material/curriculum_database.json", "r", encoding="utf-8") as f:
    db = json.load(f)

for c in db["classes"]:
    if c["class_id"] == 11:
        c["topic_cards"] = cards
        print("Updated class 11 topic_cards in curriculum_database.json")
        break

with open("Study_Material/curriculum_database.json", "w", encoding="utf-8") as f:
    json.dump(db, f, indent=2)

print("Saved updated curriculum_database.json")
