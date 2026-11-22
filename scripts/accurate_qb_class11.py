import os
import sys

# Support both absolute and package imports
try:
    from .grounded_class_11 import get_class11_grounded_questions
except ImportError:
    try:
        from grounded_class_11 import get_class11_grounded_questions
    except ImportError:
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        from grounded_class_11 import get_class11_grounded_questions

def get_class11_questions():
    return get_class11_grounded_questions()

if __name__ == "__main__":
    qs = get_class11_questions()
    print(f"Class 11: {len(qs)} grounded questions ready.")
