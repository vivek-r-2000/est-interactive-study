#!/usr/bin/env python3
"""
Assemble Master Question Bank for Classes 11–19
Combines all slide-grounded, verified questions from the modular class scripts,
updates endsem_question_bank.json, curriculum_database.json,
and generates the comprehensive ENDSEM_QUESTION_BANK_AND_ANSWERS.md.
"""

import os
import sys
import json
import re

# Add scripts directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def load_class_questions(cid):
    grounded_mod = f"grounded_class_{cid}"
    try:
        mod = __import__(grounded_mod)
        func = getattr(mod, f"get_class{cid}_grounded_questions", None)
        if func:
            qs = func()
            print(f"Loaded Class {cid} from {grounded_mod} ({len(qs)} questions)")
            return qs
    except Exception as e:
        print(f"Note: {grounded_mod} not ready ({e}), falling back to accurate_qb scripts...")

    # Fallbacks
    if cid == 11:
        from accurate_qb_class11 import get_class11_questions
        return get_class11_questions()
    elif cid in (12, 13):
        import accurate_qb_class12_13 as m
        return getattr(m, f"get_class{cid}_questions")()
    elif cid in (14, 15):
        import accurate_qb_class14_15 as m
        return getattr(m, f"get_class{cid}_questions")()
    elif cid in (16, 17):
        import accurate_qb_class16_17 as m
        return getattr(m, f"get_class{cid}_questions")()
    elif cid in (18, 19):
        import accurate_qb_class18_19 as m
        return getattr(m, f"get_class{cid}_questions")()
    return []

def assemble_all():
    all_questions = []
    for cid in range(11, 20):
        c_qs = load_class_questions(cid)
        all_questions.extend(c_qs)

    print(f"Total questions gathered: {len(all_questions)}")

    # Ensure IDs are unique
    seen_ids = set()
    for q in all_questions:
        if q["id"] in seen_ids:
            raise ValueError(f"Duplicate ID detected: {q['id']}")
        seen_ids.add(q["id"])

    categories = [
        "MCQ & Objective",
        "Acronyms & Expansions",
        "Match the Following",
        "Short Answer & Definitions",
        "Differentiate Between",
        "Descriptive & Case Study"
    ]

    qb_data = {
        "metadata": {
            "title": "EST Endsem Master Question Bank & Answer Suite (Lectures 11–19)",
            "total_questions": len(all_questions),
            "syllabus": "Classes 11–19 (Environmental Science & Technology)",
            "analyzed_papers": 14,
            "classes_covered": [11, 12, 13, 14, 15, 16, 17, 18, 19],
            "categories": categories
        },
        "questions": all_questions
    }

    # 1. Write endsem_question_bank.json
    out_json_path = os.path.join("Study_Material", "endsem_question_bank.json")
    with open(out_json_path, "w", encoding="utf-8") as f:
        json.dump(qb_data, f, indent=2, ensure_ascii=False)
    print(f"Wrote {out_json_path} successfully ({len(all_questions)} questions).")

    # 2. Update curriculum_database.json
    db_path = os.path.join("Study_Material", "curriculum_database.json")
    if os.path.exists(db_path):
        with open(db_path, "r", encoding="utf-8") as f:
            curriculum_db = json.load(f)
        curriculum_db["endsem_question_bank"] = qb_data
        with open(db_path, "w", encoding="utf-8") as f:
            json.dump(curriculum_db, f, indent=2, ensure_ascii=False)
        print(f"Updated {db_path} with master question bank.")

    # 3. Generate Markdown Document
    md_path = os.path.join("Study_Material", "ENDSEM_QUESTION_BANK_AND_ANSWERS.md")
    generate_markdown(qb_data, md_path)
    print(f"Generated {md_path} successfully.")

def clean_html_for_md(html_str):
    """Convert simple HTML tags into clean Markdown formatting."""
    if not html_str:
        return ""
    s = html_str
    # Replace headers
    s = re.sub(r'<h4>(.*?)</h4>', r'#### \1\n', s)
    s = re.sub(r'<h5>(.*?)</h5>', r'##### \1\n', s)
    # Replace paragraphs
    s = re.sub(r'<p>(.*?)</p>', r'\1\n\n', s, flags=re.DOTALL)
    # Replace unordered lists and items
    s = re.sub(r'<ul>(.*?)</ul>', r'\1\n', s, flags=re.DOTALL)
    s = re.sub(r'<ol>(.*?)</ol>', r'\1\n', s, flags=re.DOTALL)
    s = re.sub(r'<li>(.*?)</li>', r'- \1\n', s, flags=re.DOTALL)
    # Replace bold & italics
    s = re.sub(r'<strong>(.*?)</strong>', r'**\1**', s)
    s = re.sub(r'<b>(.*?)</b>', r'**\1**', s)
    s = re.sub(r'<em>(.*?)</em>', r'*\1*', s)
    s = re.sub(r'<i>(.*?)</i>', r'*\1*', s)
    # Replace formula box
    s = re.sub(r'<div class="formula-box">(.*?)</div>', r'\n\1\n', s, flags=re.DOTALL)
    # Replace generic divs
    s = re.sub(r'<div[^>]*>', r'', s)
    s = re.sub(r'</div>', r'\n', s)
    # Tables
    s = re.sub(r'<table[^>]*>', r'\n', s)
    s = re.sub(r'</table>', r'\n', s)
    s = re.sub(r'<thead>.*?</thead>', r'', s, flags=re.DOTALL)
    s = re.sub(r'<tbody>', r'', s)
    s = re.sub(r'</tbody>', r'', s)
    s = re.sub(r'<tr>(.*?)</tr>', r'\1\n', s, flags=re.DOTALL)
    s = re.sub(r'<th>(.*?)</th>', r'| **\1** ', s)
    s = re.sub(r'<td>(.*?)</td>', r'| \1 ', s)
    # Clean up empty lines
    s = re.sub(r'\n{3,}', '\n\n', s)
    return s.strip()

def generate_markdown(qb_data, out_path):
    qs = qb_data["questions"]
    lines = []
    lines.append("# Environmental Science & Technology (ES1.101)")
    lines.append("## Master Endsem Question Bank & Answer Suite (Lectures 11–19)")
    lines.append("")
    lines.append("> **Coverage:** Verified against all 14 past exam papers (2018–2024).")
    lines.append(f"> **Total Questions:** {len(qs)}")
    lines.append("> **Structure:** Every question features two separate sections: **Key Points** and **Detailed Answer**.")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Table of contents by Class
    lines.append("### Table of Contents by Class")
    for cid in range(11, 20):
        c_qs = [q for q in qs if q["class_id"] == cid]
        if c_qs:
            c_name = c_qs[0]["class_name"]
            lines.append(f"- **Class {cid}: {c_name}** ({len(c_qs)} questions)")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Questions grouped by Class
    for cid in range(11, 20):
        c_qs = [q for q in qs if q["class_id"] == cid]
        if not c_qs:
            continue
        c_name = c_qs[0]["class_name"]
        lines.append(f"## Class {cid}: {c_name}")
        lines.append("")

        for q in c_qs:
            lines.append(f"### [{q['id']}] {q['prompt']}")
            lines.append("")
            lines.append(f"- **Topic:** {q['topic']}")
            lines.append(f"- **Category:** `{q['category']}`")
            lines.append(f"- **Marks / Importance:** {q['marks']} | {q['importance']}")
            
            exam_str = ", ".join([f"{e['paper']} ({e['section']})" for e in q["exams"]])
            lines.append(f"- **Exam Appearances:** {exam_str}")
            lines.append("")
            
            # Key Points
            lines.append("#### Key Points")
            lines.append(clean_html_for_md(q["key_answer_points"]))
            lines.append("")
            
            # Detailed Answer
            lines.append("#### Detailed Answer")
            lines.append(clean_html_for_md(q["detailed_answer"]))
            lines.append("")
            lines.append("---")
            lines.append("")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

if __name__ == "__main__":
    assemble_all()
