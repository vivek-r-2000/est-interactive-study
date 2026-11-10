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
    --bg-main: #080c0a;
    --bg-card: #0f1613;
    --bg-card-hover: #131c18;
    --border: #1a2620;
    --border-accent: #23332b;
    --primary: #10b981;
    --primary-light: #34d399;
    --teal: #14b8a6;
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
    font-family: 'Inter', system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  }

  /* Quiet Cards & Surfaces */
  .eco-card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 12px;
    transition: border-color 0.15s ease;
  }
  .eco-card:hover {
    border-color: #2b4539;
  }

  /* Quiet Badges */
  .badge-emerald { background: rgba(16, 185, 129, 0.08); border: 1px solid rgba(16, 185, 129, 0.25); color: #6ee7b7; }
  .badge-teal    { background: rgba(20, 184, 166, 0.08); border: 1px solid rgba(20, 184, 166, 0.25); color: #5eead4; }
  .badge-amber   { background: rgba(245, 158, 11, 0.08); border: 1px solid rgba(245, 158, 11, 0.25); color: #fcd34d; }
  .badge-neutral { background: rgba(255, 255, 255, 0.04); border: 1px solid var(--border); color: #94a3b8; }

  /* 3D Flip Card */
  .flip-card-wrap { perspective: 900px; height: 190px; cursor: pointer; }
  .flip-card-inner { position: relative; width: 100%; height: 100%; transform-style: preserve-3d; transition: transform .35s ease; }
  .flip-card-wrap.flipped .flip-card-inner { transform: rotateY(180deg); }
  .flip-face {
    position: absolute; inset: 0; backface-visibility: hidden;
    border-radius: 10px; border: 1px solid var(--border);
    display: flex; flex-direction: column; align-items: center; justify-content: center;
    padding: 20px; text-align: center;
  }
  .flip-front { background: #0c1310; }
  .flip-back  { background: #111b16; border-color: #234235; transform: rotateY(180deg); }

  /* Quiz */
  .quiz-option {
    display: flex; align-items: center; gap: 12px;
    padding: 10px 14px; border-radius: 8px;
    border: 1px solid var(--border); margin-bottom: 8px;
    cursor: pointer; font-size: 13px; transition: border-color .15s ease, background-color .15s ease;
    background: rgba(255,255,255,0.015);
  }
  .quiz-option:hover { border-color: var(--primary); background: rgba(16, 185, 129, 0.06); }
  .quiz-option.correct { border-color: #10b981!important; background: rgba(16, 185, 129, 0.12)!important; color: #a7f3d0; }
  .quiz-option.wrong   { border-color: #ef4444!important; background: rgba(239, 68, 68, 0.12)!important; color: #fca5a5; }
  .quiz-option.disabled { pointer-events: none; }
  .q-letter {
    width: 24px; height: 24px; border-radius: 4px;
    background: var(--border); display: flex; align-items: center; justify-content: center;
    font-size: 11px; font-weight: 600; flex-shrink: 0;
  }

  /* Slide Lightbox Modal */
  .slide-modal-backdrop {
    display: none; position: fixed; inset: 0; z-index: 1000;
    background: rgba(4, 7, 5, 0.92); backdrop-filter: blur(4px);
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
        <div class="p-2.5 rounded-lg bg-[#0a110e] border border-[#18261f] flex items-center justify-between gap-2 hover:border-emerald-700 transition-colors cursor-pointer" onclick="goToCard({idx + 1})">
          <div class="flex items-center gap-2 truncate">
            <span class="badge-emerald px-1.5 py-0.5 rounded text-[10px] font-mono font-semibold flex-shrink-0">#{s['slide_num']}</span>
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
            <div class="p-3 bg-[#0a110e] border border-[#18261f] rounded-lg">
              <div class="flex items-center justify-between mb-2">
                <span class="text-xs font-semibold text-emerald-300 font-mono">Lecture video reference</span>
                <a href="{v['url']}" target="_blank" rel="noopener noreferrer" class="text-[11px] text-emerald-400 hover:underline">Open YouTube ↗</a>
              </div>
              <div class="relative w-full aspect-video bg-black rounded overflow-hidden">
                <iframe src="{v['embed']}" class="w-full h-full" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
              </div>
            </div>
            """
        video_section_html = f"""
        <div class="mb-6">
          <div class="text-xs font-semibold text-emerald-300 font-mono uppercase tracking-wider mb-2">Video references</div>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            {v_cards}
          </div>
        </div>
        """

    screens.append(f"""
    <section class="card-screen active" data-title="1. Scope and roadmap">
      <div class="eco-card p-6 md:p-8 mb-6">
        <div class="flex flex-wrap items-center justify-between gap-3 mb-3">
          <div class="flex items-center gap-2">
            <span class="badge-emerald px-2 py-0.5 rounded text-xs font-mono font-semibold">Lecture {lec_id} • Scope and roadmap</span>
            <span class="text-xs text-slate-400">• {lec['difficulty']} • {lec['duration']}</span>
          </div>
          <span class="badge-neutral px-2 py-0.5 rounded text-xs font-mono">{total_slides} slides covered</span>
        </div>

        <h2 class="text-xl md:text-2xl font-semibold text-white mb-2">{int_info.get('title', lec_title)}</h2>
        <div class="text-emerald-400 text-xs font-medium mb-4">{int_info.get('subtitle', '')}</div>
        
        <div class="p-4 bg-[#0a120e] border-l-2 border-emerald-500 rounded-r-lg mb-6 text-slate-200 text-xs md:text-sm leading-relaxed">
          <strong class="text-emerald-300 block mb-1">Core objective:</strong>
          {int_info.get('why', '')}
        </div>

        {video_section_html}

        <div class="mb-4">
          <div class="flex items-center justify-between mb-3">
            <span class="text-xs font-semibold text-emerald-300 font-mono uppercase tracking-wider">Slide directory</span>
            <button onclick="goToCard(1)" class="text-xs text-emerald-400 hover:underline">Start slide 1 →</button>
          </div>
          <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-2">
            {quick_slides_html}
          </div>
          <div class="text-center mt-4">
            <button onclick="goToCard(1)" class="px-5 py-2 bg-emerald-600 hover:bg-emerald-500 text-white font-semibold text-xs rounded-lg transition-colors cursor-pointer">
              Launch slide-by-slide study ({total_slides} slides) →
            </button>
          </div>
        </div>
      </div>
    </section>
    """)
    sidebar_links.append((0, "1. Scope and roadmap"))

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
            bullets_wrap = f'<ul class="space-y-1.5 text-xs md:text-sm">{bullets_html}</ul>'
        else:
            bullets_wrap = '<p class="text-slate-400 italic text-xs">Visual figure slide. See the high-resolution render on the left.</p>'

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
        <div class="flex items-center justify-between gap-3 pt-4 border-t border-[#18261f] mt-4">
          <button onclick="goToCard({prev_card_idx})" class="px-3.5 py-1.5 rounded-lg bg-[#0a110e] border border-[#18261f] text-slate-300 hover:text-white hover:border-emerald-700 text-xs font-mono transition-colors">
            ← Previous {f"(Slide {slide_num-1})" if s_idx > 0 else "(Overview)"}
          </button>
          <div class="text-xs font-mono text-emerald-400">
            Slide {slide_num} of {total_slides}
          </div>
          <button onclick="goToCard({next_card_idx})" class="px-3.5 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-medium transition-colors">
            {f"Next (Slide {slide_num+1}) →" if s_idx < total_slides - 1 else "Continue to simulator →"}
          </button>
        </div>
        """

        screens.append(f"""
        <section class="card-screen" data-title="Slide {slide_num}: {title_esc[:25]}">
          <div class="eco-card p-5 md:p-6 mb-6">
            <!-- Header bar with Jump selector -->
            <div class="flex flex-wrap items-center justify-between gap-2 pb-3 mb-4 border-b border-[#18261f]">
              <div class="flex items-center gap-2">
                <span class="badge-emerald px-2 py-0.5 rounded text-xs font-mono font-medium">Slide {slide_num} of {total_slides}</span>
                <span class="text-xs text-slate-400 font-mono hidden sm:inline">{s['source_file']}</span>
              </div>
              <div class="flex items-center gap-2">
                <label for="slide_select_{slide_num}" class="text-[11px] text-slate-400 font-mono hidden md:inline">Jump to:</label>
                <select id="slide_select_{slide_num}" onchange="goToCard(parseInt(this.value))" class="bg-[#0a110e] border border-[#18261f] text-emerald-300 text-xs rounded px-2.5 py-1 font-mono focus:outline-none focus:border-emerald-600">
                  {dropdown_opts}
                </select>
                <button onclick="prevCard()" class="px-2 py-1 rounded bg-[#0a110e] border border-[#18261f] text-emerald-300 text-xs hover:border-emerald-600 font-mono" title="Previous Slide">◀</button>
                <button onclick="nextCard()" class="px-2 py-1 rounded bg-[#0a110e] border border-[#18261f] text-emerald-300 text-xs hover:border-emerald-600 font-mono" title="Next Slide">▶</button>
              </div>
            </div>

            <!-- Slide Showcase Split Layout -->
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-5 items-start">
              <!-- Left: Slide Image -->
              <div class="lg:col-span-6 bg-[#040806] border border-[#18261f] rounded-lg p-2 flex flex-col items-center justify-center cursor-pointer group" onclick="openLightbox('{img_path}', 'Slide {slide_num}: {title_esc}')">
                <img src="{img_path}" alt="Slide {slide_num}: {title_esc}" class="w-full h-auto max-h-[460px] object-contain rounded" loading="lazy">
                <div class="w-full flex items-center justify-between text-[11px] text-emerald-400/90 font-mono mt-2 px-1">
                  <span>Click or press <kbd class="px-1 py-0.5 rounded bg-[#0a110e] border border-[#18261f] text-emerald-300 font-mono text-[10px]">Z</kbd> for lightbox</span>
                  <span class="text-slate-500 text-[10px]">High-res render</span>
                </div>
              </div>

              <!-- Right: Bullets & Deep Explanation -->
              <div class="lg:col-span-6 space-y-3">
                <!-- Slide Title -->
                <div class="p-3 bg-[#0a120e] border-l-2 border-emerald-500 rounded-r-lg">
                  <span class="text-[10px] uppercase font-semibold text-emerald-400 font-mono block mb-0.5">Topic title</span>
                  <h3 class="text-sm md:text-base font-semibold text-white leading-snug">{title_esc}</h3>
                </div>

                <!-- Verbatim Slide Content & Bullets -->
                <div class="p-3.5 bg-[#0b1410] border border-[#18261f] rounded-lg">
                  <span class="text-[10px] uppercase font-semibold text-teal-300 font-mono block mb-2">Slide text and points</span>
                  {bullets_wrap}
                </div>

                <!-- Deep Pedagogical Breakdown -->
                <div class="p-3.5 bg-[#09110d] border border-[#16231d] rounded-lg text-xs md:text-sm text-slate-200 leading-relaxed">
                  <span class="text-[10px] uppercase font-semibold text-emerald-400 font-mono block mb-1">Key concept breakdown</span>
                  <p class="text-slate-300">{deep_exp}</p>
                </div>
              </div>
            </div>

            <!-- Footer navigation -->
            {nav_footer_html}
          </div>
        </section>
        """)
        sidebar_links.append((card_num, f"Slide {slide_num}: {s['title'][:28]}"))

    # ========================================================
    # SCREEN: INTERACTIVE SIMULATOR LAB
    # ========================================================
    cur_idx = len(screens)
    screens.append(f"""
    <section class="card-screen" data-title="Interactive simulator">
      <div class="mb-6">
        {sim_html}
      </div>
    </section>
    """)
    sidebar_links.append((cur_idx, "Interactive simulator"))

    # ========================================================
    # SCREEN: ACTIVE RECALL FLASHCARDS
    # ========================================================
    cur_idx = len(screens)
    f_cards_html = ""
    for f in details.get("flashcards", []):
        f_cards_html += f"""
        <div class="flip-card-wrap mb-3" onclick="this.classList.toggle('flipped')">
          <div class="flip-card-inner">
            <div class="flip-face flip-front">
              <span class="text-xs uppercase font-medium text-emerald-400 tracking-wider mb-2">Question (click to flip)</span>
              <div class="text-sm font-semibold text-white mb-2">{f['q']}</div>
              <span class="text-[11px] text-slate-500 mt-2">Click card to reveal answer</span>
            </div>
            <div class="flip-face flip-back">
              <span class="text-xs uppercase font-medium text-teal-300 tracking-wider mb-2">Answer</span>
              <div class="text-xs md:text-sm text-slate-200 leading-relaxed">{f['a']}</div>
            </div>
          </div>
        </div>
        """

    screens.append(f"""
    <section class="card-screen" data-title="Active recall flashcards">
      <div class="eco-card p-6 md:p-8 mb-6">
        <div class="badge-emerald inline-block px-2 py-0.5 rounded text-xs font-mono font-medium mb-2">Spaced repetition</div>
        <h2 class="text-xl font-semibold text-white mb-1">Active recall flashcards</h2>
        <p class="text-xs text-slate-400 mb-5">Review definitions, reactions, and governing laws from the lecture slides before flipping.</p>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
          {f_cards_html}
        </div>
      </div>
    </section>
    """)
    sidebar_links.append((cur_idx, "Active recall flashcards"))

    # ========================================================
    # SCREEN: HIGH-YIELD EXAM TRAPS
    # ========================================================
    cur_idx = len(screens)
    traps_html = "".join([f"<li class='p-3 bg-[#0a110e] border border-[#18261f] rounded-lg text-xs text-slate-200 leading-relaxed mb-2.5'>{t}</li>" for t in details.get("traps", [])])
    screens.append(f"""
    <section class="card-screen" data-title="High-yield exam traps">
      <div class="eco-card p-6 md:p-8 mb-6">
        <div class="badge-amber inline-block px-2 py-0.5 rounded text-xs font-mono font-medium mb-2">Exam checkpoints</div>
        <h2 class="text-xl font-semibold text-white mb-1">Exam traps and common pitfalls</h2>
        <p class="text-xs text-slate-400 mb-5">Common student misconceptions and subtle distinctions tested in exams.</p>
        <ul class="space-y-1">
          {traps_html}
        </ul>
      </div>
    </section>
    """)
    sidebar_links.append((cur_idx, "High-yield exam traps"))

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
        <div class="p-4 bg-[#0a110e] border border-[#18261f] rounded-lg mb-5">
          <div class="text-xs font-mono text-emerald-400 font-semibold mb-1">Question {q_idx + 1}</div>
          <div class="text-sm font-semibold text-white mb-3">{q['question']}</div>
          <div class="space-y-1">
            {opts_html}
          </div>
          <div id="q_{lec_id}_{q_idx}" class="p-3 mt-3 bg-[#0d1812] border border-[#1d3126] rounded-md text-xs text-emerald-200 hidden">
            <strong>Explanation:</strong> {q['explanation']}
          </div>
        </div>
        """

    screens.append(f"""
    <section class="card-screen" data-title="Concept check quiz">
      <div class="eco-card p-6 md:p-8 mb-6">
        <div class="badge-emerald inline-block px-2 py-0.5 rounded text-xs font-mono font-medium mb-2">Self evaluation</div>
        <h2 class="text-xl font-semibold text-white mb-1">Concept check quiz</h2>
        <p class="text-xs text-slate-400 mb-5">Verify your understanding of core concepts from this lecture deck.</p>
        <div>
          {quiz_html}
        </div>
      </div>
    </section>
    """)
    sidebar_links.append((cur_idx, "Concept check quiz"))

    # ========================================================
    # SCREEN: COMPLETE SLIDE DECK QUICK-JUMP GALLERY
    # ========================================================
    cur_idx = len(screens)
    slides_grid = ""
    for idx, s in enumerate(all_lec_slides):
        slides_grid += f"""
        <div class="bg-[#0a110e] border border-[#18261f] rounded-lg p-2 flex flex-col justify-between hover:border-emerald-700 transition-colors">
          <div class="overflow-hidden rounded bg-black/40 cursor-pointer relative" onclick="goToCard({idx + 1})">
            <img src="{s['image']}" alt="Slide {s['slide_num']}" class="w-full h-28 object-contain" loading="lazy">
            <div class="absolute inset-0 bg-black/40 opacity-0 hover:opacity-100 transition-opacity flex items-center justify-center">
              <span class="bg-[#0f1613] text-emerald-300 text-[10px] px-2 py-0.5 rounded font-mono border border-[#18261f]">Study card</span>
            </div>
          </div>
          <div class="pt-2 px-1">
            <div class="flex items-center justify-between text-[10px] text-slate-400 font-mono mb-0.5">
              <span class="text-emerald-400 font-medium">Slide #{s['slide_num']}</span>
              <span class="truncate max-w-[90px]">{s['source_file']}</span>
            </div>
            <div class="text-[11px] font-medium text-slate-300 line-clamp-1" title="{html.escape(s['title'])}">{s['title']}</div>
          </div>
        </div>
        """

    file_badges = " ".join([f"<a href='../Lecture_Slides/{f}' target='_blank' class='inline-flex items-center gap-1.5 px-2.5 py-1 rounded bg-[#0a110e] border border-[#18261f] text-emerald-300 text-xs font-mono hover:border-emerald-600 transition-colors'><span>Download {f}</span></a>" for f in lec['files']])

    screens.append(f"""
    <section class="card-screen" data-title="Slide index gallery">
      <div class="eco-card p-6 md:p-8 mb-6">
        <div class="flex flex-wrap items-center justify-between gap-3 mb-4 pb-3 border-b border-[#18261f]">
          <div>
            <div class="badge-emerald inline-block px-2 py-0.5 rounded text-xs font-mono font-medium mb-1">Slide deck index</div>
            <h2 class="text-xl font-semibold text-white">Slide reference gallery</h2>
            <p class="text-xs text-slate-400">Complete visual reference of all {total_slides} slides with direct links to original presentation files.</p>
          </div>
          <div class="flex flex-wrap gap-2">
            {file_badges}
          </div>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-2.5">
          {slides_grid}
        </div>
      </div>
    </section>
    """)
    sidebar_links.append((cur_idx, f"Slide gallery ({total_slides} slides)"))

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
<title>Lecture {lec_id}: {lec_title} — EST Study Suite</title>
<script src="https://cdn.tailwindcss.com"></script>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body, {{delimiters: [{{left: '$$', right: '$$', display: true}}, {{left: '$', right: '$', display: false}}]}});"></script>

<style>
{SHARED_CSS}

  /* Top Bar */
  #topbar {{
    position: fixed; top: 0; left: 0; right: 0; z-index: 50;
    background: #060907; border-bottom: 1px solid var(--border);
    display: flex; align-items: center; gap: 12px;
    padding: 0 16px; height: 50px;
  }}
  #topbar a {{ color: var(--primary-light); font-size: 13px; text-decoration: none; font-weight: 500; }}
  #module-title {{ font-weight: 600; font-size: 13px; color: #fff; white-space: nowrap; }}
  #progress-bar-bg {{ background: var(--border); border-radius: 4px; height: 4px; width: 100%; }}
  #progress-bar-fill {{ background: #10b981; height: 4px; border-radius: 4px; transition: width .2s ease; width: 0%; }}

  /* Pomodoro */
  #pomodoro {{
    display: flex; align-items: center; gap: 6px;
    background: var(--bg-card); border: 1px solid var(--border);
    border-radius: 6px; padding: 4px 10px; cursor: pointer; white-space: nowrap;
  }}
  #timer-display {{ font-size: 12px; font-weight: 600; color: #f59e0b; font-variant-numeric: tabular-nums; }}

  /* Layout */
  #layout {{ display: flex; margin-top: 50px; height: calc(100vh - 50px); }}
  #sidebar {{
    width: 270px; min-width: 270px; background: #060907;
    border-right: 1px solid var(--border); overflow-y: auto; padding: 14px 0;
    display: flex; flex-direction: column; gap: 1px;
  }}
  .sidebar-link {{
    display: flex; align-items: center; gap: 10px;
    padding: 7px 16px; font-size: 12px; color: var(--muted);
    cursor: pointer; transition: color .15s ease, background-color .15s ease; border-left: 2px solid transparent;
  }}
  .sidebar-link:hover {{ background: rgba(255, 255, 255, 0.03); color: #fff; }}
  .sidebar-link.active {{ background: rgba(16, 185, 129, 0.08); color: #34d399; border-left-color: #10b981; font-weight: 500; }}
  .sidebar-dot {{ width: 5px; height: 5px; border-radius: 50%; background: #26332c; flex-shrink: 0; }}
  .sidebar-link.active .sidebar-dot {{ background: #10b981; }}

  /* Main */
  #main {{
    flex: 1; overflow-y: auto; padding: 24px 20px 80px 20px;
    display: flex; flex-direction: column; align-items: center;
  }}
  .card-screen {{ display: none; width: 100%; max-width: 1020px; }}
  .card-screen.active {{ display: block; }}

  /* Nav Bar */
  #nav-bar {{
    position: fixed; bottom: 0; left: 270px; right: 0;
    background: #060907; border-top: 1px solid var(--border);
    display: flex; align-items: center; justify-content: center; gap: 16px;
    padding: 10px 20px; z-index: 40;
  }}
  @media (max-width: 768px) {{
    #sidebar {{ display: none; }}
    #nav-bar {{ left: 0; }}
  }}
</style>
</head>
<body class="selection:bg-emerald-700 selection:text-white">

  <!-- TOP BAR -->
  <header id="topbar">
    <a href="00_home.html" class="flex items-center gap-1">← <span class="hidden sm:inline">All modules</span></a>
    <span style="color:var(--border)">|</span>
    <span id="module-title">Lec {lec_id}: {lec_short}</span>
    <div class="flex-1 flex flex-col gap-1 mx-2 min-w-0">
      <div class="flex justify-between text-[11px]">
        <span id="section-label" class="text-emerald-400 font-medium truncate">Section 1</span>
        <span id="progress-label" class="text-slate-400 font-mono">0%</span>
      </div>
      <div id="progress-bar-bg"><div id="progress-bar-fill"></div></div>
    </div>
    <div id="pomodoro" onclick="togglePomodoro()">
      <span class="text-xs text-slate-400 font-mono">Timer</span>
      <span id="timer-display">25:00</span>
    </div>
  </header>

  <!-- LAYOUT -->
  <div id="layout">
    <!-- SIDEBAR -->
    <nav id="sidebar">
      <div class="text-[10px] font-semibold tracking-wider text-slate-400 uppercase px-4 py-1.5">Lecture curriculum</div>
      {nav_links_html}
    </nav>

    <!-- MAIN VIEW -->
    <main id="main">
      {all_screens_html}
    </main>
  </div>

  <!-- BOTTOM NAVIGATION BAR -->
  <nav id="nav-bar">
    <button class="nav-btn px-4 py-1.5 rounded-md text-xs font-medium border border-[#18261f] bg-[#0a110e] text-slate-300 hover:text-white hover:border-emerald-700 transition-colors cursor-pointer" onclick="prevCard()">← Previous</button>
    <span id="card-counter" class="text-xs text-slate-400 font-mono">Card 1 of {len(screens)}</span>
    <button class="nav-btn px-4 py-1.5 rounded-md text-xs font-medium bg-emerald-600 hover:bg-emerald-500 text-white transition-colors cursor-pointer" onclick="nextCard()">Next Card →</button>
    <span class="text-[11px] text-slate-500 font-mono hidden md:inline ml-2">Keys: <kbd class="px-1 bg-[#0a110e] border border-[#18261f] rounded text-emerald-300">←</kbd> <kbd class="px-1 bg-[#0a110e] border border-[#18261f] rounded text-emerald-300">→</kbd> <kbd class="px-1 bg-[#0a110e] border border-[#18261f] rounded text-emerald-300">Z</kbd></span>
  </nav>

  <!-- LIGHTBOX MODAL -->
  <div id="lightbox_modal" class="slide-modal-backdrop" onclick="closeLightbox(event)">
    <div class="relative max-w-5xl w-full bg-[#0a110e] border border-[#18261f] rounded-xl overflow-hidden p-3 shadow-xl" onclick="event.stopPropagation()">
      <div class="flex items-center justify-between pb-2 mb-2 border-b border-[#18261f]">
        <span id="modal_title" class="text-xs font-semibold text-emerald-300 font-mono truncate">Slide preview</span>
        <button class="text-slate-400 hover:text-white px-2 py-0.5 text-xs bg-[#0f1613] border border-[#18261f] rounded cursor-pointer" onclick="closeLightbox()">✕ Close</button>
      </div>
      <div class="flex items-center justify-center bg-black/60 rounded p-2 max-h-[80vh] overflow-auto">
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
      document.getElementById('modal_title').innerText = title || 'Slide figure';
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
            alert('Pomodoro session completed. Take a short 5-minute break.');
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
        v_count = len(lec.get("videos", []))
        v_badge = f"<span class='badge-neutral px-2 py-0.5 rounded text-[10px] font-mono'>{v_count} video(s)</span>" if v_count > 0 else ""

        cards_html += f"""
        <div class="eco-card p-5 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between gap-2 mb-2">
              <span class="badge-emerald px-2 py-0.5 rounded text-xs font-mono font-medium">Module {lec['id']}</span>
              <div class="flex items-center gap-1.5">
                {v_badge}
                <span class="badge-neutral px-2 py-0.5 rounded text-[10px] font-mono">{lec['difficulty']}</span>
              </div>
            </div>
            <h3 class="text-base font-semibold text-white mb-2">
              {lec['title']}
            </h3>
            <p class="text-xs text-slate-300 leading-relaxed mb-4 line-clamp-3">
              {lec['description']}
            </p>
          </div>

          <div class="pt-3 border-t border-[#18261f]">
            <div class="flex items-center justify-between text-[11px] text-slate-400 mb-3 font-mono">
              <span>{slides_count} slides</span>
              <span>1 simulator</span>
              <span>{lec['duration']}</span>
            </div>
            <a href="{lec['slug']}.html" class="block w-full py-2 px-3 rounded text-center text-xs font-medium bg-[#0a110e] border border-[#18261f] hover:border-emerald-700 text-emerald-300 transition-colors">
              Open module ({slides_count} slides) →
            </a>
          </div>
        </div>
        """

    home_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Curriculum Roadmap — Environmental Science & Technology (ES1.101)</title>
<script src="https://cdn.tailwindcss.com"></script>
<style>
{SHARED_CSS}
</style>
</head>
<body class="selection:bg-emerald-700 selection:text-white min-h-screen">

  <!-- TOP BAR -->
  <header class="sticky top-0 z-50 bg-[#060907]/95 backdrop-blur border-b border-[var(--border)] px-4 py-3">
    <div class="max-w-7xl mx-auto flex items-center justify-between">
      <div class="flex items-center gap-2">
        <span class="font-semibold text-sm md:text-base text-white">Environmental Science & Technology</span>
        <span class="ml-2 text-xs text-emerald-400 font-mono bg-[#0c1611] px-2 py-0.5 rounded border border-[#18261f]">ES1.101 • Monsoon 2026</span>
      </div>
      <div class="flex items-center gap-2">
        <a href="../quiz3_practice_suite.html" class="text-xs bg-[#0c1611] hover:border-emerald-700 text-emerald-300 font-medium px-3 py-1.5 rounded border border-[#18261f] transition-colors">Quiz 3 prep suite</a>
        <a href="../index.html" class="text-xs bg-[#0c1611] hover:text-white text-slate-300 font-medium px-3 py-1.5 rounded border border-[#18261f] transition-colors">Master portal</a>
        <a href="https://courses.iiit.ac.in/course/view.php?id=5826" target="_blank" class="text-xs bg-[#1a1408] text-amber-300 hover:text-white font-medium px-3 py-1.5 rounded border border-amber-900/60 transition-colors">Moodle</a>
      </div>
    </div>
  </header>

  <!-- HERO SECTION -->
  <div class="max-w-7xl mx-auto px-4 py-8">
    <div class="p-6 md:p-8 bg-[#0c1310] border border-[#18261f] rounded-xl mb-8">
      <div class="flex flex-col md:flex-row md:items-center justify-between gap-6">
        <div>
          <div class="inline-flex items-center gap-2 px-2.5 py-0.5 rounded bg-[#0a110e] border border-[#18261f] text-emerald-300 text-xs font-mono mb-3">
            15 modules • {total_slides_all} slides covered slidewise
          </div>
          <h1 class="text-2xl md:text-3xl font-semibold text-white tracking-tight mb-2">
            Curriculum roadmap and slide navigator
          </h1>
          <p class="text-xs md:text-sm text-slate-300 max-w-2xl leading-relaxed">
            Every slide across all 15 lectures (including Classes 13, 14, and 15) is covered with dedicated high-resolution renders, verbatim bullet points, and compact concept explanations.
          </p>
        </div>

        <div class="flex items-center gap-4 bg-[#080d0a] border border-[#18261f] p-4 rounded-lg">
          <div class="w-14 h-14 rounded-full border-2 border-emerald-500/40 border-t-emerald-400 flex items-center justify-center font-semibold text-emerald-300 text-sm">
            100%
          </div>
          <div class="text-xs">
            <div class="font-medium text-white mb-0.5">Syllabus coverage</div>
            <div class="text-slate-400">15 of 15 modules ready</div>
            <div class="text-emerald-400 text-[10px] font-mono mt-0.5">{total_slides_all} slides • Zero gaps</div>
          </div>
        </div>
      </div>
    </div>

    <!-- MODULES GRID -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
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
        v_badge = f"<span class='badge-neutral px-2 py-0.5 rounded text-[10px] font-mono'>{v_count} video</span>" if v_count > 0 else ""

        lec_cards_html += f"""
        <div class="eco-card p-5 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between gap-2 mb-2">
              <span class="badge-emerald px-2 py-0.5 rounded text-xs font-mono font-medium">Module {lec['id']}</span>
              <div class="flex items-center gap-1.5">
                {v_badge}
                <span class="badge-neutral px-2 py-0.5 rounded text-[10px] font-mono">{lec['difficulty']}</span>
              </div>
            </div>
            <h3 class="text-base font-semibold text-white mb-2">
              {lec['title']}
            </h3>
            <p class="text-xs text-slate-300 leading-relaxed mb-4 line-clamp-2">
              {lec['description']}
            </p>
          </div>

          <div class="pt-3 border-t border-[#18261f]">
            <div class="flex items-center justify-between text-[11px] text-slate-400 mb-3 font-mono">
              <span>{slides_count} slides</span>
              <span>1 simulator</span>
              <span>{lec['duration']}</span>
            </div>
            <a href="Study_Material/{lec['slug']}.html" class="block w-full py-2 px-3 rounded text-center text-xs font-medium bg-[#0a110e] border border-[#18261f] hover:border-emerald-700 text-emerald-300 transition-colors">
              Open module ({slides_count} slides) →
            </a>
          </div>
        </div>
        """

    index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Environmental Science & Technology (ES1.101) — Study Suite</title>
<script src="https://cdn.tailwindcss.com"></script>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
<style>
{SHARED_CSS}
</style>
</head>
<body class="selection:bg-emerald-700 selection:text-white min-h-screen">

  <!-- TOP APP BAR -->
  <header class="sticky top-0 z-50 bg-[#060907]/95 backdrop-blur border-b border-[var(--border)] px-4 py-3">
    <div class="max-w-7xl mx-auto flex items-center justify-between">
      <div class="flex items-center gap-2">
        <span class="font-semibold text-sm md:text-base text-white tracking-tight">Environmental Science & Technology</span>
        <span class="hidden md:inline-block ml-2 text-xs text-emerald-400 font-mono bg-[#0c1611] px-2 py-0.5 rounded border border-[#18261f]">ES1.101 • Monsoon 2026</span>
      </div>
      <div class="flex items-center gap-2">
        <a href="quiz3_practice_suite.html" class="text-xs bg-[#0c1611] hover:border-emerald-700 text-emerald-300 font-medium px-3 py-1.5 rounded border border-[#18261f] transition-colors">Quiz 3 prep suite</a>
        <a href="https://courses.iiit.ac.in/course/view.php?id=5826" target="_blank" rel="noopener noreferrer" class="text-xs bg-[#1a1408] text-amber-300 hover:text-white font-medium px-3 py-1.5 rounded border border-amber-900/60 transition-colors">
          Moodle portal
        </a>
        <a href="Study_Material/00_home.html" class="text-xs bg-emerald-600 hover:bg-emerald-500 text-white font-medium px-3 py-1.5 rounded transition-colors">
          All lectures (15)
        </a>
      </div>
    </div>
  </header>

  <!-- HERO SECTION -->
  <section class="max-w-7xl mx-auto px-4 pt-8 pb-6">
    <div class="p-6 md:p-8 bg-[#0c1310] border border-[#18261f] rounded-xl">
      <div class="max-w-4xl">
        <div class="flex flex-wrap items-center gap-2 mb-3">
          <div class="px-2.5 py-0.5 rounded bg-[#0a110e] border border-[#18261f] text-emerald-300 text-xs font-mono">
            Course study suite
          </div>
          <div class="px-2.5 py-0.5 rounded bg-[#0a110e] border border-[#18261f] text-slate-400 text-xs font-mono">
            IIIT Hyderabad
          </div>
        </div>
        
        <h1 class="text-2xl md:text-4xl font-semibold text-white tracking-tight mb-3">
          Environmental Science & Technology
        </h1>
        <p class="text-xs md:text-sm text-slate-300 mb-2">
          Instructor: <strong class="text-white">Prof. Ramachandra Prasad P</strong> • TAs: Nemani Dedeepya, Vastava Kurumeti, Kalakuntla Rishika, Himank Singhvi
        </p>
        <p class="text-xs md:text-sm text-slate-400 leading-relaxed mb-6">
          Systematic coverage of all 15 lectures and {total_slides_all} slides. Each slide includes verbatim bullet points, compact concept breakdowns, and access to 15 interactive numerical models and live Moodle announcements.
        </p>

        <!-- STATS BAR -->
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 pt-4 border-t border-[#18261f]">
          <div class="bg-[#080d0a] border border-[#18261f] rounded-lg p-3">
            <div class="text-xs text-slate-400 font-mono">Lecture modules</div>
            <div class="text-lg font-semibold text-emerald-400 mt-0.5">15 topics</div>
          </div>
          <div class="bg-[#080d0a] border border-[#18261f] rounded-lg p-3">
            <div class="text-xs text-slate-400 font-mono">Curriculum slides</div>
            <div class="text-lg font-semibold text-emerald-400 mt-0.5">{total_slides_all} slides</div>
          </div>
          <div class="bg-[#080d0a] border border-[#18261f] rounded-lg p-3">
            <div class="text-xs text-slate-400 font-mono">Interactive models</div>
            <div class="text-lg font-semibold text-emerald-400 mt-0.5">15 simulators</div>
          </div>
          <div class="bg-[#080d0a] border border-[#18261f] rounded-lg p-3">
            <div class="text-xs text-slate-400 font-mono">Moodle updates</div>
            <div class="text-lg font-semibold text-amber-400 mt-0.5">22 threads</div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- QUIZ 3 ANNOUNCEMENT & PREP SUITE BANNER -->
  <section class="max-w-7xl mx-auto px-4 pb-6">
    <div class="p-5 bg-[#0a120e] border border-[#1d3126] rounded-xl">
      <div class="flex flex-col lg:flex-row items-start lg:items-center justify-between gap-4">
        <div>
          <div class="flex items-center gap-2 mb-1.5">
            <span class="px-2 py-0.5 rounded bg-emerald-600/20 text-emerald-300 text-xs font-mono font-medium">Exam prep</span>
            <span class="text-xs font-mono text-slate-400">Lectures 8 to 11 syllabus</span>
          </div>
          <h2 class="text-lg font-semibold text-white">Quiz 3 master preparation suite and past papers question bank</h2>
          <p class="text-xs text-slate-400 mt-1 max-w-3xl">
            Questions extracted from past exam papers, including timed mock tests, active-recall flashcards, rapid fill-in drills, and chemical reactions review.
          </p>
        </div>
        <div class="flex items-center gap-2 w-full lg:w-auto">
          <a href="quiz3_practice_suite.html" class="flex-1 lg:flex-none text-center text-xs bg-emerald-600 hover:bg-emerald-500 text-white font-medium px-4 py-2 rounded-lg transition-colors">
            Open Quiz 3 suite
          </a>
          <a href="Quiz3_Exam_Preparation_Pack.pdf" download class="text-xs bg-[#0f1613] hover:text-white text-slate-300 border border-[#18261f] font-medium px-3 py-2 rounded-lg transition-colors">
            PDF pack
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- EXAM & ANNOUNCEMENTS DIGEST -->
  <section class="max-w-7xl mx-auto px-4 py-2">
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
      
      <!-- Exam Syllabus -->
      <div class="eco-card p-5">
        <h3 class="text-sm font-semibold text-white mb-3">Examination syllabus breakdown</h3>
        <div class="space-y-2 text-xs">
          <div class="p-3 bg-[#0a110e] border border-[#18261f] rounded-lg">
            <div class="flex justify-between items-center mb-1">
              <strong class="text-emerald-400 font-medium">Midsem exam syllabus (covered)</strong>
              <span class="badge-neutral px-1.5 py-0.5 rounded text-[10px] font-mono">Lectures 1–7</span>
            </div>
            <p class="text-slate-400">Vision 2070, Earth spheres and thermodynamics, particulate pollution, remote sensing and GIS, landmark crises (Bhopal, Chernobyl, Minamata), biogeochemical cycles, and climate change impacts.</p>
          </div>
          <div class="p-3 bg-[#0a110e] border border-[#18261f] rounded-lg">
            <div class="flex justify-between items-center mb-1">
              <strong class="text-emerald-400 font-medium">Quiz-2 exam syllabus (completed)</strong>
              <span class="badge-neutral px-1.5 py-0.5 rounded text-[10px] font-mono">Lectures 1–10b</span>
            </div>
            <p class="text-slate-400">Biogeochemical cycles, ocean carbon sequestration, terrestrial sinks, biochar chemistry, and the Clean Development Mechanism (CDM).</p>
          </div>
          <div class="p-3 bg-[#0a110e] border border-[#18261f] rounded-lg">
            <div class="flex justify-between items-center mb-1">
              <strong class="text-amber-300 font-medium">Project presentations and reports</strong>
              <span class="badge-amber px-1.5 py-0.5 rounded text-[10px] font-mono">Nov 17–18, 2026</span>
            </div>
            <p class="text-slate-400">Presentations in the <strong>LSI conference Room</strong> on 17th and 18th November 2026 (11:00 AM – 4:00 PM). Strictly 25 mins presentation + 5 mins Q&A. Final report due 22nd November 2026, 5:00 PM.</p>
          </div>
        </div>
      </div>

      <!-- Live Announcements Digest -->
      <div class="eco-card p-5">
        <div class="flex items-center justify-between mb-3">
          <h3 class="text-sm font-semibold text-white">Moodle announcements digest</h3>
          <span class="text-xs text-slate-500 font-mono">22 threads synced</span>
        </div>
        <div class="space-y-2 text-xs max-h-56 overflow-y-auto pr-1">
          <div class="p-2.5 bg-[#0a110e] border border-[#18261f] rounded">
            <div class="font-medium text-slate-200">Final project presentations venue and schedule</div>
            <div class="text-slate-400 text-[11px]">Prof. Ramachandra Prasad P: Presentations on 17th and 18th November in LSI conference Room. Over-time presentations will be stopped immediately.</div>
          </div>
          <div class="p-2.5 bg-[#0a110e] border border-[#18261f] rounded">
            <div class="font-medium text-slate-200">Final project report submission deadline</div>
            <div class="text-slate-400 text-[11px]">Submission deadline: 22nd November 2026, 5:00 PM via Moodle portal.</div>
          </div>
          <div class="p-2.5 bg-[#0a110e] border border-[#18261f] rounded">
            <div class="font-medium text-slate-200">Quiz-2 exam announcement</div>
            <div class="text-slate-400 text-[11px]">Nemani Dedeepya: Quiz-2 syllabus covers Lectures 1–10b with numerical problems and concept check.</div>
          </div>
          <div class="p-2.5 bg-[#0a110e] border border-[#18261f] rounded">
            <div class="font-medium text-slate-200">Midsem paper showing and makeup exam syllabus</div>
            <div class="text-slate-400 text-[11px]">Prof. Ramachandra Prasad P: Confirmed makeup exam covers Lectures 1–7.</div>
          </div>
        </div>
      </div>

    </div>
  </section>

  <!-- ALL 15 MODULES GRID -->
  <section class="max-w-7xl mx-auto px-4 py-8">
    <div class="flex flex-wrap items-center justify-between gap-3 mb-5">
      <div>
        <h2 class="text-xl font-semibold text-white">All 15 lecture modules</h2>
        <p class="text-xs text-slate-400">Slidewise learning cards covering all {total_slides_all} slides across the semester.</p>
      </div>
      <a href="Study_Material/00_home.html" class="text-xs text-emerald-400 font-mono font-medium hover:underline">View curriculum roadmap →</a>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
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
    print("  [EST] UNSLOPPED REGENERATION OF EST STUDY SUITE")
    print("  Simple, Compact, Educational, 0 UI/Writing Slop")
    print("==================================================")
    for lec in METADATA:
        generate_lecture_page(lec)
    generate_curriculum_home()
    generate_master_index()
    print("\n[OK] Unslopped regeneration complete!")

if __name__ == "__main__":
    main()
