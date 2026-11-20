"""
check_redundancy.py
Checks for sentence-level or semantic duplicates across all report sections.
"""

import re
from collections import Counter

from report_sections.section1_intro import ABSTRACT_TEXT, INTRO_PARAGRAPHS
from report_sections.section2_study_area import STUDY_AREA_PARAGRAPHS
from report_sections.section3_methods import METHODS_PARAGRAPHS
from report_sections.section4_results import RESULTS_PARAGRAPHS
from report_sections.section5_discussion import DISCUSSION_PARAGRAPHS
from report_sections.section6_limitations_conclusions import LIMITATIONS_PARAGRAPHS, CONCLUSIONS_PARAGRAPHS

all_paras = []
all_paras.extend(INTRO_PARAGRAPHS)
all_paras.extend(STUDY_AREA_PARAGRAPHS)
for v in METHODS_PARAGRAPHS.values():
    all_paras.extend(v)
for v in RESULTS_PARAGRAPHS.values():
    all_paras.extend(v)
for v in DISCUSSION_PARAGRAPHS.values():
    all_paras.extend(v)
all_paras.extend(LIMITATIONS_PARAGRAPHS)
all_paras.extend(CONCLUSIONS_PARAGRAPHS)

sents = []
for p in all_paras:
    for s in re.split(r'(?<=[.!?])\s+', p.strip()):
        s_clean = ' '.join(s.split())
        if len(s_clean) > 30:
            sents.append(s_clean)

cnt = Counter(sents)
dups = [k for k, v in cnt.items() if v > 1]
print(f'Total sentences analyzed: {len(sents)}')
print(f'Duplicate sentences: {len(dups)}')
for d in dups:
    print('DUP:', d)
