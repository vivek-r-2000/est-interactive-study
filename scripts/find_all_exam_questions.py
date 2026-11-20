import os
import glob
import re

search_terms = [
    "diamond", "diamonds", "aether", "novacem", "portland", "cement", "blue carbon", "mangrove", "mangroves",
    "seaweed", "cattle", "enteric", "methane", "cows", "climeworks", "direct air capture", "dac",
    "wild me", "trase", "vertical farm", "aerofarms", "biochar", "pyrolysis", "weathering", "flettner",
    "cloud brightening", "trap cropping", "marigold", "xprize", "hydrogen ship", "tree corridors", "floating solar"
]

files = glob.glob("Previous_Exam_Papers/extracted_questions/*.txt")
print(f"Total files: {len(files)}")

matches = []

for fpath in files:
    fname = os.path.basename(fpath)
    if fname == "ALL_PREVIOUS_EXAM_QUESTIONS.txt":
        continue
    with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()
        
    for i, line in enumerate(lines):
        line_lower = line.lower()
        for term in search_terms:
            if term in line_lower:
                snippet = "".join(lines[max(0, i-2):min(len(lines), i+4)]).strip()
                matches.append({
                    "file": fname,
                    "term": term,
                    "line_num": i+1,
                    "snippet": snippet
                })
                break

print(f"Total matches found: {len(matches)}")
for m in matches:
    print(f"\n--- [{m['file']}] Term: '{m['term']}' (Line {m['line_num']}) ---")
    print(m['snippet'])
