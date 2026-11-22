import json
import os
from qb_class11 import class_11_questions
from qb_class12 import class_12_questions
from qb_class13 import class_13_questions
from qb_class14 import class_14_questions
from qb_class15 import class_15_questions
from qb_class16 import class_16_questions
from qb_class17 import class_17_questions
from qb_class18 import class_18_questions
from qb_class19 import class_19_questions

def assemble_qb():
    all_questions = (
        class_11_questions +
        class_12_questions +
        class_13_questions +
        class_14_questions +
        class_15_questions +
        class_16_questions +
        class_17_questions +
        class_18_questions +
        class_19_questions
    )

    print(f"Total questions assembled: {len(all_questions)}")
    for cid in range(11, 20):
        c_qs = [q for q in all_questions if q["class_id"] == cid]
        print(f"Class {cid}: {len(c_qs)} questions")

    # 1. Save JSON
    out_json = "Study_Material/endsem_question_bank.json"
    qb_data = {
        "metadata": {
            "title": "EST Endsem Master Question Bank & Answer Suite (Lectures 11–19)",
            "total_questions": len(all_questions),
            "syllabus": "Classes 11–19 (Environmental Science & Technology)",
            "analyzed_papers": 14,
            "classes_covered": [11, 12, 13, 14, 15, 16, 17, 18, 19]
        },
        "questions": all_questions
    }

    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(qb_data, f, indent=2, ensure_ascii=False)
    print(f"[+] Saved {out_json}")

    # 2. Update curriculum_database.json
    db_path = "Study_Material/curriculum_database.json"
    with open(db_path, "r", encoding="utf-8") as f:
        db = json.load(f)

    db["endsem_question_bank"] = qb_data
    with open(db_path, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)
    print(f"[+] Injected endsem_question_bank into {db_path}")

    # 3. Generate Markdown Study Guide
    out_md = "Study_Material/ENDSEM_QUESTION_BANK_AND_ANSWERS.md"
    with open(out_md, "w", encoding="utf-8") as f:
        f.write("# Environmental Science & Technology (ES1.101)\n")
        f.write("## Endsem Question Bank & Model Answers Suite (Lectures 11–19)\n\n")
        f.write("> **Comprehensive exam preparation pack synthesized from 14 previous exam papers (2018–2024 End-Sems, Mid-Sems & Quizzes).**\n")
        f.write("> For each question, two sections are provided: **Key Answer Points** (for rapid recall) and **Detailed Answer & Context** (with scientific mechanisms, equations, and case studies).\n\n")
        f.write("---\n\n")

        current_class = None
        for q in all_questions:
            if q["class_id"] != current_class:
                current_class = q["class_id"]
                f.write(f"\n# Class {current_class}: {q['class_name']}\n\n")

            exams_str = ", ".join([f"**{e['paper']}** ({e['section']}, {e['marks']})" for e in q["exams"]])
            f.write(f"### [{q['id']}] {q['topic']}\n")
            f.write(f"- **Category:** `{q['category']}` | **Importance:** {q['importance']} | **Marks:** `{q['marks']}`\n")
            f.write(f"- **Exam Appearances:** {exams_str}\n\n")
            f.write(f"**Question:**\n> *{q['prompt']}*\n\n")

            f.write("#### 🔑 Section 1: Key Answer Points\n")
            # Convert simple HTML bullet points to markdown if needed or write cleanly
            clean_key = q["key_answer_points"].replace("<ul>", "").replace("</ul>", "").replace("<li>", "- ").replace("</li>", "\n").replace("<br>", "\n  ").strip()
            clean_key = clean_key.replace("<strong>", "**").replace("</strong>", "**").replace("<em>", "*").replace("</em>", "*")
            f.write(clean_key + "\n\n")

            f.write("#### 📖 Section 2: Detailed Answer with All Relevant Context\n")
            clean_det = q["detailed_answer"].replace('<div class="detailed-body">', '').replace('</div>', '')
            clean_det = clean_det.replace('<div class="formula-box">', '\n\n').replace('</div>', '\n\n')
            clean_det = clean_det.replace("<h4>", "\n##### ").replace("</h4>", "\n")
            clean_det = clean_det.replace("<p>", "\n").replace("</p>", "\n")
            clean_det = clean_det.replace("<strong>", "**").replace("</strong>", "**").replace("<em>", "*").replace("</em>", "*")
            clean_det = clean_det.replace("<ul>", "").replace("</ul>", "").replace("<li>", "- ").replace("</li>", "\n")
            clean_det = clean_det.replace("<ol>", "").replace("</ol>", "").replace("<li>", "1. ").replace("</li>", "\n")
            f.write(clean_det.strip() + "\n\n")
            f.write("---\n\n")

    print(f"[+] Generated markdown study guide: {out_md}")

if __name__ == "__main__":
    assemble_qb()
