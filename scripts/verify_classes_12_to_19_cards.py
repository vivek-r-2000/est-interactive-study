import json
import sys
from pathlib import Path

expected_slides = {
    11: 29,
    12: 32,
    13: 15,
    14: 35,
    15: 28,
    16: 45,
    17: 36,
    18: 25,
    19: 16
}

def verify_all_topic_cards():
    db_path = Path("Study_Material/curriculum_database.json")
    if not db_path.exists():
        print("FAIL: curriculum_database.json missing")
        sys.exit(1)

    with open(db_path, "r", encoding="utf-8") as f:
        db = json.load(f)

    total_cards = 0
    total_questions = 0

    for cid, exp_count in expected_slides.items():
        c = next((cl for cl in db["classes"] if cl["class_id"] == cid), None)
        if not c:
            print(f"FAIL: Class {cid} not found in database")
            sys.exit(1)

        topic_cards = c.get("topic_cards", [])
        if not topic_cards:
            print(f"FAIL: Class {cid} has no topic_cards")
            sys.exit(1)

        total_cards += len(topic_cards)
        covered_slides = set()

        for card in topic_cards:
            assert "card_num" in card, f"Class {cid} card missing card_num"
            assert "title" in card, f"Class {cid} card missing title"
            assert "act" in card, f"Class {cid} card missing act"
            assert "slides_covered" in card, f"Class {cid} card missing slides_covered"
            assert "slides_label" in card, f"Class {cid} card missing slides_label"
            assert "exam_rating" in card, f"Class {cid} card missing exam_rating"
            assert "tier" in card["exam_rating"], f"Class {cid} card exam_rating missing tier"
            assert "stars" in card["exam_rating"], f"Class {cid} card exam_rating missing stars"
            assert "badge_class" in card["exam_rating"], f"Class {cid} card exam_rating missing badge_class"
            assert "frequency_count" in card["exam_rating"], f"Class {cid} card exam_rating missing frequency_count"
            assert "recent_papers" in card["exam_rating"], f"Class {cid} card exam_rating missing recent_papers"
            assert "exam_tip" in card["exam_rating"], f"Class {cid} card exam_rating missing exam_tip"
            assert "eli15_takeaway" in card, f"Class {cid} card missing eli15_takeaway"
            assert "key_facts" in card and len(card["key_facts"]) >= 3, f"Class {cid} card {card['card_num']} has insufficient key facts"
            assert "mental_model" in card, f"Class {cid} card missing mental_model"
            assert "checkpoint" in card, f"Class {cid} card missing checkpoint"
            
            # Exam questions assertions
            assert "exam_questions" in card, f"Class {cid} card {card['card_num']} missing exam_questions"
            assert len(card["exam_questions"]) >= 2, f"Class {cid} card {card['card_num']} has < 2 exam questions ({len(card['exam_questions'])})"
            total_questions += len(card["exam_questions"])

            for eq in card["exam_questions"]:
                assert "paper" in eq, f"Class {cid} question missing paper"
                assert "section" in eq, f"Class {cid} question missing section"
                assert "marks" in eq, f"Class {cid} question missing marks"
                assert "question" in eq, f"Class {cid} question missing question"
                assert "answer_guideline" in eq, f"Class {cid} question missing answer_guideline"

            for s in card["slides_covered"]:
                if isinstance(s, int):
                    covered_slides.add(s)

        expected_set = set(range(1, exp_count + 1))
        missing = expected_set - covered_slides
        if missing:
            print(f"FAIL: Class {cid} missing slides: {missing}")
            sys.exit(1)

        print(f"PASS: Class {cid} ({exp_count} slides -> {len(topic_cards)} cards, {len(covered_slides)} slides covered, {sum(len(tc['exam_questions']) for tc in topic_cards)} exam questions)")

    print(f"\nALL_CLASSES_11_TO_19_VERIFIED: {total_cards} TOPIC CARDS, 261 SLIDES COVERED, {total_questions} EXAM QUESTIONS ATTACHED")
    sys.exit(0)

if __name__ == "__main__":
    verify_all_topic_cards()
