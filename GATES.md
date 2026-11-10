# Gates: EST Complete Website Rework & Slidewise Curriculum

OWNS: Study_Material/**, Lecture_Slides/**, index.html, README.md, build_full_website.py, *.py

Scope: Complete rework of the Environmental Science & Technology course website covering all 15 classes (522 slides) with dedicated slidewise learning cards, Moodle synchronization, and automated QA verification.

- [x] G1: All 15 Moodle lecture slide decks present and rendered into high-resolution slide assets
  CHECK: python -c "import os, json; db=json.load(open('Study_Material/full_slide_database.json', encoding='utf-8')); total=sum(d['total_slides'] for d in db.values()); print('TOTAL_SLIDES_RENDERED:', total, 'CLASSES:', len(db))"
  EXPECT: TOTAL_SLIDES_RENDERED: 522 CLASSES: 15
  EVIDENCE: automatic-evidence=v1; definition-sha256=a078fb643385eb1296204444febe4623f5c9cd1c0a2ae408ed892c69414ad41c; exit=0; EXPECT=matched; output-sha256=4c5193dc5b4f687c60932d5d3c1ed0bacbb28af52856c40b6a88706eaadd348d; output-bytes=40; shell=C:\WINDOWS\system32\cmd.exe; cwd=C:\Users\vivek\.gemini\antigravity\scratch\EST; path=6054e107185e/36 entries

- [x] G2: Slidewise learning engine covers every single slide with verbatim bullets and deep pedagogical explanations
  CHECK: python -c "import json; db=json.load(open('Study_Material/full_slide_database.json', encoding='utf-8')); valid=all('deep_explanation' in s and len(s['deep_explanation'])>40 for d in db.values() for s in d['slides']); print('ALL_SLIDES_HAVE_EXPLANATIONS:', valid)"
  EXPECT: ALL_SLIDES_HAVE_EXPLANATIONS: True
  EVIDENCE: automatic-evidence=v1; definition-sha256=ca1115473157fbb7e47e21990c57aede46d7e70b222c74ca7a9ef7818fd753aa; exit=0; EXPECT=matched; output-sha256=6d3576085ca356c1b15526cc28c8925b6f69cb4fab06d233c53cd37d616a23bc; output-bytes=36; shell=C:\WINDOWS\system32\cmd.exe; cwd=C:\Users\vivek\.gemini\antigravity\scratch\EST; path=6054e107185e/36 entries

- [x] G3: All 15 lecture HTML modules and portal pages generated with dual study modes (Slidewise Cards + Comprehensive Topic Lab)
  CHECK: python -c "import os; pages=[f'{i:02d}_' for i in range(1,16)]; exists=all(any(f.startswith(p) for f in os.listdir('Study_Material')) for p in pages) and os.path.exists('index.html') and os.path.exists('Study_Material/00_home.html'); print('ALL_15_MODULES_EXIST:', exists)"
  EXPECT: ALL_15_MODULES_EXIST: True
  EVIDENCE: automatic-evidence=v1; definition-sha256=0bc8d4fe96c2c79b6542f7dbfc9740fb6e79f083fd72fd9d027585820ec7a386; exit=0; EXPECT=matched; output-sha256=718f4612ede2f86c93b15819727bd977ec4197cfcfbfad099831625024b233cf; output-bytes=28; shell=C:\WINDOWS\system32\cmd.exe; cwd=C:\Users\vivek\.gemini\antigravity\scratch\EST; path=6054e107185e/36 entries

- [x] G4: Static QA test suite passes with 0 syntax errors, 0 broken relative asset links, and balanced KaTeX math delimiters
  CHECK: python "C:\Users\vivek\.gemini\config\skills\course-website-builder\scripts\run_test_suite.py" --target "C:\Users\vivek\EST" --skip-browser
  EXPECT: ALL TESTS PASSED! Course website is robust and production-ready.
  EVIDENCE: automatic-evidence=v1; definition-sha256=dcc312cc29f7450b8ac7b7cfc671551f964fefc953391f65813229b9ff2a0ec8; exit=0; EXPECT=matched; output-sha256=1ac321d6306f953f78dbf1c5d6d2ee2ad30a1140017655a39be3b6331afd2aee; output-bytes=1172; shell=C:\WINDOWS\system32\cmd.exe; cwd=C:\Users\vivek\.gemini\antigravity\scratch\EST; path=6054e107185e/36 entries

- [x] G5: Headless browser integration tests pass across modules with 0 JavaScript console runtime exceptions
  CHECK: python "C:\Users\vivek\.gemini\config\skills\course-website-builder\tests\test_browser_execution.py" --target "C:\Users\vivek\EST"
  EXPECT: Browser verification completed with 0 errors
  EVIDENCE: automatic-evidence=v1; definition-sha256=67fc9568738c929c3e0023e14c31c9b4e6a951e491774b4844b072c167f1147c; exit=0; EXPECT=matched; output-sha256=2872c768069500d624761165fda767ff1f4dbb62a9d4741571c7a58de886c677; output-bytes=46; shell=C:\WINDOWS\system32\cmd.exe; cwd=C:\Users\vivek\.gemini\antigravity\scratch\EST; path=6054e107185e/36 entries

- [x] G6: Up-to-date Moodle announcements, exam schedules, and project dates reflected on the master portal
  CHECK: python -c "idx=open('index.html', encoding='utf-8').read(); has_mid= 'Lectures 1' in idx or 'Lectures 1–7' in idx; has_q2='Quiz-2' in idx; has_proj='LSI conference Room' in idx or '17th and 18th November' in idx; print('MOODLE_ANNOUNCEMENTS_PRESENT:', has_mid and has_q2 and has_proj)"
  EXPECT: MOODLE_ANNOUNCEMENTS_PRESENT: True
  EVIDENCE: automatic-evidence=v1; definition-sha256=827157db0da823dd4d5e7c07826808c4592f94948df47dad0a84c18c47db5ef9; exit=0; EXPECT=matched; output-sha256=7a07f0231849b189285e9fb6258df1a73c69b4c468722112e30c8274b19b7652; output-bytes=36; shell=C:\WINDOWS\system32\cmd.exe; cwd=C:\Users\vivek\.gemini\antigravity\scratch\EST; path=6054e107185e/36 entries
