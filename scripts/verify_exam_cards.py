import json
import sys
from pathlib import Path

def test_exam_cards():
    db_path = Path("Study_Material/curriculum_database.json")
    if not db_path.exists():
        print("FAIL: curriculum_database.json missing")
        sys.exit(1)
        
    with open(db_path, "r", encoding="utf-8") as f:
        db = json.load(f)
        
    c11 = next((c for c in db.get("classes", []) if c.get("class_id") == 11), None)
    if not c11:
        print("FAIL: class 11 missing")
        sys.exit(1)
        
    topic_cards = c11.get("topic_cards", [])
    if len(topic_cards) != 14:
        print(f"FAIL: expected 14 zero-loss topic cards, found {len(topic_cards)}")
        sys.exit(1)
        
    covered_slides = set()
    for tc in topic_cards:
        assert "card_num" in tc, "Card missing card_num"
        assert "title" in tc, "Card missing title"
        assert "slides_covered" in tc, "Card missing slides_covered"
        assert "exam_rating" in tc, "Card missing exam_rating"
        assert "tier" in tc["exam_rating"], "Card exam_rating missing tier"
        assert "stars" in tc["exam_rating"], "Card exam_rating missing stars"
        assert "frequency_count" in tc["exam_rating"], "Card exam_rating missing frequency_count"
        assert "recent_papers" in tc["exam_rating"], "Card exam_rating missing recent_papers"
        assert "exam_tip" in tc["exam_rating"], "Card exam_rating missing exam_tip"
        assert "eli15_takeaway" in tc, "Card missing eli15_takeaway"
        assert "key_facts" in tc, "Card missing key_facts"
        assert len(tc["key_facts"]) >= 4, f"Card {tc['card_num']} has insufficient key facts ({len(tc['key_facts'])})"
        assert "checkpoint" in tc, "Card missing checkpoint"
        assert "exam_questions" in tc, f"Card {tc['card_num']} missing exam_questions"
        assert len(tc["exam_questions"]) >= 2, f"Card {tc['card_num']} has insufficient exam questions ({len(tc['exam_questions'])})"
        for eq in tc["exam_questions"]:
            assert "paper" in eq, "Exam question missing paper"
            assert "section" in eq, "Exam question missing section"
            assert "marks" in eq, "Exam question missing marks"
            assert "question" in eq, "Exam question missing question"
            assert "answer_guideline" in eq, "Exam question missing answer_guideline"
        
        for s in tc["slides_covered"]:
            if isinstance(s, int):
                covered_slides.add(s)

    all_expected = set(range(1, 30))
    missing = all_expected - covered_slides
    if missing:
        print(f"FAIL: Missing slides: {missing}")
        sys.exit(1)
        
    q_bank = Path("Previous_Exam_Papers/QUESTION_BANK_MASTER.md")
    if not q_bank.exists() or q_bank.stat().st_size < 1000:
        print("FAIL: QUESTION_BANK_MASTER.md missing or too small")
        sys.exit(1)
        
    freq_analysis = Path("Previous_Exam_Papers/class_11_exam_frequency_analysis.json")
    if not freq_analysis.exists():
        print("FAIL: class_11_exam_frequency_analysis.json missing")
        sys.exit(1)

    print("EXAM_CARDS_VERIFIED: 14_ZERO_LOSS_TOPIC_CARDS_MAPPED_TO_PAST_EXAMS")
    sys.exit(0)

if __name__ == "__main__":
    test_exam_cards()
