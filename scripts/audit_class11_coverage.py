import json
import pypdf

# 1. Read the original PDF text per slide
pdf_path = "Lecture_Slides/Class-11-Climate Change-Technology Solutions.pdf"
reader = pypdf.PdfReader(pdf_path)
pdf_slides = {}
for i, page in enumerate(reader.pages):
    pdf_slides[i + 1] = page.extract_text().strip()

print(f"Total PDF pages: {len(pdf_slides)}")

# 2. Read the curriculum database
with open("Study_Material/curriculum_database.json", "r", encoding="utf-8") as f:
    db = json.load(f)

c11 = next(c for c in db["classes"] if c["class_id"] == 11)
submodules = c11.get("submodules", [])
topic_cards = c11.get("topic_cards", [])

print(f"Total submodules (slides): {len(submodules)}")
print(f"Total topic cards: {len(topic_cards)}")

# Check slide numbers mapping in topic_cards
covered_in_cards = set()
for tc in topic_cards:
    for s in tc["slides_covered"]:
        covered_in_cards.add(s)

all_slides = set(range(1, len(pdf_slides) + 1))
missing = all_slides - covered_in_cards
print(f"Missing slide numbers: {missing}")

# Check content details in topic cards vs submodules/pdf
print("\n--- Card Coverage Audit ---")
for tc in topic_cards:
    print(f"\nCard {tc['card_num']}: {tc['title']} (Slides: {tc['slides_covered']})")
    # check how much detail each card has
    facts_count = len(tc.get("key_facts", []))
    print(f"  Key facts count: {facts_count}")
    # print the slides text snippet
    for s in tc["slides_covered"]:
        pdf_text = pdf_slides.get(s, "").replace("\n", " ")[:100]
        print(f"    Slide {s} raw: {pdf_text}")
