"""Verification script for cards_class_12_13.json
Checks:
- All slide numbers 1..32 covered in Class 12 cards (zero loss).
- All slide numbers 1..15 covered in Class 13 cards (zero loss).
- Complete schema validation for every card.
- Exam ratings, checkpoints, key facts, and exam questions with answer guidelines.
"""

import json
import sys
from pathlib import Path

def verify():
    cards_path = Path("Study_Material/cards_class_12_13.json")
    if not cards_path.exists():
        print(f"FAIL: File {cards_path} not found.")
        sys.exit(1)

    with open(cards_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if "12" not in data or "13" not in data:
        print("FAIL: Root JSON must have keys '12' and '13'.")
        sys.exit(1)

    # Validate Class 12
    c12_cards = data["12"]
    print(f"Verifying Class 12: {len(c12_cards)} cards found.")
    c12_slides_covered = set()
    c12_total_questions = 0

    for idx, card in enumerate(c12_cards, start=1):
        assert card.get("card_num") == idx, f"Class 12 card {idx} card_num mismatch: {card.get('card_num')}"
        assert card.get("title"), f"Class 12 card {idx} missing title"
        assert card.get("act"), f"Class 12 card {idx} missing act"
        assert isinstance(card.get("slides_covered"), list), f"Class 12 card {idx} slides_covered not a list"
        assert card.get("slides_label"), f"Class 12 card {idx} missing slides_label"
        
        # Rating checks
        er = card.get("exam_rating")
        assert er and isinstance(er, dict), f"Class 12 card {idx} missing exam_rating"
        assert er.get("tier"), f"Class 12 card {idx} missing exam_rating.tier"
        assert isinstance(er.get("stars"), int) and er.get("stars") in [3, 4, 5], f"Class 12 card {idx} invalid stars"
        assert er.get("badge_class") in ["badge-critical", "badge-high", "badge-medium"], f"Class 12 card {idx} invalid badge_class"
        assert er.get("frequency_count"), f"Class 12 card {idx} missing frequency_count"
        assert isinstance(er.get("recent_papers"), list) and len(er["recent_papers"]) > 0, f"Class 12 card {idx} missing recent_papers"
        assert er.get("exam_tip"), f"Class 12 card {idx} missing exam_tip"

        # Pedagogical fields
        assert card.get("eli15_takeaway"), f"Class 12 card {idx} missing eli15_takeaway"
        assert isinstance(card.get("key_facts"), list) and len(card["key_facts"]) >= 3, f"Class 12 card {idx} insufficient key_facts"
        for kf in card["key_facts"]:
            assert "<strong>Slide" in kf, f"Class 12 card {idx} key fact missing Slide provenance tag: {kf[:40]}"
        assert card.get("mental_model"), f"Class 12 card {idx} missing mental_model"

        # Checkpoint checks
        cp = card.get("checkpoint")
        assert cp and isinstance(cp, dict), f"Class 12 card {idx} missing checkpoint"
        assert cp.get("question"), f"Class 12 card {idx} checkpoint missing question"
        assert isinstance(cp.get("options"), list) and len(cp["options"]) == 4, f"Class 12 card {idx} checkpoint options != 4"
        assert isinstance(cp.get("correct"), int) and cp["correct"] in [0, 1, 2, 3], f"Class 12 card {idx} checkpoint correct not in 0..3"
        assert cp.get("explanation"), f"Class 12 card {idx} checkpoint missing explanation"

        # Exam questions checks
        eqs = card.get("exam_questions")
        assert isinstance(eqs, list) and len(eqs) >= 2, f"Class 12 card {idx} exam_questions < 2"
        for qidx, eq in enumerate(eqs, start=1):
            assert eq.get("paper"), f"Class 12 card {idx} Q{qidx} missing paper"
            assert eq.get("section"), f"Class 12 card {idx} Q{qidx} missing section"
            assert eq.get("marks"), f"Class 12 card {idx} Q{qidx} missing marks"
            assert eq.get("question"), f"Class 12 card {idx} Q{qidx} missing question"
            assert eq.get("answer_guideline") and ("<ul>" in eq["answer_guideline"] or "<ol>" in eq["answer_guideline"]), f"Class 12 card {idx} Q{qidx} missing HTML answer_guideline"
        c12_total_questions += len(eqs)

        for s in card["slides_covered"]:
            assert isinstance(s, int), f"Class 12 card {idx} contains non-integer slide: {s}"
            c12_slides_covered.add(s)

    expected_c12 = set(range(1, 33))
    missing_c12 = expected_c12 - c12_slides_covered
    extra_c12 = c12_slides_covered - expected_c12
    if missing_c12:
        print(f"FAIL: Class 12 missing slides: {missing_c12}")
        sys.exit(1)
    if extra_c12:
        print(f"FAIL: Class 12 unexpected extra slides: {extra_c12}")
        sys.exit(1)

    print(f"PASS: Class 12 verified successfully! 32/32 slides covered in {len(c12_cards)} cards with {c12_total_questions} exam questions.")

    # Validate Class 13
    c13_cards = data["13"]
    print(f"\nVerifying Class 13: {len(c13_cards)} cards found.")
    c13_slides_covered = set()
    c13_total_questions = 0

    for idx, card in enumerate(c13_cards, start=1):
        assert card.get("card_num") == idx, f"Class 13 card {idx} card_num mismatch: {card.get('card_num')}"
        assert card.get("title"), f"Class 13 card {idx} missing title"
        assert card.get("act"), f"Class 13 card {idx} missing act"
        assert isinstance(card.get("slides_covered"), list), f"Class 13 card {idx} slides_covered not a list"
        assert card.get("slides_label"), f"Class 13 card {idx} missing slides_label"
        
        # Rating checks
        er = card.get("exam_rating")
        assert er and isinstance(er, dict), f"Class 13 card {idx} missing exam_rating"
        assert er.get("tier"), f"Class 13 card {idx} missing exam_rating.tier"
        assert isinstance(er.get("stars"), int) and er.get("stars") in [3, 4, 5], f"Class 13 card {idx} invalid stars"
        assert er.get("badge_class") in ["badge-critical", "badge-high", "badge-medium"], f"Class 13 card {idx} invalid badge_class"
        assert er.get("frequency_count"), f"Class 13 card {idx} missing frequency_count"
        assert isinstance(er.get("recent_papers"), list) and len(er["recent_papers"]) > 0, f"Class 13 card {idx} missing recent_papers"
        assert er.get("exam_tip"), f"Class 13 card {idx} missing exam_tip"

        # Pedagogical fields
        assert card.get("eli15_takeaway"), f"Class 13 card {idx} missing eli15_takeaway"
        assert isinstance(card.get("key_facts"), list) and len(card["key_facts"]) >= 3, f"Class 13 card {idx} insufficient key_facts"
        for kf in card["key_facts"]:
            assert "<strong>Slide" in kf, f"Class 13 card {idx} key fact missing Slide provenance tag: {kf[:40]}"
        assert card.get("mental_model"), f"Class 13 card {idx} missing mental_model"

        # Checkpoint checks
        cp = card.get("checkpoint")
        assert cp and isinstance(cp, dict), f"Class 13 card {idx} missing checkpoint"
        assert cp.get("question"), f"Class 13 card {idx} checkpoint missing question"
        assert isinstance(cp.get("options"), list) and len(cp["options"]) == 4, f"Class 13 card {idx} checkpoint options != 4"
        assert isinstance(cp.get("correct"), int) and cp["correct"] in [0, 1, 2, 3], f"Class 13 card {idx} checkpoint correct not in 0..3"
        assert cp.get("explanation"), f"Class 13 card {idx} checkpoint missing explanation"

        # Exam questions checks
        eqs = card.get("exam_questions")
        assert isinstance(eqs, list) and len(eqs) >= 2, f"Class 13 card {idx} exam_questions < 2"
        for qidx, eq in enumerate(eqs, start=1):
            assert eq.get("paper"), f"Class 13 card {idx} Q{qidx} missing paper"
            assert eq.get("section"), f"Class 13 card {idx} Q{qidx} missing section"
            assert eq.get("marks"), f"Class 13 card {idx} Q{qidx} missing marks"
            assert eq.get("question"), f"Class 13 card {idx} Q{qidx} missing question"
            assert eq.get("answer_guideline") and ("<ul>" in eq["answer_guideline"] or "<ol>" in eq["answer_guideline"]), f"Class 13 card {idx} Q{qidx} missing HTML answer_guideline"
        c13_total_questions += len(eqs)

        for s in card["slides_covered"]:
            assert isinstance(s, int), f"Class 13 card {idx} contains non-integer slide: {s}"
            c13_slides_covered.add(s)

    expected_c13 = set(range(1, 16))
    missing_c13 = expected_c13 - c13_slides_covered
    extra_c13 = c13_slides_covered - expected_c13
    if missing_c13:
        print(f"FAIL: Class 13 missing slides: {missing_c13}")
        sys.exit(1)
    if extra_c13:
        print(f"FAIL: Class 13 unexpected extra slides: {extra_c13}")
        sys.exit(1)

    print(f"PASS: Class 13 verified successfully! 15/15 slides covered in {len(c13_cards)} cards with {c13_total_questions} exam questions.")

    print("\n" + "="*60)
    print("ALL VERIFICATIONS PASSED: ZERO LOSS CONFIRMED!")
    print(f"Total Class 12 Cards: {len(c12_cards)}, Slides Covered: 1..32, Questions: {c12_total_questions}")
    print(f"Total Class 13 Cards: {len(c13_cards)}, Slides Covered: 1..15, Questions: {c13_total_questions}")
    print("="*60)

if __name__ == "__main__":
    verify()
