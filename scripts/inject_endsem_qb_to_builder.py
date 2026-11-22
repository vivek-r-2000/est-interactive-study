import re
import os

with open("scripts/build_modern_website.py", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add CSS for Endsem Question Bank Suite
qb_css_raw = """
    /* ============================================================
       ENDSEM QUESTION BANK & MODEL ANSWERS SUITE (Lectures 11–19)
       ============================================================ */
    .qb-container {
      display: flex;
      flex-direction: column;
      gap: 20px;
    }
    .qb-toolbar {
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 16px 20px;
      display: flex;
      flex-direction: column;
      gap: 14px;
    }
    .qb-class-pills {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      align-items: center;
    }
    .qb-pill {
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
    }
    .qb-pill:hover {
      border-color: var(--border-accent);
      color: var(--text);
      background: var(--card-hover);
    }
    .qb-pill.active {
      background: var(--accent);
      color: #FFFFFF;
      border-color: var(--accent);
      font-weight: 600;
    }
    html.dark .qb-pill.active {
      color: #121413;
    }
    .qb-pill .count {
      font-size: 10px;
      padding: 1px 6px;
      border-radius: 10px;
      background: var(--tag-bg);
      color: var(--tag-text);
      font-weight: 700;
    }
    .qb-pill.active .count {
      background: rgba(255, 255, 255, 0.25);
      color: #FFFFFF;
    }
    html.dark .qb-pill.active .count {
      background: rgba(0, 0, 0, 0.25);
      color: #121413;
    }
    .qb-filters-row {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      padding-top: 12px;
      border-top: 1px dashed var(--border);
    }
    .qb-filter-group {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 8px;
    }
    .qb-select {
      padding: 6px 10px;
      border-radius: 6px;
      border: 1px solid var(--border);
      background: var(--card-bg);
      color: var(--text);
      font-size: 12px;
      outline: none;
      cursor: pointer;
    }
    .qb-search-input {
      padding: 6px 12px;
      border-radius: 6px;
      border: 1px solid var(--border);
      background: var(--card-hover);
      color: var(--text);
      font-size: 12px;
      outline: none;
      width: 220px;
      transition: all 0.15s ease;
    }
    .qb-search-input:focus {
      border-color: var(--accent);
      background: var(--card-bg);
      width: 260px;
    }
    .qb-mode-group {
      display: inline-flex;
      background: var(--card-hover);
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 2px;
    }
    .qb-mode-btn {
      padding: 4px 10px;
      font-size: 11px;
      font-weight: 600;
      border: none;
      background: transparent;
      color: var(--text-muted);
      cursor: pointer;
      border-radius: 4px;
      transition: all 0.15s ease;
    }
    .qb-mode-btn.active {
      background: var(--card-bg);
      color: var(--accent);
      box-shadow: 0 1px 2px rgba(0, 0, 0, 0.08);
    }
    .qb-stats-strip {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      font-size: 12px;
      color: var(--text-muted);
      padding: 0 4px;
    }
    .qb-progress-track {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-weight: 600;
      color: var(--text);
    }
    .qb-progress-bar-mini {
      width: 100px;
      height: 6px;
      background: var(--border);
      border-radius: 3px;
      overflow: hidden;
      display: inline-block;
    }
    .qb-progress-bar-fill {
      height: 100%;
      background: var(--success);
      width: 0%;
      transition: width 0.3s ease;
    }

    /* Question Cards */
    .qb-cards-deck {
      display: flex;
      flex-direction: column;
      gap: 20px;
    }
    .qb-card {
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 22px 24px;
      display: flex;
      flex-direction: column;
      gap: 14px;
      position: relative;
      transition: border-color 0.15s ease, box-shadow 0.15s ease;
    }
    .qb-card:hover {
      border-color: var(--border-accent);
    }
    .qb-card.mastered {
      border-left: 4px solid var(--success);
    }
    .qb-card-header {
      display: flex;
      flex-direction: column;
      gap: 8px;
    }
    .qb-card-meta {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 8px;
    }
    .qb-q-id {
      font-family: ui-monospace, monospace;
      font-size: 11px;
      font-weight: 700;
      padding: 2px 7px;
      border-radius: 4px;
      background: var(--tag-bg);
      color: var(--tag-text);
    }
    .qb-class-tag {
      font-size: 11px;
      font-weight: 600;
      padding: 2px 8px;
      border-radius: 4px;
      background: var(--accent-soft);
      color: var(--accent-text);
    }
    .qb-cat-tag {
      font-size: 11px;
      font-weight: 500;
      padding: 2px 7px;
      border-radius: 4px;
      border: 1px solid var(--border);
      background: var(--card-bg);
      color: var(--text-muted);
    }
    .qb-marks-tag {
      margin-left: auto;
      font-size: 11px;
      font-weight: 700;
      padding: 2px 8px;
      border-radius: 4px;
      background: #ecfdf5;
      color: #065f46;
      border: 1px solid #a7f3d0;
    }
    html.dark .qb-marks-tag {
      background: #142820;
      color: #34d399;
      border-color: #244134;
    }
    .qb-exams-row {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 6px;
    }
    .qb-exam-pill {
      font-size: 11px;
      padding: 2px 8px;
      border-radius: 4px;
      background: #fef3c7;
      color: #92400e;
      border: 1px solid #fcd34d;
      font-weight: 600;
    }
    html.dark .qb-exam-pill {
      background: #2b1f05;
      color: #fcd34d;
      border-color: #78350f;
    }
    .qb-prompt-box {
      background: var(--card-hover);
      border-left: 4px solid var(--accent);
      padding: 14px 16px;
      border-radius: 0 6px 6px 0;
      font-size: 14px;
      font-weight: 600;
      line-height: 1.55;
      color: var(--text);
    }

    /* Section 1: Key Answer Points */
    .qb-section-key {
      background: var(--success-bg);
      border: 1px solid #bbf7d0;
      border-radius: 6px;
      padding: 14px 16px;
    }
    html.dark .qb-section-key {
      background: #142820;
      border-color: #244134;
    }
    .qb-section-title-key {
      font-size: 12px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      color: var(--success);
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .qb-section-key ul {
      padding-left: 18px;
      display: flex;
      flex-direction: column;
      gap: 6px;
      font-size: 13px;
      line-height: 1.55;
      color: var(--text);
    }

    /* Section 2: Detailed Answer */
    .qb-section-det {
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 16px 18px;
    }
    .qb-section-title-det {
      font-size: 12px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      color: #1e40af;
      margin-bottom: 10px;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    html.dark .qb-section-title-det {
      color: #93c5fd;
    }
    .qb-section-det .detailed-body {
      font-size: 13px;
      line-height: 1.6;
      color: var(--text);
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    .qb-section-det h4 {
      font-size: 13px;
      font-weight: 700;
      margin-top: 6px;
      color: var(--accent);
    }
    .qb-section-det ol, .qb-section-det ul {
      padding-left: 18px;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }
    .qb-section-det .formula-box {
      background: var(--card-hover);
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 8px 12px;
      margin: 6px 0;
      overflow-x: auto;
    }

    /* Card Actions */
    .qb-card-actions {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding-top: 12px;
      border-top: 1px solid var(--border);
      margin-top: 2px;
    }
    .btn-qb-action {
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
    }
    .btn-qb-action:hover {
      background: var(--border);
    }
    .btn-qb-master {
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
    }
    .btn-qb-master:hover {
      border-color: var(--border-accent);
      color: var(--text);
    }
    .btn-qb-master.checked {
      background: var(--success-bg);
      border-color: var(--success);
      color: var(--success);
      font-weight: 600;
    }
"""
qb_css = qb_css_raw.replace("{", "{{").replace("}", "}}")

# Insert CSS right before </style>
if "</style>" in content and ".qb-container" not in content:
    content = content.replace("</style>", qb_css + "\n  </style>", 1)
    print("[+] Injected QB CSS into <style>")

# 2. Add Top Navbar Tab
qb_tab_html = '<button class="pillar-tab" id="endsem-qb-tab" data-view="endsem-qb" style="border-color: #f59e0b; background: rgba(245, 158, 11, 0.08); font-weight: 600;">🎯 Endsem Q-Bank (77 Qs)</button>'
if 'id="formula-sheet"' in content and 'id="endsem-qb-tab"' not in content:
    content = content.replace(
        '<button class="pillar-tab" id="formula-sheet" data-view="cheat-sheet">📐 Formula Sheet</button>',
        '<button class="pillar-tab" id="formula-sheet" data-view="cheat-sheet">📐 Formula Sheet</button>\n      ' + qb_tab_html,
        1
    )
    print("[+] Injected Endsem Q-Bank tab in navbar")

# 3. Add JS Navigation Listener
nav_snippet = """      }} else if (v === "endsem-qb") {{
        currentView = "endsem-qb";
        classPills.style.display = "none";
        actBar.style.display = "none";
        renderEndsemQuestionBank();"""

if 'v === "cheat-sheet"' in content and 'v === "endsem-qb"' not in content:
    content = content.replace(
        """      } else if (v === "cheat-sheet") {{
        currentView = "cheat-sheet";
        classPills.style.display = "none";
        renderCheatSheet();
      }}""",
        """      } else if (v === "cheat-sheet") {{
        currentView = "cheat-sheet";
        classPills.style.display = "none";
        renderCheatSheet();
      }} else if (v === "endsem-qb") {{
        currentView = "endsem-qb";
        classPills.style.display = "none";
        actBar.style.display = "none";
        renderEndsemQuestionBank();
      }}""",
        1
    )
    print("[+] Injected JS nav click listener for endsem-qb")

# 4. Add JS Functions for Endsem Question Bank Suite
qb_js_raw = """
    // ============================================================
    // ENDSEM QUESTION BANK & MODEL ANSWERS SUITE (Lectures 11–19)
    // ============================================================
    let qbCurrentClass = "ALL";
    let qbCurrentPaper = "ALL";
    let qbCurrentCat = "ALL";
    let qbSearchQuery = "";
    let qbViewMode = "both"; // "both", "key", "detailed"
    let qbMastered = new Set(JSON.parse(localStorage.getItem("est_qb_mastered") || "[]"));

    window.setQBClass = function(cid) {
      qbCurrentClass = cid;
      document.querySelectorAll(".qb-pill").forEach(p => {
        p.classList.toggle("active", p.dataset.cid === String(cid));
      });
      renderQBQuestions();
    };

    window.setQBPaper = function(val) {
      qbCurrentPaper = val;
      renderQBQuestions();
    };

    window.setQBCategory = function(val) {
      qbCurrentCat = val;
      renderQBQuestions();
    };

    window.setQBViewMode = function(mode) {
      qbViewMode = mode;
      document.querySelectorAll(".qb-mode-btn").forEach(b => {
        b.classList.toggle("active", b.dataset.mode === mode);
      });
      renderQBQuestions();
    };

    window.handleQBSearch = function(val) {
      qbSearchQuery = val.trim().toLowerCase();
      renderQBQuestions();
    };

    window.toggleQBMastered = function(qid, btn) {
      if (qbMastered.has(qid)) {
        qbMastered.delete(qid);
        btn.classList.remove("checked");
        btn.innerHTML = `<span>○</span> Mark as Mastered`;
        const el = document.getElementById(`card-${qid}`);
        if (el) el.classList.remove("mastered");
      } else {
        qbMastered.add(qid);
        btn.classList.add("checked");
        btn.innerHTML = `<span>✓</span> Mastered`;
        const el = document.getElementById(`card-${qid}`);
        if (el) el.classList.add("mastered");
      }
      localStorage.setItem("est_qb_mastered", JSON.stringify([...qbMastered]));
      updateQBStats();
    };

    window.copyQBAnswer = function(qid, btn) {
      const q = (DB.endsem_question_bank && DB.endsem_question_bank.questions) ? 
        DB.endsem_question_bank.questions.find(x => x.id === qid) : null;
      if (!q) return;

      const tempDiv = document.createElement("div");
      tempDiv.innerHTML = q.key_answer_points;
      const keyText = tempDiv.innerText;
      tempDiv.innerHTML = q.detailed_answer;
      const detText = tempDiv.innerText;

      const copyPayload = `[${q.id}] ${q.topic} (${q.class_name})\\nMarks: ${q.marks} | Importance: ${q.importance}\\nQuestion:\\n${q.prompt}\\n\\n=========================\\nSECTION 1: KEY ANSWER POINTS\\n=========================\\n${keyText}\\n\\n=========================\\nSECTION 2: DETAILED ANSWER & CONTEXT\\n=========================\\n${detText}`;

      navigator.clipboard.writeText(copyPayload).then(() => {
        const orig = btn.innerHTML;
        btn.innerHTML = `<span>✓</span> Copied to Clipboard!`;
        btn.style.color = "var(--success)";
        setTimeout(() => {
          btn.innerHTML = orig;
          btn.style.color = "";
        }, 1800);
      }).catch(err => {
        alert("Clipboard copy error: " + err);
      });
    };

    window.resetQBFilters = function() {
      qbCurrentClass = "ALL";
      qbCurrentPaper = "ALL";
      qbCurrentCat = "ALL";
      qbSearchQuery = "";
      qbViewMode = "both";
      renderEndsemQuestionBank();
    };

    function updateQBStats() {
      const total = (DB.endsem_question_bank && DB.endsem_question_bank.questions) ? 
        DB.endsem_question_bank.questions.length : 77;
      const mCount = qbMastered.size;
      const pct = Math.round((mCount / total) * 100);

      const countEl = document.getElementById("qb-mastered-count");
      const barEl = document.getElementById("qb-mastered-bar");
      if (countEl) countEl.textContent = `${mCount} / ${total} (${pct}%)`;
      if (barEl) barEl.style.width = pct + "%";
    }

    function renderEndsemQuestionBank() {
      actBar.style.display = "none";
      viewTitle.textContent = "Endsem Question Bank & Model Answers Suite (Lectures 11–19)";
      viewDesc.textContent = "77 master exam questions synthesized across 14 IIIT previous exam papers (2018–2024 End-Sems, Mid-Sems & Quizzes). Each question includes: (1) Key Answer Points (high-yield keywords) and (2) Detailed Answer with Full Context & Explanations.";

      const qb = DB.endsem_question_bank || { questions: [] };
      const qs = qb.questions;

      // Compute counts per class
      const classCounts = {};
      for (let c = 11; c <= 19; c++) classCounts[c] = 0;
      qs.forEach(q => {
        if (classCounts[q.class_id] !== undefined) classCounts[q.class_id]++;
      });

      const classTitles = {
        11: "Cleantech Solutions",
        12: "EIA Framework",
        13: "Env. Movements",
        14: "Green Computing",
        15: "Green Engineering",
        16: "Green Accounting",
        17: "SDG & Sustainability",
        18: "NRA & Geospatial",
        19: "Ethics & Legislation"
      };

      let html = `
        <div class="qb-container">
          <!-- TOOLBAR -->
          <div class="qb-toolbar">
            <!-- CLASS PILLS -->
            <div class="qb-class-pills">
              <button class="qb-pill ${qbCurrentClass === 'ALL' ? 'active' : ''}" data-cid="ALL" onclick="setQBClass('ALL')">
                All Classes (11–19) <span class="count">${qs.length}</span>
              </button>
      `;

      for (let c = 11; c <= 19; c++) {
        html += `
          <button class="qb-pill ${String(qbCurrentClass) === String(c) ? 'active' : ''}" data-cid="${c}" onclick="setQBClass(${c})">
            C${c}: ${classTitles[c]} <span class="count">${classCounts[c]}</span>
          </button>
        `;
      }

      html += `
            </div>

            <!-- FILTERS ROW -->
            <div class="qb-filters-row">
              <div class="qb-filter-group">
                <input type="text" id="qb-search" class="qb-search-input" placeholder="🔍 Search questions, formulas, cases..." value="${qbSearchQuery}" oninput="handleQBSearch(this.value)">

                <select class="qb-select" onchange="setQBPaper(this.value)">
                  <option value="ALL" ${qbCurrentPaper === 'ALL' ? 'selected' : ''}>All Papers (14 Exam Papers)</option>
                  <option value="End Exam 2024" ${qbCurrentPaper === 'End Exam 2024' ? 'selected' : ''}>EST End Exam 2024</option>
                  <option value="End Exam 2023" ${qbCurrentPaper === 'End Exam 2023' ? 'selected' : ''}>EVS End Exam 2023</option>
                  <option value="End Exam 2022" ${qbCurrentPaper === 'End Exam 2022' ? 'selected' : ''}>EVS End Exam 2022</option>
                  <option value="End Exam 2019" ${qbCurrentPaper === 'End Exam 2019' ? 'selected' : ''}>EVS End Exam 2019</option>
                  <option value="End Exam 2018" ${qbCurrentPaper === 'End Exam 2018' ? 'selected' : ''}>EVS End Exam 2018</option>
                  <option value="Mid" ${qbCurrentPaper === 'Mid' ? 'selected' : ''}>Mid-Sem Papers (2018–2024)</option>
                  <option value="Quiz" ${qbCurrentPaper === 'Quiz' ? 'selected' : ''}>Quizzes (2020–2023)</option>
                </select>

                <select class="qb-select" onchange="setQBCategory(this.value)">
                  <option value="ALL" ${qbCurrentCat === 'ALL' ? 'selected' : ''}>All Question Types</option>
                  <option value="Comprehensive Descriptive" ${qbCurrentCat === 'Comprehensive Descriptive' ? 'selected' : ''}>Comprehensive (4M – 10M)</option>
                  <option value="Differentiate Between" ${qbCurrentCat === 'Differentiate Between' ? 'selected' : ''}>Differentiate Between (2M – 4M)</option>
                  <option value="Short Definition" ${qbCurrentCat === 'Short Definition' ? 'selected' : ''}>Definitions & What is (1M – 2M)</option>
                  <option value="Match the Following" ${qbCurrentCat === 'Match the Following' ? 'selected' : ''}>Match the Following (5M)</option>
                </select>
              </div>

              <div class="qb-filter-group">
                <!-- VIEW MODE SWITCHER -->
                <div class="qb-mode-group">
                  <button class="qb-mode-btn ${qbViewMode === 'both' ? 'active' : ''}" data-mode="both" onclick="setQBViewMode('both')">Both Sections</button>
                  <button class="qb-mode-btn ${qbViewMode === 'key' ? 'active' : ''}" data-mode="key" onclick="setQBViewMode('key')">Key Points Only</button>
                  <button class="qb-mode-btn ${qbViewMode === 'detailed' ? 'active' : ''}" data-mode="detailed" onclick="setQBViewMode('detailed')">Detailed Only</button>
                </div>

                <button class="btn-qb-action" onclick="resetQBFilters()">↺ Reset</button>
              </div>
            </div>

            <!-- STATS STRIP -->
            <div class="qb-stats-strip">
              <span id="qb-matched-count">Showing matching questions...</span>
              <div class="qb-progress-track">
                <span>Mastery Progress:</span>
                <span id="qb-mastered-count">0 / ${qs.length} (0%)</span>
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
    }

    function renderQBQuestions() {
      const listEl = document.getElementById("qb-questions-list");
      const matchedEl = document.getElementById("qb-matched-count");
      if (!listEl) return;

      const qb = DB.endsem_question_bank || { questions: [] };
      let filtered = qb.questions;

      // 1. Filter by Class
      if (qbCurrentClass !== "ALL") {
        const cid = parseInt(qbCurrentClass, 10);
        filtered = filtered.filter(q => q.class_id === cid);
      }

      // 2. Filter by Paper
      if (qbCurrentPaper !== "ALL") {
        filtered = filtered.filter(q => {
          return q.exams.some(e => e.paper.toLowerCase().includes(qbCurrentPaper.toLowerCase()));
        });
      }

      // 3. Filter by Category
      if (qbCurrentCat !== "ALL") {
        filtered = filtered.filter(q => q.category === qbCurrentCat);
      }

      // 4. Search Filter
      if (qbSearchQuery) {
        filtered = filtered.filter(q => {
          const textCorpus = (
            q.id + " " + q.topic + " " + q.class_name + " " + q.prompt + " " +
            q.key_answer_points + " " + q.detailed_answer
          ).toLowerCase();
          return textCorpus.includes(qbSearchQuery);
        });
      }

      if (matchedEl) {
        matchedEl.innerHTML = `Showing <strong>${filtered.length}</strong> of ${qb.questions.length} questions (Classes 11–19)`;
      }

      if (filtered.length === 0) {
        listEl.innerHTML = `
          <div style="background: var(--card-bg); border: 1px dashed var(--border); border-radius: 8px; padding: 40px 20px; text-align: center;">
            <p style="font-size: 16px; font-weight: 600; margin-bottom: 6px;">No questions match your current filters</p>
            <p style="font-size: 13px; color: var(--text-muted); margin-bottom: 14px;">Try selecting 'All Classes' or clearing the search query.</p>
            <button class="btn-qb-action" onclick="resetQBFilters()">Reset All Filters</button>
          </div>
        `;
        return;
      }

      let html = "";
      filtered.forEach(q => {
        const isMastered = qbMastered.has(q.id);
        const importanceClass = q.importance.includes("CRITICAL") ? "badge-critical" : 
                               (q.importance.includes("HIGH") ? "badge-high" : "badge-medium");

        html += `
          <div class="qb-card ${isMastered ? 'mastered' : ''}" id="card-${q.id}">
            <!-- HEADER -->
            <div class="qb-card-header">
              <div class="qb-card-meta">
                <span class="qb-q-id">${q.id}</span>
                <span class="qb-class-tag">Class ${q.class_id}: ${q.class_name}</span>
                <span class="qb-cat-tag">${q.category}</span>
                <span class="${importanceClass}">${q.importance}</span>
                <span class="qb-marks-tag">${q.marks}</span>
              </div>
              <div class="qb-exams-row">
                <span style="font-size: 11px; font-weight: 600; color: var(--text-muted);">Exam Appearances:</span>
                ${q.exams.map(e => `
                  <span class="qb-exam-pill">📄 ${e.paper} (${e.section}${e.marks ? ', ' + e.marks : ''})</span>
                `).join('')}
              </div>
            </div>

            <!-- PROMPT -->
            <div class="qb-prompt-box">
              ${q.prompt}
            </div>

            <!-- SECTION 1: KEY ANSWER POINTS -->
            ${(qbViewMode === 'both' || qbViewMode === 'key') ? `
              <div class="qb-section-key">
                <div class="qb-section-title-key">
                  <span>🔑 Section 1: Key Answer Points (Exam High-Yield Summary)</span>
                </div>
                ${q.key_answer_points}
              </div>
            ` : ''}

            <!-- SECTION 2: DETAILED ANSWER & CONTEXT -->
            ${(qbViewMode === 'both' || qbViewMode === 'detailed') ? `
              <div class="qb-section-det">
                <div class="qb-section-title-det">
                  <span>📖 Section 2: Detailed Answer with All Relevant Context & Slide Connections</span>
                </div>
                ${q.detailed_answer}
              </div>
            ` : ''}

            <!-- ACTIONS -->
            <div class="qb-card-actions">
              <button class="btn-qb-action" onclick="copyQBAnswer('${q.id}', this)">
                <span>📋</span> Copy Full Answer
              </button>
              <button class="btn-qb-master ${isMastered ? 'checked' : ''}" onclick="toggleQBMastered('${q.id}', this)">
                <span>${isMastered ? '✓' : '○'}</span> ${isMastered ? 'Mastered' : 'Mark as Mastered'}
              </button>
            </div>
          </div>
        `;
      });

      listEl.innerHTML = html;
      triggerKaTeX();
    }
"""
qb_js = qb_js_raw.replace("{", "{{").replace("}", "}}")

if 'function renderEndsemQuestionBank' not in content:
    content = content.replace(
        "    // Render Cheat Sheet",
        qb_js + "\n    // Render Cheat Sheet",
        1
    )
    print("[+] Injected JS functions for renderEndsemQuestionBank")

# Write back
with open("scripts/build_modern_website.py", "w", encoding="utf-8") as f:
    f.write(content)

print("[+] Successfully updated scripts/build_modern_website.py!")
