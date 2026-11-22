import json
import os

def build_website():
    db_path = os.path.join("Study_Material", "curriculum_database.json")
    with open(db_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    qb_path = os.path.join("Study_Material", "endsem_question_bank.json")
    if os.path.exists(qb_path):
        with open(qb_path, "r", encoding="utf-8") as fq:
            data["endsem_question_bank"] = json.load(fq)
        
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
          onload="renderMathInElement(document.body, {{delimiters: [{{left: '$$', right: '$$', display: true}}, {{left: '\\\\(', right: '\\\\)', display: false}}, {{left: '\\\\[', right: '\\\\]', display: true}}], throwOnError: false}});"></script>
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
      overflow-wrap: break-word;
      word-wrap: break-word;
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

    /* Exam Rating Badges & Mode Switcher */
    .view-mode-bar {{
      display: inline-flex;
      gap: 6px;
      margin-bottom: 16px;
      background: var(--card-hover);
      padding: 4px;
      border-radius: 8px;
      border: 1px solid var(--border);
    }}
    .view-mode-btn {{
      background: transparent;
      border: none;
      padding: 6px 12px;
      font-size: 12px;
      font-weight: 600;
      color: var(--text-muted);
      border-radius: 6px;
      cursor: pointer;
      transition: all 0.15s ease;
    }}
    .view-mode-btn:hover {{
      color: var(--text);
    }}
    .view-mode-btn.active {{
      background: var(--card-bg);
      color: var(--accent);
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08);
    }}
    .badge-critical {{
      font-size: 11px;
      font-weight: 700;
      padding: 2px 8px;
      background: #fef3c7;
      color: #92400e;
      border: 1px solid #fcd34d;
      border-radius: 4px;
      display: inline-flex;
      align-items: center;
      gap: 4px;
    }}
    .badge-high {{
      font-size: 11px;
      font-weight: 700;
      padding: 2px 8px;
      background: #ecfdf5;
      color: #065f46;
      border: 1px solid #a7f3d0;
      border-radius: 4px;
      display: inline-flex;
      align-items: center;
      gap: 4px;
    }}
    .badge-medium {{
      font-size: 11px;
      font-weight: 600;
      padding: 2px 8px;
      background: #eff6ff;
      color: #1e40af;
      border: 1px solid #bfdbfe;
      border-radius: 4px;
      display: inline-flex;
      align-items: center;
      gap: 4px;
    }}
    .badge-slides {{
      font-size: 11px;
      font-weight: 600;
      font-family: ui-monospace, monospace;
      padding: 2px 8px;
      background: var(--tag-bg);
      color: var(--tag-text);
      border: 1px solid var(--border);
      border-radius: 4px;
    }}
    .exam-provenance-box {{
      background: var(--card-hover);
      border: 1px solid var(--border);
      border-left: 3px solid #d97706;
      border-radius: 0 6px 6px 0;
      padding: 10px 14px;
      margin-bottom: 14px;
      font-size: 12px;
    }}
    .exam-hdr {{
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      color: #d97706;
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .exam-chip-list {{
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-bottom: 8px;
    }}
    .exam-chip {{
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 4px;
      padding: 2px 8px;
      font-size: 11px;
      font-weight: 600;
      color: var(--text);
    }}
    .exam-tip {{
      color: var(--text);
      font-size: 12px;
      line-height: 1.45;
    }}

    /* Attached Exam Questions Section */
    .exam-questions-section {{
      background: var(--card-hover);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 14px;
      margin-top: 16px;
      margin-bottom: 14px;
    }}
    .exam-q-hdr {{
      font-size: 12px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: #b45309;
      display: flex;
      align-items: center;
      gap: 6px;
      margin-bottom: 10px;
    }}
    .exam-q-list {{
      display: flex;
      flex-direction: column;
      gap: 10px;
    }}
    .exam-q-card {{
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-left: 3px solid #f59e0b;
      border-radius: 4px;
      padding: 10px 12px;
    }}
    .exam-q-meta {{
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 6px;
      margin-bottom: 6px;
      font-size: 11px;
    }}
    .exam-q-paper {{
      font-weight: 700;
      color: #b45309;
      background: rgba(245, 158, 11, 0.1);
      padding: 2px 6px;
      border-radius: 3px;
    }}
    .exam-q-section {{
      color: var(--text-muted);
      font-weight: 500;
    }}
    .exam-q-marks {{
      margin-left: auto;
      font-weight: 700;
      color: #047857;
      background: rgba(16, 185, 129, 0.1);
      padding: 2px 6px;
      border-radius: 3px;
    }}
    .exam-q-prompt {{
      font-size: 13px;
      font-weight: 600;
      color: var(--text);
      line-height: 1.45;
      margin-bottom: 8px;
    }}
    .exam-answer-details {{
      background: var(--bg);
      border: 1px solid var(--border);
      border-radius: 4px;
      overflow: hidden;
      margin-top: 6px;
    }}
    .exam-answer-summary {{
      cursor: pointer;
      padding: 6px 10px;
      font-size: 11px;
      font-weight: 700;
      color: #b45309;
      display: flex;
      align-items: center;
      gap: 6px;
      user-select: none;
      background: rgba(245, 158, 11, 0.05);
    }}
    .exam-answer-summary:hover {{
      background: rgba(245, 158, 11, 0.12);
    }}
    .exam-answer-body {{
      padding: 10px 12px;
      font-size: 12px;
      color: var(--text);
      line-height: 1.55;
      border-top: 1px solid var(--border);
    }}
    .exam-answer-body ul, .exam-answer-body ol {{
      margin: 4px 0 4px 18px;
      padding: 0;
    }}
    .exam-answer-body li {{
      margin-bottom: 4px;
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
      margin-bottom: 9px;
      font-size: 13.5px;
      line-height: 1.6;
      color: var(--text);
      overflow-wrap: break-word;
      word-wrap: break-word;
    }}
    .bullets-list li::before {{
      content: "•";
      position: absolute;
      left: 4px;
      color: var(--accent);
      font-weight: bold;
    }}

    /* KaTeX math typography & overflow safety */
    .katex {{
      font-size: 1.05em;
      text-rendering: auto;
      white-space: normal;
    }}
    .katex-display {{
      margin: 1em 0;
      overflow-x: auto;
      overflow-y: hidden;
      padding: 4px 0;
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
  
    /* ============================================================
       ENDSEM QUESTION BANK & MODEL ANSWERS SUITE (Lectures 11–19)
       ============================================================ */
    .qb-container {{
      display: flex;
      flex-direction: column;
      gap: 20px;
    }}
    .qb-toolbar {{
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 16px 20px;
      display: flex;
      flex-direction: column;
      gap: 14px;
    }}
    .qb-class-pills {{
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      align-items: center;
    }}
    .qb-pill {{
      padding: 6px 12px;
      border-radius: 20px;
      border: 1px solid var(--border);
      background: var(--card-bg);
      color: var(--text-muted);
      font-size: 12px;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.15s ease;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }}
    .qb-pill:hover {{
      border-color: var(--border-accent);
      color: var(--text);
      background: var(--card-hover);
    }}
    .qb-pill.active {{
      background: var(--accent);
      color: #FFFFFF;
      border-color: var(--accent);
      font-weight: 600;
    }}
    html.dark .qb-pill.active {{
      color: #121413;
    }}
    .qb-pill .count {{
      font-size: 10px;
      padding: 1px 6px;
      border-radius: 10px;
      background: var(--tag-bg);
      color: var(--tag-text);
      font-weight: 700;
    }}
    .qb-pill.active .count {{
      background: rgba(255, 255, 255, 0.25);
      color: #FFFFFF;
    }}
    html.dark .qb-pill.active .count {{
      background: rgba(0, 0, 0, 0.25);
      color: #121413;
    }}
    .qb-filters-row {{
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      padding-top: 12px;
      border-top: 1px dashed var(--border);
    }}
    .qb-filter-group {{
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 8px;
    }}
    .qb-select {{
      padding: 6px 10px;
      border-radius: 6px;
      border: 1px solid var(--border);
      background: var(--card-bg);
      color: var(--text);
      font-size: 12px;
      outline: none;
      cursor: pointer;
    }}
    .qb-cat-checkbox-group {{
      display: flex;
      flex-direction: column;
      gap: 8px;
      width: 100%;
      padding-top: 10px;
      border-top: 1px dashed var(--border);
    }}
    .qb-cat-label-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
    }}
    .qb-cat-title {{
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--text-muted);
    }}
    .qb-cat-chips-row {{
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      align-items: center;
    }}
    .qb-check-chip {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 5px 10px;
      border-radius: 6px;
      border: 1px solid var(--border);
      background: var(--card-bg);
      color: var(--text);
      font-size: 11.5px;
      font-weight: 500;
      cursor: pointer;
      user-select: none;
      transition: all 0.15s ease;
    }}
    .qb-check-chip:hover {{
      background: var(--card-hover);
      border-color: var(--accent);
    }}
    .qb-check-chip.active {{
      background: var(--accent-subtle, rgba(46, 125, 50, 0.08));
      border-color: var(--accent);
      color: var(--accent);
      font-weight: 600;
    }}
    .qb-check-chip input[type="checkbox"] {{
      margin: 0;
      cursor: pointer;
      accent-color: var(--accent);
      width: 13px;
      height: 13px;
    }}
    .qb-check-chip .chip-count {{
      font-size: 10.5px;
      padding: 1px 6px;
      border-radius: 10px;
      background: var(--card-hover);
      color: var(--text-muted);
    }}
    .qb-check-chip.active .chip-count {{
      background: var(--accent);
      color: #ffffff;
    }}
    .qb-search-input {{
      padding: 6px 12px;
      border-radius: 6px;
      border: 1px solid var(--border);
      background: var(--card-hover);
      color: var(--text);
      font-size: 12px;
      outline: none;
      width: 220px;
      transition: all 0.15s ease;
    }}
    .qb-search-input:focus {{
      border-color: var(--accent);
      background: var(--card-bg);
      width: 260px;
    }}
    .qb-mode-group {{
      display: inline-flex;
      background: var(--card-hover);
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 2px;
    }}
    .qb-mode-btn {{
      padding: 4px 10px;
      font-size: 11px;
      font-weight: 600;
      border: none;
      background: transparent;
      color: var(--text-muted);
      cursor: pointer;
      border-radius: 4px;
      transition: all 0.15s ease;
    }}
    .qb-mode-btn.active {{
      background: var(--card-bg);
      color: var(--accent);
      box-shadow: 0 1px 2px rgba(0, 0, 0, 0.08);
    }}
    .qb-stats-strip {{
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      font-size: 12px;
      color: var(--text-muted);
      padding: 0 4px;
    }}
    .qb-progress-track {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-weight: 600;
      color: var(--text);
    }}
    .qb-progress-bar-mini {{
      width: 100px;
      height: 6px;
      background: var(--border);
      border-radius: 3px;
      overflow: hidden;
      display: inline-block;
    }}
    .qb-progress-bar-fill {{
      height: 100%;
      background: var(--success);
      width: 0%;
      transition: width 0.3s ease;
    }}

    /* Question Cards */
    .qb-cards-deck {{
      display: flex;
      flex-direction: column;
      gap: 20px;
    }}
    .qb-card {{
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 22px 24px;
      display: flex;
      flex-direction: column;
      gap: 14px;
      position: relative;
      transition: border-color 0.15s ease, box-shadow 0.15s ease;
    }}
    .qb-card:hover {{
      border-color: var(--border-accent);
    }}
    .qb-card.mastered {{
      border-left: 4px solid var(--success);
    }}
    .qb-card-header {{
      display: flex;
      flex-direction: column;
      gap: 8px;
    }}
    .qb-card-meta {{
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 8px;
    }}
    .qb-q-id {{
      font-family: ui-monospace, monospace;
      font-size: 11px;
      font-weight: 700;
      padding: 2px 7px;
      border-radius: 4px;
      background: var(--tag-bg);
      color: var(--tag-text);
    }}
    .qb-class-tag {{
      font-size: 11px;
      font-weight: 600;
      padding: 2px 8px;
      border-radius: 4px;
      background: var(--accent-soft);
      color: var(--accent-text);
    }}
    .qb-cat-tag {{
      font-size: 11px;
      font-weight: 500;
      padding: 2px 7px;
      border-radius: 4px;
      border: 1px solid var(--border);
      background: var(--card-bg);
      color: var(--text-muted);
    }}
    .qb-marks-tag {{
      margin-left: auto;
      font-size: 11px;
      font-weight: 700;
      padding: 2px 8px;
      border-radius: 4px;
      background: #ecfdf5;
      color: #065f46;
      border: 1px solid #a7f3d0;
    }}
    html.dark .qb-marks-tag {{
      background: #142820;
      color: #34d399;
      border-color: #244134;
    }}
    .qb-exams-row {{
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 6px;
    }}
    .qb-exam-pill {{
      font-size: 11px;
      padding: 2px 8px;
      border-radius: 4px;
      background: #fef3c7;
      color: #92400e;
      border: 1px solid #fcd34d;
      font-weight: 600;
    }}
    html.dark .qb-exam-pill {{
      background: #2b1f05;
      color: #fcd34d;
      border-color: #78350f;
    }}
    .qb-prompt-box {{
      background: var(--card-hover);
      border-left: 4px solid var(--accent);
      padding: 14px 16px;
      border-radius: 0 6px 6px 0;
      font-size: 14px;
      font-weight: 600;
      line-height: 1.55;
      color: var(--text);
    }}

    /* Collapsible Question Sections */
    details.qb-section {{
      border: 1px solid var(--border);
      border-radius: 6px;
      overflow: hidden;
      margin-top: 8px;
      background: var(--card-bg);
      transition: border-color 0.15s ease;
    }}
    details.qb-section:hover {{
      border-color: var(--border-accent, #cbd5e1);
    }}
    details.qb-section summary::-webkit-details-marker,
    details.qb-section summary::marker {{
      display: none;
    }}
    .qb-summary {{
      cursor: pointer;
      list-style: none;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 9px 14px;
      user-select: none;
      transition: background 0.15s ease;
    }}
    .qb-summary:hover {{
      background: var(--card-hover);
    }}
    .qb-summary-title {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-size: 13px;
      font-weight: 600;
      letter-spacing: -0.01em;
    }}
    .qb-chevron-icon {{
      transition: transform 0.18s ease;
      color: var(--text-muted);
      flex-shrink: 0;
    }}
    details:not([open]) .qb-chevron-icon {{
      transform: rotate(-90deg);
    }}
    details[open] .qb-chevron-icon {{
      transform: rotate(0deg);
    }}
    .qb-summary-hint {{
      font-size: 11px;
      color: var(--text-muted);
      opacity: 0.65;
      font-weight: 500;
    }}
    .qb-summary:hover .qb-summary-hint {{
      opacity: 1;
    }}

    /* Section 0: Expected Answer */
    .qb-section-exp {{
      border-color: #cbd5e1;
      margin-bottom: 8px;
    }}
    html.dark .qb-section-exp {{
      border-color: #27272a;
    }}
    .qb-section-exp .qb-summary {{
      background: rgba(217, 119, 6, 0.05);
      border-bottom: 1px solid transparent;
    }}
    details.qb-section-exp[open] .qb-summary {{
      border-bottom-color: rgba(217, 119, 6, 0.18);
    }}
    html.dark .qb-section-exp .qb-summary {{
      background: rgba(217, 119, 6, 0.09);
    }}
    .qb-section-exp .qb-summary-title {{
      color: #b45309;
    }}
    html.dark .qb-section-exp .qb-summary-title {{
      color: #fbbf24;
    }}
    .qb-section-exp .qb-section-body {{
      padding: 13px 16px;
      background: var(--card-bg);
    }}
    .qb-section-exp .expected-body {{
      font-size: 13px;
      line-height: 1.6;
      color: var(--text);
      display: flex;
      flex-direction: column;
      gap: 10px;
    }}
    .qb-section-exp ol, .qb-section-exp ul {{
      padding-left: 18px;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}
    .qb-section-exp .formula-box {{
      background: var(--card-hover);
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 8px 12px;
      text-align: center;
      margin: 6px 0;
      overflow-x: auto;
    }}

    /* Section 1: Key Points */
    .qb-section-key {{
      border-color: #cbd5e1;
    }}
    html.dark .qb-section-key {{
      border-color: #27272a;
    }}
    .qb-section-key .qb-summary {{
      background: rgba(16, 185, 129, 0.05);
      border-bottom: 1px solid transparent;
    }}
    details.qb-section-key[open] .qb-summary {{
      border-bottom-color: rgba(16, 185, 129, 0.15);
    }}
    html.dark .qb-section-key .qb-summary {{
      background: rgba(16, 185, 129, 0.08);
    }}
    .qb-section-key .qb-summary-title {{
      color: #047857;
    }}
    html.dark .qb-section-key .qb-summary-title {{
      color: #34d399;
    }}
    .qb-section-key .qb-section-body {{
      padding: 12px 16px;
      background: var(--card-bg);
    }}
    .qb-section-key ul {{
      padding-left: 18px;
      display: flex;
      flex-direction: column;
      gap: 6px;
      font-size: 13px;
      line-height: 1.55;
      color: var(--text);
    }}

    /* Section 2: Detailed Answer */
    .qb-section-det {{
      border-color: var(--border);
    }}
    .qb-section-det .qb-summary {{
      background: rgba(59, 130, 246, 0.04);
      border-bottom: 1px solid transparent;
    }}
    details.qb-section-det[open] .qb-summary {{
      border-bottom-color: rgba(59, 130, 246, 0.12);
    }}
    html.dark .qb-section-det .qb-summary {{
      background: rgba(59, 130, 246, 0.08);
    }}
    .qb-section-det .qb-summary-title {{
      color: #1d4ed8;
    }}
    html.dark .qb-section-det .qb-summary-title {{
      color: #93c5fd;
    }}
    .qb-section-det .qb-section-body {{
      padding: 14px 16px;
      background: var(--card-bg);
    }}
    .qb-section-det .detailed-body {{
      font-size: 13px;
      line-height: 1.6;
      color: var(--text);
      display: flex;
      flex-direction: column;
      gap: 10px;
    }}
    .qb-section-det h4 {{
      font-size: 13px;
      font-weight: 600;
      margin-top: 6px;
      color: var(--text);
    }}
    .qb-section-det ol, .qb-section-det ul {{
      padding-left: 18px;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}
    .qb-section-det .formula-box {{
      background: var(--card-hover);
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 8px 12px;
      margin: 6px 0;
      overflow-x: auto;
    }}

    /* Card Actions */
    .qb-card-actions {{
      display: flex;
      align-items: center;
      gap: 8px;
      padding-top: 10px;
      border-top: 1px solid var(--border);
      margin-top: 4px;
    }}
    .btn-qb-action {{
      background: var(--card-hover);
      border: 1px solid var(--border);
      color: var(--text);
      border-radius: 4px;
      padding: 5px 12px;
      font-size: 11px;
      font-weight: 500;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      transition: all 0.15s ease;
    }}
    .btn-qb-action:hover {{
      background: var(--border);
    }}
    .btn-qb-master {{
      margin-left: auto;
      background: none;
      border: 1px solid var(--border);
      color: var(--text-muted);
      border-radius: 4px;
      padding: 5px 12px;
      font-size: 11px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.15s ease;
    }}
    .btn-qb-master:hover {{
      border-color: var(--border-accent);
      color: var(--text);
    }}
    .btn-qb-master.checked {{
      background: var(--success-bg);
      border-color: var(--success);
      color: var(--success);
      font-weight: 600;
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
          <input type="text" id="search-input" class="search-input" placeholder="Search any concept, case study, or formula..." autocomplete="off">
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
      <button class="pillar-tab" id="endsem-qb-tab" data-view="endsem-qb" style="border-color: #f59e0b; background: rgba(245, 158, 11, 0.08); font-weight: 600;">🎯 Endsem Q-Bank (77 Qs)</button>
    </nav>

    <!-- CLASS PILLS -->
    <div class="class-bar" id="class-pills"></div>

    <!-- ACT FILTER BAR (FOR CLASS 11) -->
    <div class="act-bar" id="act-bar" style="display: none;"></div>

    <!-- VIEW HEADER -->
    <div class="view-header" id="view-header">
      <h1 class="view-title" id="view-title">Pillar 1: Planetary Foundations & Human Pressures</h1>
      <p class="view-desc" id="view-desc">How Earth's living systems work, the laws of physics that govern energy, and how human population and consumption stretch our planet's limits.</p>
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
    let classViewMode = "cards"; // "cards" or "slides"
    let currentView = "curriculum"; // "curriculum", "case-studies", "cheat-sheet", "search"
    let completedSubmodules = new Set(JSON.parse(localStorage.getItem("est_completed_subs") || "[]"));

    window.setClassViewMode = function(mode) {{
      classViewMode = mode;
      currentActFilter = "ALL";
      renderCurrentClassContent();
    }};

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

      // Topic Cards View (e.g. Class 11 Exam-Rated Topic Cards)
      if (c.topic_cards && c.topic_cards.length > 0 && classViewMode !== "slides") {{
        renderTopicCardsDeck(c);
        return;
      }}

      // Slidewise Rendering for any class with slides (Classes 11 to 19)
      if (c.slides && c.slides.length > 0) {{
        renderSlidewiseDeck(c);
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

    // Render Topic Cards Deck with Exam Ratings (e.g. Class 11)
    function renderTopicCardsDeck(c) {{
      actBar.style.display = "flex";
      actBar.innerHTML = "";

      let switcherHtml = "";
      if (c.slides && c.slides.length > 0) {{
        switcherHtml = `
          <div class="view-mode-bar">
            <button class="view-mode-btn ${{classViewMode === 'cards' ? 'active' : ''}}" onclick="setClassViewMode('cards')">
              🎴 ${{c.topic_cards.length}} Exam-Rated Topic Cards (Recommended)
            </button>
            <button class="view-mode-btn ${{classViewMode === 'slides' ? 'active' : ''}}" onclick="setClassViewMode('slides')">
              📑 ${{c.slides.length}} Individual Slides View
            </button>
          </div>
        `;
      }}

      const acts = [{{ id: "ALL", label: `All ${{c.topic_cards.length}} Topic Cards` }}];
      const seenActs = new Set();
      c.topic_cards.forEach(card => {{
        if (card.act) {{
          const actKey = card.act.split(':')[0].trim();
          if (!seenActs.has(actKey)) {{
            seenActs.add(actKey);
            const shortLabel = card.act.length > 35 ? card.act.substring(0, 32) + '...' : card.act;
            acts.push({{ id: actKey, label: shortLabel }});
          }}
        }}
      }});

      acts.forEach(a => {{
        const btn = document.createElement("button");
        btn.className = "act-pill" + (currentActFilter === a.id ? " active" : "");
        btn.textContent = a.label;
        btn.addEventListener("click", () => {{
          currentActFilter = a.id;
          renderTopicCardsDeck(c);
        }});
        actBar.appendChild(btn);
      }});

      let filteredCards = c.topic_cards;
      if (currentActFilter !== "ALL") {{
        filteredCards = c.topic_cards.filter(card => card.act && card.act.startsWith(currentActFilter));
      }}

      let html = switcherHtml + `<div class="submodule-grid">`;
      filteredCards.forEach(card => {{
        const cardId = `${{c.class_id}}.card.${{card.card_num}}`;
        const isDone = completedSubmodules.has(cardId);
        html += `
          <div class="submodule-card" id="sub-${{cardId}}">
            <div class="card-top">
              <div class="card-badges">
                <span class="badge-subid">TOPIC CARD ${{card.card_num}}</span>
                <span class="badge-slides">${{card.slides_label}}</span>
                <span class="badge-act">${{card.act ? card.act.split(':')[0] : 'ACT'}}</span>
                <span class="${{card.exam_rating.badge_class}}">🎯 ${{card.exam_rating.tier}}</span>
              </div>
              <button class="btn-complete ${{isDone ? 'checked' : ''}}" onclick="toggleSubmoduleCompletion('${{cardId}}', this)">
                <span>${{isDone ? '✓' : '○'}}</span> ${{isDone ? 'Completed' : 'Mark Complete'}}
              </button>
            </div>

            <!-- Exam Provenance Box -->
            <div class="exam-provenance-box">
              <div class="exam-hdr">
                <span>📝</span> Past Exam Frequency: ${{card.exam_rating.frequency_count}}
              </div>
              <div class="exam-chip-list">
                ${{card.exam_rating.recent_papers.map(p => `<span class="exam-chip">${{p}}</span>`).join('')}}
              </div>
              <div class="exam-tip"><strong>💡 Exam Strategy & Core Trap:</strong> ${{card.exam_rating.exam_tip}}</div>
            </div>

            <h2 class="submodule-title">${{card.title}}</h2>

            <div class="callout-eli15">
              <div class="callout-label">ELI15 Core Takeaway</div>
              <div class="callout-text">${{card.eli15_takeaway}}</div>
            </div>

            <ul class="bullets-list">
              ${{card.key_facts.map(f => `<li>${{f}}</li>`).join('')}}
            </ul>

            <div class="mental-box">
              <span class="mental-icon">💡</span>
              <div class="mental-desc"><strong>Mental Model:</strong> ${{card.mental_model}}</div>
            </div>

            <!-- Attached Past Exam Questions & Model Answers -->
            ${{card.exam_questions && card.exam_questions.length > 0 ? `
              <div class="exam-questions-section">
                <div class="exam-q-hdr">
                  <span>🎯</span> Past Exam Questions Asked on this Topic (${{card.exam_questions.length}})
                </div>
                <div class="exam-q-list">
                  ${{card.exam_questions.map((q, qidx) => `
                    <div class="exam-q-card">
                      <div class="exam-q-meta">
                        <span class="exam-q-paper">${{q.paper}}</span>
                        <span class="exam-q-section">${{q.section}}</span>
                        <span class="exam-q-marks">${{q.marks}}</span>
                      </div>
                      <div class="exam-q-prompt">“${{q.question}}”</div>
                      <details class="exam-answer-details">
                        <summary class="exam-answer-summary">
                          <span>📖 View Professor's Model Answer & Scoring Breakdown</span>
                        </summary>
                        <div class="exam-answer-body">
                          ${{q.answer_guideline}}
                        </div>
                      </details>
                    </div>
                  `).join('')}}
                </div>
              </div>
            ` : ''}}

            <div class="checkpoint-wrap">
              <div class="checkpoint-hdr"><span>⚡</span> Instant Recall Checkpoint</div>
              <div class="checkpoint-q">${{card.checkpoint.question}}</div>
              <div class="checkpoint-options" id="cp-opts-${{cardId.split('.').join('-')}}">
                ${{card.checkpoint.options.map((opt, idx) => `
                  <button class="cp-opt" onclick="handleCheckpoint('${{cardId}}', ${{idx}}, ${{card.checkpoint.correct !== undefined ? card.checkpoint.correct : card.checkpoint.correct_index}}, '${{encodeURIComponent(card.checkpoint.explanation)}}', this)">
                    ${{opt}}
                  </button>
                `).join('')}}
              </div>
              <div class="cp-feedback" id="cp-fb-${{cardId.split('.').join('-')}}"></div>
            </div>
          </div>
        `;
      }});
      html += `</div>`;
      contentContainer.innerHTML = html;
      triggerKaTeX();
    }}

    // Render Slidewise Deck with Dynamic Narrative Acts & Continuity (Classes 11 to 19)
    function renderSlidewiseDeck(c) {{
      actBar.style.display = "flex";
      actBar.innerHTML = "";

      let switcherHtml = "";
      if (c.topic_cards && c.topic_cards.length > 0) {{
        switcherHtml = `
          <div class="view-mode-bar">
            <button class="view-mode-btn ${{classViewMode === 'cards' ? 'active' : ''}}" onclick="setClassViewMode('cards')">
              🎴 ${{c.topic_cards.length}} Exam-Rated Topic Cards (Recommended)
            </button>
            <button class="view-mode-btn ${{classViewMode === 'slides' ? 'active' : ''}}" onclick="setClassViewMode('slides')">
              📑 ${{c.slides.length}} Individual Slides View
            </button>
          </div>
        `;
      }}

      const acts = [{{ id: "ALL", label: `All ${{c.slides.length}} Slides` }}];
      const seenActs = new Set();
      c.slides.forEach(s => {{
        if (s.act) {{
          const actKey = s.act.split(':')[0].trim();
          if (!seenActs.has(actKey)) {{
            seenActs.add(actKey);
            const shortLabel = s.act.length > 35 ? s.act.substring(0, 32) + '...' : s.act;
            acts.push({{ id: actKey, label: shortLabel }});
          }}
        }}
      }});

      acts.forEach(a => {{
        const btn = document.createElement("button");
        btn.className = "act-pill" + (currentActFilter === a.id ? " active" : "");
        btn.textContent = a.label;
        btn.addEventListener("click", () => {{
          currentActFilter = a.id;
          renderSlidewiseDeck(c);
        }});
        actBar.appendChild(btn);
      }});

      let filteredSlides = c.slides;
      if (currentActFilter !== "ALL") {{
        filteredSlides = c.slides.filter(s => s.act && s.act.startsWith(currentActFilter));
      }}

      let html = switcherHtml + `<div class="submodule-grid">`;
      filteredSlides.forEach(s => {{
        const slideId = `${{c.class_id}}.${{s.slide_num}}`;
        const isDone = completedSubmodules.has(slideId);
        html += `
          <div class="submodule-card" id="sub-${{slideId}}">
            <div class="card-top">
              <div class="card-badges">
                <span class="badge-subid">SLIDE ${{s.slide_num}} / ${{c.slides.length}}</span>
                <span class="badge-act">${{s.act ? s.act.split(':')[0] : 'ACT'}}</span>
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
            {{left: '\\\\(', right: '\\\\)', display: false}},
            {{left: '\\\\[', right: '\\\\]', display: true}}
          ],
          ignoredTags: ["script", "noscript", "style", "textarea", "pre", "code"],
          throwOnError: false
        }});
      }} else {{
        setTimeout(triggerKaTeX, 150);
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
      viewDesc.textContent = "Real-world environmental disasters explained in three clear steps: what happened, what went wrong, and what we learned from it.";

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


    // ============================================================
    // ENDSEM QUESTION BANK & MODEL ANSWERS SUITE (Lectures 11–19)
    // ============================================================
    let qbCurrentClass = "ALL";
    let qbCurrentPaper = "ALL";
    let qbSelectedCats = new Set(["ALL"]);
    let qbSearchQuery = "";
    let qbViewMode = "all"; // "all", "expected", "key", "detailed"
    let qbMastered = new Set(JSON.parse(localStorage.getItem("est_qb_mastered") || "[]"));

    window.setQBClass = function(cid) {{
      qbCurrentClass = cid;
      document.querySelectorAll(".qb-pill").forEach(p => {{
        p.classList.toggle("active", p.dataset.cid === String(cid));
      }});
      renderQBQuestions();
    }};

    window.setQBPaper = function(val) {{
      qbCurrentPaper = val;
      renderQBQuestions();
    }};

    window.toggleQBCat = function(cat) {{
      if (cat === "ALL") {{
        qbSelectedCats.clear();
        qbSelectedCats.add("ALL");
      }} else {{
        qbSelectedCats.delete("ALL");
        if (qbSelectedCats.has(cat)) {{
          qbSelectedCats.delete(cat);
          if (qbSelectedCats.size === 0) {{
            qbSelectedCats.add("ALL");
          }}
        }} else {{
          qbSelectedCats.add(cat);
        }}
      }}
      updateQBCatChips();
      renderQBQuestions();
    }};

    function updateQBCatChips() {{
      document.querySelectorAll(".qb-check-chip").forEach(chip => {{
        const inp = chip.querySelector("input");
        if (!inp) return;
        const cat = inp.getAttribute("data-cat");
        const isChecked = (cat === "ALL") ? qbSelectedCats.has("ALL") : qbSelectedCats.has(cat);
        inp.checked = isChecked;
        chip.classList.toggle("active", isChecked);
      }});
    }}

    window.setQBCategory = function(val) {{
      if (val === "ALL") {{
        qbSelectedCats.clear();
        qbSelectedCats.add("ALL");
      }} else {{
        qbSelectedCats.clear();
        qbSelectedCats.add(val);
      }}
      updateQBCatChips();
      renderQBQuestions();
    }};

    window.setQBViewMode = function(mode) {{
      qbViewMode = mode;
      document.querySelectorAll(".qb-mode-btn").forEach(b => {{
        b.classList.toggle("active", b.dataset.mode === mode);
      }});
      renderQBQuestions();
    }};

    window.handleQBSearch = function(val) {{
      qbSearchQuery = val.trim().toLowerCase();
      renderQBQuestions();
    }};

    window.toggleQBMastered = function(qid, btn) {{
      if (qbMastered.has(qid)) {{
        qbMastered.delete(qid);
        btn.classList.remove("checked");
        btn.innerHTML = `<span>○</span> Mark Mastered`;
        const el = document.getElementById(`card-${{qid}}`);
        if (el) el.classList.remove("mastered");
      }} else {{
        qbMastered.add(qid);
        btn.classList.add("checked");
        btn.innerHTML = `<span>✓</span> Mastered`;
        const el = document.getElementById(`card-${{qid}}`);
        if (el) el.classList.add("mastered");
      }}
      localStorage.setItem("est_qb_mastered", JSON.stringify([...qbMastered]));
      updateQBStats();
    }};

    window.toggleCardCollapse = function(qid, btn) {{
      const card = document.getElementById("card-" + qid);
      if (!card) return;
      const detailsList = card.querySelectorAll("details.qb-section");
      if (detailsList.length === 0) return;
      const anyOpen = Array.from(detailsList).some(d => d.open);
      detailsList.forEach(d => {{
        d.open = !anyOpen;
      }});
      btn.textContent = anyOpen ? "Expand" : "Collapse";
    }};

    window.setAllQBSections = function(openState) {{
      const list = document.getElementById("qb-questions-list");
      if (!list) return;
      list.querySelectorAll("details.qb-section").forEach(d => {{
        d.open = openState;
      }});
      list.querySelectorAll(".btn-card-toggle").forEach(b => {{
        b.textContent = openState ? "Collapse" : "Expand";
      }});
    }};

    window.copyQBAnswer = function(qid, btn) {{
      const q = (DB.endsem_question_bank && DB.endsem_question_bank.questions) ? 
        DB.endsem_question_bank.questions.find(x => x.id === qid) : null;
      if (!q) return;

      const tempDiv = document.createElement("div");
      let expText = "";
      if (q.expected_answer) {{
        tempDiv.innerHTML = q.expected_answer;
        expText = `\n\n=========================\nEXPECTED ANSWER (MODEL EXAM SCRIPT)\n=========================\n${{tempDiv.innerText}}`;
      }}
      tempDiv.innerHTML = q.key_answer_points;
      const keyText = tempDiv.innerText;
      tempDiv.innerHTML = q.detailed_answer;
      const detText = tempDiv.innerText;

      const copyPayload = `[${{q.id}}] ${{q.topic}} (${{q.class_name}})\nMarks: ${{q.marks}} | Importance: ${{q.importance}}\nQuestion:\n${{q.prompt}}${{expText}}\n\n=========================\nKEY POINTS\n=========================\n${{keyText}}\n\n=========================\nDETAILED ANSWER\n=========================\n${{detText}}`;

      navigator.clipboard.writeText(copyPayload).then(() => {{
        const orig = btn.innerHTML;
        btn.textContent = "Copied!";
        btn.style.color = "var(--success)";
        setTimeout(() => {{
          btn.innerHTML = orig;
          btn.style.color = "";
        }}, 1800);
      }}).catch(err => {{
        alert("Clipboard copy error: " + err);
      }});
    }};

    window.resetQBFilters = function() {{
      qbCurrentClass = "ALL";
      qbCurrentPaper = "ALL";
      qbSelectedCats = new Set(["ALL"]);
      qbSearchQuery = "";
      qbViewMode = "all";
      renderEndsemQuestionBank();
    }};

    function updateQBStats() {{
      const total = (DB.endsem_question_bank && DB.endsem_question_bank.questions) ? 
        DB.endsem_question_bank.questions.length : 82;
      const mCount = qbMastered.size;
      const pct = Math.round((mCount / total) * 100);

      const countEl = document.getElementById("qb-mastered-count");
      const barEl = document.getElementById("qb-mastered-bar");
      if (countEl) countEl.textContent = `${{mCount}} / ${{total}} (${{pct}}%)`;
      if (barEl) barEl.style.width = pct + "%";
    }}

    function renderEndsemQuestionBank() {{
      actBar.style.display = "none";
      viewTitle.textContent = "Endsem Question Bank & Model Answers (Lectures 11–19)";
      viewDesc.textContent = "82 real exam questions from 14 past papers (2018–2024), covering all objective MCQs, acronyms, match tables, short answers, comparisons, and descriptive case studies.";

      const qb = DB.endsem_question_bank || {{ questions: [] }};
      const qs = qb.questions;

      // Compute counts per class
      const classCounts = {{}};
      for (let c = 11; c <= 19; c++) classCounts[c] = 0;
      qs.forEach(q => {{
        if (classCounts[q.class_id] !== undefined) classCounts[q.class_id]++;
      }});

      const allCategories = [
        "MCQ & Objective",
        "Acronyms & Expansions",
        "Match the Following",
        "Short Answer & Definitions",
        "Differentiate Between",
        "Descriptive & Case Study"
      ];

      const catCounts = {{}};
      allCategories.forEach(c => catCounts[c] = 0);
      qs.forEach(q => {{
        if (catCounts[q.category] !== undefined) catCounts[q.category]++;
      }});

      const classTitles = {{
        11: "Cleantech Solutions",
        12: "EIA Framework",
        13: "Env. Movements",
        14: "Green Computing",
        15: "Green Engineering",
        16: "Green Accounting",
        17: "SDG & Sustainability",
        18: "NRA & Geospatial",
        19: "Ethics & Legislation"
      }};

      let html = `
        <div class="qb-container">
          <!-- TOOLBAR -->
          <div class="qb-toolbar">
            <!-- CLASS PILLS -->
            <div class="qb-class-pills">
              <button class="qb-pill ${{qbCurrentClass === 'ALL' ? 'active' : ''}}" data-cid="ALL" onclick="setQBClass('ALL')">
                All Classes (11–19) <span class="count">${{qs.length}}</span>
              </button>
      `;

      for (let c = 11; c <= 19; c++) {{
        html += `
          <button class="qb-pill ${{String(qbCurrentClass) === String(c) ? 'active' : ''}}" data-cid="${{c}}" onclick="setQBClass(${{c}})">
            C${{c}}: ${{classTitles[c]}} <span class="count">${{classCounts[c]}}</span>
          </button>
        `;
      }}

      html += `
            </div>

            <!-- FILTERS ROW 1: SEARCH, PAPERS & VIEW CONTROLS -->
            <div class="qb-filters-row">
              <div class="qb-filter-group">
                <input type="text" id="qb-search" class="qb-search-input" placeholder="Search any question, formula, or case study..." value="${{qbSearchQuery}}" oninput="handleQBSearch(this.value)">

                <select id="qb-paper-select" class="qb-select" onchange="setQBPaper(this.value)">
                  <option value="ALL" ${{qbCurrentPaper === 'ALL' ? 'selected' : ''}}>All Papers (14 Exam Papers)</option>
                  <option value="End Exam 2024" ${{qbCurrentPaper === 'End Exam 2024' ? 'selected' : ''}}>EST End Exam 2024</option>
                  <option value="End Exam 2023" ${{qbCurrentPaper === 'End Exam 2023' ? 'selected' : ''}}>EVS End Exam 2023</option>
                  <option value="End Exam 2022" ${{qbCurrentPaper === 'End Exam 2022' ? 'selected' : ''}}>EVS End Exam 2022</option>
                  <option value="End Exam 2019" ${{qbCurrentPaper === 'End Exam 2019' ? 'selected' : ''}}>EVS End Exam 2019</option>
                  <option value="End Exam 2018" ${{qbCurrentPaper === 'End Exam 2018' ? 'selected' : ''}}>EVS End Exam 2018</option>
                  <option value="Mid" ${{qbCurrentPaper === 'Mid' ? 'selected' : ''}}>Mid-Sem Papers (2018–2024)</option>
                  <option value="Quiz" ${{qbCurrentPaper === 'Quiz' ? 'selected' : ''}}>Quizzes (2020–2023)</option>
                </select>
              </div>

              <div class="qb-filter-group">
                <!-- VIEW MODE SWITCHER -->
                <div class="qb-mode-group">
                  <button class="qb-mode-btn ${{ (qbViewMode === 'all' || qbViewMode === 'both') ? 'active' : '' }}" data-mode="all" onclick="setQBViewMode('all')">All Sections</button>
                  <button class="qb-mode-btn ${{ qbViewMode === 'expected' ? 'active' : '' }}" data-mode="expected" onclick="setQBViewMode('expected')">Expected Answer</button>
                  <button class="qb-mode-btn ${{ qbViewMode === 'key' ? 'active' : '' }}" data-mode="key" onclick="setQBViewMode('key')">Key Points</button>
                  <button class="qb-mode-btn ${{ qbViewMode === 'detailed' ? 'active' : '' }}" data-mode="detailed" onclick="setQBViewMode('detailed')">Detailed Answer</button>
                </div>

                <div class="qb-collapse-group" style="display: flex; gap: 4px;">
                  <button class="btn-qb-action" onclick="setAllQBSections(false)" title="Minimize all answers">Collapse All</button>
                  <button class="btn-qb-action" onclick="setAllQBSections(true)" title="Expand all answers">Expand All</button>
                </div>

                <button class="btn-qb-action" onclick="resetQBFilters()">Reset</button>
              </div>
            </div>

            <!-- FILTERS ROW 2: CATEGORY MULTI-SELECT CHECKBOXES -->
            <div class="qb-cat-checkbox-group">
              <div class="qb-cat-label-row">
                <span class="qb-cat-title">Question Type Filters (Multi-Select Checkboxes):</span>
                <span style="font-size: 11px; color: var(--text-muted);">Select any combination of question types</span>
              </div>
              <div class="qb-cat-chips-row">
                <label class="qb-check-chip ${{qbSelectedCats.has('ALL') ? 'active' : ''}}">
                  <input type="checkbox" data-cat="ALL" ${{qbSelectedCats.has('ALL') ? 'checked' : ''}} onchange="toggleQBCat('ALL')">
                  <span>All Types</span>
                  <span class="chip-count">${{qs.length}}</span>
                </label>
                ${{allCategories.map(cat => `
                  <label class="qb-check-chip ${{qbSelectedCats.has(cat) ? 'active' : ''}}">
                    <input type="checkbox" data-cat="${{cat}}" ${{qbSelectedCats.has(cat) ? 'checked' : ''}} onchange="toggleQBCat('${{cat}}')">
                    <span>${{cat}}</span>
                    <span class="chip-count">${{catCounts[cat] || 0}}</span>
                  </label>
                `).join('')}}
              </div>
            </div>

            <!-- STATS STRIP -->
            <div class="qb-stats-strip">
              <span id="qb-matched-count">Showing matching questions...</span>
              <div class="qb-progress-track">
                <span>Mastery Progress:</span>
                <span id="qb-mastered-count">0 / ${{qs.length}} (0%)</span>
                <div class="qb-progress-bar-mini">
                  <div id="qb-mastered-bar" class="qb-progress-bar-fill"></div>
                </div>
              </div>
            </div>
          </div>

          <!-- QUESTIONS CONTAINER -->
          <div id="qb-questions-list" class="qb-cards-deck"></div>
        </div>
      `;

      contentContainer.innerHTML = html;
      renderQBQuestions();
      updateQBStats();
    }}

    function renderQBQuestions() {{
      const listEl = document.getElementById("qb-questions-list");
      const matchedEl = document.getElementById("qb-matched-count");
      if (!listEl) return;

      const qb = DB.endsem_question_bank || {{ questions: [] }};
      let filtered = qb.questions;

      // 1. Filter by Class
      if (qbCurrentClass !== "ALL") {{
        const cid = parseInt(qbCurrentClass, 10);
        filtered = filtered.filter(q => q.class_id === cid);
      }}

      // 2. Filter by Paper
      if (qbCurrentPaper !== "ALL") {{
        filtered = filtered.filter(q => {{
          return q.exams.some(e => e.paper.toLowerCase().includes(qbCurrentPaper.toLowerCase()));
        }});
      }}

      // 3. Filter by Category (Multi-Select)
      if (!qbSelectedCats.has("ALL") && qbSelectedCats.size > 0) {{
        filtered = filtered.filter(q => qbSelectedCats.has(q.category));
      }}

      // 4. Search Filter
      if (qbSearchQuery) {{
        filtered = filtered.filter(q => {{
          const textCorpus = (
            q.id + " " + q.topic + " " + q.class_name + " " + q.prompt + " " +
            q.key_answer_points + " " + q.detailed_answer
          ).toLowerCase();
          return textCorpus.includes(qbSearchQuery);
        }});
      }}

      if (matchedEl) {{
        matchedEl.innerHTML = `Showing <strong>${{filtered.length}}</strong> of ${{qb.questions.length}} questions (Classes 11–19)`;
      }}

      if (filtered.length === 0) {{
        listEl.innerHTML = `
          <div style="background: var(--card-bg); border: 1px dashed var(--border); border-radius: 8px; padding: 40px 20px; text-align: center;">
            <p style="font-size: 16px; font-weight: 600; margin-bottom: 6px;">No questions match your current filters</p>
            <p style="font-size: 13px; color: var(--text-muted); margin-bottom: 14px;">Try selecting 'All Types', 'All Classes', or clearing the search query.</p>
            <button class="btn-qb-action" onclick="resetQBFilters()">Reset All Filters</button>
          </div>
        `;
        return;
      }}

      let html = "";
      filtered.forEach(q => {{
        const isMastered = qbMastered.has(q.id);
        const importanceClass = q.importance.includes("CRITICAL") ? "badge-critical" : 
                               (q.importance.includes("HIGH") ? "badge-high" : "badge-medium");

        html += `
          <div class="qb-card ${{isMastered ? 'mastered' : ''}}" id="card-${{q.id}}">
            <!-- HEADER -->
            <div class="qb-card-header">
              <div class="qb-card-meta">
                <span class="qb-q-id">${{q.id}}</span>
                <span class="qb-class-tag">Class ${{q.class_id}}: ${{q.class_name}}</span>
                <span class="qb-cat-tag">${{q.category}}</span>
                <span class="${{importanceClass}}">${{q.importance}}</span>
                <span class="qb-marks-tag">${{q.marks}}</span>
              </div>
              <div class="qb-exams-row">
                <span style="font-size: 11px; font-weight: 600; color: var(--text-muted);">Exam Appearances:</span>
                ${{q.exams.map(e => `
                  <span class="qb-exam-pill">📄 ${{e.paper}} (${{e.section}}${{e.marks ? ', ' + e.marks : ''}})</span>
                `).join('')}}
              </div>
            </div>

            <!-- PROMPT -->
            <div class="qb-prompt-box">
              ${{q.prompt}}
            </div>

            <!-- SECTION 1: EXPECTED ANSWER (MODEL EXAM SCRIPT) -->
            ${{(q.expected_answer && (qbViewMode === 'all' || qbViewMode === 'both' || qbViewMode === 'expected')) ? `
              <details class="qb-section qb-section-exp" open id="sec-exp-${{q.id}}">
                <summary class="qb-summary">
                  <span class="qb-summary-title">
                    <svg class="qb-chevron-icon" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
                    <span>Expected Answer</span>
                  </span>
                  <span class="qb-summary-hint">Toggle</span>
                </summary>
                <div class="qb-section-body">
                  ${{q.expected_answer}}
                </div>
              </details>
            ` : ''}}

            <!-- SECTION 2: KEY POINTS -->
            ${{(qbViewMode === 'all' || qbViewMode === 'both' || qbViewMode === 'key') ? `
              <details class="qb-section qb-section-key" open id="sec-key-${{q.id}}">
                <summary class="qb-summary">
                  <span class="qb-summary-title">
                    <svg class="qb-chevron-icon" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
                    <span>Key Points</span>
                  </span>
                  <span class="qb-summary-hint">Toggle</span>
                </summary>
                <div class="qb-section-body">
                  ${{q.key_answer_points}}
                </div>
              </details>
            ` : ''}}

            <!-- SECTION 3: DETAILED ANSWER -->
            ${{(qbViewMode === 'all' || qbViewMode === 'both' || qbViewMode === 'detailed') ? `
              <details class="qb-section qb-section-det" open id="sec-det-${{q.id}}">
                <summary class="qb-summary">
                  <span class="qb-summary-title">
                    <svg class="qb-chevron-icon" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
                    <span>Detailed Answer</span>
                  </span>
                  <span class="qb-summary-hint">Toggle</span>
                </summary>
                <div class="qb-section-body">
                  ${{q.detailed_answer}}
                </div>
              </details>
            ` : ''}}

            <!-- ACTIONS -->
            <div class="qb-card-actions">
              <button class="btn-qb-action btn-card-toggle" onclick="toggleCardCollapse('${{q.id}}', this)">
                Collapse
              </button>
              <button class="btn-qb-action" onclick="copyQBAnswer('${{q.id}}', this)">
                Copy Answer
              </button>
              <button class="btn-qb-master ${{isMastered ? 'checked' : ''}}" onclick="toggleQBMastered('${{q.id}}', this)">
                <span>${{isMastered ? '✓' : '○'}}</span> ${{isMastered ? 'Mastered' : 'Mark Mastered'}}
              </button>
            </div>
          </div>
        `;
      }});

      listEl.innerHTML = html;
      triggerKaTeX();
    }}

    // Render Cheat Sheet
    function renderCheatSheet() {{
      actBar.style.display = "none";
      viewTitle.textContent = "Formula & Law Cheat Sheet";
      viewDesc.textContent = "Essential formulas, core environmental laws, and practical indices you need to know for the exam.";

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

        // Also search Topic Cards (Class 11)
        if (c.topic_cards) {{
          c.topic_cards.forEach(card => {{
            const eqText = card.exam_questions ? card.exam_questions.map(eq => eq.paper + " " + eq.section + " " + eq.question + " " + eq.answer_guideline).join(" ") : "";
            const textCorpus = (card.title + " " + card.eli15_takeaway + " " + card.key_facts.join(" ") + " " + card.mental_model + " " + card.exam_rating.tier + " " + card.exam_rating.exam_tip + " " + card.exam_rating.recent_papers.join(" ") + " " + eqText).toLowerCase();
            if (textCorpus.includes(q)) {{
              matches.push({{
                type: "topic_card",
                class_id: c.class_id,
                class_title: c.title,
                data: card
              }});
            }}
          }});
        }}

        // Also search Class slides
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

      // Also search Endsem Question Bank
      if (DB.endsem_question_bank && DB.endsem_question_bank.questions) {{
        DB.endsem_question_bank.questions.forEach(qItem => {{
          const qCorpus = (qItem.id + " " + qItem.topic + " " + qItem.class_name + " " + qItem.prompt + " " + qItem.key_answer_points + " " + qItem.detailed_answer).toLowerCase();
          if (qCorpus.includes(q)) {{
            matches.push({{
              type: "qb_question",
              class_id: qItem.class_id,
              class_title: qItem.class_name,
              data: qItem
            }});
          }}
        }});
      }}

      viewDesc.textContent = matches.length === 1 ? "Found 1 matching topic across the course." : `Found ${{matches.length}} matching topics across the course.`;

      if (matches.length === 0) {{
        contentContainer.innerHTML = `<div style="text-align: center; padding: 60px 20px; color: var(--text-muted);"><div style="font-size: 24px; margin-bottom: 8px;">🔍</div><strong>Nothing found for "${{q}}".</strong><p style="margin-top: 6px; font-size: 13px;">Try checking your spelling or search friendly terms like "carbon", "NDVI", "Aether", "Zelp", "seaweed", "Bhopal", or "EIA".</p></div>`;
        return;
      }}

      let html = `<div class="submodule-grid">`;
      matches.forEach(m => {{
        if (m.type === "topic_card") {{
          const card = m.data;
          const cardId = `${{m.class_id}}.card.${{card.card_num}}`;
          const isDone = completedSubmodules.has(cardId);
          html += `
            <div class="submodule-card" id="sub-${{cardId}}">
              <div class="card-top">
                <div class="card-badges">
                  <span class="badge-subid">CLASS ${{m.class_id}} • TOPIC CARD ${{card.card_num}}</span>
                  <span class="badge-slides">${{card.slides_label}}</span>
                  <span class="${{card.exam_rating.badge_class}}">🎯 ${{card.exam_rating.tier}}</span>
                </div>
                <button class="btn-complete ${{isDone ? 'checked' : ''}}" onclick="toggleSubmoduleCompletion('${{cardId}}', this)">
                  <span>${{isDone ? '✓' : '○'}}</span> ${{isDone ? 'Completed' : 'Mark Complete'}}
                </button>
              </div>
              <div class="exam-provenance-box">
                <div class="exam-hdr"><span>📝</span> ${{card.exam_rating.frequency_count}}</div>
                <div class="exam-chip-list">
                  ${{card.exam_rating.recent_papers.map(p => `<span class="exam-chip">${{p}}</span>`).join('')}}
                </div>
                <div class="exam-tip"><strong>💡 Exam Strategy:</strong> ${{card.exam_rating.exam_tip}}</div>
              </div>
              <h2 class="submodule-title">${{card.title}}</h2>
              <div class="callout-eli15">
                <div class="callout-label">ELI15 Core Takeaway</div>
                <div class="callout-text">${{card.eli15_takeaway}}</div>
              </div>
              <ul class="bullets-list">
                ${{card.key_facts.map(f => `<li>${{f}}</li>`).join('')}}
              </ul>
              ${{card.exam_questions && card.exam_questions.length > 0 ? `
                <div class="exam-questions-section">
                  <div class="exam-q-hdr"><span>🎯</span> Past Exam Questions Asked on this Topic (${{card.exam_questions.length}})</div>
                  <div class="exam-q-list">
                    ${{card.exam_questions.map((q, qidx) => `
                      <div class="exam-q-card">
                        <div class="exam-q-meta">
                          <span class="exam-q-paper">${{q.paper}}</span>
                          <span class="exam-q-section">${{q.section}}</span>
                          <span class="exam-q-marks">${{q.marks}}</span>
                        </div>
                        <div class="exam-q-prompt">“${{q.question}}”</div>
                        <details class="exam-answer-details">
                          <summary class="exam-answer-summary"><span>📖 View Model Answer & Key Points</span></summary>
                          <div class="exam-answer-body">${{q.answer_guideline}}</div>
                        </details>
                      </div>
                    `).join('')}}
                  </div>
                </div>
              ` : ''}}
            </div>
          `;
        }} else if (m.type === "slide") {{
          const s = m.data;
          const slideId = `${{m.class_id}}.${{s.slide_num}}`;
          const isDone = completedSubmodules.has(slideId);
          html += `
            <div class="submodule-card" id="sub-${{slideId}}">
              <div class="card-top">
                <div class="card-badges">
                  <span class="badge-subid">CLASS ${{m.class_id}} • SLIDE ${{s.slide_num}}</span>
                  <span class="badge-act">${{s.act ? s.act.split(':')[0] : 'ACT'}}</span>
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
        }} else if (m.type === "qb_question") {{
          const q = m.data;
          const isMastered = qbMastered.has(q.id);
          html += `
            <div class="qb-card ${{isMastered ? 'mastered' : ''}}" id="card-${{q.id}}" style="border-left: 4px solid #f59e0b;">
              <div class="qb-card-header">
                <div class="qb-card-meta">
                  <span class="qb-q-id">${{q.id}}</span>
                  <span class="qb-class-tag">Class ${{q.class_id}}: ${{q.class_name}}</span>
                  <span class="qb-cat-tag">${{q.category}}</span>
                  <span class="badge-critical">${{q.importance}}</span>
                  <span class="qb-marks-tag">${{q.marks}}</span>
                </div>
                <div class="qb-exams-row">
                  <span style="font-size: 11px; font-weight: 600; color: var(--text-muted);">Exam Appearances:</span>
                  ${{q.exams.map(e => `
                    <span class="qb-exam-pill">📄 ${{e.paper}} (${{e.section}}${{e.marks ? ', ' + e.marks : ''}})</span>
                  `).join('')}}
                </div>
              </div>

              <div class="qb-prompt-box">
                ${{q.prompt}}
              </div>

              <!-- EXPECTED ANSWER -->
              ${{q.expected_answer ? `
                <details class="qb-section qb-section-exp" open id="search-sec-exp-${{q.id}}">
                  <summary class="qb-summary">
                    <span class="qb-summary-title">
                      <svg class="qb-chevron-icon" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
                      <span>Expected Answer</span>
                    </span>
                    <span class="qb-summary-hint">Toggle</span>
                  </summary>
                  <div class="qb-section-body">
                    ${{q.expected_answer}}
                  </div>
                </details>
              ` : ''}}

              <details class="qb-section qb-section-key" open id="search-sec-key-${{q.id}}">
                <summary class="qb-summary">
                  <span class="qb-summary-title">
                    <svg class="qb-chevron-icon" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
                    <span>Key Points</span>
                  </span>
                  <span class="qb-summary-hint">Toggle</span>
                </summary>
                <div class="qb-section-body">
                  ${{q.key_answer_points}}
                </div>
              </details>

              <details class="qb-section qb-section-det" open id="search-sec-det-${{q.id}}">
                <summary class="qb-summary">
                  <span class="qb-summary-title">
                    <svg class="qb-chevron-icon" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
                    <span>Detailed Answer</span>
                  </span>
                  <span class="qb-summary-hint">Toggle</span>
                </summary>
                <div class="qb-section-body">
                  ${{q.detailed_answer}}
                </div>
              </details>

              <div class="qb-card-actions">
                <button class="btn-qb-action btn-card-toggle" onclick="toggleCardCollapse('${{q.id}}', this)">
                  Collapse
                </button>
                <button class="btn-qb-action" onclick="copyQBAnswer('${{q.id}}', this)">
                  Copy Answer
                </button>
                <button class="btn-qb-master ${{isMastered ? 'checked' : ''}}" onclick="toggleQBMastered('${{q.id}}', this)">
                  <span>${{isMastered ? '✓' : '○'}}</span> ${{isMastered ? 'Mastered' : 'Mark Mastered'}}
                </button>
              </div>
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
      classPills.style.display = "";
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
        window.location.hash = "pillar-" + pId;
        renderPillarView(parseInt(pId, 10));
      }} else if (v === "case-studies") {{
        window.location.hash = "case-studies";
        currentView = "case-studies";
        classPills.style.display = "none";
        renderCaseStudies();
      }} else if (v === "cheat-sheet") {{
        window.location.hash = "cheat-sheet";
        currentView = "cheat-sheet";
        classPills.style.display = "none";
        renderCheatSheet();
      }} else if (v === "endsem-qb") {{
        window.location.hash = "endsem-qb";
        currentView = "endsem-qb";
        classPills.style.display = "none";
        renderEndsemQuestionBank();
      }}
    }});

    function handleHashNavigation() {{
      const hash = (window.location.hash || "").replace("#", "");
      if (hash === "endsem-qb") {{
        const tab = document.getElementById("endsem-qb-tab");
        if (tab) {{
          document.querySelectorAll(".pillar-tab").forEach(t => t.classList.remove("active"));
          tab.classList.add("active");
          currentView = "endsem-qb";
          classPills.style.display = "none";
          renderEndsemQuestionBank();
        }}
      }} else if (hash === "case-studies") {{
        const tab = document.getElementById("case-study-hub");
        if (tab) {{
          document.querySelectorAll(".pillar-tab").forEach(t => t.classList.remove("active"));
          tab.classList.add("active");
          currentView = "case-studies";
          classPills.style.display = "none";
          renderCaseStudies();
        }}
      }} else if (hash === "cheat-sheet") {{
        const tab = document.getElementById("formula-sheet");
        if (tab) {{
          document.querySelectorAll(".pillar-tab").forEach(t => t.classList.remove("active"));
          tab.classList.add("active");
          currentView = "cheat-sheet";
          classPills.style.display = "none";
          renderCheatSheet();
        }}
      }} else if (hash.startsWith("pillar-")) {{
        const pId = parseInt(hash.replace("pillar-", ""), 10);
        const tab = document.querySelector(`.pillar-tab[data-pillar="${{pId}}"]`);
        if (tab) {{
          document.querySelectorAll(".pillar-tab").forEach(t => t.classList.remove("active"));
          tab.classList.add("active");
          renderPillarView(pId);
        }}
      }}
    }}

    window.addEventListener("hashchange", handleHashNavigation);

    // Boot
    initTheme();
    updateProgress();
    renderClassPills();
    if (window.location.hash) {{
      handleHashNavigation();
    }} else {{
      renderCurrentClassContent();
    }}
  </script>
</body>
</html>'''

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
        
    print(f"Successfully generated index.html ({len(html)} bytes).")

if __name__ == "__main__":
    build_website()
