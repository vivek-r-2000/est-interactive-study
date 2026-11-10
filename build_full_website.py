import os
import json
import re
import html

WORKSPACE = r"C:\Users\vivek\EST"
METADATA_PATH = os.path.join(WORKSPACE, "Study_Material", "lectures_metadata.json")
STUDY_DIR = os.path.join(WORKSPACE, "Study_Material")

with open(METADATA_PATH, "r", encoding="utf-8") as f:
    METADATA = json.load(f)

with open(os.path.join(STUDY_DIR, "full_slide_database.json"), "r", encoding="utf-8") as f:
    SLIDE_DB = json.load(f)

# Import lecture contents and simulators for all 15 lectures
from lecture_content_data_1 import LECTURE_DETAILS as D1
from lecture_content_data_2 import LECTURE_DETAILS_2 as D2
from lecture_content_data_3 import LECTURE_DETAILS_3 as D3
from lecture_content_data_4 import LECTURE_DETAILS_4 as D4

from simulators_data import SIMULATORS as S1
from simulators_data_2 import SIMULATORS_2 as S2
from simulators_data_3 import SIMULATORS_3 as S3
from simulators_data_4 import SIMULATORS_4 as S4

from diagram_explanations import DIAGRAM_EXPLANATIONS

ALL_DETAILS = {}
ALL_DETAILS.update(D1)
ALL_DETAILS.update(D2)
ALL_DETAILS.update(D3)
ALL_DETAILS.update(D4)

ALL_SIMS = {}
ALL_SIMS.update(S1)
ALL_SIMS.update(S2)
ALL_SIMS.update(S3)
ALL_SIMS.update(S4)

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
    details = ALL_DETAILS.get(lec_id, {})
    sim_html = ALL_SIMS.get(f"sim_{lec_id}", ALL_SIMS.get(lec_id, "<p class='text-slate-400'>Interactive model loaded.</p>"))

    all_lec_slides = SLIDE_DB.get(lec_id, {}).get("slides", [])
    total_slides = len(all_lec_slides)

    videos = lec.get("videos", [])
    video_embeds = []
    for v in videos:
        emb = get_youtube_embed(v)
        if emb:
            video_embeds.append({"url": v, "embed": emb})

    screens = []
    sidebar_links = []

    # ========================================================
    # SCREEN 0: LECTURE OVERVIEW & SYLLABUS ROADMAP
    # ========================================================
    int_info = details.get("intuition", {})
    
    # Quick visual slide table
    quick_slides_html = ""
    for idx, s in enumerate(all_lec_slides[:12]):
        quick_slides_html += f"""
        <div class="p-2.5 rounded-lg bg-[#081711] border border-emerald-900/60 flex items-center justify-between gap-2 hover:border-emerald-600 transition-all cursor-pointer" onclick="goToCard({idx + 1})">
          <div class="flex items-center gap-2 truncate">
            <span class="badge-emerald px-1.5 py-0.5 rounded text-[10px] font-mono font-bold flex-shrink-0">#{s['slide_num']}</span>
            <span class="text-xs text-white truncate">{html.escape(s['title'])}</span>
          </div>
          <span class="text-[10px] text-emerald-400 font-mono flex-shrink-0">Study →</span>
        </div>
        """

    video_section_html = ""
    if video_embeds:
        v_cards = ""
        for v in video_embeds:
            v_cards += f"""
            <div class="p-3 bg-[#05120d] border border-emerald-900/80 rounded-xl">
              <div class="flex items-center justify-between mb-2">
                <span class="text-xs font-bold text-emerald-300 font-mono">▶️ Professor Lecture Video</span>
                <a href="{v['url']}" target="_blank" rel="noopener noreferrer" class="text-[11px] text-emerald-400 hover:underline">Open YouTube ↗</a>
              </div>
              <div class="relative w-full aspect-video bg-black rounded-lg overflow-hidden">
                <iframe src="{v['embed']}" class="w-full h-full" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
              </div>
            </div>
            """
        video_section_html = f"""
        <div class="mb-6">
          <div class="text-xs font-bold text-emerald-300 font-mono uppercase tracking-wider mb-2">📹 Lecture Video Reference</div>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            {v_cards}
          </div>
        </div>
        """

    screens.append(f"""
    <section class="card-screen active" data-title="1. Lecture Scope & Roadmap">
      <div class="eco-card p-6 md:p-8 border-emerald-800/80 mb-6">
        <div class="flex flex-wrap items-center justify-between gap-3 mb-3">
          <div class="flex items-center gap-2">
            <span class="badge-emerald px-2.5 py-1 rounded text-xs font-mono font-bold">Lecture {lec_id} • Syllabus Roadmap</span>
            <span class="text-xs text-slate-400">• {lec['difficulty']} • {lec['duration']}</span>
          </div>
          <span class="badge-teal px-2.5 py-1 rounded text-xs font-mono">📚 {total_slides} Slides Covered Slidewise</span>
        </div>

        <h2 class="text-2xl md:text-3xl font-black text-white mb-2">{int_info.get('title', lec_title)}</h2>
        <div class="text-emerald-400 text-sm font-semibold mb-4">{int_info.get('subtitle', '')}</div>
        
        <div class="p-4 bg-[#05140d] border-l-4 border-emerald-500 rounded-r-xl mb-6 text-emerald-100 text-xs md:text-sm leading-relaxed">
          <strong class="text-emerald-300 block mb-1">💡 Why This Lecture Matters:</strong>
          {int_info.get('why', '')}
        </div>

        {video_section_html}

        <div class="mb-4">
          <div class="flex items-center justify-between mb-3">
            <span class="text-xs font-bold text-emerald-300 font-mono uppercase tracking-wider">Slide Navigation Directory</span>
            <button onclick="goToCard(1)" class="text-xs font-bold text-emerald-400 hover:underline">Start Slide 1 →</button>
          </div>
          <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-2">
            {quick_slides_html}
          </div>
          <div class="text-center mt-3">
            <button onclick="goToCard(1)" class="px-5 py-2.5 bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white font-bold text-xs rounded-xl shadow-lg shadow-emerald-950 transition-all cursor-pointer">
              Launch Slidewise Learning (Slide 1 of {total_slides}) →
            </button>
          </div>
        </div>
      </div>
    </section>
    """)
    sidebar_links.append((0, "📌 1. Lecture Overview & Roadmap"))

    # ========================================================
    # SCREENS 1 to N: DEDICATED SLIDE-BY-SLIDE LEARNING CARDS
    # ========================================================
    for s_idx, s in enumerate(all_lec_slides):
        card_num = s_idx + 1
        slide_num = s["slide_num"]
        title_esc = html.escape(s["title"])
        img_path = s["image"]
        bullets = s.get("bullets", [])
        deep_exp = s.get("deep_explanation", "")

        # Bullets formatting
        if bullets:
            bullets_html = "".join([f'<li class="flex items-start gap-2 text-slate-200"><span class="text-emerald-400 font-bold mt-0.5">•</span><span class="leading-relaxed">{html.escape(b)}</span></li>' for b in bullets])
            bullets_wrap = f'<ul class="space-y-2 text-xs md:text-sm">{bullets_html}</ul>'
        else:
            bullets_wrap = '<p class="text-slate-400 italic text-xs">Visual figure / diagram presentation slide. Review the high-resolution render on the left.</p>'

        # Build Slide Dropdown options
        dropdown_opts = ""
        for opt_idx, opt_s in enumerate(all_lec_slides):
            sel = "selected" if opt_idx == s_idx else ""
            opt_title = opt_s['title'][:32] + "..." if len(opt_s['title']) > 35 else opt_s['title']
            dropdown_opts += f'<option value="{opt_idx + 1}" {sel}>Slide {opt_s["slide_num"]}: {html.escape(opt_title)}</option>'

        # Next / Prev labels
        prev_card_idx = card_num - 1
        next_card_idx = card_num + 1

        nav_footer_html = f"""
        <div class="flex items-center justify-between gap-3 pt-4 border-t border-emerald-900/60 mt-4">
          <button onclick="goToCard({prev_card_idx})" class="px-4 py-2 rounded-lg bg-[#071912] border border-emerald-900 text-slate-300 hover:text-white hover:border-emerald-500 text-xs font-mono transition-all">
            ← Previous {f"(Slide {slide_num-1})" if s_idx > 0 else "(Overview)"}
          </button>
          <div class="text-xs font-mono text-emerald-400">
            Slide {slide_num} of {total_slides}
          </div>
          <button onclick="goToCard({next_card_idx})" class="px-4 py-2 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold transition-all shadow-md shadow-emerald-950">
            {f"Next (Slide {slide_num+1}) →" if s_idx < total_slides - 1 else "Continue to Interactive Lab →"}
          </button>
        </div>
        """

        screens.append(f"""
        <section class="card-screen" data-title="Slide {slide_num}: {title_esc[:25]}">
          <div class="eco-card p-5 md:p-7 border-emerald-800/80 mb-6">
            <!-- Header bar with Jump selector -->
            <div class="flex flex-wrap items-center justify-between gap-2 pb-3 mb-4 border-b border-emerald-900/60">
              <div class="flex items-center gap-2">
                <span class="badge-emerald px-2.5 py-1 rounded text-xs font-mono font-bold">Slide {slide_num} of {total_slides}</span>
                <span class="text-xs text-slate-400 font-mono hidden sm:inline">{s['source_file']}</span>
              </div>
              <div class="flex items-center gap-2">
                <label for="slide_select_{slide_num}" class="text-[11px] text-slate-400 font-mono hidden md:inline">Jump to:</label>
                <select id="slide_select_{slide_num}" onchange="goToCard(parseInt(this.value))" class="bg-[#05140e] border border-emerald-800 text-emerald-300 text-xs rounded px-2.5 py-1 font-mono focus:outline-none focus:border-emerald-500">
                  {dropdown_opts}
                </select>
                <button onclick="prevCard()" class="px-2 py-1 rounded bg-[#071a12] border border-emerald-800 text-emerald-300 text-xs hover:bg-emerald-800 font-mono" title="Previous Slide">◀</button>
                <button onclick="nextCard()" class="px-2 py-1 rounded bg-[#071a12] border border-emerald-800 text-emerald-300 text-xs hover:bg-emerald-800 font-mono" title="Next Slide">▶</button>
              </div>
            </div>

            <!-- Slide Showcase Split Layout -->
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
              <!-- Left: Slide Image -->
              <div class="lg:col-span-6 bg-black/60 border border-emerald-900/80 rounded-xl p-2.5 flex flex-col items-center justify-center cursor-pointer group" onclick="openLightbox('{img_path}', 'Slide {slide_num}: {title_esc}')">
                <img src="{img_path}" alt="Slide {slide_num}: {title_esc}" class="w-full h-auto max-h-[460px] object-contain rounded group-hover:scale-[1.01] transition-all" loading="lazy">
                <div class="w-full flex items-center justify-between text-[11px] text-emerald-400 font-mono mt-2.5 px-1">
                  <span class="flex items-center gap-1"><span>🔍</span> Click or press <kbd class="px-1.5 py-0.5 rounded bg-emerald-950 border border-emerald-700 text-emerald-300 font-mono text-[10px]">Z</kbd> for lightbox</span>
                  <span class="text-slate-400 text-[10px]">High-Res Render</span>
                </div>
              </div>

              <!-- Right: Bullets & Deep Explanation -->
              <div class="lg:col-span-6 space-y-4">
                <!-- Official Slide Title -->
                <div class="p-3.5 bg-[#081a13] border-l-4 border-emerald-500 rounded-r-xl">
                  <span class="text-[10px] uppercase font-bold text-emerald-400 font-mono block mb-0.5">Slide Title</span>
                  <h3 class="text-base md:text-lg font-bold text-white leading-snug">{title_esc}</h3>
                </div>

                <!-- Verbatim Slide Content & Bullets -->
                <div class="p-4 bg-[#0a2017] border border-emerald-900/60 rounded-xl">
                  <span class="text-[10px] uppercase font-bold text-teal-300 font-mono block mb-2">📝 Slide Content & Key Bullet Points</span>
                  {bullets_wrap}
                </div>

                <!-- Deep Pedagogical Breakdown & Professor Explanation -->
                <div class="p-4 bg-[#071912] border border-emerald-800/80 rounded-xl text-xs md:text-sm text-emerald-100 leading-relaxed">
                  <span class="text-[10px] uppercase font-bold text-emerald-400 font-mono block mb-1.5">💡 Scientific Breakdown & Teaching Analysis</span>
                  <p class="text-slate-200">{deep_exp}</p>
                </div>
              </div>
            </div>

            <!-- Footer navigation -->
            {nav_footer_html}
          </div>
        </section>
        """)
        sidebar_links.append((card_num, f"Slide {slide_num}: {s['title'][:26]}"))

    # ========================================================
    # SCREEN: INTERACTIVE SIMULATOR LAB
    # ========================================================
    cur_idx = len(screens)
    screens.append(f"""
    <section class="card-screen" data-title="🧪 Interactive Simulator Lab">
      <div class="mb-6">
        {sim_html}
      </div>
    </section>
    """)
    sidebar_links.append((cur_idx, "🧪 Interactive Simulator Lab"))

    # ========================================================
    # SCREEN: ACTIVE RECALL FLASHCARDS
    # ========================================================
    cur_idx = len(screens)
    f_cards_html = ""
    for f in details.get("flashcards", []):
        f_cards_html += f"""
        <div class="flip-card-wrap mb-4" onclick="this.classList.toggle('flipped')">
          <div class="flip-card-inner">
            <div class="flip-face flip-front">
              <span class="text-xs uppercase font-bold text-emerald-400 tracking-wider mb-2">Question (Click / Space to Flip)</span>
              <div class="text-sm md:text-base font-bold text-white mb-2">{f['q']}</div>
              <span class="text-[11px] text-slate-400 mt-2">🔄 Click card to reveal answer</span>
            </div>
            <div class="flip-face flip-back">
              <span class="text-xs uppercase font-bold text-teal-300 tracking-wider mb-2">Answer</span>
              <div class="text-xs md:text-sm font-semibold text-emerald-100 leading-relaxed">{f['a']}</div>
            </div>
          </div>
        </div>
        """

    screens.append(f"""
    <section class="card-screen" data-title="🗂️ Active Recall Flashcards">
      <div class="eco-card p-6 md:p-8 border-emerald-800/80 mb-6">
        <div class="badge-emerald inline-block px-2.5 py-1 rounded text-xs font-mono font-bold mb-3">Spaced Repetition</div>
        <h2 class="text-2xl font-black text-white mb-2">Active Recall Flashcards</h2>
        <p class="text-xs text-slate-300 mb-6">Test yourself on essential slide definitions, reactions, and principles before flipping.</p>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          {f_cards_html}
        </div>
      </div>
    </section>
    """)
    sidebar_links.append((cur_idx, "🗂️ Active Recall Flashcards"))

    # ========================================================
    # SCREEN: HIGH-YIELD EXAM TRAPS
    # ========================================================
    cur_idx = len(screens)
    traps_html = "".join([f"<li class='p-3 bg-[#05140d] border border-amber-900/60 rounded-xl text-xs text-slate-200 leading-relaxed mb-3'>{t}</li>" for t in details.get("traps", [])])
    screens.append(f"""
    <section class="card-screen" data-title="⚠️ High-Yield Exam Traps">
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
    sidebar_links.append((cur_idx, "⚠️ High-Yield Exam Traps"))

    # ========================================================
    # SCREEN: CONCEPT CHECK QUIZ
    # ========================================================
    cur_idx = len(screens)
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
    <section class="card-screen" data-title="📝 Concept Check Quiz">
      <div class="eco-card p-6 md:p-8 border-emerald-800/80 mb-6">
        <div class="badge-emerald inline-block px-2.5 py-1 rounded text-xs font-mono font-bold mb-3">Knowledge Verification</div>
        <h2 class="text-2xl font-black text-white mb-2">Concept Check Quiz</h2>
        <p class="text-xs text-slate-300 mb-6">Instant feedback on core conceptual and quantitative questions from the lecture slides.</p>
        <div>
          {quiz_html}
        </div>
      </div>
    </section>
    """)
    sidebar_links.append((cur_idx, "📝 Concept Check Quiz"))

    # ========================================================
    # SCREEN: COMPLETE SLIDE DECK QUICK-JUMP GALLERY
    # ========================================================
    cur_idx = len(screens)
    slides_grid = ""
    for idx, s in enumerate(all_lec_slides):
        slides_grid += f"""
        <div class="bg-[#05140d] border border-emerald-900/80 rounded-xl p-2 flex flex-col justify-between group hover:border-emerald-500 transition-all">
          <div class="overflow-hidden rounded-lg bg-black/50 cursor-pointer relative" onclick="goToCard({idx + 1})">
            <img src="{s['image']}" alt="Slide {s['slide_num']}" class="w-full h-28 object-contain group-hover:scale-105 transition-all" loading="lazy">
            <div class="absolute inset-0 bg-emerald-950/20 opacity-0 group-hover:opacity-100 transition-all flex items-center justify-center">
              <span class="bg-black/80 text-emerald-300 text-[10px] px-2 py-0.5 rounded-full font-mono">📖 Study Card</span>
            </div>
          </div>
          <div class="pt-2 px-1">
            <div class="flex items-center justify-between text-[10px] text-slate-400 font-mono mb-1">
              <span class="text-emerald-400 font-bold">Slide #{s['slide_num']}</span>
              <span class="truncate max-w-[100px]">{s['source_file']}</span>
            </div>
            <div class="text-[11px] font-semibold text-slate-200 line-clamp-1" title="{html.escape(s['title'])}">{s['title']}</div>
          </div>
        </div>
        """

    file_badges = " ".join([f"<a href='../Lecture_Slides/{f}' target='_blank' class='inline-flex items-center gap-1.5 px-3 py-1 rounded-lg bg-emerald-950/80 border border-emerald-800 text-emerald-300 text-xs font-mono hover:bg-emerald-900 transition-all'><span>📄 Download {f}</span></a>" for f in lec['files']])

    screens.append(f"""
    <section class="card-screen" data-title="📚 Slide Quick-Jump Gallery">
      <div class="eco-card p-6 md:p-8 border-emerald-800/80 mb-6">
        <div class="flex flex-wrap items-center justify-between gap-3 mb-4 pb-3 border-b border-emerald-900/80">
          <div>
            <div class="badge-emerald inline-block px-2.5 py-1 rounded text-xs font-mono font-bold mb-1">📚 Master Slide Reference</div>
            <h2 class="text-2xl font-black text-white">Complete Slide Deck Quick-Jump Gallery</h2>
            <p class="text-xs text-slate-300">Quick visual reference of all {total_slides} slides across this lecture deck with PDF downloads.</p>
          </div>
          <div class="flex flex-wrap gap-2">
            {file_badges}
          </div>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-3">
          {slides_grid}
        </div>
      </div>
    </section>
    """)
    sidebar_links.append((cur_idx, f"📚 Slide Gallery ({total_slides} Slides)"))

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
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body, {{delimiters: [{{left: '$$', right: '$$', display: true}}, {{left: '$', right: '$', display: false}}]}});"></script>

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
    width: 280px; min-width: 280px; background: #040b08;
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
    flex: 1; overflow-y: auto; padding: 24px 20px 100px 20px;
    display: flex; flex-direction: column; align-items: center;
  }}
  .card-screen {{ display: none; width: 100%; max-width: 1050px; animation: fadeIn .2s ease; }}
  .card-screen.active {{ display: block; }}
  @keyframes fadeIn {{ from {{ opacity:0; transform:translateY(6px); }} to {{ opacity:1; transform:translateY(0); }} }}

  /* Nav Bar */
  #nav-bar {{
    position: fixed; bottom: 0; left: 280px; right: 0;
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
    <button class="nav-btn px-5 py-2 rounded-lg text-xs font-bold border border-emerald-900 bg-[#071710] text-slate-300 hover:border-emerald-500 transition-all cursor-pointer" onclick="prevCard()">← Previous</button>
    <span id="card-counter" class="text-xs text-slate-400 font-mono">Card 1 of {len(screens)}</span>
    <button class="nav-btn px-5 py-2 rounded-lg text-xs font-bold bg-gradient-to-r from-emerald-600 to-teal-600 text-white hover:opacity-90 transition-all shadow-md shadow-emerald-950 cursor-pointer" onclick="nextCard()">Next Card →</button>
    <span class="text-[11px] text-slate-500 font-mono hidden md:inline ml-2">Keys: <kbd class="px-1 bg-emerald-950 border border-emerald-800 rounded text-emerald-300">←</kbd> <kbd class="px-1 bg-emerald-950 border border-emerald-800 rounded text-emerald-300">→</kbd> <kbd class="px-1 bg-emerald-950 border border-emerald-800 rounded text-emerald-300">Z</kbd></span>
  </nav>

  <!-- LIGHTBOX MODAL -->
  <div id="lightbox_modal" class="slide-modal-backdrop" onclick="closeLightbox(event)">
    <div class="relative max-w-5xl w-full bg-[#07130e] border border-emerald-800 rounded-2xl overflow-hidden p-3 shadow-2xl" onclick="event.stopPropagation()">
      <div class="flex items-center justify-between pb-2 mb-2 border-b border-emerald-900/80">
        <span id="modal_title" class="text-sm font-bold text-emerald-300 font-mono truncate">Slide Preview</span>
        <button class="text-slate-400 hover:text-white px-2 py-1 text-sm font-bold bg-emerald-950 rounded cursor-pointer" onclick="closeLightbox()">✕ Close</button>
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

      for (let i = 0; i < totalCards; i++) {{
        const el = document.getElementById('slink_' + i);
        if (el) {{
          el.classList.toggle('active', i === currentCard);
          if (i === currentCard) {{
            el.scrollIntoView({{ block: 'nearest', behavior: 'smooth' }});
          }}
        }}
      }}

      document.getElementById('card-counter').innerText = `Card ${{currentCard + 1}} of ${{totalCards}}`;
      const pct = Math.round(((currentCard) / (totalCards - 1)) * 100);
      document.getElementById('progress-bar-fill').style.width = pct + '%';
      document.getElementById('progress-label').innerText = pct + '%';
      
      const title = screens[currentCard].getAttribute('data-title') || `Section ${{currentCard + 1}}`;
      document.getElementById('section-label').innerText = title;

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

    document.addEventListener('keydown', (e) => {{
      if (e.key === 'ArrowRight') nextCard();
      else if (e.key === 'ArrowLeft') prevCard();
      else if (e.key === 'Escape') closeLightbox();
      else if (e.key === 'z' || e.key === 'Z') {{
        const modal = document.getElementById('lightbox_modal');
        if (modal.classList.contains('show')) {{
          closeLightbox();
        }} else {{
          const activeScreen = screens[currentCard];
          const img = activeScreen.querySelector('img');
          if (img) {{
            openLightbox(img.src, img.alt);
          }}
        }}
      }}
    }});

    function openLightbox(imgSrc, title) {{
      document.getElementById('modal_img').src = imgSrc;
      document.getElementById('modal_title').innerText = title || 'Slide Figure';
      document.getElementById('lightbox_modal').classList.add('show');
    }}
    function closeLightbox() {{
      document.getElementById('lightbox_modal').classList.remove('show');
    }}

    function handleQuiz(el, isCorrect, feedbackId) {{
      const parent = el.parentElement;
      const opts = parent.querySelectorAll('.quiz-option');
      opts.forEach(o => o.classList.add('disabled'));

      if (isCorrect) {{
        el.classList.add('correct');
      }} else {{
        el.classList.add('wrong');
        opts.forEach(o => {{
          if (o.getAttribute('onclick') && o.getAttribute('onclick').includes(', 1,')) {{
            o.classList.add('correct');
          }}
        }});
      }}
      const fb = document.getElementById(feedbackId);
      if (fb) fb.classList.remove('hidden');
    }}

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

    updateCardView();
  </script>
</body>
</html>
"""
    out_file = os.path.join(STUDY_DIR, f"{lec_slug}.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"  [+] Generated {out_file} ({len(screens)} screens, {total_slides} slides covered slidewise)")
    return out_file

def generate_curriculum_home():
    total_slides_all = sum(len(lec["slides"]) for lec in METADATA)
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
              <span>📚 {slides_count} Slides Slidewise</span>
              <span>🧪 1 Simulator Lab</span>
              <span>⏱️ {lec['duration']}</span>
            </div>
            <a href="{lec['slug']}.html" class="block w-full py-2 px-3 rounded-lg text-center text-xs font-bold bg-[#091a13] border border-emerald-900 group-hover:bg-gradient-to-r group-hover:from-emerald-600 group-hover:to-teal-600 group-hover:text-white text-emerald-300 transition-all">
              Launch Lecture Module ({slides_count} Slides) →
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
        <a href="../quiz3_practice_suite.html" class="text-xs bg-gradient-to-r from-emerald-500 to-teal-500 hover:from-emerald-400 text-white font-bold px-3 py-1.5 rounded-lg transition-all flex items-center gap-1 shadow-sm mr-1"><span>⚡ Quiz 3 Prep Suite</span></a>
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
            15 Interactive Lecture Modules • {total_slides_all} Slides Systematically Taught Slidewise
          </div>
          <h1 class="text-3xl md:text-4xl font-black text-white tracking-tight mb-2">
            Curriculum Roadmap & Slide Navigator
          </h1>
          <p class="text-xs md:text-sm text-slate-300 max-w-2xl leading-relaxed">
            Every single slide across all 15 lectures (including Classes 13, 14, 15) is covered with dedicated high-resolution slide renders, verbatim bullets, and deep pedagogical explanations, accompanied by 15 interactive simulators.
          </p>
        </div>

        <div class="flex items-center gap-4 bg-[#05130d] border border-emerald-900/80 p-4 rounded-xl">
          <div class="w-16 h-16 rounded-full border-4 border-emerald-500/20 border-t-emerald-400 flex items-center justify-center font-black text-emerald-300 text-base">
            100%
          </div>
          <div class="text-xs">
            <div class="font-bold text-white mb-0.5">Slide Curriculum</div>
            <div class="text-slate-400">15 of 15 Modules Ready</div>
            <div class="text-emerald-400 text-[10px] font-mono mt-1">{total_slides_all} Slides • Zero Gaps</div>
          </div>
        </div>
      </div>
    </div>

    <!-- MODULES GRID -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
      {cards_html}
    </div>
  </div>
</body>
</html>
"""
    out_home = os.path.join(STUDY_DIR, "00_home.html")
    with open(out_home, "w", encoding="utf-8") as f:
        f.write(home_html)
    print(f"[+] Generated Curriculum Roadmap: {out_home}")
    return out_home

def generate_master_index():
    total_slides_all = sum(len(lec["slides"]) for lec in METADATA)
    lec_cards_html = ""
    for idx, lec in enumerate(METADATA, 1):
        slides_count = len(lec["slides"])
        v_count = len(lec.get("videos", []))
        v_badge = f"<span class='badge-cyan px-2 py-0.5 rounded text-[10px] font-mono'>▶️ {v_count} Video</span>" if v_count > 0 else ""

        lec_cards_html += f"""
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
            <p class="text-xs text-slate-300 leading-relaxed mb-4 line-clamp-2">
              {lec['description']}
            </p>
          </div>

          <div class="pt-3 border-t border-emerald-950/80">
            <div class="flex items-center justify-between text-[11px] text-slate-400 mb-3">
              <span>📚 {slides_count} Slides Slidewise</span>
              <span>🧪 1 Lab</span>
              <span>⏱️ {lec['duration']}</span>
            </div>
            <a href="Study_Material/{lec['slug']}.html" class="block w-full py-2 px-3 rounded-lg text-center text-xs font-bold bg-[#091a13] border border-emerald-900 group-hover:bg-gradient-to-r group-hover:from-emerald-600 group-hover:to-teal-600 group-hover:text-white text-emerald-300 transition-all">
              Launch Lecture Module →
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
        <a href="quiz3_practice_suite.html" class="text-xs bg-gradient-to-r from-emerald-500 to-teal-500 hover:from-emerald-400 hover:to-teal-400 text-white font-bold px-3 py-1.5 rounded-lg transition-all flex items-center gap-1 shadow-sm border border-emerald-400/40 mr-1"><span>⚡ Quiz 3 Prep Suite</span></a>
        <a href="https://courses.iiit.ac.in/course/view.php?id=5826" target="_blank" rel="noopener noreferrer" class="text-xs bg-amber-600/90 hover:bg-amber-500 text-white font-bold px-3 py-1.5 rounded-lg transition-all flex items-center gap-1 shadow-sm">
          <span>🏛️ Moodle Portal</span>
        </a>
        <a href="Study_Material/00_home.html" class="text-xs bg-emerald-600 hover:bg-emerald-500 text-white font-bold px-3 py-1.5 rounded-lg transition-all flex items-center gap-1 shadow-sm">
          <span>📘 All Lectures (15)</span>
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
          Every single slide across all 15 lectures is systematically mapped into dedicated slide learning cards with verbatim text, deep pedagogical breakdowns, 15 interactive simulators, active recall flashcards, and live Moodle announcements.
        </p>

        <!-- STATS BAR -->
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 pt-4 border-t border-emerald-900/60">
          <div class="bg-[#05140d] border border-emerald-900/80 rounded-xl p-3">
            <div class="text-xs text-slate-400">Lecture Modules</div>
            <div class="text-xl font-black text-emerald-400 mt-1">15 Topics</div>
          </div>
          <div class="bg-[#05140d] border border-emerald-900/80 rounded-xl p-3">
            <div class="text-xs text-slate-400">Primary Slides</div>
            <div class="text-xl font-black text-teal-400 mt-1">{total_slides_all} Slides</div>
          </div>
          <div class="bg-[#05140d] border border-emerald-900/80 rounded-xl p-3">
            <div class="text-xs text-slate-400">Interactive Labs</div>
            <div class="text-xl font-black text-cyan-400 mt-1">15 Simulators</div>
          </div>
          <div class="bg-[#05140d] border border-emerald-900/80 rounded-xl p-3">
            <div class="text-xs text-slate-400">Moodle Synced</div>
            <div class="text-xl font-black text-amber-400 mt-1">22 Threads</div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- QUIZ 3 ANNOUNCEMENT & PREP SUITE BANNER -->
  <section class="max-w-7xl mx-auto px-4 pb-6">
    <div class="p-6 bg-gradient-to-r from-[#0d2a1f] via-[#0b1f17] to-[#071711] border-2 border-emerald-500/80 rounded-2xl relative overflow-hidden shadow-xl shadow-emerald-950/50">
      <div class="flex flex-col lg:flex-row items-start lg:items-center justify-between gap-4 relative z-10">
        <div>
          <div class="flex items-center gap-2 mb-2">
            <span class="px-2.5 py-0.5 rounded-full bg-emerald-500 text-black text-xs font-black uppercase tracking-wide">Exam Prep</span>
            <span class="text-xs font-mono text-emerald-300">Lectures 8 to 11 Syllabus</span>
          </div>
          <h2 class="text-xl md:text-2xl font-black text-white">⚡ Quiz 3 Master Preparation Suite & Past Papers Question Bank</h2>
          <p class="text-xs md:text-sm text-slate-300 mt-1 max-w-3xl">
            Complete question extraction from past exam papers, featuring timed mock exams with grading rubrics, active-recall 3D flashcards, rapid-fire fill-in-the-blank drills, and chemical reactions lab.
          </p>
        </div>
        <div class="flex items-center gap-2 w-full lg:w-auto">
          <a href="quiz3_practice_suite.html" class="flex-1 lg:flex-none text-center text-xs md:text-sm bg-gradient-to-r from-emerald-500 to-teal-500 hover:from-emerald-400 hover:to-teal-400 text-white font-black px-5 py-3 rounded-xl transition-all shadow-lg shadow-emerald-950 flex items-center justify-center gap-2">
            <span>🚀 Open Quiz 3 Exam Suite</span>
          </a>
          <a href="Quiz3_Exam_Preparation_Pack.pdf" download class="text-xs bg-red-700 hover:bg-red-600 text-white font-bold px-4 py-3 rounded-xl transition-all shadow-md flex items-center justify-center gap-1.5 mr-2"><span>📄 PDF Pack</span></a>
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
              <span class="badge-emerald px-2 py-0.5 rounded text-[10px]">Lectures 1–7</span>
            </div>
            <p class="text-slate-300">Overview & 2070 Vision, Earth Spheres & Thermodynamics, Pollution & Particulates, Remote Sensing & GIS, Landmark Events (Bhopal, Chernobyl, Minamata), Biogeochemical Cycles, Climate Impacts.</p>
          </div>
          <div class="p-3 bg-[#06140e] border border-teal-900/80 rounded-xl">
            <div class="flex justify-between items-center mb-1">
              <strong class="text-teal-300 font-bold">Quiz-2 Exam Syllabus (Completed)</strong>
              <span class="badge-teal px-2 py-0.5 rounded text-[10px]">Lectures 1–10b</span>
            </div>
            <p class="text-slate-300">Biogeochemical cycles, Ocean Carbon Sequestration, Terrestrial Sinks, Biochar chemistry, and Clean Development Mechanism (CDM).</p>
          </div>
          <div class="p-3 bg-[#06140e] border border-amber-900/80 rounded-xl">
            <div class="flex justify-between items-center mb-1">
              <strong class="text-amber-300 font-bold">Course Project Presentations & Deadlines</strong>
              <span class="badge-amber px-2 py-0.5 rounded text-[10px]">Nov 17–18, 2026</span>
            </div>
            <p class="text-slate-300">Presentations in <strong>LSI conference Room</strong> on 17th and 18th November 2026 (11:00 AM – 4:00 PM). Strictly 25 mins presentation + 5 mins Q&A. Final Project Report due 22nd November 2026, 5:00 PM.</p>
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
          <span class="text-xs text-emerald-400 font-mono">22 Threads Synced</span>
        </div>
        <div class="space-y-2 text-xs max-h-56 overflow-y-auto pr-1">
          <div class="p-2.5 bg-[#06140e] border border-emerald-950 rounded-lg">
            <div class="font-bold text-slate-200">Final Project Presentations Venue & Schedule</div>
            <div class="text-slate-400 text-[11px]">Prof. Ramachandra Prasad P: Presentations on 17th and 18th November in LSI conference Room. Over-time presentations will be stopped immediately.</div>
          </div>
          <div class="p-2.5 bg-[#06140e] border border-emerald-950 rounded-lg">
            <div class="font-bold text-slate-200">Final Project Report Submission Deadline</div>
            <div class="text-slate-400 text-[11px]">Submission deadline: 22nd November 2026, 5:00 PM via Moodle portal.</div>
          </div>
          <div class="p-2.5 bg-[#06140e] border border-emerald-950 rounded-lg">
            <div class="font-bold text-slate-200">Quiz-2 Exam Announcement</div>
            <div class="text-slate-400 text-[11px]">Nemani Dedeepya: Quiz-2 syllabus covers Lectures 1–10b with numerical problems and concept check.</div>
          </div>
          <div class="p-2.5 bg-[#06140e] border border-emerald-950 rounded-lg">
            <div class="font-bold text-slate-200">Midsem Paper Showing & Makeup Exam Syllabus</div>
            <div class="text-slate-400 text-[11px]">Prof. Ramachandra Prasad P: Confirmed makeup exam covers Lectures 1–7.</div>
          </div>
        </div>
      </div>

    </div>
  </section>

  <!-- ALL 15 MODULES GRID -->
  <section class="max-w-7xl mx-auto px-4 py-8">
    <div class="flex flex-wrap items-center justify-between gap-3 mb-6">
      <div>
        <h2 class="text-2xl font-black text-white">All 15 Lecture Modules</h2>
        <p class="text-xs text-slate-300">Complete slidewise learning cards covering all {total_slides_all} slides across the semester.</p>
      </div>
      <a href="Study_Material/00_home.html" class="text-xs text-emerald-400 font-mono font-bold hover:underline">View Detailed Curriculum Roadmap →</a>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
      {lec_cards_html}
    </div>
  </section>

</body>
</html>
"""
    out_index = os.path.join(WORKSPACE, "index.html")
    with open(out_index, "w", encoding="utf-8") as f:
        f.write(index_html)
    print(f"[+] Generated Master Portal: {out_index}")
    return out_index

def main():
    print("==================================================")
    print("  [EST] REGENERATING FULL EST STUDY SUITE")
    print("  Covering 100% of 522 Slides Across 15 Modules")
    print("==================================================")
    for lec in METADATA:
        generate_lecture_page(lec)
    generate_curriculum_home()
    generate_master_index()
    print("\n[OK] Website regeneration complete!")

if __name__ == "__main__":
    main()
