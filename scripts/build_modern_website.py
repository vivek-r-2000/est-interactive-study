import json
import os

def build_website():
    db_path = os.path.join("Study_Material", "curriculum_database.json")
    with open(db_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    db_json_escaped = json.dumps(data, ensure_ascii=False)
    
    html = f'''<!DOCTYPE html>
<html lang="en" class="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Environmental Science & Technology — Micro-Study Suite (ES1.101)</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"
          onload="renderMathInElement(document.body, {{delimiters: [{{left: '$$', right: '$$', display: true}}, {{left: '$', right: '$', display: false}}, {{left: '\\\\(', right: '\\\\)', display: false}}, {{left: '\\\\[', right: '\\\\]', display: true}}], throwOnError: false}});"></script>
  <style>
    :root {{
      --bg: #FBFBFA;
      --card-bg: #FFFFFF;
      --card-hover: #F7F7F5;
      --border: #E7E6E2;
      --border-accent: #D1D0CA;
      --text: #191919;
      --text-muted: #666662;
      --accent: #1E3A2F;
      --accent-soft: #EAF0EC;
      --accent-text: #142820;
      --callout-bg: #F4F6F4;
      --callout-border: #C8D8CF;
      --checkpoint-bg: #FAF9F6;
      --tag-bg: #EFEFEA;
      --tag-text: #444440;
      --success: #1E6B47;
      --success-bg: #EAF7EE;
      --danger: #992828;
      --danger-bg: #FDF0F0;
      --bridge-bg: #F0F4F8;
      --bridge-border: #3B82F6;
      --bridge-text: #1E40AF;
    }}

    html.dark {{
      --bg: #121413;
      --card-bg: #181B1A;
      --card-hover: #1E2220;
      --border: #282E2B;
      --border-accent: #373F3B;
      --text: #E8ECE9;
      --text-muted: #969F9A;
      --accent: #34D399;
      --accent-soft: #162B22;
      --accent-text: #A7F3D0;
      --callout-bg: #15221C;
      --callout-border: #244134;
      --checkpoint-bg: #141716;
      --tag-bg: #222724;
      --tag-text: #B4BCB7;
      --success: #34D399;
      --success-bg: #142820;
      --danger: #F87171;
      --danger-bg: #2B1515;
      --bridge-bg: #13202E;
      --bridge-border: #60A5FA;
      --bridge-text: #93C5FD;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      background: var(--bg);
      color: var(--text);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      line-height: 1.55;
      -webkit-font-smoothing: antialiased;
      transition: background-color 0.2s ease, color 0.2s ease;
    }}

    /* Layout & Header */
    header {{
      position: sticky;
      top: 0;
      z-index: 100;
      background: var(--card-bg);
      border-bottom: 1px solid var(--border);
      backdrop-filter: blur(8px);
    }}
    .header-inner {{
      max-width: 1200px;
      margin: 0 auto;
      padding: 12px 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
    }}
    .brand {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .brand-logo {{
      width: 28px;
      height: 28px;
      background: var(--accent);
      color: var(--card-bg);
      border-radius: 6px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 700;
      font-size: 14px;
    }}
    .brand-title {{
      font-weight: 600;
      font-size: 15px;
      letter-spacing: -0.01em;
    }}
    .brand-badge {{
      font-size: 11px;
      padding: 2px 7px;
      border-radius: 4px;
      background: var(--tag-bg);
      color: var(--tag-text);
      font-weight: 500;
    }}

    .header-actions {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    .search-wrap {{
      position: relative;
      width: 240px;
    }}
    .search-input {{
      width: 100%;
      padding: 6px 12px 6px 30px;
      border-radius: 6px;
      border: 1px solid var(--border);
      background: var(--card-hover);
      color: var(--text);
      font-size: 13px;
      outline: none;
      transition: border-color 0.15s ease;
    }}
    .search-input:focus {{
      border-color: var(--accent);
      background: var(--card-bg);
    }}
    .search-icon {{
      position: absolute;
      left: 10px;
      top: 8px;
      font-size: 12px;
      color: var(--text-muted);
      pointer-events: none;
    }}
    .btn-toggle {{
      background: var(--card-hover);
      border: 1px solid var(--border);
      color: var(--text);
      border-radius: 6px;
      padding: 6px 10px;
      font-size: 12px;
      font-weight: 500;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: background-color 0.15s ease;
    }}
    .btn-toggle:hover {{
      background: var(--border);
    }}

    /* Global Progress Bar */
    .progress-strip {{
      background: var(--border);
      height: 3px;
      width: 100%;
      position: relative;
    }}
    .progress-fill {{
      height: 100%;
      background: var(--accent);
      width: 0%;
      transition: width 0.3s ease;
    }}

    /* Main Container */
    main {{
      max-width: 1200px;
      margin: 0 auto;
      padding: 24px 20px 80px;
    }}

    /* Pillar Tabs */
    .pillar-nav {{
      display: flex;
      gap: 8px;
      overflow-x: auto;
      padding-bottom: 12px;
      border-bottom: 1px solid var(--border);
      margin-bottom: 24px;
      scrollbar-width: thin;
    }}
    .pillar-tab {{
      flex-shrink: 0;
      padding: 8px 14px;
      border-radius: 6px;
      border: 1px solid var(--border);
      background: var(--card-bg);
      color: var(--text-muted);
      font-size: 13px;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.15s ease;
    }}
    .pillar-tab:hover {{
      border-color: var(--border-accent);
      color: var(--text);
      background: var(--card-hover);
    }}
    .pillar-tab.active {{
      background: var(--accent);
      border-color: var(--accent);
      color: #FFFFFF;
      font-weight: 600;
    }}
    html.dark .pillar-tab.active {{
      color: #121413;
    }}

    /* Class Sub-Nav */
    .class-bar {{
      display: flex;
      align-items: center;
      gap: 8px;
      overflow-x: auto;
      padding-bottom: 12px;
      margin-bottom: 20px;
    }}
    .class-pill {{
      flex-shrink: 0;
      padding: 5px 12px;
      border-radius: 20px;
      border: 1px solid var(--border);
      background: var(--card-bg);
      color: var(--text-muted);
      font-size: 12px;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.15s ease;
    }}
    .class-pill:hover {{
      border-color: var(--border-accent);
      color: var(--text);
    }}
    .class-pill.active {{
      background: var(--accent-soft);
      border-color: var(--accent);
      color: var(--accent-text);
      font-weight: 600;
    }}

    /* Act Bar for Class 11 */
    .act-bar {{
      display: flex;
      gap: 6px;
      overflow-x: auto;
      padding-bottom: 12px;
      margin-bottom: 20px;
      border-bottom: 1px dashed var(--border);
    }}
    .act-pill {{
      flex-shrink: 0;
      padding: 5px 12px;
      border-radius: 6px;
      border: 1px solid var(--border);
      background: var(--card-bg);
      color: var(--text-muted);
      font-size: 11px;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.15s ease;
    }}
    .act-pill:hover {{
      border-color: var(--border-accent);
      color: var(--text);
    }}
    .act-pill.active {{
      background: var(--accent);
      color: #FFFFFF;
      border-color: var(--accent);
      font-weight: 600;
    }}
    html.dark .act-pill.active {{
      color: #121413;
    }}

    /* Overview Header */
    .view-header {{
      margin-bottom: 24px;
      padding: 18px 20px;
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 8px;
    }}
    .view-title {{
      font-size: 20px;
      font-weight: 600;
      letter-spacing: -0.01em;
      margin-bottom: 6px;
    }}
    .view-desc {{
      font-size: 13px;
      color: var(--text-muted);
    }}

    /* Submodule & Slide Card Deck */
    .submodule-grid {{
      display: grid;
      grid-template-columns: 1fr;
      gap: 24px;
    }}
    .submodule-card {{
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 22px 24px;
      position: relative;
      transition: border-color 0.15s ease;
    }}
    .submodule-card:hover {{
      border-color: var(--border-accent);
    }}
    .card-top {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      margin-bottom: 12px;
    }}
    .card-badges {{
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }}
    .badge-subid {{
      font-size: 11px;
      font-weight: 700;
      font-family: ui-monospace, monospace;
      padding: 2px 6px;
      background: var(--tag-bg);
      color: var(--tag-text);
      border-radius: 4px;
    }}
    .badge-act {{
      font-size: 11px;
      font-weight: 500;
      padding: 2px 6px;
      background: var(--accent-soft);
      color: var(--accent-text);
      border-radius: 4px;
    }}
    .badge-readtime {{
      font-size: 11px;
      color: var(--text-muted);
    }}
    .btn-complete {{
      background: none;
      border: 1px solid var(--border);
      color: var(--text-muted);
      border-radius: 6px;
      padding: 3px 8px;
      font-size: 11px;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 4px;
    }}
    .btn-complete.checked {{
      background: var(--success-bg);
      border-color: var(--success);
      color: var(--success);
      font-weight: 600;
    }}

    /* Continuity Bridge */
    .continuity-bridge {{
      background: var(--bridge-bg);
      border-left: 3px solid var(--bridge-border);
      padding: 8px 12px;
      border-radius: 0 6px 6px 0;
      margin-bottom: 14px;
      font-size: 12px;
      display: flex;
      align-items: baseline;
      gap: 8px;
    }}
    .bridge-tag {{
      font-size: 10px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--bridge-text);
      flex-shrink: 0;
    }}
    .bridge-text {{
      color: var(--text);
      font-style: italic;
      line-height: 1.45;
    }}

    .submodule-title {{
      font-size: 18px;
      font-weight: 600;
      margin-bottom: 12px;
      letter-spacing: -0.01em;
    }}

    /* ELI15 Callout */
    .callout-eli15 {{
      background: var(--callout-bg);
      border-left: 3px solid var(--accent);
      padding: 12px 16px;
      border-radius: 0 6px 6px 0;
      margin-bottom: 16px;
    }}
    .callout-label {{
      font-size: 10px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--accent);
      margin-bottom: 4px;
    }}
    .callout-text {{
      font-size: 14px;
      font-weight: 500;
      line-height: 1.5;
    }}

    /* Bullets */
    .bullets-list {{
      list-style: none;
      margin-bottom: 16px;
    }}
    .bullets-list li {{
      position: relative;
      padding-left: 18px;
      margin-bottom: 8px;
      font-size: 13px;
      color: var(--text);
    }}
    .bullets-list li::before {{
      content: "•";
      position: absolute;
      left: 4px;
      color: var(--accent);
      font-weight: bold;
    }}

    /* Mental Model Box */
    .mental-box {{
      background: var(--card-hover);
      border: 1px dashed var(--border-accent);
      border-radius: 6px;
      padding: 12px 14px;
      margin-bottom: 18px;
      font-size: 12px;
      display: flex;
      gap: 10px;
      align-items: flex-start;
    }}
    .mental-icon {{
      font-size: 16px;
      flex-shrink: 0;
      line-height: 1;
    }}
    .mental-desc {{
      color: var(--text);
      line-height: 1.45;
    }}

    /* Checkpoint Active Recall */
    .checkpoint-wrap {{
      background: var(--checkpoint-bg);
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 16px;
      margin-top: 14px;
    }}
    .checkpoint-hdr {{
      display: flex;
      align-items: center;
      gap: 6px;
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      color: var(--text-muted);
      margin-bottom: 8px;
    }}
    .checkpoint-q {{
      font-size: 13px;
      font-weight: 600;
      margin-bottom: 12px;
      line-height: 1.4;
    }}
    .checkpoint-options {{
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}
    .cp-opt {{
      padding: 8px 12px;
      border-radius: 6px;
      border: 1px solid var(--border);
      background: var(--card-bg);
      color: var(--text);
      font-size: 12px;
      cursor: pointer;
      text-align: left;
      transition: all 0.15s ease;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .cp-opt:hover:not(.disabled) {{
      border-color: var(--accent);
      background: var(--card-hover);
    }}
    .cp-opt.correct {{
      background: var(--success-bg) !important;
      border-color: var(--success) !important;
      color: var(--success) !important;
      font-weight: 600;
    }}
    .cp-opt.wrong {{
      background: var(--danger-bg) !important;
      border-color: var(--danger) !important;
      color: var(--danger) !important;
    }}
    .cp-opt.disabled {{
      cursor: default;
    }}
    .cp-feedback {{
      margin-top: 10px;
      font-size: 12px;
      padding: 8px 12px;
      border-radius: 6px;
      display: none;
      line-height: 1.4;
    }}
    .cp-feedback.show {{
      display: block;
    }}

    /* Case Study Dossier Hub */
    .case-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
      gap: 20px;
    }}
    .case-card {{
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 20px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}
    .case-title {{
      font-size: 16px;
      font-weight: 600;
      margin-bottom: 12px;
      line-height: 1.35;
    }}
    .case-section {{
      margin-bottom: 12px;
    }}
    .case-label {{
      font-size: 10px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 3px;
    }}
    .case-label.what {{ color: #C2410C; }}
    .case-label.cause {{ color: #B45309; }}
    .case-label.takeaway {{ color: var(--accent); }}
    .case-text {{
      font-size: 12px;
      line-height: 1.45;
      color: var(--text);
    }}

    /* Formula Cheat Sheet */
    .cheat-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
      gap: 20px;
    }}
    .cheat-card {{
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 20px;
    }}
    .cheat-title {{
      font-size: 15px;
      font-weight: 600;
      margin-bottom: 10px;
    }}
    .cheat-formula {{
      background: var(--card-hover);
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 12px;
      text-align: center;
      margin-bottom: 12px;
      font-size: 15px;
      overflow-x: auto;
    }}
    .cheat-desc {{
      font-size: 12px;
      color: var(--text-muted);
      line-height: 1.45;
    }}

    /* Responsive */
    @media (max-width: 768px) {{
      .header-inner {{ flex-direction: column; align-items: stretch; }}
      .search-wrap {{ width: 100%; }}
      .case-grid, .cheat-grid {{ grid-template-columns: 1fr; }}
    }}
  </style>
</head>
<body>

  <!-- HEADER -->
  <header>
    <div class="header-inner">
      <div class="brand">
        <div class="brand-logo">E</div>
        <div>
          <span class="brand-title">Environmental Science & Technology</span>
          <span class="brand-badge">ES1.101 • Field Guide</span>
        </div>
      </div>
      <div class="header-actions">
        <div class="search-wrap">
          <span class="search-icon">🔍</span>
          <input type="text" id="search-input" class="search-input" placeholder="Search concepts, case studies, formulas..." autocomplete="off">
        </div>
        <button id="theme-toggle" class="btn-toggle">
          <span id="theme-icon">🌙</span> <span id="theme-label">Dark</span>
        </button>
      </div>
    </div>
    <div class="progress-strip">
      <div id="progress-fill" class="progress-fill"></div>
    </div>
  </header>

  <!-- MAIN -->
  <main>
    <!-- PILLAR TABS -->
    <nav class="pillar-nav" id="pillar-tabs">
      <button class="pillar-tab active" data-pillar="1">1. Foundations & Pressures</button>
      <button class="pillar-tab" data-pillar="2">2. Earth Systems & Disasters</button>
      <button class="pillar-tab" data-pillar="3">3. Climate & Sinks</button>
      <button class="pillar-tab" data-pillar="4">4. Cleantech & Engineering</button>
      <button class="pillar-tab" data-pillar="5">5. Governance & Ethics</button>
      <button class="pillar-tab" id="case-study-hub" data-view="case-studies">📁 Case Study Hub (12)</button>
      <button class="pillar-tab" id="formula-sheet" data-view="cheat-sheet">📐 Formula Sheet</button>
    </nav>

    <!-- CLASS PILLS -->
    <div class="class-bar" id="class-pills"></div>

    <!-- ACT FILTER BAR (FOR CLASS 11) -->
    <div class="act-bar" id="act-bar" style="display: none;"></div>

    <!-- VIEW HEADER -->
    <div class="view-header" id="view-header">
      <h1 class="view-title" id="view-title">Pillar 1: Planetary Foundations & Human Pressures</h1>
      <p class="view-desc" id="view-desc">Earth systems, thermodynamic constraints, population pressures, and the cautionary dystopian future.</p>
    </div>

    <!-- CONTENT DISPLAY CONTAINER -->
    <div id="content-container"></div>
  </main>

  <script>
    // Injected Curriculum Database
    const DB = {db_json_escaped};

    // State
    let currentPillar = 1;
    let currentClassId = 1;
    let currentActFilter = "ALL";
    let currentView = "curriculum"; // "curriculum", "case-studies", "cheat-sheet", "search"
    let completedSubmodules = new Set(JSON.parse(localStorage.getItem("est_completed_subs") || "[]"));

    // DOM Elements
    const pillarTabs = document.getElementById("pillar-tabs");
    const classPills = document.getElementById("class-pills");
    const actBar = document.getElementById("act-bar");
    const viewHeader = document.getElementById("view-header");
    const viewTitle = document.getElementById("view-title");
    const viewDesc = document.getElementById("view-desc");
    const contentContainer = document.getElementById("content-container");
    const searchInput = document.getElementById("search-input");
    const themeToggle = document.getElementById("theme-toggle");
    const themeIcon = document.getElementById("theme-icon");
    const themeLabel = document.getElementById("theme-label");
    const progressFill = document.getElementById("progress-fill");

    // Initialize Theme
    function initTheme() {{
      const savedTheme = localStorage.getItem("est_theme") || "light";
      if (savedTheme === "dark") {{
        document.documentElement.classList.add("dark");
        document.documentElement.classList.remove("light");
        themeIcon.textContent = "☀️";
        themeLabel.textContent = "Light";
      }} else {{
        document.documentElement.classList.add("light");
        document.documentElement.classList.remove("dark");
        themeIcon.textContent = "🌙";
        themeLabel.textContent = "Dark";
      }}
    }}

    themeToggle.addEventListener("click", () => {{
      const isDark = document.documentElement.classList.contains("dark");
      if (isDark) {{
        document.documentElement.classList.remove("dark");
        document.documentElement.classList.add("light");
        themeIcon.textContent = "🌙";
        themeLabel.textContent = "Dark";
        localStorage.setItem("est_theme", "light");
      }} else {{
        document.documentElement.classList.remove("light");
        document.documentElement.classList.add("dark");
        themeIcon.textContent = "☀️";
        themeLabel.textContent = "Light";
        localStorage.setItem("est_theme", "dark");
      }}
    }});

    // Update Progress
    function updateProgress() {{
      const total = DB.metadata.submodules_count || 63;
      const count = completedSubmodules.size;
      const pct = Math.round((count / total) * 100);
      progressFill.style.width = Math.min(100, pct) + "%";
    }}

    function toggleSubmoduleCompletion(subId, btn) {{
      if (completedSubmodules.has(subId)) {{
        completedSubmodules.delete(subId);
        btn.classList.remove("checked");
        btn.innerHTML = "<span>○</span> Mark Complete";
      }} else {{
        completedSubmodules.add(subId);
        btn.classList.add("checked");
        btn.innerHTML = "<span>✓</span> Completed";
      }}
      localStorage.setItem("est_completed_subs", JSON.stringify([...completedSubmodules]));
      updateProgress();
    }}

    // Render Classes within Pillar
    function renderClassPills() {{
      classPills.innerHTML = "";
      if (currentView !== "curriculum") {{
        classPills.style.display = "none";
        actBar.style.display = "none";
        return;
      }}
      classPills.style.display = "flex";

      const pillarObj = DB.pillars.find(p => p.id === currentPillar);
      if (!pillarObj) return;

      pillarObj.classes.forEach(cid => {{
        const c = DB.classes.find(cl => cl.class_id === cid);
        if (!c) return;
        const pill = document.createElement("button");
        pill.className = "class-pill" + (cid === currentClassId ? " active" : "");
        pill.textContent = `Class ${{c.class_id}}: ${{c.title.split(':')[0].replace('Class-', '')}}`;
        pill.addEventListener("click", () => {{
          currentClassId = cid;
          currentActFilter = "ALL";
          renderClassPills();
          renderCurrentClassContent();
        }});
        classPills.appendChild(pill);
      }});
    }}

    // Render Current Class Content
    function renderCurrentClassContent() {{
      const c = DB.classes.find(cl => cl.class_id === currentClassId);
      if (!c) return;

      viewTitle.textContent = `Class ${{c.class_id}}: ${{c.title}}`;
      viewDesc.textContent = c.summary;

      // Special Slidewise Rendering for Class 11 (29 slides)
      if (c.class_id === 11 && c.slides && c.slides.length > 0) {{
        renderClass11Slides(c);
        return;
      }}

      // Standard Submodule Rendering for other classes
      actBar.style.display = "none";
      let html = `<div class="submodule-grid">`;
      c.submodules.forEach(sub => {{
        const isDone = completedSubmodules.has(sub.id);
        html += `
          <div class="submodule-card" id="sub-${{sub.id}}">
            <div class="card-top">
              <div class="card-badges">
                <span class="badge-subid">MODULE ${{sub.id}}</span>
                <span class="badge-readtime">⚡ 2 min bite</span>
              </div>
              <button class="btn-complete ${{isDone ? 'checked' : ''}}" onclick="toggleSubmoduleCompletion('${{sub.id}}', this)">
                <span>${{isDone ? '✓' : '○'}}</span> ${{isDone ? 'Completed' : 'Mark Complete'}}
              </button>
            </div>

            <h2 class="submodule-title">${{sub.title}}</h2>

            <div class="callout-eli15">
              <div class="callout-label">ELI15 Core Takeaway</div>
              <div class="callout-text">${{sub.eli15_takeaway}}</div>
            </div>

            <ul class="bullets-list">
              ${{sub.bullets.map(b => `<li>${{b}}</li>`).join('')}}
            </ul>

            <div class="mental-box">
              <span class="mental-icon">💡</span>
              <div class="mental-desc"><strong>Mental Model:</strong> ${{sub.mental_model}}</div>
            </div>

            <div class="checkpoint-wrap">
              <div class="checkpoint-hdr"><span>⚡</span> Instant Recall Checkpoint</div>
              <div class="checkpoint-q">${{sub.checkpoint.question}}</div>
              <div class="checkpoint-options" id="cp-opts-${{sub.id.replace('.', '-')}}">
                ${{sub.checkpoint.options.map((opt, idx) => `
                  <button class="cp-opt" onclick="handleCheckpoint('${{sub.id}}', ${{idx}}, ${{sub.checkpoint.correct_index}}, '${{encodeURIComponent(sub.checkpoint.explanation)}}', this)">
                    ${{opt}}
                  </button>
                `).join('')}}
              </div>
              <div class="cp-feedback" id="cp-fb-${{sub.id.replace('.', '-')}}"></div>
            </div>
          </div>
        `;
      }});
      html += `</div>`;
      contentContainer.innerHTML = html;
      triggerKaTeX();
    }}

    // Render Class 11 Slidewise Deck with Narrative Acts & Continuity
    function renderClass11Slides(c) {{
      actBar.style.display = "flex";
      actBar.innerHTML = "";

      const acts = [
        {{ id: "ALL", label: "All 29 Slides" }},
        {{ id: "Act 1", label: "Act 1: Nature's Sponges (1–5)" }},
        {{ id: "Act 2", label: "Act 2: Earth Chemistry (6–7)" }},
        {{ id: "Act 3", label: "Act 3: Artificial Trees & DAC (8–16)" }},
        {{ id: "Act 4", label: "Act 4: Food & Farming (17–19, 25–28)" }},
        {{ id: "Act 5", label: "Act 5: Clean Propulsion & IT (21–23)" }},
        {{ id: "Act 6", label: "Act 6: Space & AI Frontier (20, 24, 29)" }}
      ];

      acts.forEach(a => {{
        const btn = document.createElement("button");
        btn.className = "act-pill" + (currentActFilter === a.id ? " active" : "");
        btn.textContent = a.label;
        btn.addEventListener("click", () => {{
          currentActFilter = a.id;
          renderClass11Slides(c);
        }});
        actBar.appendChild(btn);
      }});

      let filteredSlides = c.slides;
      if (currentActFilter !== "ALL") {{
        filteredSlides = c.slides.filter(s => s.act.startsWith(currentActFilter));
      }}

      let html = `<div class="submodule-grid">`;
      filteredSlides.forEach(s => {{
        const slideId = `11.${{s.slide_num}}`;
        const isDone = completedSubmodules.has(slideId);
        html += `
          <div class="submodule-card" id="sub-${{slideId}}">
            <div class="card-top">
              <div class="card-badges">
                <span class="badge-subid">SLIDE ${{s.slide_num}} / 29</span>
                <span class="badge-act">${{s.act.split(':')[0]}}</span>
                <span class="badge-readtime">⚡ 2 min bite</span>
              </div>
              <button class="btn-complete ${{isDone ? 'checked' : ''}}" onclick="toggleSubmoduleCompletion('${{slideId}}', this)">
                <span>${{isDone ? '✓' : '○'}}</span> ${{isDone ? 'Completed' : 'Mark Complete'}}
              </button>
            </div>

            <!-- Continuity Bridge -->
            <div class="continuity-bridge">
              <span class="bridge-tag">🔗 Continuity Bridge</span>
              <span class="bridge-text">${{s.continuity_bridge}}</span>
            </div>

            <h2 class="submodule-title">${{s.title}}</h2>

            <div class="callout-eli15">
              <div class="callout-label">ELI15 Core Takeaway</div>
              <div class="callout-text">${{s.eli15_takeaway}}</div>
            </div>

            <ul class="bullets-list">
              ${{s.key_facts.map(f => `<li>${{f}}</li>`).join('')}}
            </ul>

            <div class="mental-box">
              <span class="mental-icon">💡</span>
              <div class="mental-desc"><strong>Mental Model:</strong> ${{s.mental_model}}</div>
            </div>

            <div class="checkpoint-wrap">
              <div class="checkpoint-hdr"><span>⚡</span> Instant Recall Checkpoint</div>
              <div class="checkpoint-q">${{s.checkpoint.question}}</div>
              <div class="checkpoint-options" id="cp-opts-${{slideId.replace('.', '-')}}">
                ${{s.checkpoint.options.map((opt, idx) => `
                  <button class="cp-opt" onclick="handleCheckpoint('${{slideId}}', ${{idx}}, ${{s.checkpoint.correct_index}}, '${{encodeURIComponent(s.checkpoint.explanation)}}', this)">
                    ${{opt}}
                  </button>
                `).join('')}}
              </div>
              <div class="cp-feedback" id="cp-fb-${{slideId.replace('.', '-')}}"></div>
            </div>
          </div>
        `;
      }});
      html += `</div>`;
      contentContainer.innerHTML = html;
      triggerKaTeX();
    }}

    function triggerKaTeX() {{
      if (window.renderMathInElement) {{
        renderMathInElement(contentContainer, {{
          delimiters: [
            {{left: '$$', right: '$$', display: true}},
            {{left: '$', right: '$', display: false}},
            {{left: '\\(', right: '\\)', display: false}},
            {{left: '\\[', right: '\\]', display: true}}
          ],
          throwOnError: false
        }});
      }}
    }}

    // Checkpoint Handler
    window.handleCheckpoint = function(subId, selectedIdx, correctIdx, encodedExpl, btn) {{
      const safeId = subId.replace('.', '-');
      const container = document.getElementById(`cp-opts-${{safeId}}`);
      const feedback = document.getElementById(`cp-fb-${{safeId}}`);
      const expl = decodeURIComponent(encodedExpl);

      const buttons = container.querySelectorAll(".cp-opt");
      buttons.forEach((b, idx) => {{
        b.classList.add("disabled");
        if (idx === correctIdx) {{
          b.classList.add("correct");
        }}
      }});

      if (selectedIdx === correctIdx) {{
        btn.classList.add("correct");
        feedback.className = "cp-feedback show";
        feedback.style.background = "var(--success-bg)";
        feedback.style.color = "var(--success)";
        feedback.innerHTML = `<strong>✓ Correct!</strong> ${{expl}}`;
        const card = document.getElementById(`sub-${{subId}}`);
        if (card) {{
          const compBtn = card.querySelector(".btn-complete");
          if (!completedSubmodules.has(subId)) {{
            toggleSubmoduleCompletion(subId, compBtn);
          }}
        }}
      }} else {{
        btn.classList.add("wrong");
        feedback.className = "cp-feedback show";
        feedback.style.background = "var(--danger-bg)";
        feedback.style.color = "var(--danger)";
        feedback.innerHTML = `<strong>✗ Not quite.</strong> ${{expl}}`;
      }}
    }};

    // Render Case Studies Hub
    function renderCaseStudies() {{
      actBar.style.display = "none";
      viewTitle.textContent = "Case Study Hub: 12 Landmark Historical Incidents";
      viewDesc.textContent = "Structured 3-part breakdowns (What Happened → The Root Cause → The Takeaway) for exams and real-world retention.";

      let html = `<div class="case-grid">`;
      DB.case_studies.forEach(cs => {{
        html += `
          <div class="case-card">
            <div>
              <span class="badge-subid" style="margin-bottom: 8px; display: inline-block;">CLASS ${{cs.class_id}} CASE STUDY</span>
              <h3 class="case-title">${{cs.name}}</h3>
              
              <div class="case-section">
                <div class="case-label what">What Happened</div>
                <div class="case-text">${{cs.what_happened}}</div>
              </div>

              <div class="case-section">
                <div class="case-label cause">The Root Cause</div>
                <div class="case-text">${{cs.root_cause}}</div>
              </div>
            </div>

            <div class="case-section" style="border-top: 1px solid var(--border); padding-top: 10px; margin-top: 10px;">
              <div class="case-label takeaway">The Takeaway & Fix</div>
              <div class="case-text">${{cs.takeaway}}</div>
            </div>
          </div>
        `;
      }});
      html += `</div>`;
      contentContainer.innerHTML = html;
      triggerKaTeX();
    }}

    // Render Cheat Sheet
    function renderCheatSheet() {{
      actBar.style.display = "none";
      viewTitle.textContent = "Formula & Law Cheat Sheet";
      viewDesc.textContent = "Key ecological laws, mathematical indices (IPAT, NDVI, PUE, Green GDP), and thermodynamic equations.";

      let html = `<div class="cheat-grid">`;
      DB.cheat_sheet.forEach(item => {{
        html += `
          <div class="cheat-card">
            <span class="badge-subid" style="margin-bottom: 8px; display: inline-block;">${{item.category}}</span>
            <h3 class="cheat-title">${{item.title}}</h3>
            <div class="cheat-formula">$$${{item.formula}}$$</div>
            <p class="cheat-desc">${{item.explanation}}</p>
          </div>
        `;
      }});
      html += `</div>`;
      contentContainer.innerHTML = html;
      triggerKaTeX();
    }}

    // Search Execution
    function handleSearch(q) {{
      q = q.trim().toLowerCase();
      if (!q) {{
        renderPillarView(currentPillar);
        return;
      }}

      currentView = "search";
      classPills.style.display = "none";
      actBar.style.display = "none";
      viewTitle.textContent = `Search Results for "${{q}}"`;

      let matches = [];
      DB.classes.forEach(c => {{
        if (c.submodules) {{
          c.submodules.forEach(sub => {{
            const textCorpus = (sub.title + " " + sub.eli15_takeaway + " " + sub.bullets.join(" ") + " " + sub.mental_model).toLowerCase();
            if (textCorpus.includes(q)) {{
              matches.push({{
                type: "submodule",
                class_id: c.class_id,
                class_title: c.title,
                data: sub
              }});
            }}
          }});
        }}

        // Also search Class 11 slides
        if (c.slides) {{
          c.slides.forEach(slide => {{
            const textCorpus = (slide.title + " " + slide.continuity_bridge + " " + slide.eli15_takeaway + " " + slide.key_facts.join(" ") + " " + slide.mental_model).toLowerCase();
            if (textCorpus.includes(q)) {{
              matches.push({{
                type: "slide",
                class_id: c.class_id,
                class_title: c.title,
                data: slide
              }});
            }}
          }});
        }}
      }});

      DB.case_studies.forEach(cs => {{
        const csCorpus = (cs.name + " " + cs.what_happened + " " + cs.root_cause + " " + cs.takeaway).toLowerCase();
        if (csCorpus.includes(q)) {{
          matches.push({{
            type: "case_study",
            data: cs
          }});
        }}
      }});

      viewDesc.textContent = `Found ${{matches.length}} matching item(s) across the course materials.`;

      if (matches.length === 0) {{
        contentContainer.innerHTML = `<div style="text-align: center; padding: 60px 20px; color: var(--text-muted);">No results found matching "${{q}}". Try searching for "carbon", "NDVI", "Aether", "Zelp", "seaweed", "Bhopal", or "EIA".</div>`;
        return;
      }}

      let html = `<div class="submodule-grid">`;
      matches.forEach(m => {{
        if (m.type === "slide") {{
          const s = m.data;
          const slideId = `11.${{s.slide_num}}`;
          const isDone = completedSubmodules.has(slideId);
          html += `
            <div class="submodule-card" id="sub-${{slideId}}">
              <div class="card-top">
                <div class="card-badges">
                  <span class="badge-subid">CLASS 11 • SLIDE ${{s.slide_num}}</span>
                  <span class="badge-act">${{s.act.split(':')[0]}}</span>
                  <span class="badge-readtime">⚡ 2 min bite</span>
                </div>
                <button class="btn-complete ${{isDone ? 'checked' : ''}}" onclick="toggleSubmoduleCompletion('${{slideId}}', this)">
                  <span>${{isDone ? '✓' : '○'}}</span> ${{isDone ? 'Completed' : 'Mark Complete'}}
                </button>
              </div>
              <div class="continuity-bridge">
                <span class="bridge-tag">🔗 Continuity</span>
                <span class="bridge-text">${{s.continuity_bridge}}</span>
              </div>
              <h2 class="submodule-title">${{s.title}}</h2>
              <div class="callout-eli15">
                <div class="callout-label">ELI15 Core Takeaway</div>
                <div class="callout-text">${{s.eli15_takeaway}}</div>
              </div>
              <ul class="bullets-list">
                ${{s.key_facts.map(f => `<li>${{f}}</li>`).join('')}}
              </ul>
            </div>
          `;
        }} else if (m.type === "submodule") {{
          const sub = m.data;
          const isDone = completedSubmodules.has(sub.id);
          html += `
            <div class="submodule-card" id="sub-${{sub.id}}">
              <div class="card-top">
                <div class="card-badges">
                  <span class="badge-subid">CLASS ${{m.class_id}} • MODULE ${{sub.id}}</span>
                  <span class="badge-readtime">${{m.class_title.split(':')[0]}}</span>
                </div>
                <button class="btn-complete ${{isDone ? 'checked' : ''}}" onclick="toggleSubmoduleCompletion('${{sub.id}}', this)">
                  <span>${{isDone ? '✓' : '○'}}</span> ${{isDone ? 'Completed' : 'Mark Complete'}}
                </button>
              </div>
              <h2 class="submodule-title">${{sub.title}}</h2>
              <div class="callout-eli15">
                <div class="callout-label">ELI15 Core Takeaway</div>
                <div class="callout-text">${{sub.eli15_takeaway}}</div>
              </div>
              <ul class="bullets-list">
                ${{sub.bullets.map(b => `<li>${{b}}</li>`).join('')}}
              </ul>
            </div>
          `;
        }} else if (m.type === "case_study") {{
          const cs = m.data;
          html += `
            <div class="submodule-card" style="border-left: 3px solid #C2410C;">
              <span class="badge-subid" style="margin-bottom: 8px; display: inline-block;">CASE STUDY • CLASS ${{cs.class_id}}</span>
              <h2 class="submodule-title">${{cs.name}}</h2>
              <p style="font-size: 13px; margin-bottom: 8px;"><strong>What Happened:</strong> ${{cs.what_happened}}</p>
              <p style="font-size: 13px; margin-bottom: 8px;"><strong>Root Cause:</strong> ${{cs.root_cause}}</p>
              <p style="font-size: 13px; color: var(--accent);"><strong>Takeaway:</strong> ${{cs.takeaway}}</p>
            </div>
          `;
        }}
      }});
      html += `</div>`;
      contentContainer.innerHTML = html;
      triggerKaTeX();
    }}

    searchInput.addEventListener("input", (e) => {{
      handleSearch(e.target.value);
    }});

    // Pillar Navigation Click
    function renderPillarView(pId) {{
      currentView = "curriculum";
      currentPillar = pId;
      const pillarObj = DB.pillars.find(p => p.id === currentPillar);
      if (pillarObj && !pillarObj.classes.includes(currentClassId)) {{
        currentClassId = pillarObj.classes[0];
      }}
      currentActFilter = "ALL";
      renderClassPills();
      renderCurrentClassContent();
    }}

    pillarTabs.addEventListener("click", (e) => {{
      const tab = e.target.closest(".pillar-tab");
      if (!tab) return;

      document.querySelectorAll(".pillar-tab").forEach(t => t.classList.remove("active"));
      tab.classList.add("active");

      const pId = tab.dataset.pillar;
      const v = tab.dataset.view;

      if (pId) {{
        renderPillarView(parseInt(pId, 10));
      }} else if (v === "case-studies") {{
        currentView = "case-studies";
        classPills.style.display = "none";
        renderCaseStudies();
      }} else if (v === "cheat-sheet") {{
        currentView = "cheat-sheet";
        classPills.style.display = "none";
        renderCheatSheet();
      }}
    }});

    // Boot
    initTheme();
    updateProgress();
    renderClassPills();
    renderCurrentClassContent();
  </script>
</body>
</html>'''

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
        
    print(f"Successfully generated index.html ({len(html)} bytes).")

if __name__ == "__main__":
    build_website()
