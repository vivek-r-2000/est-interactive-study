import os
import json
import re
import html

WORKSPACE = r"C:\Users\vivek\EST"
METADATA_PATH = os.path.join(WORKSPACE, "Study_Material", "lectures_metadata.json")
STUDY_DIR = os.path.join(WORKSPACE, "Study_Material")

with open(METADATA_PATH, "r", encoding="utf-8") as f:
    METADATA = json.load(f)

# Import lecture contents and simulators
from lecture_content_data_1 import LECTURE_DETAILS as D1
from lecture_content_data_2 import LECTURE_DETAILS_2 as D2
from lecture_content_data_3 import LECTURE_DETAILS_3 as D3
from simulators_data import SIMULATORS as S1
from simulators_data_2 import SIMULATORS_2 as S2
from simulators_data_3 import SIMULATORS_3 as S3
from diagram_explanations import DIAGRAM_EXPLANATIONS

ALL_DETAILS = {}
ALL_DETAILS.update(D1)
ALL_DETAILS.update(D2)
ALL_DETAILS.update(D3)

ALL_SIMS = {}
ALL_SIMS.update(S1)
ALL_SIMS.update(S2)
ALL_SIMS.update(S3)

def get_youtube_embed(url):
    m = re.search(r'(?:v=|youtu\.be/|embed/)([a-zA-Z0-9_-]{11})', url)
    if m:
        return f"https://www.youtube-nocookie.com/embed/{m.group(1)}"
    return None

SHARED_CSS = """
  :root {
    --bg-main: #060f0b;
    --bg-card: #0b1a14;
    --bg-card-hover: #10241c;
    --border: #183327;
    --border-accent: #23523f;
    --primary: #10b981;
    --primary-light: #34d399;
    --primary-glow: rgba(16, 185, 129, 0.35);
    --teal: #14b8a6;
    --cyan: #06b6d4;
    --amber: #f59e0b;
    --red: #ef4444;
    --text: #f0fdf4;
    --muted: #94a3b8;
    --muted-green: #a7f3d0;
  }

  * { box-sizing: border-box; }
  body {
    background: var(--bg-main);
    color: var(--text);
    font-family: 'Inter', system-ui, -apple-system, sans-serif;
  }

  /* Eco Glassmorphism & Cards */
  .eco-card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 16px;
    transition: all 0.25s ease;
  }
  .eco-card:hover {
    border-color: var(--primary);
    box-shadow: 0 10px 30px -10px var(--primary-glow);
    transform: translateY(-2px);
  }
  .eco-card-static {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 16px;
  }

  /* Badges */
  .badge-emerald { background: rgba(16, 185, 129, 0.12); border: 1px solid rgba(16, 185, 129, 0.3); color: #6ee7b7; }
  .badge-teal    { background: rgba(20, 184, 166, 0.12); border: 1px solid rgba(20, 184, 166, 0.3); color: #5eead4; }
  .badge-amber   { background: rgba(245, 158, 11, 0.12); border: 1px solid rgba(245, 158, 11, 0.3); color: #fcd34d; }
  .badge-cyan    { background: rgba(6, 182, 212, 0.12); border: 1px solid rgba(6, 182, 212, 0.3); color: #67e8f9; }

  /* 3D Flip Card */
  .flip-card-wrap { perspective: 900px; height: 210px; cursor: pointer; }
  .flip-card-inner { position: relative; width: 100%; height: 100%; transform-style: preserve-3d; transition: transform .5s cubic-bezier(0.4, 0, 0.2, 1); }
  .flip-card-wrap.flipped .flip-card-inner { transform: rotateY(180deg); }
  .flip-face {
    position: absolute; inset: 0; backface-visibility: hidden;
    border-radius: 14px; border: 1px dashed var(--border-accent);
    display: flex; flex-direction: column; align-items: center; justify-content: center;
    padding: 24px; text-align: center;
  }
  .flip-front { background: rgba(16, 185, 129, 0.05); }
  .flip-back  { background: rgba(20, 184, 166, 0.12); border-color: var(--teal); transform: rotateY(180deg); }

  /* Quiz */
  .quiz-option {
    display: flex; align-items: center; gap: 12px;
    padding: 12px 16px; border-radius: 10px;
    border: 1px solid var(--border); margin-bottom: 10px;
    cursor: pointer; font-size: 14px; transition: all .2s;
    background: rgba(255,255,255,0.02);
  }
  .quiz-option:hover { border-color: var(--primary); background: rgba(16, 185, 129, 0.08); }
  .quiz-option.correct { border-color: #10b981!important; background: rgba(16, 185, 129, 0.18)!important; color: #a7f3d0; }
  .quiz-option.wrong   { border-color: #ef4444!important; background: rgba(239, 68, 68, 0.18)!important; color: #fca5a5; }
  .quiz-option.disabled { pointer-events: none; }
  .q-letter {
    width: 26px; height: 26px; border-radius: 50%;
    background: var(--border-accent); display: flex; align-items: center; justify-content: center;
    font-size: 12px; font-weight: 700; flex-shrink: 0;
  }

  /* Slide Lightbox Modal */
  .slide-modal-backdrop {
    display: none; position: fixed; inset: 0; z-index: 1000;
    background: rgba(3, 7, 5, 0.94); backdrop-filter: blur(8px);
    align-items: center; justify-content: center; padding: 24px;
  }
  .slide-modal-backdrop.show { display: flex; }
"""

def generate_lecture_page(lec):
    lec_id = lec["id"]
    lec_slug = lec["slug"]
    lec_title = lec["title"]
    lec_short = lec.get("short_title", lec_title)
    lec_meta = lec
    details = ALL_DETAILS.get(lec_id, {})
    sim_html = ALL_SIMS.get(f"sim_{lec_id}", ALL_SIMS.get(lec_id, "<p class='text-slate-400'>Interactive model loaded.</p>"))

    total_slides = len(lec["slides"])
    extracted_diags = []
    for s in lec["slides"]:
        for d in s.get("diagrams", []):
            extracted_diags.append(d)

    videos = lec.get("videos", [])
    video_embeds = []
    for v in videos:
        emb = get_youtube_embed(v)
        if emb:
            video_embeds.append({"url": v, "embed": emb})

    # Prepare Screens / Cards:
    # 0: Big Picture (Intuition)
    # 1: Scientific Foundations & Theory
    # 2: Visual Deep-Dive & Extracted Diagrams
    # 3: Mathematical Formulations & Data Tables
    # 4: (If videos) Video Masterclass
    # 5: Interactive Simulator
    # 6: Active Recall Flashcards
    # 7: High-Yield Exam Traps
    # 8: Concept Check Quiz
    # 9: Complete Slide Reference Gallery

    screens = []
    sidebar_links = []

    # SCREEN 1: INTUITION
    int_info = details.get("intuition", {})
    pillars_html = ""
    for p in int_info.get("pillars", []):
        pillars_html += f"""
        <div class="p-4 rounded-xl bg-[#081610] border border-emerald-900/60 mb-3">
          <div class="flex items-center gap-2 mb-1">
            <span class="badge-emerald px-2 py-0.5 rounded text-[11px] font-bold font-mono">{p.get('badge','Concept')}</span>
            <strong class="text-emerald-300 text-sm">{p.get('title','')}</strong>
          </div>
          <p class="text-xs text-slate-300 leading-relaxed">{p.get('desc','')}</p>
        </div>
        """

    screens.append(f"""
    <section class="card-screen active" data-title="Big Picture & Intuition">
      <div class="eco-card p-6 md:p-8 border-emerald-800/80 mb-6">
        <div class="flex items-center gap-2 mb-3">
          <span class="badge-emerald px-2.5 py-1 rounded text-xs font-mono font-bold">Lecture {lec_id} • Fundamental Concept</span>
          <span class="text-xs text-slate-400">• {lec['difficulty']} • {lec['duration']}</span>
        </div>
        <h2 class="text-2xl md:text-3xl font-black text-white mb-2">{int_info.get('title', lec_title)}</h2>
        <div class="text-emerald-400 text-sm font-semibold mb-4">{int_info.get('subtitle', '')}</div>
        
        <div class="p-4 bg-[#05140d] border-l-4 border-emerald-500 rounded-r-xl mb-6 text-emerald-100 text-sm leading-relaxed">
          <strong>💡 Why This Topic Matters:</strong><br/>
          {int_info.get('why', '')}
        </div>

        <div class="space-y-2">
          {pillars_html}
        </div>
      </div>
    </section>
    """)
    sidebar_links.append((0, "1. Big Picture & Intuition"))

    # SCREEN 2: THEORY
    theory_info = details.get("theory", {})
    screens.append(f"""
    <section class="card-screen" data-title="Scientific Foundations">
      <div class="eco-card p-6 md:p-8 border-emerald-800/80 mb-6">
        <div class="badge-teal inline-block px-2.5 py-1 rounded text-xs font-mono font-bold mb-3">Core Mechanics</div>
        <h2 class="text-2xl font-black text-white mb-4">{theory_info.get('title', 'Scientific Principles & Dynamics')}</h2>
        <div class="text-sm leading-relaxed text-slate-200">
          {theory_info.get('content', '')}
        </div>
      </div>
    </section>
    """)
    sidebar_links.append((1, "2. Scientific Foundations"))

    # SCREEN 3: VISUAL DEEP-DIVE & EXTRACTED DIAGRAM BREAKDOWN
    diag_items = DIAGRAM_EXPLANATIONS.get(lec_id, [])
    diag_cards_html = ""
    for d_idx, d in enumerate(diag_items, 1):
        diag_cards_html += f"""
        <div class="eco-card p-5 border-emerald-800/80 mb-6 bg-[#071711]">
          <div class="flex flex-wrap items-center justify-between gap-2 mb-3 pb-2 border-b border-emerald-900/60">
            <div class="flex items-center gap-2">
              <span class="badge-emerald px-2.5 py-1 rounded text-xs font-mono font-bold">Figure {d_idx}</span>
              <h3 class="text-base font-bold text-white">{d['title']}</h3>
            </div>
            <span class="text-[11px] text-emerald-400 font-mono">📍 {d['source']}</span>
          </div>

          <div class="grid grid-cols-1 lg:grid-cols-12 gap-5 items-center mb-4">
            <!-- Isolated Extracted Diagram Image with Click-to-Zoom -->
            <div class="lg:col-span-5 bg-black/60 border border-emerald-900/80 rounded-xl p-3 flex flex-col items-center justify-center cursor-pointer group" onclick="openLightbox('{d['image']}', '{html.escape(d['title'])}')">
              <img src="{d['image']}" alt="{html.escape(d['title'])}" class="max-h-64 w-auto object-contain rounded group-hover:scale-105 transition-all" loading="lazy">
              <div class="text-[10px] text-emerald-400 font-mono mt-2 flex items-center gap-1">
                <span>🔍</span> Click diagram to zoom in full lightbox
              </div>
            </div>

            <!-- Deep Scientific & Pedagogical Explanation -->
            <div class="lg:col-span-7 space-y-3 text-xs leading-relaxed">
              <div class="p-3 bg-[#0a1e16] border-l-2 border-emerald-400 rounded-r-lg">
                <strong class="text-emerald-300 font-bold block mb-1">👁️ What the Diagram Shows:</strong>
                <span class="text-slate-300">{d['what_it_shows']}</span>
              </div>

              <div class="p-3 bg-[#0a1e16] border-l-2 border-teal-400 rounded-r-lg">
                <strong class="text-teal-300 font-bold block mb-1">🔬 Scientific & Environmental Mechanism:</strong>
                <span class="text-slate-300">{d['scientific_mechanism']}</span>
              </div>

              <div class="p-3 bg-[#0a1e16] border-l-2 border-cyan-400 rounded-r-lg">
                <strong class="text-cyan-300 font-bold block mb-1">📊 Quantitative / Mathematical Model:</strong>
                <span class="text-slate-300">{d['quantitative_math']}</span>
              </div>
            </div>
          </div>

          <!-- Exam Trap Callout Box -->
          <div class="p-3 bg-[#17130b] border border-amber-900/80 rounded-xl text-xs text-amber-200">
            {d['exam_trap']}
          </div>
        </div>
        """

    screens.append(f"""
    <section class="card-screen" data-title="Extracted Diagram Breakdown">
      <div class="eco-card p-6 md:p-8 border-emerald-800/80 mb-6">
        <div class="flex items-center justify-between mb-3">
          <span class="badge-emerald px-2.5 py-1 rounded text-xs font-mono font-bold">🎨 Detailed Diagram Breakdown</span>
          <span class="text-xs text-slate-400">Extracted from instructor slide decks</span>
        </div>
        <h2 class="text-2xl font-black text-white mb-2">Scientific Diagrams & Structural Analysis</h2>
        <p class="text-xs text-slate-300 mb-6">In-depth explanations of the isolated figures, flowcharts, and empirical curves from this lecture.</p>
        
        <div>
          {diag_cards_html}
        </div>
      </div>
    </section>
    """)
    sidebar_links.append((2, "3. Diagram Breakdown & Analysis"))

    # SCREEN 4: MATH FORMULATIONS & DATA TABLES
    math_info = details.get("math", {})
    t_headers = "".join([f"<th class='p-3 border-r border-emerald-900'>{h}</th> " for h in math_info.get("table_headers", [])])
    t_rows = ""
    for r in math_info.get("table_rows", []):
        cols = "".join([f"<td class='p-3 border-r border-emerald-900 font-mono'>{c}</td> " for c in r])
        t_rows += f"<tr class='hover:bg-emerald-950/20'>{cols}</tr>\n"

    screens.append(f"""
    <section class="card-screen" data-title="Mathematical Formulations">
      <div class="eco-card p-6 md:p-8 border-emerald-800/80 mb-6">
        <div class="badge-amber inline-block px-2.5 py-1 rounded text-xs font-mono font-bold mb-3">Rigorous Quantitative Model</div>
        <h2 class="text-2xl font-black text-white mb-4">{math_info.get('title', 'Mathematical Formulations')}</h2>
        
        <div class="p-4 bg-[#05120c] border border-emerald-900/80 rounded-xl text-center my-4 overflow-x-auto">
          <div class="text-lg md:text-xl font-mono text-emerald-300">
            $${math_info.get('formula', '')}$$
          </div>
        </div>
        <p class="text-xs text-slate-300 mb-6">{math_info.get('notes', '')}</p>

        <div class="overflow-x-auto rounded-xl border border-emerald-900/80">
          <table class="w-full text-xs text-left text-slate-300">
            <thead class="bg-[#05140d] text-emerald-400 uppercase text-[10px] tracking-wider border-b border-emerald-900">
              <tr>{t_headers}</tr>
            </thead>
            <tbody class="divide-y divide-emerald-950 font-sans">
              {t_rows}
            </tbody>
          </table>
        </div>
      </div>
    </section>
    """)
    sidebar_links.append((3, "4. Math & Empirical Tables"))

    # SCREEN 5: VIDEO MASTERCLASS (if video exists)
    cur_idx = 4
    if video_embeds:
        v_cards = ""
        for v in video_embeds:
            v_cards += f"""
            <div class="bg-[#05140d] border border-emerald-900/80 rounded-xl overflow-hidden mb-6">
              <div class="p-3 bg-[#0a1f15] border-b border-emerald-900/80 flex items-center justify-between">
                <span class="text-xs font-bold text-emerald-300 flex items-center gap-2">
                  <span>▶️</span> Recommended Video Lecture / Documentary Reference
                </span>
                <a href="{v['url']}" target="_blank" rel="noopener noreferrer" class="text-[11px] text-emerald-400 hover:underline">Open on YouTube ↗</a>
              </div>
              <div class="relative w-full aspect-video bg-black">
                <iframe src="{v['embed']}" class="w-full h-full" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
              </div>
            </div>
            """

        screens.append(f"""
        <section class="card-screen" data-title="Video Masterclass">
          <div class="eco-card p-6 md:p-8 border-emerald-800/80 mb-6">
            <div class="badge-cyan inline-block px-2.5 py-1 rounded text-xs font-mono font-bold mb-3">Audiovisual Deep-Dive</div>
            <h2 class="text-2xl font-black text-white mb-2">Lecture Videos & Multimedia Documentaries</h2>
            <p class="text-xs text-slate-300 mb-6">Referenced directly from the course slides for active conceptual reinforcement.</p>
            {v_cards}
          </div>
        </section>
        """)
        sidebar_links.append((cur_idx, f"{cur_idx+1}. Video Masterclass"))
        cur_idx += 1

    # SCREEN: INTERACTIVE SIMULATOR
    screens.append(f"""
    <section class="card-screen" data-title="Interactive Simulator">
      <div class="mb-6">
        {sim_html}
      </div>
    </section>
    """)
    sidebar_links.append((cur_idx, f"{cur_idx+1}. Interactive Simulator"))
    cur_idx += 1

    # SCREEN: FLASHCARDS
    f_cards_html = ""
    for f in details.get("flashcards", []):
        f_cards_html += f"""
        <div class="flip-card-wrap mb-4" onclick="this.classList.toggle('flipped')">
          <div class="flip-card-inner">
            <div class="flip-face flip-front">
              <span class="text-xs uppercase font-bold text-emerald-400 tracking-wider mb-2">Question (Click / Space to Flip)</span>
              <div class="text-base font-bold text-white mb-2">{f['q']}</div>
              <span class="text-[11px] text-slate-400 mt-2">🔄 Click card to reveal answer</span>
            </div>
            <div class="flip-face flip-back">
              <span class="text-xs uppercase font-bold text-teal-300 tracking-wider mb-2">Answer</span>
              <div class="text-sm font-semibold text-emerald-100 leading-relaxed">{f['a']}</div>
            </div>
          </div>
        </div>
        """

    screens.append(f"""
    <section class="card-screen" data-title="Active Recall Flashcards">
      <div class="eco-card p-6 md:p-8 border-emerald-800/80 mb-6">
        <div class="badge-emerald inline-block px-2.5 py-1 rounded text-xs font-mono font-bold mb-3">Spaced Repetition</div>
        <h2 class="text-2xl font-black text-white mb-2">Active Recall Flashcards</h2>
        <p class="text-xs text-slate-300 mb-6">Test yourself on essential definitions, reactions, and principles before flipping.</p>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          {f_cards_html}
        </div>
      </div>
    </section>
    """)
    sidebar_links.append((cur_idx, f"{cur_idx+1}. Active Recall Flashcards"))
    cur_idx += 1

    # SCREEN: EXAM TRAPS & HIGH-YIELD PITFALLS
    traps_html = "".join([f"<li class='p-3 bg-[#05140d] border border-amber-900/60 rounded-xl text-xs text-slate-200 leading-relaxed mb-3'>{t}</li>" for t in details.get("traps", [])])
    screens.append(f"""
    <section class="card-screen" data-title="Exam Traps & Pitfalls">
      <div class="eco-card p-6 md:p-8 border-amber-800/80 mb-6">
        <div class="badge-amber inline-block px-2.5 py-1 rounded text-xs font-mono font-bold mb-3">High-Yield Insights</div>
        <h2 class="text-2xl font-black text-white mb-2">Exam Traps, Fallacies & Professor Emphasis Points</h2>
        <p class="text-xs text-slate-300 mb-6">Common student misconceptions and subtle distinctions tested in Midsem and Endsem exams.</p>
        <ul class="space-y-1">
          {traps_html}
        </ul>
      </div>
    </section>
    """)
    sidebar_links.append((cur_idx, f"{cur_idx+1}. High-Yield Exam Traps"))
    cur_idx += 1

    # SCREEN: CONCEPT CHECK QUIZ
    quiz_html = ""
    for q_idx, q in enumerate(details.get("quiz", [])):
        opts_html = ""
        letters = ["A", "B", "C", "D"]
        for opt_idx, opt in enumerate(q["options"]):
            is_cor = (opt_idx == q["correct"])
            opts_html += f"""
            <div class="quiz-option" onclick="handleQuiz(this, {1 if is_cor else 0}, 'q_{lec_id}_{q_idx}')">
              <span class="q-letter">{letters[opt_idx]}</span>
              <span>{opt}</span>
            </div>
            """
        quiz_html += f"""
        <div class="p-5 bg-[#05140d] border border-emerald-900/80 rounded-xl mb-6">
          <div class="text-xs font-mono text-emerald-400 font-bold mb-2">Question {q_idx + 1}</div>
          <div class="text-sm font-bold text-white mb-4">{q['question']}</div>
          <div class="space-y-1">
            {opts_html}
          </div>
          <div id="q_{lec_id}_{q_idx}" class="p-3 mt-3 bg-[#0a1e15] border border-emerald-800 rounded-lg text-xs text-emerald-200 hidden">
            <strong>Explanation:</strong> {q['explanation']}
          </div>
        </div>
        """

    screens.append(f"""
    <section class="card-screen" data-title="Concept Check Quiz">
      <div class="eco-card p-6 md:p-8 border-emerald-800/80 mb-6">
        <div class="badge-emerald inline-block px-2.5 py-1 rounded text-xs font-mono font-bold mb-3">Knowledge Verification</div>
        <h2 class="text-2xl font-black text-white mb-2">Concept Check Quiz</h2>
        <p class="text-xs text-slate-300 mb-6">Instant feedback on core conceptual and quantitative questions.</p>
        <div>
          {quiz_html}
        </div>
      </div>
    </section>
    """)
    sidebar_links.append((cur_idx, f"{cur_idx+1}. Concept Check Quiz"))
    cur_idx += 1

    # FINAL SCREEN: COMPLETE SLIDE REFERENCE GALLERY (User Requirement!)
    slides_grid = ""
    for s in lec["slides"]:
        slides_grid += f"""
        <div class="bg-[#05140d] border border-emerald-900/80 rounded-xl p-2 flex flex-col justify-between group hover:border-emerald-500 transition-all">
          <div class="overflow-hidden rounded-lg bg-black/50 cursor-pointer relative" onclick="openLightbox('{s['image']}', 'Slide {s['slide_num']}: {html.escape(s['title'])}')">
            <img src="{s['image']}" alt="Slide {s['slide_num']}" class="w-full h-36 object-contain group-hover:scale-105 transition-all" loading="lazy">
            <div class="absolute inset-0 bg-emerald-950/20 opacity-0 group-hover:opacity-100 transition-all flex items-center justify-center">
              <span class="bg-black/80 text-emerald-300 text-xs px-2.5 py-1 rounded-full font-mono">🔍 Click to Zoom</span>
            </div>
          </div>
          <div class="pt-2 px-1">
            <div class="flex items-center justify-between text-[10px] text-slate-400 font-mono mb-1">
              <span class="text-emerald-400 font-bold">Slide #{s['slide_num']}</span>
              <span>{s['source_file']}</span>
            </div>
            <div class="text-xs font-semibold text-slate-200 line-clamp-2" title="{html.escape(s['title'])}">{s['title']}</div>
          </div>
        </div>
        """

    file_badges = " ".join([f"<a href='../Lecture_Slides/{f}' target='_blank' class='inline-flex items-center gap-1.5 px-3 py-1 rounded-lg bg-emerald-950/80 border border-emerald-800 text-emerald-300 text-xs font-mono hover:bg-emerald-900 transition-all'><span>📄 Download {f}</span></a>" for f in lec['files']])

    screens.append(f"""
    <section class="card-screen" data-title="Slide Reference Gallery">
      <div class="eco-card p-6 md:p-8 border-emerald-800/80 mb-6">
        <div class="flex flex-wrap items-center justify-between gap-3 mb-4 pb-3 border-b border-emerald-900/80">
          <div>
            <div class="badge-emerald inline-block px-2.5 py-1 rounded text-xs font-mono font-bold mb-1">📚 Primary Course Slides</div>
            <h2 class="text-2xl font-black text-white">Complete Slide Reference Gallery</h2>
            <p class="text-xs text-slate-300">All {total_slides} slides from the lecture presentations for instant reference and review.</p>
          </div>
          <div class="flex flex-wrap gap-2">
            {file_badges}
          </div>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-3">
          {slides_grid}
        </div>
      </div>
    </section>
    """)
    sidebar_links.append((cur_idx, f"{cur_idx+1}. Complete Slide Gallery ({total_slides} Slides)"))

    # Build Sidebar links HTML
    nav_links_html = ""
    for idx, title in sidebar_links:
        act = "active" if idx == 0 else ""
        nav_links_html += f"""
        <div class="sidebar-link {act}" onclick="goToCard({idx})" id="slink_{idx}">
          <span class="sidebar-dot"></span>
          <span class="truncate">{title}</span>
        </div>
        """

    all_screens_html = "\n".join(screens)

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Lecture {lec_id}: {lec_title} — EST Study Suite 🌿</title>
<script src="https://cdn.tailwindcss.com"></script>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body);"></script>

<style>
{SHARED_CSS}

  /* Top Bar */
  #topbar {{
    position: fixed; top: 0; left: 0; right: 0; z-index: 50;
    background: #040a07; border-bottom: 1px solid var(--border);
    display: flex; align-items: center; gap: 12px;
    padding: 0 16px; height: 54px;
  }}
  #topbar a {{ color: var(--primary-light); font-size: 13px; text-decoration: none; font-weight: 600; }}
  #module-title {{ font-weight: 800; font-size: 13px; color: #fff; white-space: nowrap; }}
  #progress-bar-bg {{ background: var(--border); border-radius: 99px; height: 6px; width: 100%; }}
  #progress-bar-fill {{ background: linear-gradient(90deg, #10b981, #14b8a6); height: 6px; border-radius: 99px; transition: width .3s ease; width: 0%; }}

  /* Pomodoro */
  #pomodoro {{
    display: flex; align-items: center; gap: 6px;
    background: var(--bg-card); border: 1px solid var(--border);
    border-radius: 8px; padding: 4px 12px; cursor: pointer; white-space: nowrap;
  }}
  #timer-display {{ font-size: 13px; font-weight: 700; color: #f59e0b; font-variant-numeric: tabular-nums; }}

  /* Layout */
  #layout {{ display: flex; margin-top: 54px; height: calc(100vh - 54px); }}
  #sidebar {{
    width: 250px; min-width: 250px; background: #040b08;
    border-right: 1px solid var(--border); overflow-y: auto; padding: 16px 0;
    display: flex; flex-direction: column; gap: 2px;
  }}
  .sidebar-link {{
    display: flex; align-items: center; gap: 10px;
    padding: 8px 16px; font-size: 12px; color: var(--muted);
    cursor: pointer; transition: all .2s; border-left: 3px solid transparent;
  }}
  .sidebar-link:hover {{ background: rgba(16, 185, 129, 0.08); color: #fff; }}
  .sidebar-link.active {{ background: rgba(16, 185, 129, 0.15); color: #34d399; border-left-color: #10b981; font-weight: 700; }}
  .sidebar-dot {{ width: 6px; height: 6px; border-radius: 50%; background: #334155; flex-shrink: 0; }}
  .sidebar-link.active .sidebar-dot {{ background: #10b981; box-shadow: 0 0 8px #10b981; }}

  /* Main */
  #main {{
    flex: 1; overflow-y: auto; padding: 28px 24px 100px 24px;
    display: flex; flex-direction: column; align-items: center;
  }}
  .card-screen {{ display: none; width: 100%; max-width: 900px; animation: fadeIn .25s ease; }}
  .card-screen.active {{ display: block; }}
  @keyframes fadeIn {{ from {{ opacity:0; transform:translateY(8px); }} to {{ opacity:1; transform:translateY(0); }} }}

  /* Nav Bar */
  #nav-bar {{
    position: fixed; bottom: 0; left: 250px; right: 0;
    background: #040a07; border-top: 1px solid var(--border);
    display: flex; align-items: center; justify-content: center; gap: 16px;
    padding: 12px 24px; z-index: 40;
  }}
  @media (max-width: 768px) {{
    #sidebar {{ display: none; }}
    #nav-bar {{ left: 0; }}
  }}
</style>
</head>
<body class="selection:bg-emerald-600 selection:text-white">

  <!-- TOP BAR -->
  <header id="topbar">
    <a href="00_home.html" class="flex items-center gap-1">← <span class="hidden sm:inline">All Modules</span></a>
    <span style="color:var(--border)">|</span>
    <span id="module-title">Lec {lec_id}: {lec_short}</span>
    <div class="flex-1 flex flex-col gap-1 mx-2 min-w-0">
      <div class="flex justify-between text-[11px]">
        <span id="section-label" class="text-emerald-400 font-semibold truncate">Section 1</span>
        <span id="progress-label" class="text-slate-400 font-mono">0%</span>
      </div>
      <div id="progress-bar-bg"><div id="progress-bar-fill"></div></div>
    </div>
    <div id="pomodoro" onclick="togglePomodoro()">
      <span>⏱️</span>
      <span id="timer-display">25:00</span>
    </div>
  </header>

  <!-- LAYOUT -->
  <div id="layout">
    <!-- SIDEBAR -->
    <nav id="sidebar">
      <div class="text-[10px] font-bold tracking-widest text-emerald-400/80 uppercase px-4 py-2">Lecture Curriculum</div>
      {nav_links_html}
    </nav>

    <!-- MAIN VIEW -->
    <main id="main">
      {all_screens_html}
    </main>
  </div>

  <!-- BOTTOM NAVIGATION BAR -->
  <nav id="nav-bar">
    <button class="nav-btn px-5 py-2 rounded-lg text-xs font-bold border border-emerald-900 bg-[#071710] text-slate-300 hover:border-emerald-500 transition-all" onclick="prevCard()">← Previous</button>
    <span id="card-counter" class="text-xs text-slate-400 font-mono">Card 1 of {len(screens)}</span>
    <button class="nav-btn px-5 py-2 rounded-lg text-xs font-bold bg-gradient-to-r from-emerald-600 to-teal-600 text-white hover:opacity-90 transition-all shadow-md shadow-emerald-950" onclick="nextCard()">Next Card →</button>
  </nav>

  <!-- LIGHTBOX MODAL -->
  <div id="lightbox_modal" class="slide-modal-backdrop" onclick="closeLightbox(event)">
    <div class="relative max-w-5xl w-full bg-[#07130e] border border-emerald-800 rounded-2xl overflow-hidden p-3 shadow-2xl" onclick="event.stopPropagation()">
      <div class="flex items-center justify-between pb-2 mb-2 border-b border-emerald-900/80">
        <span id="modal_title" class="text-sm font-bold text-emerald-300 font-mono truncate">Slide Preview</span>
        <button class="text-slate-400 hover:text-white px-2 py-1 text-sm font-bold bg-emerald-950 rounded" onclick="closeLightbox()">✕ Close</button>
      </div>
      <div class="flex items-center justify-center bg-black/60 rounded-xl p-2 max-h-[80vh] overflow-auto">
        <img id="modal_img" src="" alt="Full view" class="max-h-[75vh] object-contain rounded">
      </div>
    </div>
  </div>

  <script>
    let currentCard = 0;
    const screens = document.querySelectorAll('.card-screen');
    const totalCards = screens.length;

    function updateCardView() {{
      screens.forEach((s, i) => {{
        s.classList.toggle('active', i === currentCard);
      }});

      // Update sidebar
      for (let i = 0; i < totalCards; i++) {{
        const el = document.getElementById('slink_' + i);
        if (el) el.classList.toggle('active', i === currentCard);
      }}

      // Counter & Progress
      document.getElementById('card-counter').innerText = `Card ${{currentCard + 1}} of ${{totalCards}}`;
      const pct = Math.round(((currentCard) / (totalCards - 1)) * 100);
      document.getElementById('progress-bar-fill').style.width = pct + '%';
      document.getElementById('progress-label').innerText = pct + '%';
      
      const title = screens[currentCard].getAttribute('data-title') || `Section ${{currentCard + 1}}`;
      document.getElementById('section-label').innerText = title;

      // Scroll to top
      document.getElementById('main').scrollTop = 0;
    }}

    function nextCard() {{
      if (currentCard < totalCards - 1) {{
        currentCard++;
        updateCardView();
      }}
    }}

    function prevCard() {{
      if (currentCard > 0) {{
        currentCard--;
        updateCardView();
      }}
    }}

    function goToCard(idx) {{
      if (idx >= 0 && idx < totalCards) {{
        currentCard = idx;
        updateCardView();
      }}
    }}

    // Keyboard navigation
    document.addEventListener('keydown', (e) => {{
      if (e.key === 'ArrowRight') nextCard();
      else if (e.key === 'ArrowLeft') prevCard();
      else if (e.key === 'Escape') closeLightbox();
    }});

    // Lightbox Modal
    function openLightbox(imgSrc, title) {{
      document.getElementById('modal_img').src = imgSrc;
      document.getElementById('modal_title').innerText = title || 'Slide Figure';
      document.getElementById('lightbox_modal').classList.add('show');
    }}
    function closeLightbox() {{
      document.getElementById('lightbox_modal').classList.remove('show');
    }}

    // Quiz evaluation
    function handleQuiz(el, isCorrect, feedbackId) {{
      const parent = el.parentElement;
      const opts = parent.querySelectorAll('.quiz-option');
      opts.forEach(o => o.classList.add('disabled'));

      if (isCorrect) {{
        el.classList.add('correct');
      }} else {{
        el.classList.add('wrong');
        // highlight correct option
        opts.forEach(o => {{
          if (o.getAttribute('onclick') && o.getAttribute('onclick').includes(', 1,')) {{
            o.classList.add('correct');
          }}
        }});
      }}
      const fb = document.getElementById(feedbackId);
      if (fb) fb.classList.remove('hidden');
    }}

    // Pomodoro Timer
    let timerSec = 25 * 60;
    let timerRunning = false;
    let timerInterval = null;

    function togglePomodoro() {{
      if (timerRunning) {{
        clearInterval(timerInterval);
        timerRunning = false;
      }} else {{
        timerRunning = true;
        timerInterval = setInterval(() => {{
          if (timerSec > 0) {{
            timerSec--;
            const m = Math.floor(timerSec / 60);
            const s = timerSec % 60;
            document.getElementById('timer-display').innerText = `${{m < 10 ? '0' : ''}}${{m}}:${{s < 10 ? '0' : ''}}${{s}}`;
          }} else {{
            clearInterval(timerInterval);
            timerRunning = false;
            alert('🎉 Pomodoro Session Completed! Take a 5-minute breather.');
            timerSec = 25 * 60;
            document.getElementById('timer-display').innerText = '25:00';
          }}
        }}, 1000);
      }}
    }}

    // Initialize
    updateCardView();
  </script>
</body>
</html>
"""
    out_file = os.path.join(STUDY_DIR, f"{lec_slug}.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"  [+] Generated {out_file} ({len(screens)} screens, {total_slides} slides)")
    return out_file

def generate_curriculum_home():
    cards_html = ""
    for idx, lec in enumerate(METADATA, 1):
        slides_count = len(lec["slides"])
        diags_count = lec.get("diagram_count", 0)
        v_count = len(lec.get("videos", []))
        v_badge = f"<span class='badge-cyan px-2 py-0.5 rounded text-[10px] font-mono'>▶️ {v_count} Video(s)</span>" if v_count > 0 else ""

        cards_html += f"""
        <div class="eco-card p-5 flex flex-col justify-between group">
          <div>
            <div class="flex items-center justify-between gap-2 mb-2">
              <span class="badge-emerald px-2.5 py-1 rounded text-xs font-mono font-bold">Module {lec['id']}</span>
              <div class="flex items-center gap-1.5">
                {v_badge}
                <span class="badge-teal px-2 py-0.5 rounded text-[10px] font-mono">{lec['difficulty']}</span>
              </div>
            </div>
            <h3 class="text-base font-bold text-white group-hover:text-emerald-400 transition-all mb-2 flex items-center gap-2">
              <span>{lec['icon']}</span>
              <span>{lec['title']}</span>
            </h3>
            <p class="text-xs text-slate-300 leading-relaxed mb-4 line-clamp-3">
              {lec['description']}
            </p>
          </div>

          <div class="pt-3 border-t border-emerald-950/80">
            <div class="flex items-center justify-between text-[11px] text-slate-400 mb-3">
              <span>📚 {slides_count} Slides</span>
              <span>🎨 {diags_count} Visuals</span>
              <span>⏱️ {lec['duration']}</span>
            </div>
            <a href="{lec['slug']}.html" class="block w-full py-2 px-3 rounded-lg text-center text-xs font-bold bg-[#091a13] border border-emerald-900 group-hover:bg-gradient-to-r group-hover:from-emerald-600 group-hover:to-teal-600 group-hover:text-white text-emerald-300 transition-all">
              Launch Lecture Module →
            </a>
          </div>
        </div>
        """

    home_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Curriculum Roadmap — Environmental Science & Technology (ES1.101) 🌿</title>
<script src="https://cdn.tailwindcss.com"></script>
<style>
{SHARED_CSS}
</style>
</head>
<body class="selection:bg-emerald-600 selection:text-white min-h-screen">

  <!-- TOP BAR -->
  <header class="sticky top-0 z-50 bg-[#040a07]/90 backdrop-blur-md border-b border-[var(--border)] px-4 py-3">
    <div class="max-w-7xl mx-auto flex items-center justify-between">
      <div class="flex items-center gap-2">
        <span class="text-2xl">🌱</span>
        <div>
          <span class="font-black text-sm md:text-base text-white">Environmental Science & Technology</span>
          <span class="ml-2 text-xs text-emerald-400 font-mono bg-emerald-950/80 px-2 py-0.5 rounded border border-emerald-800">ES1.101 • Monsoon 2026</span>
        </div>
      </div>
      <div class="flex items-center gap-2">
        <a href="../index.html" class="text-xs bg-slate-900 hover:bg-slate-800 text-slate-300 font-bold px-3 py-1.5 rounded-lg border border-slate-700">← Master Portal</a>
        <a href="https://courses.iiit.ac.in/course/view.php?id=5826" target="_blank" class="text-xs bg-amber-600/90 hover:bg-amber-500 text-white font-bold px-3 py-1.5 rounded-lg">🏛️ Moodle</a>
      </div>
    </div>
  </header>

  <!-- HERO SECTION -->
  <div class="max-w-7xl mx-auto px-4 py-8">
    <div class="p-6 md:p-8 bg-gradient-to-br from-[#0c1f17] via-[#091711] to-[#040e0a] border border-emerald-800/60 rounded-2xl mb-8">
      <div class="flex flex-col md:flex-row md:items-center justify-between gap-6">
        <div>
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-950 border border-emerald-800 text-emerald-300 text-xs font-semibold mb-3">
            <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
            12 Interactive Lecture Modules • 444 Primary Slides
          </div>
          <h1 class="text-3xl md:text-4xl font-black text-white tracking-tight mb-2">
            Curriculum Roadmap & Study Navigator
          </h1>
          <p class="text-xs md:text-sm text-slate-300 max-w-2xl leading-relaxed">
            Every lecture deck is transformed into a structured, ADHD-friendly, and mathematically rigorous study suite featuring extracted slide diagrams, KaTeX formulas, active recall flashcards, and playable videos.
          </p>
        </div>

        <!-- CIRCULAR PROGRESS RING -->
        <div class="bg-[#05140d] border border-emerald-900 rounded-xl p-4 flex items-center gap-4 flex-shrink-0">
          <div class="relative w-20 h-20">
            <svg class="w-full h-full transform -rotate-90">
              <circle cx="40" cy="40" r="32" stroke="#132b20" stroke-width="6" fill="transparent" />
              <circle cx="40" cy="40" r="32" stroke="#10b981" stroke-width="6" fill="transparent" stroke-dasharray="201" stroke-dashoffset="150" class="transition-all duration-500" id="progress_circle" />
            </svg>
            <span class="absolute inset-0 flex items-center justify-center text-xs font-black text-emerald-400 font-mono" id="progress_pct">25%</span>
          </div>
          <div>
            <div class="text-xs font-bold text-white mb-0.5">Course Completion</div>
            <div class="text-[11px] text-slate-400">3 of 12 Modules Mastered</div>
            <div class="text-[10px] text-emerald-400 mt-1 font-mono">Status: Midsem Ready</div>
          </div>
        </div>
      </div>
    </div>

    <!-- MODULES GRID -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
      {cards_html}
    </div>
  </div>

  <footer class="mt-12 py-6 border-t border-emerald-950 text-center text-xs text-slate-500">
    Environmental Science & Technology (ES1.101) • IIIT Hyderabad • Built with Course Website Builder
  </footer>
</body>
</html>
"""
    out_file = os.path.join(STUDY_DIR, "00_home.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(home_html)
    print(f"[+] Generated Curriculum Roadmap: {out_file}")

def generate_master_index():
    # Lecture modules cards for index.html
    lec_cards = ""
    for l in METADATA:
        lec_cards += f"""
        <div class="eco-card p-5 flex flex-col justify-between group">
          <div>
            <div class="flex items-center justify-between text-xs mb-2">
              <span class="badge-emerald px-2 py-0.5 rounded font-mono font-bold">Lec {l['id']}</span>
              <span class="text-slate-400 text-[11px]">⏱️ {l['duration']}</span>
            </div>
            <h4 class="text-sm font-bold text-white group-hover:text-emerald-400 transition-all mb-1 flex items-center gap-1.5">
              <span>{l['icon']}</span>
              <span class="truncate">{l['title']}</span>
            </h4>
            <p class="text-xs text-slate-400 line-clamp-2 mb-3">{l['description']}</p>
          </div>
          <div class="pt-2 border-t border-emerald-950 flex items-center justify-between">
            <span class="text-[11px] text-emerald-400 font-mono">📚 {len(l['slides'])} Slides</span>
            <a href="Study_Material/{l['slug']}.html" class="text-xs font-bold text-emerald-300 hover:text-white flex items-center gap-1">
              Explore Module →
            </a>
          </div>
        </div>
        """

    index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Environmental Science & Technology (ES1.101) — Interactive Learning Hub 🌿</title>
<script src="https://cdn.tailwindcss.com"></script>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
<style>
{SHARED_CSS}
</style>
</head>
<body class="selection:bg-emerald-600 selection:text-white min-h-screen">

  <!-- TOP APP BAR -->
  <header class="sticky top-0 z-50 bg-[#040a07]/90 backdrop-blur-md border-b border-[var(--border)] px-4 py-3">
    <div class="max-w-7xl mx-auto flex items-center justify-between">
      <div class="flex items-center gap-2">
        <span class="text-2xl">🌍</span>
        <div>
          <span class="font-black text-sm md:text-base text-white tracking-tight">Environmental Science & Technology</span>
          <span class="hidden md:inline-block ml-2 text-xs text-emerald-400 font-mono bg-emerald-950/80 px-2 py-0.5 rounded border border-emerald-800">ES1.101 • Monsoon 2026</span>
        </div>
      </div>
      <div class="flex items-center gap-2">
        <a href="https://courses.iiit.ac.in/course/view.php?id=5826" target="_blank" rel="noopener noreferrer" class="text-xs bg-amber-600/90 hover:bg-amber-500 text-white font-bold px-3 py-1.5 rounded-lg transition-all flex items-center gap-1 shadow-sm">
          <span>🏛️ Moodle Portal</span>
        </a>
        <a href="Study_Material/00_home.html" class="text-xs bg-emerald-600 hover:bg-emerald-500 text-white font-bold px-3 py-1.5 rounded-lg transition-all flex items-center gap-1 shadow-sm">
          <span>📘 Lectures (12)</span>
        </a>
        <a href="#assignments" class="text-xs bg-teal-700 hover:bg-teal-600 text-white font-bold px-3 py-1.5 rounded-lg transition-all flex items-center gap-1 shadow-sm">
          <span>📂 Projects & Docs</span>
        </a>
      </div>
    </div>
  </header>

  <!-- HERO SECTION -->
  <section class="max-w-7xl mx-auto px-4 pt-8 pb-6">
    <div class="p-6 md:p-10 bg-gradient-to-br from-[#0c241b] via-[#091a13] to-[#040f0b] border border-emerald-800/80 rounded-2xl relative overflow-hidden">
      <div class="relative z-10 max-w-4xl">
        <div class="flex flex-wrap items-center gap-2 mb-4">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-950 border border-emerald-800 text-emerald-300 text-xs font-semibold">
            <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
            Interactive Eco-Tech Learning Platform
          </div>
          <div class="inline-flex items-center gap-1 px-2.5 py-1 rounded-full bg-amber-950/80 border border-amber-800 text-amber-300 text-xs font-semibold">
            <span>🏛️ IIIT Hyderabad</span>
          </div>
        </div>
        
        <h1 class="text-3xl md:text-5xl font-black text-white tracking-tight mb-4 leading-tight">
          Environmental Science & Technology <br/>
          <span class="text-transparent bg-clip-text bg-gradient-to-r from-emerald-400 via-teal-300 to-cyan-400">
            Interactive Study Suite & Visual Archive
          </span>
        </h1>
        <p class="text-sm md:text-base text-emerald-100/90 leading-relaxed mb-3">
          Instructor: <strong class="text-white">Prof. Ramachandra Prasad P</strong> • Teaching Assistants: Nemani Dedeepya, Vastava Kurumeti, Kalakuntla Rishika, Himank Singhvi
        </p>
        <p class="text-xs md:text-sm text-slate-300 leading-relaxed mb-6">
          Bite-sized, ADHD-friendly, and mathematically rigorous. Fully synced with 18 slide decks, 444 primary slides, 770+ extracted figures and diagrams, interactive simulators, active recall flashcards, and Moodle discussion threads.
        </p>

        <!-- STATS BAR -->
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 pt-4 border-t border-emerald-900/60">
          <div class="bg-[#05140d] border border-emerald-900/80 rounded-xl p-3">
            <div class="text-xs text-slate-400">Lecture Modules</div>
            <div class="text-xl font-black text-emerald-400 mt-1">12 Topics</div>
          </div>
          <div class="bg-[#05140d] border border-emerald-900/80 rounded-xl p-3">
            <div class="text-xs text-slate-400">Primary Slides</div>
            <div class="text-xl font-black text-teal-400 mt-1">444 Slides</div>
          </div>
          <div class="bg-[#05140d] border border-emerald-900/80 rounded-xl p-3">
            <div class="text-xs text-slate-400">Extracted Visuals</div>
            <div class="text-xl font-black text-cyan-400 mt-1">770+ Diagrams</div>
          </div>
          <div class="bg-[#05140d] border border-emerald-900/80 rounded-xl p-3">
            <div class="text-xs text-slate-400">Announcements</div>
            <div class="text-xl font-black text-amber-400 mt-1">18 Synced</div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- EXAM & ANNOUNCEMENTS DIGEST -->
  <section class="max-w-7xl mx-auto px-4 py-4">
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
      
      <!-- Midsem & Endsem Syllabus -->
      <div class="eco-card p-6 border-emerald-800">
        <div class="flex items-center gap-2 mb-3">
          <span class="text-xl">📋</span>
          <h3 class="text-lg font-bold text-white">Official Exam Syllabus Breakdown</h3>
        </div>
        <div class="space-y-3 text-xs">
          <div class="p-3 bg-[#06140e] border border-emerald-900/80 rounded-xl">
            <div class="flex justify-between items-center mb-1">
              <strong class="text-emerald-400 font-bold">Midsem Exam Syllabus (Covered)</strong>
              <span class="badge-emerald px-2 py-0.5 rounded text-[10px]">Lectures 1 to 7</span>
            </div>
            <p class="text-slate-300">Overview & 2070 Vision, Earth Spheres & Thermodynamics, Pollution & Particulates, Remote Sensing & GIS, Landmark Events (Bhopal, Chernobyl, Minamata), Biogeochemical Cycles, Climate Impacts.</p>
          </div>
          <div class="p-3 bg-[#06140e] border border-teal-900/80 rounded-xl">
            <div class="flex justify-between items-center mb-1">
              <strong class="text-teal-300 font-bold">Endsem Exam Focus (Advanced)</strong>
              <span class="badge-teal px-2 py-0.5 rounded text-[10px]">Lectures 8 to 12</span>
            </div>
            <p class="text-slate-300">Unexpected Climate Changes & Tipping Points (AMOC), Terrestrial Carbon Sinks & Biochar, Clean Development Mechanism (CDM) & Ocean Injection, Clean Tech Solutions, EIA Framework.</p>
          </div>
        </div>
      </div>

      <!-- Live Announcements Digest -->
      <div class="eco-card p-6 border-emerald-800">
        <div class="flex items-center justify-between mb-3">
          <div class="flex items-center gap-2">
            <span class="text-xl">📢</span>
            <h3 class="text-lg font-bold text-white">Moodle Announcements Digest</h3>
          </div>
          <span class="text-xs text-emerald-400 font-mono">18 Threads Synced</span>
        </div>
        <div class="space-y-2 text-xs max-h-48 overflow-y-auto pr-1">
          <div class="p-2.5 bg-[#06140e] border border-emerald-950 rounded-lg">
            <div class="font-bold text-slate-200">Midsem Paper Showing & Makeup Exam Syllabus</div>
            <div class="text-slate-400 text-[11px]">Prof. Ramachandra Prasad P: Confirmed makeup exam covers Lectures 1–7.</div>
          </div>
          <div class="p-2.5 bg-[#06140e] border border-emerald-950 rounded-lg">
            <div class="font-bold text-slate-200">Course Project Mid-Evaluation Guidelines</div>
            <div class="text-slate-400 text-[11px]">Kalakuntla Rishika: Expecting 50-60% completion (Problem statement, data, methodology).</div>
          </div>
          <div class="p-2.5 bg-[#06140e] border border-emerald-950 rounded-lg">
            <div class="font-bold text-slate-200">Quiz-1 Paper Showing & Makeup Exam</div>
            <div class="text-slate-400 text-[11px]">Seating arrangements and evaluation guidelines released.</div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- LECTURE MODULES GRID -->
  <section class="max-w-7xl mx-auto px-4 py-8">
    <div class="flex flex-wrap items-center justify-between gap-4 mb-6">
      <div>
        <h2 class="text-2xl font-black text-white">Interactive Lecture Modules (1 to 12)</h2>
        <p class="text-xs text-slate-400">Complete curriculum with real slide figures, KaTeX math, active recall cards, and interactive simulators.</p>
      </div>
      <a href="Study_Material/00_home.html" class="text-xs bg-emerald-600 hover:bg-emerald-500 text-white font-bold px-4 py-2 rounded-lg flex items-center gap-1 shadow-md">
        <span>View Full Curriculum Roadmap →</span>
      </a>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
      {lec_cards}
    </div>
  </section>

  <!-- ASSIGNMENTS & PROJECT TRACKER -->
  <section id="assignments" class="max-w-7xl mx-auto px-4 py-8">
    <div class="eco-card p-6 border-emerald-800">
      <div class="flex items-center justify-between mb-4 pb-3 border-b border-emerald-900">
        <div>
          <h2 class="text-xl font-bold text-white flex items-center gap-2">
            <span>📂</span> Course Project & Literature Review Tracker
          </h2>
          <p class="text-xs text-slate-300">Track guidelines, deliverables, and submissions for Monsoon 2026.</p>
        </div>
        <span class="badge-emerald px-3 py-1 rounded text-xs font-mono font-bold">Assignments</span>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div class="p-4 bg-[#05140d] border border-emerald-900 rounded-xl">
          <div class="flex justify-between items-center mb-2">
            <strong class="text-emerald-400 text-sm">Course Project (EST 2026)</strong>
            <span class="badge-amber px-2 py-0.5 rounded text-[10px] font-mono">50-60% Mid-Evaluation</span>
          </div>
          <p class="text-xs text-slate-300 mb-3 leading-relaxed">
            Hands-on environmental modeling project. Focus areas: Paleoclimate reconstruction, pollen binning, and climate trend analysis.
          </p>
          <div class="flex flex-wrap gap-2 text-[11px]">
            <a href="Course_Materials/EVS-Projects-2026.docx" class="text-emerald-300 hover:underline">📄 EVS-Projects-2026.docx</a>
            <span class="text-slate-500">•</span>
            <a href="Assignments/EST-PROJECT/" class="text-emerald-300 hover:underline">📁 Project Workspace</a>
          </div>
        </div>

        <div class="p-4 bg-[#05140d] border border-emerald-900 rounded-xl">
          <div class="flex justify-between items-center mb-2">
            <strong class="text-teal-300 text-sm">Literature Review Assignment</strong>
            <span class="badge-emerald px-2 py-0.5 rounded text-[10px] font-mono">Format: team_name.pdf</span>
          </div>
          <p class="text-xs text-slate-300 mb-3 leading-relaxed">
            In-depth academic literature review summarizing contemporary research papers on climate change mitigation, remote sensing, and carbon sequestration.
          </p>
          <div class="flex flex-wrap gap-2 text-[11px]">
            <a href="Course_Materials/Literature Review Assignment.docx" class="text-teal-300 hover:underline">📄 Literature Review Assignment.docx</a>
            <span class="text-slate-500">•</span>
            <a href="Assignments/Literature Review Submission/instructions.txt" class="text-teal-300 hover:underline">📋 Submission Instructions</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- FOOTER -->
  <footer class="mt-16 py-8 border-t border-emerald-950 text-center text-xs text-slate-500">
    <p>Environmental Science & Technology (ES1.101) • Department of Civil & Environmental Engineering • IIIT Hyderabad</p>
    <p class="mt-1">Generated with Course Website Builder • Zero External Node Dependencies</p>
  </footer>

</body>
</html>
"""
    out_file = os.path.join(WORKSPACE, "index.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(index_html)
    print(f"[+] Generated Master Portal Hub: {out_file}")

def generate_readme():
    readme_content = """# 🌿 Environmental Science & Technology (ES1.101) — Interactive Study Suite

[![Live Hub](https://img.shields.io/badge/Study%20Suite-Live%20Portal-10b981?style=for-the-badge&logo=safari)](./index.html)
[![Course](https://img.shields.io/badge/Course-ES1.101%20EST-14b8a6?style=for-the-badge)](https://courses.iiit.ac.in/course/view.php?id=5826)
[![Slides](https://img.shields.io/badge/Primary%20Slides-444%20Rendered-f59e0b?style=for-the-badge)](./Lecture_Slides/)
[![Visuals](https://img.shields.io/badge/Extracted%20Visuals-770%2B%20Diagrams-06b6d4?style=for-the-badge)](./Study_Material/assets/diagrams/)
[![Institution](https://img.shields.io/badge/Institution-IIIT%20Hyderabad-blue?style=for-the-badge)](https://www.iiit.ac.in)

A production-grade, zero-dependency educational web application and interactive study suite for **Environmental Science & Technology (ES1.101 / Monsoon 2026)** at IIIT Hyderabad, taught by **Prof. Ramachandra Prasad P**.

---

## 🌟 Key Features

1. **Direct Slide Figures & Visualizations:** Over 770 extracted high-resolution diagrams, flowcharts, spectral curves, and disaster maps directly embedded into concept screens.
2. **Dedicated Lecture Modules (1 to 12):** Separate interactive HTML modules with working Pomodoro timers, progress trackers, active recall 3D flip cards, and multiple-choice quizzes.
3. **Complete Slide Reference Galleries:** Every lecture module ends with an interactive gallery of all slide pages from the original presentations with one-click full-screen lightbox zoom.
4. **Playable Video Masterclasses:** Embedded responsive video players for all YouTube lectures and documentary references found in the slide decks.
5. **Interactive Physics & Environmental Simulators:**
   - ⚡ *Planetary Decarbonization 2070 Pathway Simulator*
   - 🌐 *Earth Radiation Budget & Greenhouse Equilibrium Calculator*
   - 🏭 *Air Quality Index (AQI) & Plume Dispersion Calculator*
   - 🛰️ *Multispectral Remote Sensing & NDVI Visualizer*
   - ⚠️ *Toxic Chemical Exposure & Gaussian Plume Model (Bhopal Scenario)*
   - 🔄 *Biogeochemical Nutrient Flux Model*
   - 🌡️ *Sea Level Rise & Thermal Expansion Model*
   - ⚡ *AMOC Tipping Element Hysteresis Explorer*
   - 🌲 *Terrestrial Carbon Sink & Biochar Calculator*
   - 🌊 *Clean Development Mechanism (CDM) Additionality & Ocean Chemistry*
   - ⚡ *Direct Air Capture (DAC) Energy Efficacy Evaluator*
   - 📋 *EIA Leopold Matrix & Significance Evaluator*
6. **Eco-Tech Visual Design System:** Dark biosphere theme with Emerald (`#10b981`), Forest Green, Earth Amber, and Ocean Cyan palette.

---

## 📚 Curriculum Breakdown

| Module | Title | Primary Slide Decks | Key Interactive Features |
| :---: | :--- | :--- | :--- |
| **01** | [Course Overview & Vision 2070](./Study_Material/01_course_overview_vision_2070.html) | `Class-1 Overview`, `Class-1-Year_2070` (54 slides) | Decarbonization pathway simulator, Panchamrit targets |
| **02** | [Earth Spheres & Thermodynamics](./Study_Material/02_comprehending_environment_spheres.html) | `Class-2-Part-1, 2, 3` (57 slides) | Radiation balance model, Stefan-Boltzmann calculator |
| **03** | [Pollution & Anthropogenic Pressures](./Study_Material/03_environmental_issues_anthropogenic_pressures.html) | `Class-3-Part-1, 2` (34 slides) | AQI calculator, Streeter-Phelps oxygen sag curve |
| **04** | [Remote Sensing & GIS](./Study_Material/04_remote_sensing_gis_monitoring.html) | `Class-4-RS-EVS-upload` (18 slides) | Spectral reflectance curve, NDVI live classifier |
| **05** | [Landmark Environmental Disasters](./Study_Material/05_environmental_events_crises_disasters.html) | `Class-5 -Environmental Events` (30 slides) | Bhopal MIC runaway kinetics, Gaussian plume tool |
| **06** | [Biogeochemical Cycles](./Study_Material/06_earth_components_biogeochemical_cycles.html) | `Class-6 Earth components-Part-1, 2` (41 slides) | Nitrogen & carbon flux perturbator, Redfield ratio |
| **07** | [Climate Change Impacts](./Study_Material/07_climate_change_impacts_vulnerability.html) | `Class-7 Climate Change impacts` (31 slides) | Radiative forcing formula, Sea level rise model |
| **08** | [Unexpected Climate Tipping Points](./Study_Material/08_unexpected_climate_changes_tipping_points.html) | `Class-8 Unexpected climate changes` (30 slides) | AMOC Stommel bifurcation & hysteresis explorer |
| **09** | [Carbon Sequestration & Sinks](./Study_Material/09_carbon_sequestration_terrestrial_sinks.html) | `Class-9- Carbon sequestration` (34 slides) | Geological CCS trapping stages, biochar calculator |
| **10** | [CDM & Ocean Sequestration](./Study_Material/10_cdm_carbon_markets_ocean_sequestration.html) | `Class-10- CDM`, `Class-10b-Ocean` (54 slides) | Additionality proof, ocean acidification model |
| **11** | [Climate Technology Solutions](./Study_Material/11_climate_technology_solutions_cleantech.html) | `Class-11-Climate Change-Technology` (29 slides) | Direct Air Capture thermodynamics, Green hydrogen |
| **12** | [EIA Framework & Protocols](./Study_Material/12_eia_framework_methodology_protocols.html) | `Class-12 EIA` (32 slides) | Leopold matrix calculator, 8-stage EIA lifecycle |

---

## 🚀 How to Run Locally

Because the study suite uses zero external build dependencies (pure HTML5, CSS3, and Vanilla JavaScript with CDN Tailwind and KaTeX), it runs directly:

```powershell
# Option 1: Open index.html directly in browser
start index.html

# Option 2: Run local lightweight Python server
python -m http.server 8000
# Then open http://localhost:8000
```

---

## 🌐 Deploy to GitHub Pages

To publish this website live to GitHub Pages:
```powershell
./DEPLOY_GITHUB_PAGES.bat
```
"""
    out_file = os.path.join(WORKSPACE, "README.md")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(readme_content)
    print(f"[+] Generated comprehensive README.md: {out_file}")

if __name__ == "__main__":
    print("\n==========================================")
    print("Building Full Interactive Course Website")
    print("==========================================")
    for l in METADATA:
        generate_lecture_page(l)
    generate_curriculum_home()
    generate_master_index()
    generate_readme()
    print("\n[+] Build Complete! All pages generated successfully.")
