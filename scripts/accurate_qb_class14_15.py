import json

def get_class14_questions():
    return [
        {
            "id": "EQB-14-01",
            "class_id": 14,
            "class_name": "Green Computing",
            "topic": "Green Computing Definition & 4 Approaches",
            "category": "Short Answer & Definitions",
            "exams": [
                {"paper": "End Exam 2024", "section": "Section IV(e)", "marks": "2M"},
                {"paper": "End Exam 2019", "section": "Section VI, Q1", "marks": "2M"},
                {"paper": "End Exam 2018", "section": "Part II, Q1, Q2", "marks": "2M + 8M"}
            ],
            "marks": "2M",
            "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
            "prompt": "What is green computing? List the approaches of Green computing.",
            "key_answer_points": "<ul>\n<li><strong>Definition:</strong> The environmentally responsible, energy-efficient, and eco-friendly design, manufacturing, operation, and disposal of computers, servers, displays, and communications infrastructure with minimal environmental impact.</li>\n<li><strong>The 4 Lifecycle Approaches:</strong>\n<br>1. <strong>Green Design:</strong> Designing low-power processors (ARM), passive cooling architectures, non-toxic materials, and modular upgradeable hardware.\n<br>2. <strong>Green Manufacturing:</strong> Eliminating toxic heavy metals (RoHS compliance: lead-free soldering) and reducing cleanroom water and energy consumption.\n<br>3. <strong>Green Use:</strong> Slashing operational power through server virtualization, dynamic frequency scaling, power management sleep modes (Energy Star), and cloud consolidation.\n<br>4. <strong>Green Disposal:</strong> Reclaiming precious metals (urban mining), certified recycling, and preventing toxic dumping in compliance with the Basel Convention.</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>The ICT Footprint:</strong> Global IT infrastructure consumes over 2% of the world's electricity (heading toward 8% with AI). Green computing provides engineering solutions across a device's entire lifetime.</p>\n<p><em>Slide Reference: Class 14 Slides 4–10.</em></p>\n</div>"
        },
        {
            "id": "EQB-14-02",
            "class_id": 14,
            "class_name": "Green Computing",
            "topic": "Thick Client vs Thin Client Architecture",
            "category": "Differentiate Between",
            "exams": [
                {"paper": "End Exam 2024", "section": "Section IV, Q(a)", "marks": "2M"},
                {"paper": "End Exam 2023", "section": "Section IV, Q3", "marks": "4M"},
                {"paper": "End Exam 2022", "section": "Section VII, Q(a)", "marks": "2M"},
                {"paper": "End Exam 2019", "section": "Section VI, Q2", "marks": "4M"}
            ],
            "marks": "2M – 4M",
            "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
            "prompt": "Differentiate between Thick client and Thin client. (What are the advantages of Thin client over Thick client?)",
            "key_answer_points": "<ul>\n<li><strong>Core Difference:</strong>\n<br>• <em>Thick Client (Fat Client):</em> A self-contained personal computer with its own powerful CPU, dedicated hard drive, operating system, and local software applications; processes data locally without needing a server to run.\n<br>• <em>Thin Client:</em> A minimalist, low-power terminal with no local hard drive or moving parts; relies completely on a central server for computation, storage, and operating system execution.</li>\n<li><strong>Key Advantages of Thin Clients:</strong>\n<br>1. <em>Drastic Power Savings:</em> Consumes only <strong>6–15 Watts</strong> compared to <strong>80–250 Watts</strong> for a traditional thick PC (up to 80–90% power cut).\n<br>2. <em>Longer Lifecycle & Low E-Waste:</em> Lasts <strong>7–10 years</strong> with no moving parts (fans, spinning disks) vs 3–4 years for a thick PC, reducing e-waste generation by two-thirds.\n<br>3. <em>Cooler & Silent:</em> Generates near-zero heat, drastically slashing air conditioning energy demands in corporate offices and computer labs.\n<br>4. <em>Centralized Security:</em> Software updates, patches, and backups happen once on the server rather than manually across hundreds of endpoints.</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>Comparison Table:</strong></p>\n<table class=\"exam-table\">\n<thead><tr><th>Dimension</th><th>Thick Client</th><th>Thin Client</th></tr></thead>\n<tbody>\n<tr><td>Power Consumption</td><td>80 to 250 W</td><td>6 to 15 W</td></tr>\n<tr><td>Local Storage & Processing</td><td>Full local CPU/GPU/HDD</td><td>Minimalist; runs off central server</td></tr>\n<tr><td>Lifespan</td><td>3 to 4 years</td><td>7 to 10 years</td></tr>\n<tr><td>Heat & Noise</td><td>High heat output, noisy cooling fans</td><td>Silent, fanless, minimal heat</td></tr>\n</tbody>\n</table>\n<p><em>Slide Reference: Class 14 Slides 14–18.</em></p>\n</div>"
        },
        {
            "id": "EQB-14-03",
            "class_id": 14,
            "class_name": "Green Computing",
            "topic": "Moore's Law & Planned Obsolescence",
            "category": "Short Answer & Definitions",
            "exams": [
                {"paper": "End Exam 2024", "section": "Section II, Q(e)", "marks": "1M"},
                {"paper": "End Exam 2023", "section": "Section I, Q1(a)", "marks": "1M"}
            ],
            "marks": "1M",
            "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
            "prompt": "What is Moore's law?",
            "key_answer_points": "<ul>\n<li><strong>Definition:</strong> An empirical observation made in 1965 by Intel co-founder Gordon Moore stating that the <strong>number of transistors packed on a microchip doubles approximately every two years</strong> while the cost of computers is halved.</li>\n<li><strong>Environmental Consequence:</strong> While driving phenomenal compute performance, it creates rapid electronic obsolescence. Perfectly functional hardware is discarded every 2–3 years, driving the global e-waste avalanche.</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>The Double-Edged Sword:</strong> Moore's Law enabled the digital revolution, but shortening product upgrade cycles has caused electronic waste to become the fastest-growing waste stream on Earth.</p>\n<p><em>Slide Reference: Class 14 Slide 11.</em></p>\n</div>"
        },
        {
            "id": "EQB-14-04",
            "class_id": 14,
            "class_name": "Green Computing",
            "topic": "Hazardous Nature of E-Waste",
            "category": "Short Answer & Definitions",
            "exams": [
                {"paper": "End Exam 2023", "section": "Section I, Q2", "marks": "1M"}
            ],
            "marks": "1M",
            "importance": "HIGH (⭐⭐⭐⭐)",
            "prompt": "Is e-waste hazardous?",
            "key_answer_points": "<ul>\n<li><strong>Answer:</strong> <strong>Yes, e-waste is highly hazardous.</strong></li>\n<li><strong>Toxic Chemical Constituents:</strong> Contains dangerous toxic heavy metals and halogenated chemicals including:\n<br>• <strong>Lead (Pb):</strong> Solder and CRT monitor glass (neurotoxin, causes brain/kidney damage).\n<br>• <strong>Cadmium (Cd):</strong> Rechargeable chip resistors and batteries (kidney damage, carcinogen).\n<br>• <strong>Mercury (Hg):</strong> Flat-screen backlights and switches (bioaccumulative brain toxin).\n<br>• <strong>Brominated Flame Retardants (BFRs):</strong> Plastic chassis and circuit boards (endocrine disruptors).\n<br>• <strong>Polyvinyl Chloride (PVC):</strong> Cable insulation; releases highly toxic dioxins when burned.</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>Informal Recycling Dangers:</strong> When discarded electronics are open-burned or washed with acid in informal scrapyards (like Agbogbloshie or Seelampur), these toxins leach into soils and local groundwater.</p>\n<p><em>Slide Reference: Class 14 Slides 22–26.</em></p>\n</div>"
        },
        {
            "id": "EQB-14-05",
            "class_id": 14,
            "class_name": "Green Computing",
            "topic": "Basel Convention on Hazardous Wastes",
            "category": "Short Answer & Definitions",
            "exams": [
                {"paper": "End Exam 2024", "section": "Section II, Q(a)", "marks": "1M"},
                {"paper": "End Exam 2023", "section": "Section I, Q1(e)", "marks": "1M"},
                {"paper": "End Exam 2022", "section": "Section III, Q12", "marks": "1M"}
            ],
            "marks": "1M",
            "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
            "prompt": "What is Basel Convention? [one or two sentences]",
            "key_answer_points": "<ul>\n<li><strong>Definition:</strong> The <strong>Basel Convention on the Control of Transboundary Movements of Hazardous Wastes and Their Disposal</strong> is an international treaty adopted in 1989 (entered into force 1992).</li>\n<li><strong>Primary Objective:</strong> Designed to prevent rich developed nations from dumping hazardous chemical and electronic waste into developing countries, requiring Prior Informed Consent (PIC) before any transboundary movement.</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>Stopping Toxic Colonialism:</strong> The treaty ensures that developed nations manage and recycle their own toxic waste at home rather than exporting environmental burdens overseas.</p>\n<p><em>Slide Reference: Class 14 Slide 27.</em></p>\n</div>"
        },
        {
            "id": "EQB-14-06",
            "class_id": 14,
            "class_name": "Green Computing",
            "topic": "Green Website Concept & Examples",
            "category": "Short Answer & Definitions",
            "exams": [
                {"paper": "End Exam 2024", "section": "Section II, Q(d) & Section III(d)", "marks": "1M + 1M"},
                {"paper": "End Exam 2022", "section": "Section VI, Q(d)", "marks": "1M"}
            ],
            "marks": "1M",
            "importance": "HIGH (⭐⭐⭐⭐)",
            "prompt": "What is a Green Website? Give examples.",
            "key_answer_points": "<ul>\n<li><strong>Definition:</strong> A website engineered to minimize energy consumption per page visit through ultra-clean lightweight code, optimized compressed images, dark/minimalist palettes, efficient caching, and hosting exclusively on 100% renewable-powered data centers.</li>\n<li><strong>Real-World Examples:</strong> <strong>EvenGreener</strong>, <strong>City Museum</strong>, <strong>blubolt PRO</strong>, and <strong>Atomicdust PRO</strong> (or certified green-hosted websites emitting $<0.2$g $\\text{CO}_2$ per page view).</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>Web Sustainability:</strong> The average web page transfer has ballooned over 2MB. Green web engineering cuts page weight to under 500KB and runs on solar or wind-backed servers.</p>\n<p><em>Slide Reference: Class 14 Slide 20.</em></p>\n</div>"
        },
        {
            "id": "EQB-14-07",
            "class_id": 14,
            "class_name": "Green Computing",
            "topic": "Smartphone Production Environmental Impact",
            "category": "Descriptive & Case Study",
            "exams": [
                {"paper": "End Exam 2024", "section": "Section VI, Q1", "marks": "3M"}
            ],
            "marks": "3M",
            "importance": "HIGH (⭐⭐⭐⭐)",
            "prompt": "Explain the impact of smart phone/mobile devices production on environment?",
            "key_answer_points": "<ul>\n<li><strong>Disproportionate Manufacturing Footprint:</strong> Over <strong>70–80% of a smartphone's lifetime carbon footprint</strong> occurs during initial manufacturing and raw material extraction, not during daily use.</li>\n<li><strong>Destructive Mineral Mining:</strong> Requires rare minerals mined at severe environmental cost: cobalt from the DR Congo, lithium from salt flats (depleting scarce groundwater), and gold (generating 20 tonnes of toxic waste slurry per ring equivalent).</li>\n<li><strong>Cleanroom Energy & Water:</strong> Fabricating microprocessors requires ultra-pure water (thousands of liters per chip) and continuous high-energy cleanroom climate control.</li>\n<li><strong>Short Consumer Lifecycles:</strong> Millions of phones are replaced every 18–24 months due to non-replaceable glued batteries and software slowdowns, creating toxic e-waste.</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>Embodied Carbon:</strong> Unlike an automobile where most carbon comes from burning gasoline, a smartphone's carbon is locked in before you even open the box. Extending device lifespan to 4–5 years is the single most effective environmental fix.</p>\n<p><em>Slide Reference: Class 14 Slides 12–13.</em></p>\n</div>"
        },
        {
            "id": "EQB-14-08",
            "class_id": 14,
            "class_name": "Green Computing",
            "topic": "Ventilation Measurement in Mechanical Buildings",
            "category": "Descriptive & Case Study",
            "exams": [
                {"paper": "End Exam 2024", "section": "Section V, Q3", "marks": "2M"},
                {"paper": "End Exam 2023", "section": "Section II, Q2", "marks": "2M"},
                {"paper": "End Exam 2022", "section": "Section X, Q(c)", "marks": "5M"}
            ],
            "marks": "2M – 5M",
            "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
            "prompt": "How is ventilation measured in mechanically ventilated buildings?",
            "key_answer_points": "<ul>\n<li><strong>1. Infiltration Air Change per Hour (ACH):</strong> Reported as Air Changes per Hour (ACH)—the rate at which indoor air is replaced by outdoor air (ASHRAE guideline: 0.1–0.2 in airtight buildings vs 2.0–3.0 in leaky buildings).</li>\n<li><strong>2. Tracer Gas Technique:</strong> An inert, non-reactive gas (such as sulfur hexafluoride $\\\\text{SF}_6$ or nitrous oxide) is injected into the building. Measuring its concentration decay over time gives the exact natural air infiltration rate.</li>\n<li><strong>3. $\\\\text{CO}_2$ Surrogate Index (ASHRAE Mass Balance Model):</strong> In HVAC buildings, occupant-exhaled $\\\\text{CO}_2$ serves as a surrogate for ventilation rate:<div class=\"formula-box\">$$Q = \\\\frac{G}{C_i - C_a}$$</div>Where $Q$ = Outdoor airflow rate per person, $G$ = $\\\\text{CO}_2$ generation rate per occupant, $C_i$ = Indoor $\\\\text{CO}_2$ concentration, and $C_a$ = Ambient outdoor $\\\\text{CO}_2$ concentration (~420 ppm).</li>\n<li><strong>ASHRAE Standard:</strong> Minimum recommended ventilation rate is <strong>8 liters/second per person</strong> to keep indoor $\\\\text{CO}_2$ under 700 ppm above outdoor levels (under 1,000 ppm total).</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>Why Measure Ventilation?:</strong> In tight, energy-efficient data centers and offices, poor ventilation traps toxic indoor pollutants (VOCs, formaldehyde), causing Sick Building Syndrome (SBS) and reducing cognitive function.</p>\n<p><em>Slide Reference: Class 14 Slides 30–33.</em></p>\n</div>"
        },
        {
            "id": "EQB-14-09",
            "class_id": 14,
            "class_name": "Green Computing",
            "topic": "Source Isolation Strategy in Indoor Air Quality",
            "category": "Short Answer & Definitions",
            "exams": [
                {"paper": "End Exam 2024", "section": "Section III, Q(a)", "marks": "1M"},
                {"paper": "End Exam 2022", "section": "Section VI, Q(a)", "marks": "1M"}
            ],
            "marks": "1M",
            "importance": "HIGH (⭐⭐⭐⭐)",
            "prompt": "Give an example of a source isolation strategy in indoor air quality maintenance.",
            "key_answer_points": "<ul>\n<li><strong>Definition:</strong> Physically enclosing pollutant-generating equipment or activities in separate dedicated rooms with independent exhaust systems and negative air pressure to stop pollutants from circulating into the general breathing area.</li>\n<li><strong>Real-World Examples:</strong>\n<br>1. <strong>Photocopier & High-Volume Printer Rooms:</strong> Enclosed with dedicated external exhaust fans to remove toxic ozone and ultrafine toner dust particles.\n<br>2. <strong>Commercial Cafeteria Kitchens:</strong> Negative-pressure hoods to capture cooking grease and combustion gases.\n<br>3. <strong>Janitorial Chemical Storage Closets & Bathrooms:</strong> Dedicated exhaust venting directly outdoors.</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>Contaminant Containment:</strong> Source isolation is far cheaper and more effective than trying to filter out dilute chemical pollutants once they have spread across the entire office HVAC system.</p>\n<p><em>Slide Reference: Class 14 Slide 34.</em></p>\n</div>"
        },
        {
            "id": "EQB-14-10",
            "class_id": 14,
            "class_name": "Green Computing",
            "topic": "EPA 4 Most Dangerous Indoor Air Pollutants",
            "category": "Short Answer & Definitions",
            "exams": [
                {"paper": "End Exam 2023", "section": "Section IV, Q1", "marks": "4M"}
            ],
            "marks": "4M",
            "importance": "HIGH (⭐⭐⭐⭐)",
            "prompt": "According to the EPA, what are the 4 most dangerous indoor air pollutants in developed countries?",
            "key_answer_points": "<ul>\n<li><strong>1. Environmental Tobacco Smoke (ETS) / Secondhand Smoke:</strong> Contains over 4,000 chemicals, including 70 known carcinogens and carbon monoxide.</li>\n<li><strong>2. Formaldehyde (HCHO):</strong> Emitted by pressed-wood furniture, plywood adhesives, glues, carpets, and urea-formaldehyde foam insulation (irritant, potent carcinogen).</li>\n<li><strong>3. Radioactive Radon-222 Gas:</strong> Colorless, odorless noble gas that seeps from radioactive decay of natural uranium in basement soil and rocks (leading cause of lung cancer among non-smokers).</li>\n<li><strong>4. Very Fine / Ultrafine Particulate Matter (PM2.5):</strong> Emitted by office printers, cooking stoves, and fireplaces; penetrates deep into lung alveoli and crosses directly into the bloodstream.</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>The Indoor Hazard:</strong> Because modern office workers spend over 90% of their time indoors, indoor air pollutant levels are often 2 to 5 times higher than outdoor air.</p>\n<p><em>Slide Reference: Class 14 Slide 29.</em></p>\n</div>"
        },
        {
            "id": "EQB-14-11",
            "class_id": 14,
            "class_name": "Green Computing",
            "topic": "Computer Components vs Chemical Constituents",
            "category": "Match the Following",
            "exams": [
                {"paper": "End Exam 2024", "section": "Section I(A)", "marks": "5M"},
                {"paper": "End Exam 2022", "section": "Section I(A)", "marks": "5M"},
                {"paper": "End Exam 2018", "section": "Part II, Q3", "marks": "2M"}
            ],
            "marks": "5M",
            "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
            "prompt": "Section-I: Match the Following: Computer components vs Chemical constituents [5 Marks].",
            "key_answer_points": "<ul>\n<li><strong>Matching Solution:</strong>\n<br>1. <strong>Printed circuit boards</strong> $\\rightarrow$ <strong>Lead & cadmium</strong> (and brominated flame retardants)\n<br>2. <strong>Computer batteries</strong> $\\rightarrow$ <strong>Cadmium</strong> (Ni-Cd chemistry and lithium compounds)\n<br>3. <strong>Capacitors and transformers</strong> $\\rightarrow$ <strong>Poly Chlorinated Biphenyls (PCBs)</strong>\n<br>4. <strong>Switches & flat screen monitors</strong> $\\rightarrow$ <strong>Mercury</strong>\n<br>5. <strong>Cable insulation/coating</strong> $\\rightarrow$ <strong>Poly Vinyl Chloride (PVC)</strong></li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>Technical Rationale:</strong> This exact 5-point match appears repeatedly across multiple end-sem exams. Each electronic component uses specific chemical properties that become toxic hazards if landfilled.</p>\n<p><em>Slide Reference: Class 14 Slide 25.</em></p>\n</div>"
        },
        {
            "id": "EQB-14-12",
            "class_id": 14,
            "class_name": "Green Computing",
            "topic": "Source Material vs Indoor Air Pollutant",
            "category": "Match the Following",
            "exams": [
                {"paper": "End Exam 2024", "section": "Section I(B)", "marks": "5M"},
                {"paper": "End Exam 2022", "section": "Section I(D)", "marks": "5M"},
                {"paper": "Mid 2019", "section": "Part I, Q11", "marks": "2.5M"}
            ],
            "marks": "5M",
            "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
            "prompt": "Section-I: Match the Following: Source Material vs Indoor Air Pollutant [5 Marks].",
            "key_answer_points": "<ul>\n<li><strong>Matching Solution:</strong>\n<br>1. <strong>Pipe Insulation</strong> $\\rightarrow$ <strong>Asbestos</strong>\n<br>2. <strong>Furniture / Pressed Wood</strong> $\\rightarrow$ <strong>Formaldehyde</strong>\n<br>3. <strong>Air fresheners / moth balls</strong> $\\rightarrow$ <strong>Para-dichlorobenzene</strong>\n<br>4. <strong>Paint stripper / thinner</strong> $\\rightarrow$ <strong>Methyl chloride (Methylene chloride)</strong>\n<br>5. <strong>Heating and cooling ducts</strong> $\\rightarrow$ <strong>Mold, bacteria (Biological contaminants)</strong></li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>Technical Rationale:</strong> Regular high-frequency match question testing building materials and their corresponding volatile or fibrous toxic emissions.</p>\n<p><em>Slide Reference: Class 14 Slide 28.</em></p>\n</div>"
        }
    ]

def get_class15_questions():
    return [
        {
            "id": "EQB-15-01",
            "class_id": 15,
            "class_name": "Green Engineering & Industrial Ecology",
            "topic": "Green Engineering Definition",
            "category": "Short Answer & Definitions",
            "exams": [
                {"paper": "End Exam 2018", "section": "Part III, Q1", "marks": "2M"}
            ],
            "marks": "2M",
            "importance": "HIGH (⭐⭐⭐⭐)",
            "prompt": "What is Green engineering?",
            "key_answer_points": "<ul>\n<li><strong>Definition:</strong> The design, commercialization, and use of processes and products in a way that minimizes pollution, promotes sustainability, protects human health, and conserves natural resources without compromising economic viability.</li>\n<li><strong>Foundational Framework:</strong> Formulated by Paul Anastas and Julie Zimmerman as the <strong>12 Principles of Green Engineering</strong>, shifting engineering from end-of-pipe waste management to upfront benign design.</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>Paradigm Shift:</strong> Traditional engineering focused on performance and cost while treating pollution as an afterthought. Green engineering embeds ecological limits into the initial design phase.</p>\n<p><em>Slide Reference: Class 15 Slide 4.</em></p>\n</div>"
        },
        {
            "id": "EQB-15-02",
            "class_id": 15,
            "class_name": "Green Engineering & Industrial Ecology",
            "topic": "Green Computing vs Green Engineering",
            "category": "Differentiate Between",
            "exams": [
                {"paper": "End Exam 2024", "section": "Section IV(e)", "marks": "2M"},
                {"paper": "End Exam 2022", "section": "Section VII, Q(d)", "marks": "2M"}
            ],
            "marks": "2M",
            "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
            "prompt": "Differentiate between Green computing and Green Engineering.",
            "key_answer_points": "<ul>\n<li><strong>Green Computing:</strong>\n<br>• <em>Scope:</em> Narrowly focused on the lifecycle of <strong>Information & Communications Technology (ICT)</strong>—computers, microprocessors, servers, data centers, networks, and e-waste.\n<br>• <em>Core Metrics:</em> PUE (Power Usage Effectiveness), Energy Star ratings, server virtualization, RoHS compliance.\n<br>• <em>Key Goal:</em> Cutting ICT electrical power and detoxifying electronic waste.</li>\n<li><strong>Green Engineering:</strong>\n<br>• <em>Scope:</em> Broad discipline spanning <strong>all engineering domains</strong> (chemical, civil, mechanical, materials, manufacturing).\n<br>• <em>Core Principles:</em> Governed by Anastas & Zimmerman's 12 Principles (designing for non-toxicity, industrial symbiosis, life cycle design, material separation).\n<br>• <em>Key Goal:</em> Closing resource and energy loops across all manufacturing, industrial, and infrastructure systems.</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>Hierarchy:</strong> Green computing is a specialized subdomain of green engineering applied specifically to computing hardware and data centers.</p>\n<p><em>Slide Reference: Class 15 Slide 5 & Class 14 Slide 4.</em></p>\n</div>"
        },
        {
            "id": "EQB-15-03",
            "class_id": 15,
            "class_name": "Green Engineering & Industrial Ecology",
            "topic": "Principles of Green Engineering with Examples",
            "category": "Descriptive & Case Study",
            "exams": [
                {"paper": "End Exam 2024", "section": "Section VI, Q2", "marks": "3M"},
                {"paper": "End Exam 2023", "section": "Section III, Q2", "marks": "3M"},
                {"paper": "End Exam 2022", "section": "Section III, Q1", "marks": "1M"},
                {"paper": "End Exam 2019", "section": "Section VII, Q2", "marks": "3M"},
                {"paper": "End Exam 2018", "section": "Part III, Q2", "marks": "6M"}
            ],
            "marks": "3M – 6M",
            "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
            "prompt": "Explain any principles of green engineering with examples (specifically: Integrate material and energy flows, Conserve complexity, and Minimize material diversity).",
            "key_answer_points": "<ul>\n<li><strong>1. Integrate Material and Energy Flows:</strong>\n<br>• <em>Principle:</em> Industrial systems should mimic natural ecosystems where one process's waste or byproduct becomes the feedstock for another process.\n<br>• <em>Example:</em> <strong>Kalundborg Eco-Industrial Park (Denmark)</strong>—waste steam from a coal/biomass power plant heats homes and refineries; sulfur sludge from smokestack scrubbers is turned into gypsum plasterboard for construction.</li>\n<li><strong>2. Conserve Complexity:</strong>\n<br>• <em>Principle:</em> Preserve the high-value structural and chemical complexity of materials rather than degrading them into low-grade molecules during recycling.\n<br>• <em>Example:</em> Re-molding biomaterials or modularly repairing computer circuit boards rather than smelting everything down to base metals.</li>\n<li><strong>3. Minimize Material Diversity:</strong>\n<br>• <em>Principle:</em> Design products using fewer distinct types of materials to make end-of-life disassembly and recycling simple and economically feasible.\n<br>• <em>Example:</em> Manufacturing automotive bumper assemblies or consumer drink bottles from a single polymer resin (mono-material PET or polypropylene) rather than laminating multiple incompatible plastics together.</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>The 12 Principles:</strong> Formulated by Anastas & Zimmerman, these principles guide designers to make products that are safe, durable, and recyclable by design.</p>\n<p><em>Slide Reference: Class 15 Slides 6–15.</em></p>\n</div>"
        },
        {
            "id": "EQB-15-04",
            "class_id": 15,
            "class_name": "Green Engineering & Industrial Ecology",
            "topic": "Denim Manufacturing Environmental Footprint",
            "category": "Descriptive & Case Study",
            "exams": [
                {"paper": "End Exam 2024", "section": "Section VI, Q4", "marks": "3M"},
                {"paper": "End Exam 2023", "section": "Section IV, Q4", "marks": "4M"},
                {"paper": "End Exam 2022", "section": "Section IX, Q(b)", "marks": "2M"},
                {"paper": "End Exam 2019", "section": "Section VII, Q1", "marks": "4M"}
            ],
            "marks": "3M – 4M",
            "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
            "prompt": "Explain the impact of Denim manufacturing on water consumption and pollution?",
            "key_answer_points": "<ul>\n<li><strong>Astronomical Water Consumption:</strong> Producing a single pair of standard denim jeans consumes between <strong>7,000 to 10,000 liters of fresh water</strong> across its lifecycle (primarily for water-intensive cotton irrigation and multi-stage washing).</li>\n<li><strong>Toxic Indigo Dye Pollution:</strong> Synthetic indigo dye is insoluble in water; it requires toxic reducing agents like <strong>sodium hydrosulfite ($\\text{Na}_2\\text{S}_2\\text{O}_4$)</strong> and strong caustic soda ($\\text{NaOH}$). Untreated dye wastewater strips oxygen from rivers, turning waters opaque blue and killing aquatic life.</li>\n<li><strong>Heavy Metal Contamination:</strong> Fixatives and mordants contain toxic heavy metals including chromium, copper, and arsenic that accumulate in downstream farmland soils.</li>\n<li><strong>Chemical Bleaching & Finishing:</strong> Vintage distressed looks use potassium permanganate sprays, chlorine bleaching, and silica sandblasting (which causes lethal silicosis in garment workers).</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>A Case Study in Textile Ecology:</strong> Denim demonstrates why Life Cycle Assessment (LCA) is vital in industrial engineering. Greener alternatives use ozone fading, laser distressing, and organic plant dyes.</p>\n<p><em>Slide Reference: Class 15 Slides 18–22.</em></p>\n</div>"
        },
        {
            "id": "EQB-15-05",
            "class_id": 15,
            "class_name": "Green Engineering & Industrial Ecology",
            "topic": "Kalundborg Symbiosis Principle",
            "category": "MCQ & Objective",
            "exams": [
                {"paper": "End Exam 2022", "section": "Section III, Q1", "marks": "1M"}
            ],
            "marks": "1M",
            "importance": "HIGH (⭐⭐⭐⭐)",
            "prompt": "An example of \"Local industries\" was taken to discuss which principle of green engineering?",
            "key_answer_points": "<ul>\n<li><strong>Answer:</strong> <strong>Integrate Material and Energy Flows</strong> (Principle 7).</li>\n<li><strong>Case Reference:</strong> The <strong>Kalundborg Eco-Industrial Park in Denmark</strong>, where separate companies exchange waste steam, cooling water, fly ash, and sulfur to minimize waste.</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>Industrial Symbiosis:</strong> Proves that co-locating industries and creating closed-loop byproduct exchanges makes economic sense without requiring government subsidies.</p>\n<p><em>Slide Reference: Class 15 Slide 16.</em></p>\n</div>"
        }
    ]

if __name__ == "__main__":
    print(f"Class 14: {len(get_class14_questions())} Qs | Class 15: {len(get_class15_questions())} Qs.")
