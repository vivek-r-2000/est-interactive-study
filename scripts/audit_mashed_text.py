import json
import re

db = json.load(open("Study_Material/curriculum_database.json", "r", encoding="utf-8"))
classes = db.get("classes", [])

print("=== AUDITING CLASSES 11-19 FOR TEXT ANOMALIES & DELIMITERS ===")

def find_mashed_words(text):
    if not isinstance(text, str):
        return []
    clean = re.sub(r'<[^>]+>', ' ', text)
    clean = re.sub(r'https?://\S+', '', clean)
    clean = re.sub(r'\\\(.*?\\\)', '', clean)
    clean = re.sub(r'\$\$.*?\$\$', '', clean)
    
    words = clean.split()
    mashed = []
    for w in words:
        # Check words longer than 28 chars without hyphens, slashes, or underscores
        if len(w) > 28 and '-' not in w and '/' not in w and '_' not in w:
            mashed.append(w)
    return mashed

total_anomalies = 0
for idx, c in enumerate(classes):
    title = c.get("title", "")
    # Check if this class is 11-19
    match = re.search(r'Class\s*(\d+)', title)
    if not match:
        continue
    cid = int(match.group(1))
    if cid < 11 or cid > 19:
        continue
        
    print(f"\n--- Checking Class {cid}: {title} ---")
    
    # 1. Topic Cards
    cards = c.get("topic_cards", [])
    print(f"  Topic Cards: {len(cards)}")
    for c_idx, card in enumerate(cards):
        card_text = json.dumps(card, ensure_ascii=False)
        mashed = find_mashed_words(card_text)
        if mashed:
            print(f"    [Card {c_idx+1}] Potential mashed words: {mashed}")
            total_anomalies += 1
            
        open_math = len(re.findall(r'\\\(', card_text))
        close_math = len(re.findall(r'\\\)', card_text))
        if open_math != close_math:
            print(f"    [Card {c_idx+1}] Math delimiter mismatch: \\( count = {open_math}, \\) count = {close_math}")
            total_anomalies += 1

    # 2. Individual Slides
    slides = c.get("slides", [])
    print(f"  Individual Slides: {len(slides)}")
    for s_idx, slide in enumerate(slides):
        slide_text = json.dumps(slide, ensure_ascii=False)
        mashed = find_mashed_words(slide_text)
        if mashed:
            print(f"    [Slide {s_idx+1}] Potential mashed words: {mashed}")
            total_anomalies += 1
            
        open_math = len(re.findall(r'\\\(', slide_text))
        close_math = len(re.findall(r'\\\)', slide_text))
        if open_math != close_math:
            print(f"    [Slide {s_idx+1}] Math delimiter mismatch: \\( count = {open_math}, \\) count = {close_math}")
            total_anomalies += 1

print(f"\nAudit complete. Total anomaly flags: {total_anomalies}")
