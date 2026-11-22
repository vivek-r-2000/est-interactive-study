# Class 14: Green Computing Question Bank
class_14_questions = [
    {
        "id": "EQB-14-01",
        "class_id": 14,
        "class_name": "Green Computing",
        "topic": "Green Computing Definition & 4 Core Approaches",
        "category": "Comprehensive Descriptive",
        "exams": [
            {"paper": "End Exam 2018", "section": "Part II, Q1–2", "marks": "10M"},
            {"paper": "End Exam 2019", "section": "Section VI, Q1", "marks": "2M"},
            {"paper": "EST End Exam 2024", "section": "Section IV, Q(e)", "marks": "2M"}
        ],
        "marks": "2M – 10M",
        "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
        "prompt": "Define Green Computing. Explain the four fundamental approaches across the hardware lifecycle: Green Design, Green Manufacturing, Green Use, and Green Disposal.",
        "key_answer_points": """<ul>
          <li><strong>Definition:</strong> Green Computing is the environmentally responsible, eco-friendly, and energy-efficient design, manufacture, operation, and disposal of computers, servers, monitors, storage devices, and communication systems with minimal or zero environmental impact.</li>
          <li><strong>The 4 Fundamental Lifecycle Approaches:</strong>
            <br>1. <strong>Green Design:</strong> Engineering energy-efficient microprocessors, low-power sleep modes, non-toxic lead-free recyclable materials, modular components, and passive cooling architectures.
            <br>2. <strong>Green Manufacturing:</strong> Eliminating hazardous substances (lead, mercury, cadmium, hexavalent chromium) in fabrication, reducing cleanroom energy and water consumption, achieving RoHS compliance, and using renewable energy in semiconductor foundries.
            <br>3. <strong>Green Use:</strong> Minimizing electrical energy consumption of running IT equipment through dynamic voltage/frequency scaling (DVFS), server virtualization, consolidation, intelligent power management (Energy Star), and cloud resource scheduling.
            <br>4. <strong>Green Disposal:</strong> Responsible e-waste refurbishment, reuse, certified recycling, precious metal reclamation (urban mining), and eliminating informal hazardous toxic dumping in compliance with the Basel Convention.</li>
        </ul>""",
        "detailed_answer": """<div class="detailed-body">
          <p><strong>Context & Origins:</strong> The green computing movement was formally catalyzed in 1992 when the US Environmental Protection Agency (EPA) launched the <strong>Energy Star</strong> labeling program. With computing infrastructure now consuming over 2% of total global electricity (projected to surge to 8% with generative AI workloads), sustainable computing spans the entire product lifecycle.</p>
          <h4>Detailed Breakdown of the 4 Lifecycle Pillars</h4>
          <table class="exam-table">
            <thead><tr><th>Approach</th><th>Lifecycle Phase</th><th>Key Engineering Strategies</th><th>Real-World Example</th></tr></thead>
            <tbody>
              <tr><td><strong>Green Design</strong></td><td>Pre-production / R&D</td><td>Low thermal design power (TDP), eliminating halogens, modular snap-in chassis</td><td>ARM architectures, Fairphone modular design</td></tr>
              <tr><td><strong>Green Manufacturing</strong></td><td>Fabrication / Assembly</td><td>Eliminating CFC solvents, closed-loop wafer recycling, RoHS compliance</td><td>TSMC/Intel renewable energy foundries</td></tr>
              <tr><td><strong>Green Use</strong></td><td>Operation / Data Center</td><td>Server virtualization (VMware/KVM), AI-optimized cooling, dynamic frequency scaling</td><td>Google data centers using DeepMind AI to slash cooling power by 40%</td></tr>
              <tr><td><strong>Green Disposal</strong></td><td>End-of-Life / Retirement</td><td>Urban mining of gold/copper, depolymerizing plastics, zero-landfill e-waste recycling</td><td>Apple Daisy robot disassembling 200 iPhones/hr</td></tr>
            </tbody>
          </table>
          <p><em>Slide Reference: Class 14 Slides 4–10 (Green ICT Foundations).</em></p>
        </div>"""
    },
    {
        "id": "EQB-14-02",
        "class_id": 14,
        "class_name": "Green Computing",
        "topic": "Thick Client vs Thin Client Architecture",
        "category": "Differentiate Between",
        "exams": [
            {"paper": "EST End Exam 2024", "section": "Section IV, Q(a)", "marks": "2M"},
            {"paper": "End Exam 2023", "section": "Section IV, Q3", "marks": "4M"},
            {"paper": "End Exam 2022", "section": "Section VII, Q(a)", "marks": "2M"},
            {"paper": "End Exam 2019", "section": "Section VI, Q2", "marks": "4M"}
        ],
        "marks": "2M – 4M",
        "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
        "prompt": "Differentiate thoroughly between Thick Clients and Thin Clients. Compare their system architecture, energy consumption, heat output, lifecycle duration, and embodied carbon.",
        "key_answer_points": """<ul>
          <li><strong>Architecture & Processing:</strong>
            <br>• <em>Thick Client (Fat/Rich Client):</em> Self-contained computer equipped with local hard drives, powerful multi-core CPU, dedicated GPU, and local OS; executes all operating systems and software applications locally.
            <br>• <em>Thin Client:</em> Minimalist, solid-state terminal without local mechanical hard drive; relies entirely on network connection to run applications inside virtual machines on a centralized server (Virtual Desktop Infrastructure / VDI).</li>
          <li><strong>Electrical Power Consumption:</strong>
            <br>• Thick Client: High power draw of <strong>75W to 150W+</strong> per workstation.
            <br>• Thin Client: Ultra-low power draw of only <strong>5W to 15W</strong> (saving <strong>80% to 90%</strong> electricity).</li>
          <li><strong>Thermal Heat Dissipation & Noise:</strong> Thick clients generate intense heat requiring noisy fans and heavy office air conditioning; Thin clients utilize passive conduction cooling (fanless, 100% silent) with near-zero heat dissipation.</li>
          <li><strong>Hardware Lifespan & Obsolescence:</strong> Thick clients become computationally obsolete in <strong>3 to 4 years</strong>; Thin clients remain fully functional for <strong>7 to 10+ years</strong> because processing upgrades occur entirely at the central server.</li>
          <li><strong>Embodied Carbon & E-Waste:</strong> Thin clients contain 70% fewer raw materials and zero mechanical moving parts, slashing manufacturing embodied carbon and post-consumer e-waste generation.</li>
        </ul>""",
        "detailed_answer": """<div class="detailed-body">
          <p><strong>System Engineering Contrast:</strong> In enterprise, university, and banking office environments, deploying hundreds of traditional desktop PCs wastes enormous electricity and generates massive electronic waste.</p>
          <h4>Deep Comparative Architecture Matrix</h4>
          <table class="exam-table">
            <thead><tr><th>Parameter</th><th>Thick Client (Traditional Desktop PC)</th><th>Thin Client (VDI Terminal)</th></tr></thead>
            <tbody>
              <tr><td><strong>Local Storage</strong></td><td>Local HDD / SSD (512 GB – 2 TB)</td><td>None (or small flash boot ROM <8 GB)</td></tr>
              <tr><td><strong>Power Consumption</strong></td><td><strong>75W – 250W</strong> (active load)</td><td><strong>5W – 15W</strong> (peak load)</td></tr>
              <tr><td><strong>Heat Output</strong></td><td>250–600 BTU/hr (strains office HVAC)</td><td><30 BTU/hr (negligible thermal load)</td></tr>
              <tr><td><strong>Acoustic Noise</strong></td><td>Noisy (CPU fan, GPU fan, PSU fan)</td><td>Completely silent (solid-state fanless)</td></tr>
              <tr><td><strong>Average Lifespan</strong></td><td>3 to 4 years</td><td><strong>7 to 10+ years</strong></td></tr>
              <tr><td><strong>Security & Maintenance</strong></td><td>Local patch updates, vulnerable to USB data theft</td><td>Centralized server patching, zero local data leakage risk</td></tr>
              <tr><td><strong>Annual Energy (1000 seats)</strong></td><td>~300,000 kWh/yr</td><td>~30,000 kWh/yr (massive operational cost reduction)</td></tr>
            </tbody>
          </table>
          <p><em>Slide Reference: Class 14 Slides 11–16 (Client Virtualization & Energy Efficiency).</em></p>
        </div>"""
    },
    {
        "id": "EQB-14-03",
        "class_id": 14,
        "class_name": "Green Computing",
        "topic": "Toxic Chemical Constituents in E-Waste",
        "category": "Match the Following",
        "exams": [
            {"paper": "EST End Exam 2024", "section": "Section I, Q1", "marks": "5M"},
            {"paper": "End Exam 2022", "section": "Section I, Q(A)", "marks": "5M"},
            {"paper": "End Exam 2018", "section": "Part II, Q3", "marks": "2M"},
            {"paper": "End Exam 2023", "section": "Section I, Q2", "marks": "2M"}
        ],
        "marks": "2M – 5M",
        "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
        "prompt": "Match and explain why e-waste is hazardous by detailing the toxic chemical constituents in: (1) Printed circuit boards, (2) Batteries, (3) Capacitors/transformers, (4) Switches/flat-screen monitors, (5) Cable coatings.",
        "key_answer_points": """<ul>
          <li><strong>1. Printed Circuit Boards (PCBs):</strong> <strong>Lead (solder) & Cadmium</strong>, along with toxic <strong>Brominated Flame Retardants (BFRs / PBDEs)</strong> that leach into groundwater.</li>
          <li><strong>2. Computer Batteries:</strong> <strong>Cadmium (Ni-Cd), Lithium, Nickel & Cobalt</strong>; causes severe renal toxicity, lung damage, and fire hazards.</li>
          <li><strong>3. Capacitors & Old Transformers:</strong> <strong>Poly Chlorinated Bi-phenyls (PCBs)</strong>; persistent bioaccumulative organic pollutants (POPs) that act as potent endocrine disruptors and human carcinogens.</li>
          <li><strong>4. Switches & Flat Screen Monitors:</strong> <strong>Mercury</strong>; used in cold-cathode fluorescent backlights (CCFL) and tilt position switches; potent neurotoxin attacking the central nervous system.</li>
          <li><strong>5. Cable Insulation / Wire Coatings:</strong> <strong>Poly Vinyl Chloride (PVC)</strong>; plasticized with toxic endocrine-disrupting phthalates; releases deadly polychlorinated dibenzo-dioxins and furans when incinerated openly.</li>
        </ul>""",
        "detailed_answer": """<div class="detailed-body">
          <p><strong>Toxicology of Electronic Waste:</strong> Electronic devices represent only 2% of the global municipal solid waste stream by weight, but account for over <strong>70% of total heavy metals</strong> in landfills. Informal e-waste recycling (acid-leaching and open burning in places like Guiyu, China and Agbogbloshie, Ghana) causes catastrophic ecotoxicological damage.</p>
          <h4>Component-Pollutant Toxicological Mapping</h4>
          <table class="exam-table">
            <thead><tr><th>Computer Component</th><th>Hazardous Chemical Constituent</th><th>Human Health & Environmental Hazard</th></tr></thead>
            <tbody>
              <tr><td><strong>Printed Circuit Boards</strong></td><td>Lead ($\text{Pb}$) solder, Cadmium ($\text{Cd}$), BFRs</td><td>Neurodevelopmental impairment in children, acute renal failure; endocrine disruption from flame retardants.</td></tr>
              <tr><td><strong>Computer Batteries</strong></td><td>Cadmium, Lithium, Cobalt</td><td>Itai-Itai disease (severe bone softening), kidney proximal tubular damage; reactive lithium water contamination.</td></tr>
              <tr><td><strong>Capacitors / Transformers</strong></td><td>Polychlorinated Biphenyls (PCBs)</td><td>Resistant to environmental degradation; biomagnifies across aquatic food webs; liver cirrhosis and chloracne.</td></tr>
              <tr><td><strong>Switches & Flat Screens</strong></td><td>Elemental Mercury ($\text{Hg}$)</td><td>Minamata-type neurological symptoms, sensory loss, motor impairment, and congenital fetal brain damage.</td></tr>
              <tr><td><strong>Cable Insulation / Coatings</strong></td><td>Polyvinyl Chloride (PVC) + Phthalates</td><td>Releases 2,3,7,8-TCDD (deadly dioxin) upon open wire burning; bioaccumulates in breast milk and adipose tissue.</td></tr>
            </tbody>
          </table>
          <p><em>Slide Reference: Class 14 Slides 17–22 (E-Waste Toxics & RoHS).</em></p>
        </div>"""
    },
    {
        "id": "EQB-14-04",
        "class_id": 14,
        "class_name": "Green Computing",
        "topic": "Basel Convention & Transboundary E-Waste",
        "category": "Short Definition",
        "exams": [
            {"paper": "EST End Exam 2024", "section": "Section II, Q(a)", "marks": "1M"},
            {"paper": "End Exam 2023", "section": "Section I, Q1(e)", "marks": "1M"},
            {"paper": "End Exam 2022", "section": "Section III, Q12", "marks": "1M"}
        ],
        "marks": "1M",
        "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
        "prompt": "What is the Basel Convention? Explain its core objective, regulatory mechanisms, and why it was formulated to stop transboundary dumping of hazardous e-waste in developing nations.",
        "key_answer_points": """<ul>
          <li><strong>Official Title & Adoption:</strong> <strong>Basel Convention on the Control of Transboundary Movements of Hazardous Wastes and Their Disposal</strong>; adopted on 22 March 1989 in Basel, Switzerland; entered into force in 1992 under UNEP.</li>
          <li><strong>Core Objective:</strong> To strictly protect human health and the environment against the adverse effects of hazardous chemical and toxic electronic wastes by curbing their international transboundary shipments.</li>
          <li><strong>Three Pillars:</strong>
            <br>1. Reduction of hazardous waste generation at the source.
            <br>2. Promotion of domestic treatment and disposal as close to the place of generation as possible ('Proximity Principle').
            <br>3. Strict control, prior informed consent (PIC), and total prohibition of exporting hazardous wastes from OECD developed nations to developing countries (Global South).</li>
          <li><strong>E-Waste Context:</strong> Formulated to halt 'toxic colonialism'—where wealthy industrialized nations evade expensive domestic recycling costs by disguising hazardous obsolete electronics as 'charitable donations' or 'reusable second-hand goods' shipped to African and Asian scrap dumps.</li>
        </ul>""",
        "detailed_answer": """<div class="detailed-body">
          <p><strong>Historical Impetus (Toxic Colonialism):</strong> In the 1980s, tightening environmental regulations in North America and Western Europe dramatically increased hazardous waste disposal costs. Corrupt waste brokers began loading freighters with toxic chemical sludge and incinerator ash to dump in West Africa (e.g., Koko, Nigeria incident) for a fraction of the cost.</p>
          <h4>Key Mechanisms: Prior Informed Consent & The Basel Ban Amendment</h4>
          <ul>
            <li><strong>Prior Informed Consent (PIC) Procedure:</strong> Transboundary movement can only take place if the exporting state notifies authorities in the importing country and obtains written authorization beforehand, demonstrating the importing facility has environmentally sound management (ESM) capabilities.</li>
            <li><strong>The Basel Ban Amendment:</strong> Completely prohibits all exports of hazardous wastes (including non-functional e-waste) from Annex VII countries (OECD, EU, Liechtenstein) to non-Annex VII countries (developing nations) for any purpose, including recycling.</li>
          </ul>
          <p><em>Slide Reference: Class 14 Slides 23–26 (International Hazardous Waste Treaties).</em></p>
        </div>"""
    },
    {
        "id": "EQB-14-05",
        "class_id": 14,
        "class_name": "Green Computing",
        "topic": "Moore's Law & Electronic Obsolescence",
        "category": "Short Definition",
        "exams": [
            {"paper": "EST End Exam 2024", "section": "Section II, Q(e)", "marks": "1M"},
            {"paper": "End Exam 2023", "section": "Section I, Q1(a)", "marks": "1M"}
        ],
        "marks": "1M – 2M",
        "importance": "HIGH (⭐⭐⭐⭐)",
        "prompt": "What is Moore's Law? Discuss its unintended and catastrophic environmental consequences on electronic product replacement cycles and global e-waste generation.",
        "key_answer_points": """<ul>
          <li><strong>Definition of Moore's Law:</strong> Empirical observation made by Intel co-founder Gordon Moore in 1965 stating that the <strong>number of transistors packed onto a microchip doubles approximately every two years</strong> while the relative cost of computers is halved.</li>
          <li><strong>Accelerated Technological Obsolescence:</strong> Unintended consequence: computers, smartphones, and peripherals are rendered functionally 'outdated' every 24 to 36 months, even when physical hardware components remain in perfect working order.</li>
          <li><strong>Culture of Planned Obsolescence:</strong> Software operating systems and applications bloat to consume exponential chip resources (Wirth's Law), actively dropping legacy hardware support and driving aggressive consumer upgrade cycles.</li>
          <li><strong>E-Waste Surge:</strong> Has fueled an unprecedented global e-waste tsunami exceeding <strong>50 to 60 million metric tonnes annually</strong> worldwide, with <20% collected and documented through formal certified recycling channels.</li>
        </ul>""",
        "detailed_answer": """<div class="detailed-body">
          <p><strong>The Double-Edged Sword of Exponential Progress:</strong> While Moore's Law democratized computing power, it fundamentally detached hardware longevity from physical durability. A refrigerator or automobile is engineered to operate for 15–25 years; a smartphone is culturally and digitally obsoleted within 2–3 years.</p>
          <h4>The Triad of Obsolescence in Modern Computing</h4>
          <ol>
            <li><strong>Psychological / Perceived Obsolescence:</strong> Aggressive marketing conventions, aesthetic design shifts, and annual launch spectacles that persuade consumers that a functional device is socially unacceptable.</li>
            <li><strong>Software / Systemic Obsolescence:</strong> Manufacturers terminate operating system security patches, firmware updates, and app store backward-compatibility, forcing users to discard devices whose battery or display is still fully operational.</li>
            <li><strong>Hardware Incompatibility:</strong> Gluing batteries into unibody frames, soldering RAM/storage onto motherboards, and using proprietary pentalobe screws deliberately prevent consumer repairability and component modular upgrades.</li>
          </ol>
          <p><em>Slide Reference: Class 14 Slides 27–30 (Obsolescence & Circular ICT).</em></p>
        </div>"""
    },
    {
        "id": "EQB-14-06",
        "class_id": 14,
        "class_name": "Green Computing",
        "topic": "Environmental Footprint of Smartphone Production",
        "category": "Comprehensive Descriptive",
        "exams": [
            {"paper": "EST End Exam 2024", "section": "Section VI, Q1", "marks": "5M"}
        ],
        "marks": "5M",
        "importance": "HIGH (⭐⭐⭐⭐)",
        "prompt": "Explain the comprehensive life-cycle environmental impact of smartphone and mobile device production, covering mineral extraction (coltan, cobalt, gold), manufacturing energy, embodied carbon, and post-consumer disposal.",
        "key_answer_points": """<ul>
          <li><strong>Heavy Embodied Carbon Upfront:</strong> Over <strong>70% to 80% of a smartphone's lifetime carbon footprint</strong> occurs during initial raw material extraction and cleanroom chip fabrication, before the consumer ever powers on the phone.</li>
          <li><strong>Toxic & Conflict Mineral Extraction:</strong>
            <br>• <strong>Coltan (Tantalum):</strong> Sourced from artisanal mines in the Democratic Republic of Congo (DRC); fuels armed conflict, deforestation of mountain gorilla habitats, and severe soil erosion.
            <br>• <strong>Cobalt:</strong> Mined for lithium-ion battery cathodes in DRC under hazardous conditions involving toxic dust inhalation and child labor.
            <br>• <strong>Gold & Copper:</strong> Extracted via toxic cyanide heap leaching and mercury amalgamation, releasing toxic tailings into river ecosystems.
            <br>• <strong>Rare Earth Elements (Neodymium, Dysprosium):</strong> Used in vibration motors and speakers; refining produces vast radioactive thorium waste ponds.</li>
          <li><strong>Cleanroom Energy & Ultrapure Water:</strong> Fabricating a single 2-gram microchip requires <strong>32 kilograms of water, 1.6 kilograms of fossil fuels and chemicals, and 700 grams of gases</strong> in ultra-clean fabrication facilities.</li>
          <li><strong>Short Lifecycles & Dismal Recycling:</strong> Global average smartphone replacement rate is only 22–30 months, with <strong>less than 15% of phones recycled</strong>; the rest are hoarded in drawers or dumped in municipal incinerators.</li>
        </ul>""",
        "detailed_answer": """<div class="detailed-body">
          <p><strong>The Paradox of Miniaturization:</strong> Smartphones appear lightweight (~180–220 grams), yet their ecological backpack (the total quantity of natural material excavated and consumed to produce the unit) exceeds <strong>over 70 kilograms of raw materials per device</strong> (a 350:1 material multiplier ratio).</p>
          <h4>Life-Cycle Assessment (LCA) Breakdown of a Smartphone</h4>
          <table class="exam-table">
            <thead><tr><th>Life-Cycle Stage</th><th>Environmental Impacts</th><th>Key Toxins / Resources</th></tr></thead>
            <tbody>
              <tr><td><strong>Mining & Smelting</strong></td><td>Deforestation, artisanal acid mine drainage, human rights violations in conflict zones</td><td>Coltan/Tantalum, Cobalt, Gold, Silver, Rare Earths, Indium (touchscreen)</td></tr>
              <tr><td><strong>Semiconductor Fabrication</strong></td><td>Intense electrical power consumption, fluorinated greenhouse gas emissions ($\text{SF}_6, \text{NF}_3$)</td><td>Ultrapure water (UPW), hydrofluoric acid, toxic etching solvents</td></tr>
              <tr><td><strong>Consumer Use Phase</strong></td><td>Smallest footprint (~15–20% of lifetime carbon); daily grid electricity charging</td><td>Grid carbon intensity</td></tr>
              <tr><td><strong>End-of-Life Disposal</strong></td><td>Landfill leachate contamination, burning cables, low recovery of precious metals</td><td>Lead solder, brominated flame retardants, lithium battery fire hazards</td></tr>
            </tbody>
          </table>
          <p><em>Slide Reference: Class 14 Slides 31–36 (Smartphones & Ecological Footprint).</em></p>
        </div>"""
    },
    {
        "id": "EQB-14-07",
        "class_id": 14,
        "class_name": "Green Computing",
        "topic": "Data Center Power Usage Effectiveness (PUE)",
        "category": "Comprehensive Descriptive",
        "exams": [
            {"paper": "General Syllabus & End Exam 2019", "section": "Section VI", "marks": "3M"}
        ],
        "marks": "3M",
        "importance": "HIGH (⭐⭐⭐⭐)",
        "prompt": "Define Power Usage Effectiveness (PUE) in data center engineering. What is the ideal PUE, how is it calculated, and what architectural strategies lower PUE in hyperscale facilities?",
        "key_answer_points": """<ul>
          <li><strong>Definition of PUE:</strong> Power Usage Effectiveness is the globally accepted standard metric established by The Green Grid to evaluate the energy efficiency of a data center infrastructure.</li>
          <li><strong>Mathematical Formula:</strong>
            <div class="formula-box">$$\\text{PUE} = \\frac{\\text{Total Facility Power Consumption}}{\\text{IT Equipment Power Consumption}}$$</div>
            Where <em>Total Facility Power</em> includes IT servers, networking, plus overhead power (cooling chillers, HVAC fans, UPS power converters, transformers, lighting).</li>
          <li><strong>Ideal Value & Industry Benchmarks:</strong>
            <br>• The theoretical ideal PUE is exactly <strong>1.0</strong> (indicating 100% of incoming electricity goes directly to computing, with zero cooling/overhead waste).
            <br>• Legacy enterprise data centers typically average an inefficient <strong>1.8 to 2.0</strong> (meaning almost half the power is wasted on air conditioning).
            <br>• Modern hyperscale facilities (Google, Microsoft, Meta) achieve state-of-the-art PUEs of <strong>1.10 to 1.15</strong>.</li>
          <li><strong>Key Strategies to Lower PUE:</strong>
            <br>• <strong>Free-Air Cooling / Economizers:</strong> Siting data centers in sub-arctic regions (Nordics, Iceland) to circulate cold outdoor air without mechanical chillers.
            <br>• <strong>Hot/Cold Aisle Containment:</strong> Physically sealing air ducts to prevent hot server exhaust air from mixing with cold intake air.
            <br>• <strong>AI-Powered HVAC Optimization:</strong> Using neural network algorithms to dynamically adjust chiller cooling setpoints in real time.
            <br>• <strong>Direct Liquid-to-Chip Cooling:</strong> Circulating dielectric fluid or water blocks directly over hot CPUs/GPUs.</li>
        </ul>""",
        "detailed_answer": """<div class="detailed-body">
          <p><strong>Thermodynamics of Computation:</strong> All electrical power consumed by microchips is converted entirely into heat via Joule heating ($P = I^2 R$). If this heat is not continuously evacuated, silicon junctions overheat and enter thermal throttling or permanent silicon damage.</p>
          <h4>Related Metric: Data Center Infrastructure Efficiency (DCiE)</h4>
          <p>DCiE is the mathematical reciprocal of PUE, expressed as a percentage:</p>
          <div class="formula-box">$$\\text{DCiE} = \\frac{1}{\\text{PUE}} \\times 100\\% = \\frac{\\text{IT Equipment Power}}{\\text{Total Facility Power}} \\times 100\\%$$</div>
          <p>A PUE of 2.0 corresponds to a DCiE of 50%, whereas a PUE of 1.1 corresponds to a DCiE of 91%.</p>
          <p><em>Slide Reference: Class 14 Slides 37–42 (Data Center Engineering).</em></p>
        </div>"""
    },
    {
        "id": "EQB-14-08",
        "class_id": 14,
        "class_name": "Green Computing",
        "topic": "Sustainable Computer Hardware Architectures",
        "category": "Comprehensive Descriptive",
        "exams": [
            {"paper": "End Exam 2019", "section": "Section VI, Q3", "marks": "4M"}
        ],
        "marks": "4M",
        "importance": "MEDIUM (⭐⭐⭐)",
        "prompt": "Describe two computer hardware designs built specifically on the sustainable concept of green computing (e.g., fit-PC, Raspberry Pi, OLPC XO-1, Sun RAY).",
        "key_answer_points": """<ul>
          <li><strong>1. The fit-PC Architecture:</strong>
            <br>• Ultra-compact miniature PC engineered by CompuLab enclosed in an aluminum chassis that acts as a giant passive heat sink.
            <br>• Consumes only <strong>5W to 8W of electricity</strong> under full processing load (less than a single standard LED light bulb, saving 95% power over traditional 150W desktop towers).
            <br>• Fanless, silent, 100% solid-state design eliminates moving mechanical parts, extending operational lifespan to >10 years.</li>
          <li><strong>2. OLPC XO-1 (One Laptop Per Child):</strong>
            <br>• Engineered by MIT Media Lab (Nicholas Negroponte) for off-grid education in developing rural regions.
            <br>• Power consumption of just <strong>2W to 5W</strong>, designed to be recharged using an integrated solar panel, foot pump, or hand-crank generator.
            <br>• Features an innovative dual-mode transflective liquid-crystal display (readable in harsh, direct equatorial sunlight without power-hungry backlights) and an impact-resistant, non-toxic, recyclable plastic casing.</li>
          <li><strong>Alternate: Raspberry Pi:</strong> Single-board ARM-based computer running on 3W–5W powered via a standard 5V micro-USB phone charger with minimal embodied material footprint.</li>
        </ul>""",
        "detailed_answer": """<div class="detailed-body">
          <p><strong>Design Philosophy:</strong> Traditional personal computers are notoriously over-provisioned for everyday office and educational tasks. Sustainable architectures match silicon compute capabilities directly to the operational profile, eliminating superfluous silicon real-estate and power-hungry cooling fans.</p>
          <h4>Technical Highlights</h4>
          <ul>
            <li><strong>Fit-PC:</strong> Leveraged low-voltage x86 processors with deep C-state sleep capabilities. The entire motherboard is smaller than a paperback book, radically cutting the embodied copper, gold, and fiberglass PCB footprint.</li>
            <li><strong>OLPC XO-1:</strong> Built with mesh networking protocols allowing clusters of laptops to share a single satellite Internet uplink without expensive networking towers, enabling off-grid digital education with zero carbon grid infrastructure.</li>
          </ul>
          <p><em>Slide Reference: Class 14 Slides 43–46 (Green Hardware Exemplars).</em></p>
        </div>"""
    },
    {
        "id": "EQB-14-09",
        "class_id": 14,
        "class_name": "Green Computing",
        "topic": "Indoor Air Quality & Ventilation Measurement",
        "category": "Comprehensive Descriptive",
        "exams": [
            {"paper": "EST End Exam 2024", "section": "Section V, Q3", "marks": "2M"},
            {"paper": "End Exam 2023", "section": "Section II, Q2–3", "marks": "4M"},
            {"paper": "End Exam 2022", "section": "Section X, Q(c)", "marks": "5M"}
        ],
        "marks": "2M – 5M",
        "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
        "prompt": "How is ventilation measured in mechanically ventilated HVAC buildings versus naturally ventilated buildings? Explain Air Changes per Hour (ACH), the tracer gas decay method (SF6/CO2), and the ASHRAE steady-state infiltration model Q = G / (Ci - Ca).",
        "key_answer_points": """<ul>
          <li><strong>Air Changes per Hour (ACH):</strong> Measure of the air volume added to or removed from a space divided by the total room volume: $\\text{ACH} = \\frac{60 \\cdot Q}{V}$ (where $Q$ is airflow rate in CFM and $V$ is volume).
            <br>• Air-tight modern green buildings: 0.1 to 0.2 ACH (requires mechanical ventilation to prevent pollutant accumulation).
            <br>• Leaky older buildings: 2.0 to 3.0 ACH (high infiltration, massive heating/cooling energy loss).</li>
          <li><strong>Naturally Ventilated Buildings (Infiltration Measurement):</strong>
            <br>• <strong>Tracer Gas Decay Technique:</strong> A non-reactive, harmless tracer gas (such as sulfur hexafluoride $\\text{SF}_6$ or inert nitrous oxide) is injected and mixed uniformly into room air. Gas concentration is monitored over time as it decays via exfiltration, calculated by the logarithmic decay equation: $C(t) = C_0 e^{-\\text{ACH} \\cdot t}$.</li>
          <li><strong>Mechanically Ventilated HVAC Buildings (ASHRAE Model):</strong>
            <br>• Uses metabolic carbon dioxide ($\text{CO}_2$) exhaled by human occupants as a surrogate index for ventilation sufficiency.
            <br>• <strong>ASHRAE Steady-State Ventilation Formula:</strong>
            <div class="formula-box">$$Q = \\frac{G}{C_i - C_a}$$</div>
            Where $Q$ = Outdoor airflow rate per person; $G$ = Rate of $\\text{CO}_2$ generation per person (~0.005 L/s at rest); $C_i$ = Indoor steady-state $\\text{CO}_2$ concentration; $C_a$ = Ambient outdoor $\\text{CO}_2$ concentration (~420 ppm).
            <br>• <strong>ASHRAE Standard 62.1 Benchmark:</strong> Mandates minimum ventilation rate of <strong>8 Liters/second per person</strong> to maintain indoor $\text{CO}_2$ concentration below <strong>700 ppm above outdoor ambient</strong> (typically $<1,000\\text{ ppm}$).</li>
        </ul>""",
        "detailed_answer": """<div class="detailed-body">
          <p><strong>Sick Building Syndrome (SBS):</strong> In the wake of the 1970s energy crises, buildings were sealed to conserve heating and air conditioning energy. However, inadequate fresh air exchange trapped VOCs, radon, and bioeffluents, causing headaches, dizziness, and cognitive impairment among occupants.</p>
          <h4>Mathematical Derivation of the ASHRAE Formula</h4>
          <p>At steady-state equilibrium, the rate of $\text{CO}_2$ generated by building occupants must equal the rate of $\text{CO}_2$ removed via ventilation exhaust:</p>
          <div class="formula-box">$$G = Q \\times (C_i - C_a) \\implies Q = \\frac{G}{C_i - C_a}$$</div>
          <p>If indoor $\text{CO}_2$ levels rise to 2,000 ppm, it indicates acute hypoventilation ($Q$ is dangerously low), causing drowsiness and impaired executive decision-making. Modern demand-controlled ventilation (DCV) modulates fresh air dampers automatically based on real-time NDIR $\text{CO}_2$ sensor telemetry.</p>
          <p><em>Slide Reference: Class 14 Slides 47–52 (IAQ & Building Physics).</em></p>
        </div>"""
    },
    {
        "id": "EQB-14-10",
        "class_id": 14,
        "class_name": "Green Computing",
        "topic": "Indoor Air Pollutants & Source Isolation",
        "category": "Comprehensive Descriptive",
        "exams": [
            {"paper": "EST End Exam 2024", "section": "Section I(B) & III(a)", "marks": "6M"},
            {"paper": "End Exam 2023", "section": "Section IV, Q1", "marks": "4M"},
            {"paper": "End Exam 2022", "section": "Section I(D) & VI(a)", "marks": "6M"}
        ],
        "marks": "4M – 6M",
        "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
        "prompt": "Identify the 5 most dangerous indoor air pollutants and their source materials (asbestos, formaldehyde, p-dichlorobenzene, methylene chloride, mold/bacteria). Explain the Source Isolation Strategy with real-world building examples.",
        "key_answer_points": """<ul>
          <li><strong>Top 5 Indoor Air Pollutants & Source Materials:</strong>
            <br>1. <strong>Asbestos:</strong> Sourced from degraded <em>pipe insulation, fireproofing spray, and acoustic ceiling tiles</em>; inhaled microscopic fibers cause incurable asbestosis, lung cancer, and mesothelioma.
            <br>2. <strong>Formaldehyde / Chloroform:</strong> Sourced from <em>particleboard furniture, pressed-wood adhesives, carpets, and urea-formaldehyde foam insulation</em>; eye/throat irritation and known human nasopharyngeal carcinogen.
            <br>3. <strong>Para-dichlorobenzene (p-DCB):</strong> Sourced from <em>air fresheners, mothballs, and urinal toilet deodorizer blocks</em>; liver toxicity and potential carcinogen.
            <br>4. <strong>Methylene Chloride (Methyl Chloride):</strong> Sourced from <em>paint strippers, solvent thinners, and degreasing agents</em>; metabolized in liver into carbon monoxide, causing central nervous system depression.
            <br>5. <strong>Mold & Bacteria (Microbial Contaminants):</strong> Sourced from <em>damp heating and cooling ducts, uncleaned HVAC drip pans, and water-damaged gypsum drywall</em>; triggers severe asthma attacks and hypersensitivity pneumonitis.</li>
          <li><strong>Source Isolation Strategy:</strong>
            <br>• Engineering control that physically isolates pollutant-generating activities or equipment in dedicated, enclosed rooms maintained under <strong>negative air pressure</strong> relative to surrounding office areas.
            <br>• Dedicated 100% direct exhaust ventilation to the outdoor building exterior (zero air recirculation back into general office HVAC).
            <br>• <strong>Real-World Examples:</strong> Photocopier/high-volume laser printing rooms (ozone and ultrafine toner particles), commercial cafeteria food-preparation kitchens, chemical custodial closets, and restroom plumbing chases.</li>
        </ul>""",
        "detailed_answer": """<div class="detailed-body">
          <p><strong>The EPA Indoor Environment Assessment:</strong> According to the US Environmental Protection Agency (EPA), indoor levels of pollutants may be <strong>2 to 5 times (and occasionally >100 times) higher</strong> than outdoor air levels. Since urban humans spend ~90% of their lives indoors, indoor air quality (IAQ) is a critical public health determinant.</p>
          <h4>Hierarchical Approaches to IAQ Control</h4>
          <ol>
            <li><strong>Source Removal / Substitution:</strong> The most effective engineering step—banning asbestos, specifying zero-VOC paints, and purchasing formaldehyde-free furniture certified by GREENGUARD.</li>
            <li><strong>Source Isolation:</strong> Enclosing emission sources (e.g. print copy centers). By exhausting air directly outside at a higher volume than supply air, the room pressure drops below surrounding corridors ($P_{\text{room}} < P_{\text{corridor}}$). Whenever doors open, air rushes <em>inward</em> rather than allowing toxic ozone or VOC fumes to escape into employee cubicles.</li>
            <li><strong>Dilution Ventilation:</strong> Increasing outdoor air exchange rates via HVAC economizers.</li>
            <li><strong>Air Purification:</strong> High-Efficiency Particulate Air (HEPA) filters (trapping 99.97% of particles down to 0.3 microns) combined with activated carbon beds to adsorb gaseous VOCs.</li>
          </ol>
          <p><em>Slide Reference: Class 14 Slides 53–58 (IAQ Sourcing & Engineering Controls).</em></p>
        </div>"""
    }
]
