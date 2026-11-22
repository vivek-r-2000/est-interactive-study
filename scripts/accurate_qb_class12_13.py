import json

def get_class12_questions():
    return [
        {
            "id": "EQB-12-01",
            "class_id": 12,
            "class_name": "Environmental Impact Assessment (EIA)",
            "topic": "EIA Statutory Approval Year",
            "category": "MCQ & Objective",
            "exams": [
                {"paper": "End Exam 2022", "section": "Section II, Q3", "marks": "1M"}
            ],
            "marks": "1M",
            "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
            "prompt": "The Government of India approved the statutory EIA notification in the year: [a] 1996 [b] 1998 [c] 1994 [d] 2006.",
            "key_answer_points": "<ul>\n<li><strong>Correct Option:</strong> <strong>[ c ] 1994</strong> (specifically <strong>27th January 1994</strong>).</li>\n<li><strong>Key Fact:</strong> Enacted by the Ministry of Environment and Forests under Section 3 of the <strong>Environment (Protection) Act, 1986</strong>. (It was later comprehensively re-engineered on 14th September 2006 to decentralize powers to states).</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>Regulatory Context:</strong> Following the 1984 Bhopal gas tragedy, India passed the umbrella Environment (Protection) Act of 1986. Under its statutory rule-making authority, the first legally binding EIA Notification was officially notified on 27th January 1994 for 29 designated industrial categories.</p>\n<p><em>Slide Reference: Class 12 Slide 4.</em></p>\n</div>"
        },
        {
            "id": "EQB-12-02",
            "class_id": 12,
            "class_name": "Environmental Impact Assessment (EIA)",
            "topic": "Significance of Screening in EIA",
            "category": "Short Answer & Definitions",
            "exams": [
                {"paper": "End Exam 2023", "section": "Section II, Q9", "marks": "2M"},
                {"paper": "End Exam 2022", "section": "Section VIII", "marks": "2M"}
            ],
            "marks": "2M",
            "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
            "prompt": "What is the significance of the Screening activity in EIA?",
            "key_answer_points": "<ul>\n<li><strong>Definition:</strong> Screening is the initial gateway step that determines whether a proposed development project requires an Environmental Clearance (EC) and what level of environmental review is needed.</li>\n<li><strong>Category Sorting:</strong> It sorts projects into:\n<br>• <strong>Category A</strong> (heavy national-scale impact $\\rightarrow$ mandatory full EIA & Central MoEFCC appraisal),\n<br>• <strong>Category B1</strong> (moderate regional impact $\\rightarrow$ full EIA & State SEIAA appraisal),\n<br>• <strong>Category B2</strong> (low impact $\\rightarrow$ exempted from full EIA and public hearing).</li>\n<li><strong>Regulatory Efficiency:</strong> Prevents regulatory backlog by exempting small, green, or low-risk projects while ensuring mega-polluting projects face strict scrutiny.</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>The Gateway Phase:</strong> Without screening, environmental regulatory agencies would drown in paperwork evaluating every small corner shop. Screening filters projects objectively based on scale, threshold limits, and proximity to eco-sensitive zones.</p>\n<p><em>Slide Reference: Class 12 Slides 6–8.</em></p>\n</div>"
        },
        {
            "id": "EQB-12-03",
            "class_id": 12,
            "class_name": "Environmental Impact Assessment (EIA)",
            "topic": "Preliminary Assessment vs Full EIA Study",
            "category": "Differentiate Between",
            "exams": [
                {"paper": "End Exam 2023", "section": "Section IV, Q5", "marks": "4M"},
                {"paper": "End Exam 2022", "section": "Section XI", "marks": "4M"}
            ],
            "marks": "4M",
            "importance": "HIGH (⭐⭐⭐⭐)",
            "prompt": "How full EIA study differs from preliminary assessment.",
            "key_answer_points": "<ul>\n<li><strong>Preliminary Assessment (Initial Environmental Examination - IEE):</strong>\n<br>• Rapid diagnostic desk review using simple checklists and existing published secondary data.\n<br>• Purpose: Identifies if significant unknown environmental risks exist to decide if a full EIA is warranted.\n<br>• Duration & Cost: Completed in weeks at minimal cost without multi-season field sampling or public hearing.</li>\n<li><strong>Full EIA Study:</strong>\n<br>• In-depth comprehensive statutory investigation with <strong>baseline field sampling over 3 seasons</strong> (air, water, noise, soil, ecology).\n<br>• Mandates formal Scoping (Terms of Reference - ToR), impact modeling, quantitative risk assessment, an Environmental Management Plan (EMP), and a mandatory Public Hearing.\n<br>• Duration & Cost: Takes 12–18 months and involves an interdisciplinary team of certified experts.</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>Comparison:</strong> While an IEE provides a quick diagnostic check to see if a project is safe or needs further review, a Full EIA provides an exhaustive, legally enforceable environmental audit.</p>\n<p><em>Slide Reference: Class 12 Slides 10–14.</em></p>\n</div>"
        },
        {
            "id": "EQB-12-04",
            "class_id": 12,
            "class_name": "Environmental Impact Assessment (EIA)",
            "topic": "Laikipia Paper Mill Case Study & Interdisciplinary Team",
            "category": "Descriptive & Case Study",
            "exams": [
                {"paper": "End Exam 2022", "section": "Section XI (OR)", "marks": "10M"},
                {"paper": "End Exam 2018", "section": "Part I, Q3", "marks": "10M"}
            ],
            "marks": "10M",
            "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
            "prompt": "An Investor wants to put up an Industrial Plant for the manufacture of paper and its derivatives in the wet and forested slopes of Laikipia District, Mt. Kenya. Discuss the logical steps in the EIA process that your study team is likely to follow. Justify the formation of the Interdisciplinary Team for this EIA study.",
            "key_answer_points": "<ul>\n<li><strong>Phase 1 (Initial Inquiries):</strong>\n<br>• <em>Understand Activity:</em> Define paper production capacity, chemical pulp digestion process, timber feedstock demands, and freshwater requirements.\n<br>• <em>Screening:</em> Industrial paper mills are high-risk red-category units requiring mandatory full EIA.\n<br>• <em>Scoping:</em> Establish site-specific Terms of Reference (ToR) focusing on deforestation and river pollution.</li>\n<li><strong>Phase 2 (Full EIA Study Steps):</strong>\n<br>• <em>Baseline Evaluation:</em> Sample upstream/downstream water quality, forest biodiversity, and seasonal river discharge.\n<br>• <em>Identify & Choose Alternatives:</em> Compare cleaner chlorine-free bleaching (TCF) vs conventional chlorine; assess alternative industrial sites away from primary forest.\n<br>• <em>Impact Prediction & Characterization:</em> Quantify air emissions ($\\text{SO}_2$, TRS odors), black liquor toxic chemical wastewater, and loss of wildlife habitat.\n<br>• <em>EMP & Mitigation:</em> Design closed-loop chemical recovery boilers, Effluent Treatment Plants (ETP) with zero-liquid discharge (ZLD), and dedicated commercial agroforestry plantations.\n<br>• <em>Public Hearing:</em> Consult local forest communities, farmers, and downstream pastoralists.\n<br>• <em>Documentation:</em> Compile Draft and Final EIA report for regulatory appraisal.</li>\n<li><strong>Justification of Interdisciplinary Team:</strong> Paper manufacturing impacts multiple distinct ecological and human spheres. An effective audit requires:\n<br>1. <em>Chemical / Environmental Engineer:</em> Pulping processes, chemical recovery, and ETP design.\n<br>2. <em>Hydrologist / Water Resources Expert:</em> River discharge modeling and effluent dilution.\n<br>3. <em>Forest Ecologist / Botanist:</em> Forest canopy loss, biodiversity impact, and sustainable timber harvesting.\n<br>4. <em>Socio-Economist / Public Health Specialist:</em> Indigenous community rights, public consultations, and worker safety.\n<br>5. <em>Air Pollution Modeler:</em> Boiler stack emissions and toxic odor dispersion.</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>The EIA Methodology:</strong> The paper mill case on Mt. Kenya highlights the delicate balance between industrial development and critical watershed preservation. Following UNEP/ENCAP guidelines, Phase 1 establishes the scope and preliminary risks, while Phase 2 conducts baseline sampling, multi-stakeholder consultations, and designs enforceable mitigation measures.</p>\n<p><em>Slide Reference: Class 12 Slides 15–22.</em></p>\n</div>"
        },
        {
            "id": "EQB-12-05",
            "class_id": 12,
            "class_name": "Environmental Impact Assessment (EIA)",
            "topic": "Coastal Mining Environmental Audit & Baseline Defense",
            "category": "Descriptive & Case Study",
            "exams": [
                {"paper": "End Exam 2019", "section": "Section V, Q1", "marks": "10M"},
                {"paper": "End Exam 2018", "section": "Part I, Q3 (OR)", "marks": "10M"}
            ],
            "marks": "10M",
            "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
            "prompt": "An important mining company has operated for 4 years in a coastal region. During a trial, the community argues water quality deteriorated and that the company is in a protected area. (a) What document must the company present to prove water was already deteriorated before their activities began, and why is it important? (b) What document proves they are not in a protected area and which institution issues it? (c) Mention 2 environmental impacts and 2 mitigation measures for their EMP.",
            "key_answer_points": "<ul>\n<li><strong>(a) Baseline Environmental Status Report (from the approved EIA):</strong>\n<br>• The company must present the <strong>Pre-Project Baseline Environmental Report</strong> (specifically the pre-operational baseline water quality sampling data collected prior to construction).\n<br>• <em>Importance:</em> In environmental law, liability follows the Precautionary Principle. The baseline report establishes legally valid scientific benchmark data proving pre-existing contamination from upstream sources before mine commencement.</li>\n<li><strong>(b) Environmental Clearance (EC) & Coastal Regulation Zone (CRZ) Clearance:</strong>\n<br>• <em>Documents:</em> Environmental Clearance (EC) and CRZ Clearance with authenticated Survey of India boundary maps.\n<br>• <em>Issuing Authority:</em> The <strong>Ministry of Environment, Forest and Climate Change (MoEFCC)</strong> and the National/State Coastal Zone Management Authority (NCZMA/SCZMA).</li>\n<li><strong>(c) Environmental Impacts & EMP Mitigations:</strong>\n<br>• <em>Impact 1:</em> Acid Mine Drainage (AMD) and heavy metal sediment runoff during monsoons.\n<br>• <em>Mitigation 1:</em> Construct peripheral lined silt traps, retention settling ponds, and automated neutralization dosing tanks.\n<br>• <em>Impact 2:</em> Coastal saltwater intrusion into local groundwater aquifers due to excessive mine dewatering.\n<br>• <em>Mitigation 2:</em> Establish an impermeable underground grout curtain and artificial recharge borewells to maintain groundwater balance.</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>Environmental Jurisprudence:</strong> Baseline environmental data acts as the ultimate shield for responsible operators and the primary tool for judges to determine genuine environmental damage.</p>\n<p><em>Slide Reference: Class 12 Slides 23–27.</em></p>\n</div>"
        },
        {
            "id": "EQB-12-06",
            "class_id": 12,
            "class_name": "Environmental Impact Assessment (EIA)",
            "topic": "Great Nicobar Project EIA Controversies",
            "category": "Short Answer & Definitions",
            "exams": [
                {"paper": "End Exam 2023", "section": "Section II, Q11", "marks": "2M"}
            ],
            "marks": "2M",
            "importance": "HIGH (⭐⭐⭐⭐)",
            "prompt": "List any two incorrect/incomplete information furnished in the EIA report of Great Nicobar case.",
            "key_answer_points": "<ul>\n<li><strong>Flaw 1 (Underreporting Giant Leatherback Sea Turtle Nesting):</strong> The EIA claimed Galathea Bay had low ecological nesting sensitivity, ignoring that it is one of the world's premier nesting grounds for the globally vulnerable Giant Leatherback turtle.</li>\n<li><strong>Flaw 2 (Ignoring Tribal Rights of Shompen & Nicobarese):</strong> Failed to adequately consult the particularly vulnerable semi-nomadic Shompen tribe, glossing over the permanent de-notification of nearly 84 square kilometers of tribal reserve forest.</li>\n<li><strong>Flaw 3 (Severe Under-Assessment of Seismic Tsunami Hazard):</strong> Great Nicobar sits in a high-risk Seismic Zone V; the 2004 mega-tsunami dropped the island coastline by 3–4 meters, a major geological risk barely analyzed for the port breakwaters.</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>Why This Case Is Studied:</strong> The Rs 72,000-crore mega transshipment port project in pristine Great Nicobar showed how rushed single-season baseline studies can bypass critical biodiversity and indigenous safeguards.</p>\n<p><em>Slide Reference: Class 12 Slides 28–32.</em></p>\n</div>"
        },
        {
            "id": "EQB-12-07",
            "class_id": 12,
            "class_name": "Environmental Impact Assessment (EIA)",
            "topic": "Four Core Stages of Indian EIA 2006 Notification",
            "category": "Descriptive & Case Study",
            "exams": [
                {"paper": "End Exam 2024", "section": "Section V", "marks": "4M"},
                {"paper": "End Exam 2023", "section": "Section II, Q9", "marks": "2M"}
            ],
            "marks": "4M",
            "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
            "prompt": "Explain the four core stages of Environmental Impact Assessment (EIA) according to the Indian EIA Notification 2006.",
            "key_answer_points": "<ul>\n<li><strong>Stage 1: Screening:</strong> Determines whether Category B projects require a full EIA (Category B1) or are cleared based on standard application Form 1 (Category B2). Category A projects bypass screening and require mandatory full EIA.</li>\n<li><strong>Stage 2: Scoping:</strong> Formulates the official <strong>Terms of Reference (ToR)</strong> outlining all environmental concerns and baseline data parameters that the applicant's EIA report must cover.</li>\n<li><strong>Stage 3: Public Consultation:</strong> Conducts public hearings chaired by the District Magistrate at the project site, gathering oral and written objections from local affected communities.</li>\n<li><strong>Stage 4: Appraisal:</strong> The Expert Appraisal Committee (EAC or SEAC) rigorously scrutinizes the final EIA report, public hearing minutes, and EMP to recommend approval, revisions, or rejection to MoEFCC.</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>The Legal Process:</strong> Notification 2006 decentralized clearances between central and state authorities, establishing an orderly four-stage procedural pipeline to balance economic development with environmental safeguards.</p>\n<p><em>Slide Reference: Class 12 Slides 5–9.</em></p>\n</div>"
        }
    ]

def get_class13_questions():
    return [
        {
            "id": "EQB-13-01",
            "class_id": 13,
            "class_name": "Grassroots Environmental Movements in India",
            "topic": "Chipko Movement Slogan",
            "category": "Short Answer & Definitions",
            "exams": [
                {"paper": "End Exam 2023", "section": "Section I, Q1(h)", "marks": "1M"}
            ],
            "marks": "1M",
            "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
            "prompt": "Slogan of \"Chipko movement\".",
            "key_answer_points": "<ul>\n<li><strong>Original Hindi Slogan:</strong>\n<br><em>\"क्या हैं जंगल के उपकार? मिट्टी, पानी और बयार। मिट्टी, पानी और बयार, ज़िंदा रहने के आधार।\"</em></li>\n<li><strong>English Translation:</strong>\n<br><em>\"What do the forests bear? Soil, water and pure air. Soil, water and pure air are the basis of staying alive.\"</em></li>\n<li><strong>Origin:</strong> Coined in 1977 by village activist <strong>Ghanshyam Raturi</strong> and popularized by women leaders like Gaura Devi and Sudesha Devi.</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>The Ecological Meaning:</strong> This slogan radically challenged the commercial timber mindset that viewed forests merely as resin, timber, and profit, asserting that forests are vital life-support systems providing clean soil, water, and air.</p>\n<p><em>Slide Reference: Class 13 Slide 5.</em></p>\n</div>"
        },
        {
            "id": "EQB-13-02",
            "class_id": 13,
            "class_name": "Grassroots Environmental Movements in India",
            "topic": "Sunderlal Bahuguna Leadership",
            "category": "MCQ & Objective",
            "exams": [
                {"paper": "End Exam 2022", "section": "Section III, Q7", "marks": "1M"}
            ],
            "marks": "1M",
            "importance": "HIGH (⭐⭐⭐⭐)",
            "prompt": "______ (person) led both Chipko and Tehri dam movement.",
            "key_answer_points": "<ul>\n<li><strong>Answer:</strong> <strong>Sunderlal Bahuguna</strong> (1927–2021).</li>\n<li><strong>Role in Chipko:</strong> Undertook a 5,000 km trans-Himalayan march across villages in the 1970s, carrying the message to Prime Minister Indira Gandhi which resulted in a 15-year commercial logging ban in the Uttarakhand Himalayas.</li>\n<li><strong>Role in Tehri Dam:</strong> Campaigned relentlessly and went on extended hunger strikes on the banks of the Bhagirathi River to oppose the construction of the seismically dangerous mega-dam.</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>A Gandhian Crusader:</strong> Bahuguna combined non-violent satyagraha with deep ecological philosophy, coining the motto: 'Ecology is permanent economy.'</p>\n<p><em>Slide Reference: Class 13 Slides 6 & 11.</em></p>\n</div>"
        },
        {
            "id": "EQB-13-03",
            "class_id": 13,
            "class_name": "Grassroots Environmental Movements in India",
            "topic": "Negative Impacts of Tehri Dam",
            "category": "Short Answer & Definitions",
            "exams": [
                {"paper": "End Exam 2024", "section": "Section V, Q4", "marks": "2M"},
                {"paper": "End Exam 2023", "section": "Section III, Q4", "marks": "3M"}
            ],
            "marks": "2M – 3M",
            "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
            "prompt": "What are the negative impacts of Tehri Dam?",
            "key_answer_points": "<ul>\n<li><strong>Seismic Hazard (Central Himalayan Gap):</strong> Built in high-risk Seismic Zone V near active fault lines. An earthquake of magnitude >8.0 could breach the 260.5m earth-and-rockfill dam, drowning downstream holy cities (Rishikesh, Haridwar) in hours.</li>\n<li><strong>Massive Involuntary Displacement:</strong> Submerged historic Tehri town and over 100 villages, displacing over 100,000 residents with incomplete rehabilitation.</li>\n<li><strong>Reservoir-Induced Seismicity & Landslides:</strong> Huge water mass (4 cubic km) exerts enormous pore pressure on fragile slope geology, causing slope collapses.</li>\n<li><strong>Ecological Stagnation of the Bhagirathi:</strong> Impedes natural sediment flow and destroys the breeding habitat of endangered cold-water Himalayan fish (Golden Mahseer).</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>The Mega-Dam Tradeoff:</strong> While providing 1,000 MW hydro-peaking power and drinking water to Delhi, Tehri Dam remains controversial due to serious geophysical risks in a geologically active young mountain belt.</p>\n<p><em>Slide Reference: Class 13 Slide 11.</em></p>\n</div>"
        },
        {
            "id": "EQB-13-04",
            "class_id": 13,
            "class_name": "Grassroots Environmental Movements in India",
            "topic": "Kali River Environmental Issues",
            "category": "Short Answer & Definitions",
            "exams": [
                {"paper": "End Exam 2023", "section": "Section III, Q3", "marks": "3M"}
            ],
            "marks": "3M",
            "importance": "HIGH (⭐⭐⭐⭐)",
            "prompt": "What are the environmental issues associated with Kali River of Western ghats?",
            "key_answer_points": "<ul>\n<li><strong>Dam Cascade & Flow Fragmentation:</strong> Over-dammed by 6 major hydroelectric dams (Supa, Kodasalli, Kadra), drowning thousands of acres of pristine evergreen Western Ghats rainforest.</li>\n<li><strong>Industrial Effluent Pollution (Paper Mills):</strong> The West Coast Paper Mills at Dandeli discharges untreated black liquor wastewater, heavily contaminating drinking water.</li>\n<li><strong>Manganese & Iron Mining Siltation:</strong> Open-pit mining in the catchment chokes the riverbed with heavy silt, destroying endemic riverine fish species.</li>\n<li><strong>Radiation Safety Concerns:</strong> The Kaiga Nuclear Power Generating Station draws cooling water from the Kali River basin, sparking persistent local civil protests over thermal discharge and radiation safety.</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>A Choked River:</strong> The Kali River in Uttara Kannada district is a prime example of an ecologically sensitive river system fragmented by overlapping industrial, mining, and power projects.</p>\n<p><em>Slide Reference: Class 13 Slide 13.</em></p>\n</div>"
        },
        {
            "id": "EQB-13-05",
            "class_id": 13,
            "class_name": "Grassroots Environmental Movements in India",
            "topic": "Four Indian Grassroots Movements & Locations",
            "category": "Short Answer & Definitions",
            "exams": [
                {"paper": "End Exam 2019", "section": "Section IX, Q1", "marks": "2M"}
            ],
            "marks": "2M",
            "importance": "HIGH (⭐⭐⭐⭐)",
            "prompt": "List any 4 environmental movements with their location.",
            "key_answer_points": "<ul>\n<li><strong>1. Chipko Movement (1973):</strong> Chamoli District, Uttarakhand (Himalayan foothills).</li>\n<li><strong>2. Appiko Movement (1983):</strong> Uttara Kannada District, Karnataka (Western Ghats).</li>\n<li><strong>3. Silent Valley Movement (1978):</strong> Palakkad District, Kerala (Western Ghats tropical rainforest).</li>\n<li><strong>4. Narmada Bachao Andolan (1985):</strong> Narmada River Valley across Gujarat, Madhya Pradesh, and Maharashtra.</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>Grassroots Environmentalism:</strong> Unlike Western environmentalism which often centered around wildlife conservation and wilderness recreation, Indian environmental struggles have been driven by forest-dependent rural and tribal communities protecting basic survival resources.</p>\n<p><em>Slide Reference: Class 13 Slides 4–12.</em></p>\n</div>"
        },
        {
            "id": "EQB-13-06",
            "class_id": 13,
            "class_name": "Grassroots Environmental Movements in India",
            "topic": "Appiko & Silent Valley Movements",
            "category": "Descriptive & Case Study",
            "exams": [
                {"paper": "End Exam 2019", "section": "Section IX", "marks": "4M"},
                {"paper": "End Exam 2018", "section": "Part I", "marks": "4M"}
            ],
            "marks": "4M",
            "importance": "HIGH (⭐⭐⭐⭐)",
            "prompt": "Describe the Appiko movement in Karnataka and the Silent Valley movement in Kerala.",
            "key_answer_points": "<ul>\n<li><strong>Appiko Movement (1983 - Karnataka):</strong>\n<br>• <em>Meaning:</em> In Kannada, 'Appiko' means 'to hug'—the southern counterpart to Chipko, led by Pandurang Hegde in Salkani forest.\n<br>• <em>Actions:</em> Villagers hugged trees to halt clear-felling for paper mills and commercial monoculture (teak/eucalyptus).\n<br>• <em>Threefold Motto:</em> <strong>Ubsu</strong> (Save forests), <strong>Belesu</strong> (Grow new trees), <strong>Balasu</strong> (Use forest produce rationally).</li>\n<li><strong>Silent Valley Movement (1978 - Kerala):</strong>\n<br>• <em>Threat:</em> A proposed 120 MW hydroelectric dam across the Kunthipuzha River threatening to submerge 8.3 sq km of ancient untouched tropical evergreen rainforest.\n<br>• <em>Key Weapon:</em> Led by the Kerala Sastra Sahitya Parishad (KSSP) using <strong>citizen science</strong>, popular theater, and ecology education. Biologists highlighted the habitat of the rare Lion-tailed Macaque.\n<br>• <em>Victory:</em> In 1983, Prime Minister Indira Gandhi canceled the dam; Silent Valley was declared a National Park in 1985.</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>Citizen Action:</strong> Silent Valley stands out as one of India's earliest successful environmental campaigns driven not by direct forest dwellers, but by school teachers, scientists, poets, and civil society.</p>\n<p><em>Slide Reference: Class 13 Slides 8–10.</em></p>\n</div>"
        }
    ]

if __name__ == "__main__":
    print(f"Class 12: {len(get_class12_questions())} Qs | Class 13: {len(get_class13_questions())} Qs.")
