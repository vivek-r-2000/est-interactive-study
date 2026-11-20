import os
import json

# Comprehensive transcription of questions across all available exam papers
# Compiled from digital text papers + transcribed scanned exam papers:
# EST_end_2024, EST_mid1_2024, EST_quiz1_2023, EVS_end_2023, EVS_end_2022, EST_mid1_2022, 
# EVS_quiz1-4_2020, EVS_papers_2019, EVS_end_2018, EVS_mid1-2_2018.

exam_questions = [
    # CLASS 11: Climate Change Technology Solutions & Carbon Mitigation
    {
        "class_id": 11,
        "class_name": "Climate Change Technology Solutions",
        "topic": "Air-to-Diamond Synthesis (Aether Diamonds)",
        "exams": [
            {"paper": "End Exam 2023", "section": "Section III, Q5", "marks": 3, "prompt": "Explain the process of diamond manufacturing by Aether (only the process)."},
            {"paper": "End Exam 2022", "section": "Section X, Q(b)", "marks": 5, "prompt": "Give a short account on Diamonds from air pollution (Climeworks direct air capture, conversion to CH4, chemical vapor deposition reactor, Surat cutting/polishing, 20 tonnes carbon offset per carat)."}
        ],
        "frequency_score": 5,
        "importance_tier": "CRITICAL (⭐⭐⭐⭐⭐)",
        "trend_note": "Directly tested in both 2022 and 2023 End Exams. Professor specifically asks for the step-by-step chemical and physical manufacturing process."
    },
    {
        "class_id": 11,
        "class_name": "Climate Change Technology Solutions",
        "topic": "Eco-friendly Carbon-Negative Cement (Novacem vs Portland)",
        "exams": [
            {"paper": "End Exam 2023", "section": "Section III, Q7", "marks": 3, "prompt": "Difference between Portland and Novacem cement."},
            {"paper": "End Exam 2019", "section": "Section IV, Q1(d)", "marks": 3, "prompt": "Novacem as ecofriendly cement."},
            {"paper": "Mid-2 2018", "section": "Q8(b)", "marks": 1.5, "prompt": "Answer in three sentences: brief account on Novacem (MgO + CO2 -> MgCO3)."}
        ],
        "frequency_score": 5,
        "importance_tier": "CRITICAL (⭐⭐⭐⭐⭐)",
        "trend_note": "Appeared in 2018, 2019, and 2023. Core comparison tests limestone calcination vs magnesium silicate carbonation reaction."
    },
    {
        "class_id": 11,
        "class_name": "Climate Change Technology Solutions",
        "topic": "Blue Carbon Coastal Ocean Ecosystems",
        "exams": [
            {"paper": "End Exam 2023", "section": "Section I, Q1(g)", "marks": 1, "prompt": "What is Blue carbon?"},
            {"paper": "End Exam 2022", "section": "Section V, Q(e)", "marks": 2, "prompt": "Advantages of blue carbon habitat restoration (3 points: stores 3-5x more carbon than upland tropical forests in sediment, nursery grounds, coastal storm protection)."},
            {"paper": "End Exam 2019", "section": "Section X, Q1(c)", "marks": 3, "prompt": "Answer on Blue carbon."},
            {"paper": "End Exam 2018", "section": "Part IV, Q3", "marks": 4, "prompt": "What kind of ecosystem services are provided by mangrove habitats?"}
        ],
        "frequency_score": 5,
        "importance_tier": "CRITICAL (⭐⭐⭐⭐⭐)",
        "trend_note": "Appeared in 2018, 2019, 2022, and 2023 End Exams. Highlights high sediment burial rates and marine carbon sinks."
    },
    {
        "class_id": 11,
        "class_name": "Climate Change Technology Solutions",
        "topic": "Livestock Methane Reduction via Red Seaweed Feed (Asparagopsis taxiformis)",
        "exams": [
            {"paper": "End Exam 2022", "section": "Section III, Q15", "marks": 1, "prompt": "Fill in the blank: Methane reduction from livestock can be achieved by adding Seaweed to cattle feed."},
            {"paper": "Mid-2 2018", "section": "Q1(c)", "marks": 0.5, "prompt": "Fill in the blank: Enteric fermentation / cattle is the major source of agricultural methane emissions."}
        ],
        "frequency_score": 4,
        "importance_tier": "HIGH (⭐⭐⭐⭐)",
        "trend_note": "High-yield objective and short answer question testing bromoform enzyme inhibition and burp mitigation halters (Zelp)."
    },
    {
        "class_id": 11,
        "class_name": "Climate Change Technology Solutions",
        "topic": "Direct Air Capture (DAC) Companies & Chemical Contactors",
        "exams": [
            {"paper": "End Exam 2022", "section": "Section VI, Q(c)", "marks": 1, "prompt": "Give an example of Carbon capturing company: Climeworks; Carbon Engineering; Global Thermostat."},
            {"paper": "End Exam 2019", "section": "Section II, Q6", "marks": 2, "prompt": "Describe any one international carbon sequestration project."}
        ],
        "frequency_score": 4,
        "importance_tier": "HIGH (⭐⭐⭐⭐)",
        "trend_note": "Requires naming commercial pioneers (Climeworks Orca/Mammoth, Carbon Engineering) and understanding solid vs liquid contactor physics."
    },
    {
        "class_id": 11,
        "class_name": "Climate Change Technology Solutions",
        "topic": "AI for Wildlife Conservation & Environmental Defense (Wild Me & TRASE)",
        "exams": [
            {"paper": "End Exam 2023", "section": "Section I, Q1(c)", "marks": 1, "prompt": "What is Wild Me?"},
            {"paper": "End Exam 2022", "section": "Section III, Q6", "marks": 1, "prompt": "Fill in the blank: Wild Me is an open-source AI technology/platform to identify and track wildlife."},
            {"paper": "End Exam 2022", "section": "Section III, Q14", "marks": 1, "prompt": "Fill in the blank: TRASE platform maps the links between food importing countries and the places where the food is produced."}
        ],
        "frequency_score": 4,
        "importance_tier": "HIGH (⭐⭐⭐⭐)",
        "trend_note": "Repeated definition question testing computer vision animal biometrics and algorithmic supply chain transparency."
    },
    {
        "class_id": 11,
        "class_name": "Climate Change Technology Solutions",
        "topic": "Negative Emissions Technologies (NETs), Biochar & Mineral Weathering",
        "exams": [
            {"paper": "Mid-1 2022", "section": "Q3", "marks": 2, "prompt": "Concept of Kubuqi model (desert greening and soil biological crusts)."},
            {"paper": "Quiz-3 2020", "section": "Q1(b)", "marks": 0.5, "prompt": "Gross primary productivity and net addition to standing biomass in mature vs young forests."}
        ],
        "frequency_score": 3,
        "importance_tier": "MEDIUM-HIGH (⭐⭐⭐)",
        "trend_note": "Tested in broader negative emissions and carbon drawdown contexts."
    },
    {
        "class_id": 11,
        "class_name": "Climate Change Technology Solutions",
        "topic": "Controlled Environment Agriculture (Vertical Farming & AeroFarms)",
        "exams": [
            {"paper": "General Syllabus", "section": "Agritech", "marks": 3, "prompt": "Water and land efficiency metrics of vertical aeroponic systems vs conventional farming."}
        ],
        "frequency_score": 3,
        "importance_tier": "MEDIUM (⭐⭐⭐)",
        "trend_note": "Key technology in food-system emissions reduction."
    },
    {
        "class_id": 11,
        "class_name": "Climate Change Technology Solutions",
        "topic": "Solar Radiation Management & Moonshot Carbon Prizes (XPRIZE, Flettner Ships)",
        "exams": [
            {"paper": "Mid-1 2024", "section": "Section I, Q4", "marks": 2, "prompt": "Geoengineering and atmospheric tipping points."}
        ],
        "frequency_score": 3,
        "importance_tier": "MEDIUM (⭐⭐⭐)",
        "trend_note": "High conceptual relevance for global climate interventions."
    }
]

out_json = "Previous_Exam_Papers/class_11_exam_frequency_analysis.json"
with open(out_json, "w", encoding="utf-8") as f:
    json.dump({
        "course": "Environmental Science & Technology",
        "target_class": 11,
        "title": "Climate Change Technology Solutions",
        "total_analyzed_papers": 14,
        "paper_list": [
            "EST End Exam 2024", "EST Mid-1 2024", "EST Quiz-1 2023", "EVS End Exam 2023",
            "EVS End Exam 2022", "EST Mid-1 2022", "EVS Quiz 1-4 2020", "EVS Papers 2019",
            "EVS End Exam 2018", "EVS Mid-1 2018", "EVS Mid-2 2018"
        ],
        "class_11_topics": exam_questions
    }, f, indent=2)

print(f"Generated {out_json}")

# Also generate a markdown question bank for reusable student reference
out_md = "Previous_Exam_Papers/QUESTION_BANK_MASTER.md"
with open(out_md, "w", encoding="utf-8") as f:
    f.write("# Master Question Bank & Exam Topic Frequency: Environmental Science & Technology\n\n")
    f.write("> Extracted and synthesized from 14 IIIT previous exam papers (End-sems, Mid-sems, Quizzes from 2018 to 2024).\n\n")
    f.write("## 1. Class 11 (Climate Change Technology Solutions) Frequency Matrix\n\n")
    f.write("| Topic | Importance Tier | Marks Weightage | Exam Appearances | Core Concept Tested |\n")
    f.write("|---|---|---|---|---|\n")
    for q in exam_questions:
        exams_str = "<br>".join([f"• {e['paper']} ({e['section']})" for e in q['exams']])
        f.write(f"| **{q['topic']}** | `{q['importance_tier']}` | {q['exams'][0]['marks']}M | {exams_str} | {q['trend_note']} |\n")

    f.write("\n\n## 2. All Transcribed Exam Questions by Subject Pillar\n\n")
    f.write("### Pillar 1: Earth Systems, Spheres & Planetary Boundaries\n")
    f.write("- **Grasshopper Effect / Global Distillation** (Mid-1 2024, Mid-1 2022 [3M]): Volatile persistent organic pollutants (POPs) evaporating in warm equatorial regions and condensing/depositing as toxic precipitation in cold polar regions.\n")
    f.write("- **Hypercane vs Present Hurricanes** (Mid-1 2024 [2M], End 2022 [1M]): Hypothetical megastorm formed over ocean waters >50°C, injecting water vapor and chlorofluorocarbons directly into the stratosphere, destroying ozone layer.\n")
    f.write("- **Volcanic Eruptions & Deglaciation** (Mid-1 2024 [2M], Mid-2 2018 [2M]): Melting glacial ice relieves lithospheric overburden pressure, enabling magma decompression and increased explosive volcanism.\n")
    f.write("- **Aral Sea Degradation** (Mid-1 2018 [3M], Quiz-1 2023 [4M]): Soviet diversion of Amu Darya and Syr Darya for cotton farming causing 90% water loss, salt storms within 300 km radius, and fishing industry collapse.\n")
    f.write("- **Eutrophication & Mississippi Dead Zone** (Quiz-1 2023 [3M], End 2022 [1M]): Agricultural N & P runoff causing excessive algal blooms, bacterial decomposition, severe oxygen depletion (BOD spike), and hypoxic dead zones.\n\n")

    f.write("### Pillar 2: Carbon Cycle, Sinks & Market Mechanisms\n")
    f.write("- **Biomass Carbon Formula** (Mid-2 2018 [0.5M], End 2019 [0.5M], End 2022 [1M]): Dry biomass of wood contains exactly ~50% (0.5x) carbon by weight ($1 \\text{ kg dry wood} = 0.5 \\text{ kg carbon}$).\n")
    f.write("- **Kyoto Protocol vs Paris Agreement** (End 2024 [2M], End 2023 [2M], End 2022 [2M]): Kyoto imposed legally binding reduction targets exclusively on Annex-I industrialized nations; Paris established universal nationally determined contributions (NDCs) across all nations.\n")
    f.write("- **Clean Development Mechanism (CDM)** (Mid-2 2018 [0.5M], Quiz-3 2020 [0.5M], End 2022 [1M]): Nuclear projects are strictly ineligible under CDM; generates Certified Emission Reductions (CERs).\n\n")

    f.write("### Pillar 3: Technology Solutions, Green Computing & Engineering\n")
    f.write("- **Aether Air-to-Diamond Process** (End 2023 [3M], End 2022 [5M]): Climeworks DAC CO2 -> catalytic conversion to CH4 -> CVD vacuum plasma reactor at extreme temperatures -> raw diamond lattice -> cut in Surat India (offsets 20t CO2/carat).\n")
    f.write("- **Novacem vs Portland Cement** (End 2023 [3M], End 2019 [3M], Mid-2 2018 [1.5M]): Portland emits ~0.9 kg CO2/kg cement via limestone calcination at 1450°C; Novacem uses magnesium silicates at 650°C and carbonates ambient CO2 ($MgO + CO_2 \\rightarrow MgCO_3$) sequestering ~100 kg CO2 net per tonne.\n")
    f.write("- **Thin Client vs Thick Client** (End 2024 [2M], End 2023 [4M], End 2022 [2M], End 2019 [4M]): Thin client has no local disk, consumes ~5-15W, relies on central virtualization; Thick client has local OS/storage, consumes ~75-150W, high embodied carbon.\n")
    f.write("- **Green Engineering 12 Principles** (End 2024 [2M], End 2023 [4M], End 2019 [3M], End 2018 [6M]): Inherent rather than circumstantial; Prevention rather than treatment; Conserve complexity; Integrate local material/energy flows (Kalundborg industrial symbiosis).\n")
    f.write("- **Denim Manufacturing Environmental Footprint** (End 2024 [2M], End 2023 [4M], End 2022 [2M], End 2019 [4M]): 7,500L water per pair, toxic synthetic indigo effluent in Pearl River, worker silicosis from manual sandblasting.\n\n")

    f.write("### Pillar 4: Environmental Governance, Law, Accounting & Ethics\n")
    f.write("- **SNA vs SEEA Asset Classification** (End 2024 [2M], End 2023 [2M], End 2022 [10M], End 2019 [10M], End 2018 [10M]): Standard National Accounts (SNA) only counts marketed production ($GDP = C+I+G+X-M$) and treats forest clearcutting as pure positive income; SEEA creates natural capital balance sheets, tracks physical flows (residuals/ecosystem inputs), and accounts for environmental depreciation.\n")
    f.write("- **EIA Process & Great Nicobar Case** (End 2023 [2M], End 2022 [10M], End 2018 [10M]): Phase 1 Screening (triage into low, moderate, high risk) vs Phase 2 Full EIA study; Expert Appraisal Committee (EAC) 11-member composition; baseline data omission penalties.\n")
    f.write("- **Anthropocentrism vs Biocentrism vs Ecocentrism** (End 2024 [2M], End 2023 [3M], End 2022 [5M], End 2018 [6M]): Anthropocentrism (human utility only); Biocentrism (all living organisms have intrinsic moral rights); Ecocentrism (holistic biotic community, Leopold Land Ethic).\n")
    f.write("- **Indian Environmental Movements** (End 2023 [1M], Mid-1 2018 [5M], End 2019 [2M]): 1730 Bishnoi Khejarli massacre (Amrita Devi, 363 martyrs); 1973 Chipko (Gaura Devi, Sunderlal Bahuguna 'Ecology is permanent economy'); 1983 Appiko (Pandurang Hegde); Silent Valley (KSSP, Lion-tailed macaque).\n")

print(f"Generated {out_md}")
