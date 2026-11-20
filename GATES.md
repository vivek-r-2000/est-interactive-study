# Gates: EST Low-Attention Micro-Learning Suite & Complete Curriculum Redesign

OWNS: Study_Material/**, Lecture_Slides/**, index.html, scripts/**, GATES.md

Scope: Complete redesign from scratch of Environmental Science & Technology course into an editorial, unslapped, micro-learning study suite covering all 19 lecture slide decks across 5 thematic pillars with bite-sized concept cards, interactive checkpoints, and integrated case study dossiers, including deep slidewise narrative rework of Class 11 (29 slides).

- [x] G1: Comprehensive curriculum database covers all 19 classes, 5 pillars, and 50+ bite-sized submodules
  CHECK: python scripts/verify_curriculum_db.py
  EXPECT: CURRICULUM_DB_VERIFIED: 19 CLASSES, 5 PILLARS, 63 SUBMODULES
  EVIDENCE: automatic-evidence=v1; definition-sha256=2903a863d19e2cf1c23382cd013532fdc929796a2d821a40dabfc068b69cde29; exit=0; EXPECT=matched; output-sha256=5df6c6d09ed7abe036ad6e791af11c8baf45c519b53634f490dfcea2db983c7d; output-bytes=62; shell=C:\WINDOWS\system32\cmd.exe; cwd=C:\Users\vivek\.gemini\antigravity\scratch\EST; path=65842fce3bf4/36 entries

- [x] G2: Low-attention pedagogical structure active with simple ELI15 summaries and 1-click checkpoints
  CHECK: python scripts/verify_pedagogy.py
  EXPECT: PEDAGOGY_VERIFIED: 63 MICRO_LEARNING_CHECKPOINTS_ACTIVE
  EVIDENCE: automatic-evidence=v1; definition-sha256=c479d7cc67eced2bcf6e9455fc40609f5c3423d58cffb1c09b55d3d27cf6f8c6; exit=0; EXPECT=matched; output-sha256=5d62712bb743ef5d631ba7558c3af5b00f3d836e167ff3e69bea684501cb22c0; output-bytes=57; shell=C:\WINDOWS\system32\cmd.exe; cwd=C:\Users\vivek\.gemini\antigravity\scratch\EST; path=65842fce3bf4/36 entries

- [x] G3: All 12 major real-world case studies and incidents structured with 3-part root cause takeaways
  CHECK: python scripts/verify_case_studies.py
  EXPECT: CASE_STUDIES_VERIFIED: 12_MAJOR_INCIDENTS_MAPPED
  EVIDENCE: automatic-evidence=v1; definition-sha256=6ce3608ff5878a272e828a1d8f143a9f34185d34a426f0385ac4ce94e56c7e67; exit=0; EXPECT=matched; output-sha256=3d0f97d9e588e4f8b40d20f5560d08042dbc62c4fcbbb22752efbf508af2efd0; output-bytes=50; shell=C:\WINDOWS\system32\cmd.exe; cwd=C:\Users\vivek\.gemini\antigravity\scratch\EST; path=65842fce3bf4/36 entries

- [x] G4: Editorial scientific field guide single-page application built with KaTeX and unslop standards
  CHECK: python scripts/verify_website_build.py
  EXPECT: WEBSITE_BUILD_VERIFIED: EDITORIAL_STANDARDS_MET
  EVIDENCE: automatic-evidence=v1; definition-sha256=5aa1c6c0b06f172487b8f42a84ff05433f8586921d810ad3ee5bd197c4483f93; exit=0; EXPECT=matched; output-sha256=e3a8f59e595736e161bc0eeb43178ca1fb9876c3c0dad63e659a6b735ee7c986; output-bytes=49; shell=C:\WINDOWS\system32\cmd.exe; cwd=C:\Users\vivek\.gemini\antigravity\scratch\EST; path=65842fce3bf4/36 entries

- [x] G5: Zero broken assets, valid HTML5 structure, and clean local references
  CHECK: python scripts/verify_links_and_assets.py
  EXPECT: ASSET_INTEGRITY_VERIFIED: 0_BROKEN_LINKS
  EVIDENCE: automatic-evidence=v1; definition-sha256=f0f40b5091b243ca2bcba1ea919e3edda38804850983f984a5762106ee017506; exit=0; EXPECT=matched; output-sha256=f61d514b95566f7f9348d51e5123b09ee82e1404ad8dde91a5cc9171ba01f635; output-bytes=42; shell=C:\WINDOWS\system32\cmd.exe; cwd=C:\Users\vivek\.gemini\antigravity\scratch\EST; path=65842fce3bf4/36 entries

- [x] G6: Class 11 comprehensive slidewise rebuild covering all 29 slides with narrative continuity and zero AI slop
  CHECK: python scripts/verify_class11_slides.py
  EXPECT: CLASS_11_VERIFIED: ALL_29_SLIDES_COVERED_WITH_NARRATIVE_CONTINUITY
  EVIDENCE: automatic-evidence=v1; definition-sha256=9cb06a9ac200fa64b6c41ba1ef55497400eeee2bb0411dde737516b008b1befb; exit=0; EXPECT=matched; output-sha256=8afb12a85b975c2fbee76a3b04a3f76266914afe755ee26fe8cbcc635a2c1eb1; output-bytes=68; shell=C:\WINDOWS\system32\cmd.exe; cwd=C:\Users\vivek\.gemini\antigravity\scratch\EST; path=65842fce3bf4/36 entries

- [x] G7: Classes 12 to 19 comprehensive slidewise rebuild covering all 232 slides with narrative continuity and zero AI slop
  CHECK: python scripts/verify_classes_12_to_19.py
  EXPECT: CLASSES_12_TO_19_VERIFIED: ALL_8_CLASSES_MET_WITH_232_SLIDES
  EVIDENCE: automatic-evidence=v1; definition-sha256=331cc6af134647773d13a2afd69206542a15ff7928e5c66a88c0eb2c140ff031; exit=0; EXPECT=matched; output-sha256=7346cb284ca652ab0e46fbf425f76c4acf3111cf9449ccb3e807044ac40df51d; output-bytes=62; shell=C:\WINDOWS\system32\cmd.exe; cwd=C:\Users\vivek\.gemini\antigravity\scratch\EST; path=ee6bd4fcb200/36 entries
