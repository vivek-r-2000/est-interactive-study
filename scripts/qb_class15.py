# Class 15: Green Engineering Question Bank
class_15_questions = [
    {
        "id": "EQB-15-01",
        "class_id": 15,
        "class_name": "Green Engineering",
        "topic": "The 12 Principles of Green Engineering",
        "category": "Comprehensive Descriptive",
        "exams": [
            {"paper": "EST End Exam 2024", "section": "Section VI, Q2", "marks": "5M"},
            {"paper": "End Exam 2023", "section": "Section III, Q2", "marks": "4M"},
            {"paper": "End Exam 2019", "section": "Section VII, Q2", "marks": "3M"},
            {"paper": "End Exam 2018", "section": "Part III, Q2", "marks": "6M"}
        ],
        "marks": "3M – 6M",
        "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
        "prompt": "List and detail the 12 Principles of Green Engineering (Anastas & Zimmerman). Explain with concrete examples: (i) Inherent Rather Than Circumstantial, (ii) Conserve Complexity, (iii) Minimize Material Diversity, and (iv) Integrate Material and Energy Flows.",
        "key_answer_points": """<ul>
          <li><strong>Origin:</strong> Formulated by Dr. Paul Anastas and Dr. Julie Zimmerman (2003) to guide engineers in designing products, processes, and systems that are economically viable while minimizing environmental and human health risks.</li>
          <li><strong>The 12 Principles of Green Engineering:</strong>
            <br>1. <strong>Inherent Rather Than Circumstantial:</strong> Ensure all materials and energy inputs/outputs are non-hazardous inherently rather than relying on safety equipment to contain hazardous conditions.
            <br>2. <strong>Prevention Rather Than Treatment:</strong> Prevent waste generation rather than treating or cleaning up waste after it is created.
            <br>3. <strong>Design for Separation:</strong> Design operations for easy separation and purification (avoiding entraining difficult chemical mixtures).
            <br>4. <strong>Maximize Efficiency:</strong> Maximize mass, energy, space, and time efficiency throughout production.
            <br>5. <strong>Output-Pulled Versus Input-Pushed:</strong> Apply Le Chatelier's principle and 'just-in-time' production to minimize storage and waste.
            <br>6. <strong>Conserve Complexity:</strong> Preserve the structural and chemical complexity of materials rather than degrading high-entropy goods into low-value trash.
            <br>7. <strong>Durability Rather Than Immortality:</strong> Design products for targeted operational life without creating persistent bioaccumulative forever toxins.
            <br>8. <strong>Meet Need, Minimize Excess:</strong> Size capacity to actual demand without over-designing unnecessary features or excess margins.
            <br>9. <strong>Minimize Material Diversity:</strong> Standardize on uniform mono-materials to streamline disassembly and recycling.
            <br>10. <strong>Integrate Material and Energy Flows:</strong> Interconnect industrial processes so one facility's byproduct becomes another's feedstock.
            <br>11. <strong>Design for Commercial 'Afterlife':</strong> Engineer components for second-life reuse and closed-loop remanufacturing.
            <br>12. <strong>Renewable Rather Than Depleting:</strong> Use biological and renewable inputs rather than depleting fossil or virgin mineral reserves.</li>
          <li><strong>Detailed Exemplars:</strong>
            <br>• <em>Inherent Rather Than Circumstantial:</em> Replacing toxic organic solvents with supercritical $\text{CO}_2$ or water in semiconductor wafer cleaning, eliminating explosive hazards.
            <br>• <em>Conserve Complexity:</em> Reusing intact silicon wafers or composite timber beams instead of pulverizing them into low-grade filler.
            <br>• <em>Minimize Material Diversity:</em> Manufacturing a car bumper from a single recyclable polyolefin plastic rather than a glued composite of PVC, ABS, and metal.
            <br>• <em>Integrate Flows:</em> Kalundborg industrial symbiosis where surplus steam from a power plant warms fish farms and runs pharmaceutical fermentation.</li>
        </ul>""",
        "detailed_answer": """<div class="detailed-body">
          <p><strong>Paradigm Shift:</strong> Traditional environmental engineering focused on 'end-of-pipe' pollution treatment—building massive smokestack scrubbers, effluent clarifiers, and secure landfills to contain toxic waste after generation. Green engineering redesigns molecular and systems synthesis so waste is impossible by design.</p>
          <h4>Deep Analysis of Core Focus Principles</h4>
          <ol>
            <li><strong>Inherent Rather Than Circumstantial:</strong> Conventional safety relies on circumstantial barriers—pressure relief valves, chemical suits, secondary containment berms. If power fails or an operator makes an error (as in Bhopal), disaster strikes. Designing an inherently benign process means using ambient temperatures, non-toxic feedstocks, and non-flammable solvents so that catastrophic failure is physically impossible.</li>
            <li><strong>Conserve Complexity:</strong> Nature expends immense energy and biological information synthesizing intricate polymers (like wood, silk, natural resins). When products reach end-of-life, burning them or shredding them into amorphous filler destroys that thermodynamic order. Conserving complexity means reclaiming sub-assemblies and keeping polymers intact.</li>
            <li><strong>Minimize Material Diversity:</strong> Modern consumer electronics frequently combine dozens of incompatible polymers and metal alloys in a single product, glued together. Because sorting them is economically impossible, they end up in shredders. Designing products with single-polymer families (mono-materials) makes automated sorting and 100% closed-loop recycling trivial.</li>
            <li><strong>Integrate Material and Energy Flows:</strong> In nature, ecosystems produce zero net waste: the waste of one trophic organism is the vital nutrient of another. Industrial systems must mirror natural food webs through industrial ecology.</li>
          </ol>
          <p><em>Slide Reference: Class 15 Slides 4–12 (The 12 Green Engineering Principles).</em></p>
        </div>"""
    },
    {
        "id": "EQB-15-02",
        "class_id": 15,
        "class_name": "Green Engineering",
        "topic": "Differentiate: Green Computing vs Green Engineering",
        "category": "Differentiate Between",
        "exams": [
            {"paper": "EST End Exam 2024", "section": "Section IV, Q(e)", "marks": "2M"},
            {"paper": "End Exam 2022", "section": "Section VII, Q(d)", "marks": "2M"}
        ],
        "marks": "2M",
        "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
        "prompt": "Differentiate clearly between Green Computing and Green Engineering in terms of engineering domain, scope of application, methodologies, and overarching sustainability targets.",
        "key_answer_points": """<ul>
          <li><strong>Domain & Scope:</strong>
            <br>• <em>Green Computing:</em> Narrowly focused on <strong>Information & Communications Technology (ICT)</strong>—specifically computers, data centers, microprocessors, software algorithms, telecommunication networks, and e-waste.
            <br>• <em>Green Engineering:</em> Broad, overarching discipline encompassing <strong>all engineering branches</strong> (chemical, mechanical, civil, electrical, materials) applied across civil infrastructure, manufacturing factories, chemical plants, transportation, and industrial ecosystems.</li>
          <li><strong>Core Methodologies:</strong>
            <br>• Green Computing focuses on power usage effectiveness (PUE), sleep-state management, virtualization, thin client architectures, dynamic frequency scaling, and RoHS compliance.
            <br>• Green Engineering focuses on Anastas's 12 Principles: life-cycle assessment (LCA), mass/energy conservation, industrial symbiosis (byproduct synergy), renewable feedstocks, and design for disassembly.</li>
          <li><strong>Target Metric:</strong>
            <br>• Green Computing targets minimizing kilowatt-hours per compute cycle, reducing data center cooling loads, and curbing heavy metal e-waste.
            <br>• Green Engineering targets decoupling societal prosperity from total resource extraction, toxics release, and thermodynamic entropy across all industrial sectors.</li>
        </ul>""",
        "detailed_answer": """<div class="detailed-body">
          <p><strong>System Hierarchy:</strong> Green Computing can be understood as an essential, high-technology specialization <em>within</em> the broader umbrella of Green Engineering, applying green design principles specifically to digital architectures.</p>
          <h4>Structured Comparison Matrix</h4>
          <table class="exam-table">
            <thead><tr><th>Dimension</th><th>Green Computing</th><th>Green Engineering</th></tr></thead>
            <tbody>
              <tr><td><strong>Disciplinary Home</strong></td><td>Computer Science, Computer Engineering, IT</td><td>Chemical, Mechanical, Civil, Industrial, Environmental Engineering</td></tr>
              <tr><td><strong>Primary Assets Managed</strong></td><td>CPUs, GPUs, servers, optical fiber, silicon wafers, software code</td><td>Chemical reactors, power grids, bridges, supply chains, cement kilns, consumer goods</td></tr>
              <tr><td><strong>Key Principles / Codes</strong></td><td>Energy Star, RoHS, Basel Convention, WEEE Directive</td><td>12 Principles of Green Engineering, ISO 14040 (LCA), Cradle-to-Cradle (C2C)</td></tr>
              <tr><td><strong>Operational Strategies</strong></td><td>VDI virtualization, dark mode UI, server consolidation, renewable-powered cloud</td><td>Industrial symbiosis, supercritical solvents, waste heat co-generation, mono-materials</td></tr>
            </tbody>
          </table>
          <p><em>Slide Reference: Class 15 Slides 13–15 (Disciplinary Seams).</em></p>
        </div>"""
    },
    {
        "id": "EQB-15-03",
        "class_id": 15,
        "class_name": "Green Engineering",
        "topic": "Industrial Symbiosis: Kalundborg Eco-Industrial Park",
        "category": "Comprehensive Descriptive",
        "exams": [
            {"paper": "End Exam 2022", "section": "Section III, Q1", "marks": "1M"},
            {"paper": "End Exam 2018", "section": "Part III, Q2", "marks": "6M"}
        ],
        "marks": "1M – 6M",
        "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
        "prompt": "What is industrial symbiosis / industrial ecology? Explain how the Kalundborg Eco-Industrial Park in Denmark operationalizes the green engineering principle of 'Integrate Material and Energy Flows'.",
        "key_answer_points": """<ul>
          <li><strong>Industrial Symbiosis Definition:</strong> A collaborative association between diverse, collocated industrial enterprises where the <strong>waste, byproduct, or surplus energy of one facility is utilized directly as the primary raw material or energy feedstock for another</strong>, mimicking natural biological food webs.</li>
          <li><strong>Location & Prominence:</strong> <strong>Kalundborg Eco-Industrial Park in Denmark</strong>—the world's first and premier commercial working model of industrial symbiosis, operating continuously since the 1970s.</li>
          <li><strong>Key Byproduct Exchange Linkages:</strong>
            <br>1. <strong>Asnæs Power Station (Surplus Steam):</strong> Coal/biomass power station pipes residual process steam to the neighboring <strong>Novo Nordisk</strong> insulin fermentation plant and the <strong>Equinor (Statoil)</strong> oil refinery, saving thousands of tonnes of bunker oil.
            <br>2. <strong>Flue Gas Desulfurization (FGD) Gypsum:</strong> Power plant scrubbers react sulfur dioxide exhaust with limestone to produce pure synthetic gypsum ($\text{CaSO}_4\cdot 2\text{H}_2\text{O}$), piped to the adjacent <strong>Gyproc wallboard plant</strong>, completely eliminating the need to quarry open-pit gypsum in Spain.
            <br>3. <strong>Cooling Water Warming:</strong> Warm industrial cooling water from the power plant is directed into a commercial <strong>aquaculture fish farm</strong>, raising thousands of tonnes of trout and turbot in sub-arctic winter conditions.
            <br>4. <strong>Refinery Fuel Gas:</strong> Stripped gas containing sulfur is treated; sulfur is sold to Kemira sulfuric acid factory; clean fuel gas is piped back to power the power station and gypsum kilns.
            <br>5. <strong>Biological Sludge to Agricultural Fertilizer:</strong> Fermentation biomass sludge (*Novogro*) from Novo Nordisk is distributed to hundreds of local Danish farm fields as nutrient-rich organic fertilizer.</li>
        </ul>""",
        "detailed_answer": """<div class="detailed-body">
          <p><strong>Origins:</strong> Unlike government-mandated zoning parks, the Kalundborg symbiosis evolved organically from bottom-up bilateral contracts between plant managers who realized that paying to dump waste was foolish when a neighboring facility could purchase that waste as fuel or raw feedstock.</p>
          <h4>The Multi-Facility Synergy Network</h4>
          <table class="exam-table">
            <thead><tr><th>Waste Originating Facility</th><th>Byproduct / Residue Transferred</th><th>Receiving Facility</th><th>Primary Environmental Benefit</th></tr></thead>
            <tbody>
              <tr><td>Asnæs Power Station</td><td>High-pressure surplus steam</td><td>Novo Nordisk & Statoil Refinery</td><td>Eliminates individual fossil steam boilers; cuts regional $\text{CO}_2$ emissions by 80%.</td></tr>
              <tr><td>Asnæs Power Station</td><td>Scrubber Gypsum ($\text{CaSO}_4$)</td><td>Gyproc Wallboard Factory</td><td>100% replaces mined natural gypsum; saves international shipping emissions.</td></tr>
              <tr><td>Asnæs Power Station</td><td>Warm thermal cooling effluent</td><td>Aquaculture Fish Farms</td><td>Utilizes waste thermal energy; accelerates commercial fish growth without heating costs.</td></tr>
              <tr><td>Statoil Refinery</td><td>Sulfur-rich flue gas</td><td>Kemira Chemical Plant</td><td>Converts dangerous toxic gas into valuable industrial sulfuric acid ($\text{H}_2\text{SO}_4$).</td></tr>
              <tr><td>Novo Nordisk Enzyme Plant</td><td>Fermentation microbial yeast slurry</td><td>Local Danish Farms</td><td>Substitutes synthetic synthetic nitrogen/phosphorus fertilizers on >1,000 hectares.</td></tr>
            </tbody>
          </table>
          <p><em>Slide Reference: Class 15 Slides 16–22 (Kalundborg Industrial Symbiosis).</em></p>
        </div>"""
    },
    {
        "id": "EQB-15-04",
        "class_id": 15,
        "class_name": "Green Engineering",
        "topic": "Denim Manufacturing Environmental Footprint",
        "category": "Comprehensive Descriptive",
        "exams": [
            {"paper": "EST End Exam 2024", "section": "Section VI, Q4", "marks": "5M"},
            {"paper": "End Exam 2023", "section": "Section IV, Q4", "marks": "4M"},
            {"paper": "End Exam 2022", "section": "Section IX, Q(b)", "marks": "3M"},
            {"paper": "End Exam 2019", "section": "Section VII, Q1", "marks": "4M"}
        ],
        "marks": "3M – 5M",
        "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
        "prompt": "Explain in detail the environmental footprint of denim and blue jeans manufacturing, covering freshwater consumption, water pollution from synthetic indigo and mordants, sludge generation, and worker health risks (silicosis).",
        "key_answer_points": """<ul>
          <li><strong>Massive Freshwater Consumption:</strong> Producing a single pair of conventional denim jeans consumes between <strong>7,500 and 10,000 liters of freshwater</strong> (cotton irrigation, yarn spinning, multiple wet-dip dye baths, stone-washing, and finishing).</li>
          <li><strong>Toxic Chemical Pollution (Synthetic Indigo & Mordants):</strong>
            <br>• Indigo dye is insoluble in water; requires toxic chemical reducing agents like <strong>sodium hydrosulfite ($\text{Na}_2\text{S}_2\text{O}_4$) and caustic soda ($\text{NaOH}$)</strong> to chemically convert into soluble 'leuco-indigo'.
            <br>• Industrial fixatives contain toxic heavy-metal mordants (cadmium, chromium, lead, copper). Discharging untreated wastewater turns regional rivers (e.g., Pearl River basin in Xintang, China—the 'Jeans Capital of the World') jet-black or deep blue, depleting dissolved oxygen and killing aquatic life.</li>
          <li><strong>Pumice Stone Sludge & Fiber Lint:</strong> Abrasive stone-washing to achieve a 'vintage faded' look grinds volcanic pumice stones into millions of tonnes of mineral sludge contaminated with dyes, clogging municipal sewer lines.</li>
          <li><strong>Occupational Silicosis:</strong> Workers manually sandblasting dry denim with high-pressure crystalline silica quartz sand inhale microscopic dust particles, causing irreversible, fatal <strong>acute silicosis</strong> of the lungs within months of exposure.</li>
          <li><strong>Green Engineering Fixes:</strong> Transitioning to <strong>ozone gas bleaching</strong>, precision <strong>laser distressing</strong> (completely replacing manual sandblasting), foam-dyeing (99% water reduction), and biological enzymes (cellulases) replacing pumice stones.</li>
        </ul>""",
        "detailed_answer": """<div class="detailed-body">
          <p><strong>The Global Denim Machine:</strong> Over 4 billion pairs of denim jeans are manufactured globally each year. While denim is celebrated as durable workwear, its traditional production chemistry represents one of the most resource-intensive and polluting operations in the global textile industry.</p>
          <h4>Life-Cycle Environmental Breakdown</h4>
          <ol>
            <li><strong>Agricultural Phase (Cotton Cultivation):</strong> Cotton occupies only 2.4% of the world's arable land but consumes 24% of global insecticides and 11% of global pesticides (such as aldicarb and endosulfan). In Central Asia, diverting rivers to irrigate cotton fields triggered the complete ecological desiccation of the Aral Sea.</li>
            <li><strong>Dyeing & Chemical Reduction:</strong> Synthetic indigo ($\text{C}_{16}\text{H}_{10}\text{N}_2\text{O}_2$) requires chemical reduction into soluble leuco-indigo. The resulting effluents are loaded with high chemical oxygen demand (COD), extreme alkalinity (pH 11–12), and sodium sulfates that destroy freshwater ecosystems.</li>
            <li><strong>Worker Health Tragedy (Manual Sandblasting):</strong> In Turkey, Bangladesh, and China, factory workers in unventilated rooms used pneumatic spray guns to blast silica sand against denim jeans to create artificial distressed wear marks. The microscopic silica crystals lacerated lung alveoli, causing rapid-onset pulmonary fibrosis (silicosis) that led to international bans by major brands.</li>
          </ol>
          <h4>Green Engineering Solutions</h4>
          <table class="exam-table">
            <thead><tr><th>Conventional Step</th><th>Environmental Damage</th><th>Green Engineering Replacement</th></tr></thead>
            <tbody>
              <tr><td>Chemical Dye Baths</td><td>7,500L water + sulfurous salts</td><td><strong>Liquid Foam Dyeing:</strong> Uses pressurized nitrogen foam to transfer indigo onto yarn with 99% less water.</td></tr>
              <tr><td>Manual Sandblasting</td><td>Lethal worker silicosis</td><td><strong>Robotic Laser Distressing:</strong> Infrared laser beams vaporize superficial indigo dye in milliseconds with zero dust.</td></tr>
              <tr><td>Pumice Stonewashing</td><td>Volcanic sludge, fabric wear</td><td><strong>Biostonewashing:</strong> Biodegradable fungal cellulase enzymes selectively hydrolyze surface cotton fibrils.</td></tr>
              <tr><td>Chemical Chlorine Wash</td><td>Toxic chlorinated effluents</td><td><strong>Ozone Gas Bleaching:</strong> In-chamber ozone ($\text{O}_3$) oxidizes indigo, reverting naturally back into oxygen ($\text{O}_2$).</td></tr>
            </tbody>
          </table>
          <p><em>Slide Reference: Class 15 Slides 23–29 (Denim Footprint & Clean Textiles).</em></p>
        </div>"""
    },
    {
        "id": "EQB-15-05",
        "class_id": 15,
        "class_name": "Green Engineering",
        "topic": "Life Cycle Assessment (LCA) ISO 14040",
        "category": "Comprehensive Descriptive",
        "exams": [
            {"paper": "General Syllabus & End Exam Questions", "section": "Section VII", "marks": "4M"}
        ],
        "marks": "4M",
        "importance": "HIGH (⭐⭐⭐⭐)",
        "prompt": "What is Life Cycle Assessment (LCA)? Outline the four standardized phases according to ISO 14040 and contrast 'Cradle-to-Grave' with 'Cradle-to-Cradle' design.",
        "key_answer_points": """<ul>
          <li><strong>Definition:</strong> Life Cycle Assessment (LCA) is a standardized, comprehensive methodological tool for systematically assessing the environmental impacts associated with all stages of a commercial product, process, or service across its entire lifespan.</li>
          <li><strong>The 4 Standardized Phases (ISO 14040 / 14044):</strong>
            <br>1. <strong>Goal and Scope Definition:</strong> Defining the system boundaries, target application, functional unit (e.g. 1 pair of jeans, 1 passenger-kilometer, 1 kWh of power), and required data quality.
            <br>2. <strong>Life Cycle Inventory (LCI):</strong> Quantifying all raw material inputs, water, energy consumption, and environmental emissions (to air, water, land) across every stage.
            <br>3. <strong>Life Cycle Impact Assessment (LCIA):</strong> Translating inventory data into specific environmental impact categories (Global Warming Potential, Acidification, Eutrophication, Ozone Depletion, Human Toxicity).
            <br>4. <strong>Interpretation:</strong> Analyzing results, identifying critical ecological 'hotspots', and formulating engineering recommendations.</li>
          <li><strong>Cradle-to-Grave vs Cradle-to-Cradle (C2C):</strong>
            <br>• <em>Cradle-to-Grave:</em> Linear throughput model ($\text{Extract} \rightarrow \text{Produce} \rightarrow \text{Use} \rightarrow \text{Discard in Landfill}$); attempts to make products 'less bad'.
            <br>• <em>Cradle-to-Cradle (C2C):</em> Regenerative, cyclical biomimetic model where industrial materials circulate indefinitely as either <strong>biological nutrients</strong> (safely composted to feed soil) or <strong>technical nutrients</strong> (continuously disassembled and remanufactured without downcycling into trash).</li>
        </ul>""",
        "detailed_answer": """<div class="detailed-body">
          <p><strong>System Boundaries in LCA:</strong> One of the greatest dangers in environmental claims is 'burden shifting'—for example, designing an electric car that has zero tailpipe emissions but whose lithium-cobalt battery manufacturing emits vast carbon and toxic runoff. LCA evaluates the complete global supply chain.</p>
          <h4>The 4 System Boundary Models</h4>
          <ul>
            <li><strong>Cradle-to-Gate:</strong> Tracks emissions from raw material extraction up to the factory gate before consumer transportation.</li>
            <li><strong>Cradle-to-Grave:</strong> Covers raw materials, manufacturing, distribution, consumer operational use, and ultimate landfill or incineration disposal.</li>
            <li><strong>Cradle-to-Cradle (C2C):</strong> Pioneered by chemist Michael Braungart and architect William McDonough; eliminates the very concept of waste by ensuring all post-consumer elements are designed for perpetual closed loops.</li>
          </ul>
          <p><em>Slide Reference: Class 15 Slides 30–35 (LCA Methodologies).</em></p>
        </div>"""
    }
]
