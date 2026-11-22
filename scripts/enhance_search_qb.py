with open("scripts/build_modern_website.py", "r", encoding="utf-8") as f:
    code = f.read()

# 1. Add qb_question search in handleSearch
target_search = """      DB.case_studies.forEach(cs => {{
        const csCorpus = (cs.name + " " + cs.what_happened + " " + cs.root_cause + " " + cs.takeaway).toLowerCase();
        if (csCorpus.includes(q)) {{
          matches.push({{
            type: "case_study",
            data: cs
          }});
        }}
      }});"""

replacement_search = """      DB.case_studies.forEach(cs => {{
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
      }}"""

if target_search in code and "type: \"qb_question\"" not in code:
    code = code.replace(target_search, replacement_search, 1)
    print("[+] Injected qb_question search in handleSearch")

# 2. Add qb_question rendering in matches.forEach
target_render = """        }} else if (m.type === "case_study") {{
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
        }}"""

replacement_render = """        }} else if (m.type === "case_study") {{
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

              <div class="qb-section-key">
                <div class="qb-section-title-key">
                  <span>🔑 Section 1: Key Answer Points (Exam High-Yield Summary)</span>
                </div>
                ${{q.key_answer_points}}
              </div>

              <div class="qb-section-det">
                <div class="qb-section-title-det">
                  <span>📖 Section 2: Detailed Answer with All Relevant Context & Slide Connections</span>
                </div>
                ${{q.detailed_answer}}
              </div>

              <div class="qb-card-actions">
                <button class="btn-qb-action" onclick="copyQBAnswer('${{q.id}}', this)">
                  <span>📋</span> Copy Full Answer
                </button>
                <button class="btn-qb-master ${{isMastered ? 'checked' : ''}}" onclick="toggleQBMastered('${{q.id}}', this)">
                  <span>${{isMastered ? '✓' : '○'}}</span> ${{isMastered ? 'Mastered' : 'Mark as Mastered'}}
                </button>
              </div>
            </div>
          `;
        }}"""

if target_render in code and "type === \"qb_question\"" not in code:
    code = code.replace(target_render, replacement_render, 1)
    print("[+] Injected qb_question rendering in handleSearch matches")

with open("scripts/build_modern_website.py", "w", encoding="utf-8") as f:
    f.write(code)

print("[+] Updated search in build_modern_website.py successfully!")
