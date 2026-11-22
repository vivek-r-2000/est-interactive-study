"""
Grounded Class 15 Question Bank Module
Strictly audited against official lecture slides: Class-15-Green engineering.pdf (28 slides).
All detailed answers are comprehensive, multi-paragraph, and fully grounded in the official curriculum slides.
"""

def get_class15_grounded_questions():
    return [
        {
            "id": "EQB-15-01",
            "class_id": 15,
            "class_name": "Green Engineering & Industrial Ecology",
            "topic": "Green Engineering Definition & Frameworks",
            "category": "Short Answer & Definitions",
            "exams": [
                {"paper": "End Exam 2018", "section": "Part III, Q1", "marks": "2M"}
            ],
            "marks": "2M",
            "importance": "HIGH (⭐⭐⭐⭐)",
            "prompt": "What is Green engineering?",
            "key_answer_points": "<ul>\n<li><strong>EPA Definition:</strong> <em>\"Green Engineering embraces the concept that decisions to protect human health and the environment can have the greatest impact and cost effectiveness when applied early to the design and development phase of an industrial process or product.\"</em></li>\n<li><strong>Primary Goal:</strong> To incorporate risk-related concepts (hazard minimization, non-toxicity, exposure prevention) into chemical processes and commercial products designed by academia and industry.</li>\n<li><strong>Sustainability Objective:</strong> Conserve natural resources and reduce the lifecycle impacts of processes and products on the natural environment.</li>\n<li><strong>Broad Engineering Domain:</strong> Applied across diverse engineering sectors, including sustainable architecture/housing, green transportation/vehicles, electronic and electrical equipment (computers, mobiles), and industrial manufacturing devices.</li>\n<li><strong>The Sandestin Declaration:</strong> Formulates 9 overarching engineering principles emphasizing holistic systems analysis, life-cycle thinking, inherently benign inputs/outputs, waste prevention, and engaging local communities.</li>\n</ul>",
            "detailed_answer": """<div class=\"detailed-body\">
<p><strong>The Core Paradigm Shift:</strong> Historically, industrial engineering approached environmental protection as an expensive afterthought. Facilities relied on reactive \"end-of-pipe\" pollution controls—such as building taller smokestacks, installing flue gas scrubbers, creating hazardous waste retention ponds, and paying enormous sums for downstream environmental cleanup and legal remediation. <strong>Green Engineering</strong> completely upends this reactive model by embedding ecological constraints, non-toxicity, and resource stewardship directly into the initial blueprint and conceptual design stage.</p>

<h4>1. Official EPA Definition and Risk Incorporation</h4>
<p>According to the United States Environmental Protection Agency (EPA) as cited in the curriculum slides:</p>
<div class=\"formula-box\">
<p style=\"text-align:center; font-style:italic; font-size:1.02rem; margin:0.3rem 0;\">\"Green Engineering embraces the concept that decisions to protect human health and the environment can have the greatest impact and cost effectiveness when applied early to the design and development phase of an industrial process or product.\"</p>
</div>
<p>The EPA framework establishes that the primary objective of Green Engineering is to systematically integrate risk-related concepts—specifically hazard identification, toxicity elimination, and exposure control—into chemical processes, materials synthesis, and physical products developed by academia and industrial manufacturers. By addressing hazards at the molecular and conceptual level, engineers eliminate the physical possibility of catastrophic failure rather than merely trying to contain dangerous conditions with safety valves and protective gear.</p>

<h4>2. Resource Conservation and Sustainability Scope</h4>
<p>Green Engineering is fundamentally defined as the process and design of products aiming to conserve finite natural resources, directly aligning industrial production with planetary sustainability goals. It focuses equally on two complementary fronts:</p>
<ul>
<li><strong>Minimizing Environmental Impact:</strong> Reducing atmospheric emissions, water pollution, solid waste generation, and ecological degradation throughout every stage of product manufacturing and utilization.</li>
<li><strong>Cross-Sector Technological Deployment:</strong> Unlike specialized sub-fields, green engineering is applied across the entire modern engineered landscape. The curriculum specifically identifies its application to:
  <ul>
    <li><em>Sustainable Buildings & Houses:</em> Passive solar orientation, daylighting, natural ventilation, non-toxic building envelopes, and net-zero energy design.</li>
    <li><em>Green Transportation:</em> High-efficiency powertrains, electric/hybrid drivetrains, lightweight materials, and urban public transit integration.</li>
    <li><em>Consumer Products & Electronics:</em> Materials selection, recyclable computing hardware, modular smartphones, low-toxicity plastics, and non-hazardous consumer goods.</li>
    <li><em>Industrial Machinery & Devices:</em> Advanced engineering technologies that drive clean chemical synthesis, separation, and closed-loop manufacturing.</li>
  </ul>
</li>
</ul>

<h4>3. The Sandestin Declaration: Defining Principles</h4>
<p>To establish a universal professional charter, green engineers formulated the Sandestin Green Engineering Principles (curriculum Slide 20), establishing nine foundational directives:</p>
<ol>
<li><strong>Holistic Systems Analysis:</strong> Engineer processes and products holistically, applying comprehensive systems analysis and integrating rigorous environmental impact assessment tools from day one.</li>
<li><strong>Ecosystem & Human Health Protection:</strong> Conserve and improve natural ecosystems while actively safeguarding human health, worker safety, and community well-being.</li>
<li><strong>Life-Cycle Thinking:</strong> Mandate comprehensive cradle-to-grave (and cradle-to-cradle) life-cycle assessment in every engineering activity.</li>
<li><strong>Inherently Safe Inputs & Outputs:</strong> Ensure that all material and energy inputs and outputs are inherently non-toxic, non-hazardous, and environmentally benign.</li>
<li><strong>Resource Depletion Minimization:</strong> Conserve virgin ores, fossil reserves, and clean water tables by prioritizing circular recycling and renewable resources.</li>
<li><strong>Waste Prevention at Source:</strong> Strive uncompromisingly to prevent waste generation rather than treating or managing waste after it is formed.</li>
<li><strong>Local Geography and Cultural Context:</strong> Develop and apply customized engineering solutions that respect and harmonize with local geography, cultural aspirations, and regional resource availability.</li>
<li><strong>Innovation Beyond Dominant Paradigms:</strong> Create engineering solutions beyond established, polluting technologies—aggressively innovating, inventing, and commercializing breakthrough green technologies.</li>
<li><strong>Community & Stakeholder Engagement:</strong> Actively engage local communities, workers, regulators, and civic stakeholders throughout the engineering development lifecycle.</li>
</ol>
<p><em>Slide Reference: Class 15, Slides 4, 5, 20.</em></p>
</div>"""
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
            "key_answer_points": "<ul>\n<li><strong>Scope & Disciplinary Domain:</strong> Green Computing is a focused domain restricted to <em>Information & Communications Technology (ICT)</em>—computers, microprocessors, servers, data centers, networks, and electronic waste; Green Engineering is an umbrella meta-discipline spanning <em>all engineering fields</em> (chemical, civil, mechanical, materials, manufacturing, environmental).</li>\n<li><strong>Governing Frameworks:</strong> Green Computing operates through <em>4 IT lifecycle approaches</em> (Green Design, Green Manufacturing, Green Use, Green Disposal) and Energy Star/RoHS standards; Green Engineering is governed by <em>Paul Anastas & Julie Zimmerman's 12 Principles</em> and the <em>Sandestin Declaration</em>.</li>\n<li><strong>Core Metrics & Focus:</strong> Green Computing measures Power Usage Effectiveness (PUE), compute-per-watt, sleep-state efficiency, server virtualization, and e-waste toxicity; Green Engineering optimizes mass-energy-space-time efficiency, Le Chatelier equilibrium pulling, benign solvent substitution, and industrial symbiosis.</li>\n<li><strong>Systemic Relationship:</strong> Green computing is a specialized application/subdomain of green engineering principles targeted specifically at digital computation infrastructure.</li>\n</ul>",
            "detailed_answer": """<div class=\"detailed-body\">
<p><strong>Systemic Relationship:</strong> While both paradigms share the core objective of environmental sustainability and resource stewardship, they differ fundamentally in disciplinary scope, operational focus, governing frameworks, and implementation scales. <strong>Green Engineering</strong> is the overarching, universal engineering philosophy; <strong>Green Computing</strong> represents the specialized application of these sustainable principles specifically to digital computing hardware, networks, and cloud software ecosystems.</p>

<h4>Direct Comparative Matrix</h4>
<div class=\"table-responsive\">
<table class=\"table table-bordered table-striped\">
<thead class=\"table-dark\">
<tr>
<th style=\"width:22%;\">Dimension</th>
<th style=\"width:39%;\">Green Computing (Class 14)</th>
<th style=\"width:39%;\">Green Engineering (Class 15)</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Core Disciplinary Scope</strong></td>
<td>Narrowly focused on <strong>Information & Communications Technology (ICT)</strong>: computers, personal devices, processors, servers, data centers, networks, and digital peripherals.</td>
<td>Broad meta-discipline encompassing <strong>all branches of engineering</strong>: chemical synthesis, civil architecture, mechanical automotive systems, materials, metallurgy, and industrial production.</td>
</tr>
<tr>
<td><strong>Governing Framework</strong></td>
<td>Governed by the <strong>4 ICT Lifecycle Approaches</strong>: Green Design, Green Manufacturing, Green Use, and Green Disposal (along with Energy Star and EPEAT).</td>
<td>Governed by the <strong>12 Principles of Green Engineering</strong> (Paul Anastas & Julie Zimmerman) and the 9 tenets of the <strong>Sandestin Declaration</strong>.</td>
</tr>
<tr>
<td><strong>Primary Engineering Metrics</strong></td>
<td>Power Usage Effectiveness (PUE), Data Center Infrastructure Efficiency (DCIE), FLOPS-per-watt, idle standby wattage, and RoHS compliance limits.</td>
<td>Mass, energy, space, and time efficiency; atom economy; Le Chatelier reaction yields; toxicity hazard reduction; and industrial mass/energy flow integration.</td>
</tr>
<tr>
<td><strong>Upstream Design Strategy</strong></td>
<td>Designing low-power microarchitectures (ARM big.LITTLE, dark silicon), passive heatsinks, dynamic voltage/frequency scaling (DVFS), and lead-free circuit boards.</td>
<td>Designing inherently benign molecules, non-volatile solvent substitution (eliminating dichloromethane), self-separating chemical reactors, and monomaterial product assemblies.</td>
</tr>
<tr>
<td><strong>Operational / In-Use Focus</strong></td>
<td>Reducing runtime electrical consumption via server virtualization, containerization, cloud consolidation, AI workload throttling, and eco-friendly data center cooling.</td>
<td>Output-pulled reaction kinetics, minimizing parasitic pressure drops, eliminating toxic intermediate reaction steps, and passive building solar/wind capture.</td>
</tr>
<tr>
<td><strong>End-of-Life / Disposal Strategy</strong></td>
<td>Urban mining to reclaim gold, silver, copper, and palladium; certified e-waste recycling; preventing illegal toxic e-waste dumping under the Basel Convention.</td>
<td>Design for commercial afterlife: recovering modular industrial components, conversion of decommissioned factories to housing, and closed-loop industrial symbiosis.</td>
</tr>
<tr>
<td><strong>Slide Examples & Case Studies</strong></td>
<td>Google seawater/free cooling, Facebook Prineville evaporative cooling, RoHS lead-free soldering, and modular upgradeable server blades.</td>
<td>Denim manufacturing pollution abatement, IBM 1-screw PC modularity, Kalundborg industrial symbiosis, One Central Park heliostats, and Bahrain WTC wind turbines.</td>
</tr>
</tbody>
</table>
</div>

<h4>Detailed Analysis of Divergence</h4>
<ol>
<li><strong>Physical Media vs. Multi-Sector Infrastructure:</strong> Green computing deals predominantly with the electron flow, silicon wafer fabrication, magnetic/flash storage, and cooling loops of computational hardware. In contrast, green engineering addresses physical materials at macro and micro scales—from replacing petrochemical dyes in the textile industry (Slide 3) to designing multi-story vertical gardens and wind-funneling skyscrapers (Slides 26–28).</li>
<li><strong>The Subdomain Hierarchy:</strong> When a computer manufacturer redesigns a motherboard to use lead-free solder, eliminate brominated flame retardants, and snap together using a single standardized screw type (Slide 13), it is applying Green Engineering Principle 1 (Inherent Safety), Principle 6 (Conserve Complexity), and Principle 9 (Minimize Material Diversity) to the specific problem of green computing hardware. Thus, green computing is a direct operational offspring of the broader green engineering paradigm.</li>
</ol>
<p><em>Slide Reference: Class 15, Slides 4, 5; Class 14, Slides 4, 5, 6, 8.</em></p>
</div>"""
        },
        {
            "id": "EQB-15-03",
            "class_id": 15,
            "class_name": "Green Engineering & Industrial Ecology",
            "topic": "The 12 Principles of Green Engineering",
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
            "prompt": "Explain the 12 Principles of Green Engineering (Paul Anastas) with concrete examples from the lecture slides, specifically detailing Inherent Safety, Prevention, Design for Separation, Conserve Complexity, Material Diversity, and Industrial Symbiosis.",
            "key_answer_points": "<ul>\n<li><strong>Framework Origin:</strong> Codified by <strong>Paul Anastas and Julie Zimmerman</strong> to guide engineers in designing products, processes, and systems that are benign, resource-conserving, and economically viable.</li>\n<li><strong>1. Inherent Rather Than Circumstantial:</strong> Ensure materials and energy inputs/outputs are inherently benign rather than relying on circumstantial safety apparatus (Slide Example: Dichloromethane solvent hazard).</li>\n<li><strong>2. Prevention Rather Than Treatment:</strong> Waste prevention beats cleanup; saves tremendous remediation funds via solvent substitution, eliminating toxic intermediates, and new chemistry.</li>\n<li><strong>3. Design for Separation:</strong> Avoid energy-intensive distillation and chromatography by utilizing intrinsic physical/chemical properties for self-separation.</li>\n<li><strong>4. Maximize Efficiency:</strong> Maximize mass, energy, space, and time efficiency across all unit operations.</li>\n<li><strong>5. Output-Pulled vs Input-Pushed:</strong> Shift reaction equilibrium without excess energy/reagents by pulling products continuously (Slide Example: Condensation reactions producing water).</li>\n<li><strong>6. Conserve Complexity:</strong> High-complexity products must be reused; low-complexity products recycled (Slide Example: Silicon computer chip vs paper bag).</li>\n<li><strong>7. Durability Rather Than Immortality:</strong> Target operational lifetime to prevent immortal persistence in nature (Slide Example: Disposable diapers persisting 500 years).</li>\n<li><strong>8. Meet Need, Not Excess:</strong> Avoid over-designing and oversized capacity (Slide Examples: Excessive water-chlorine dosing; Global auto industry having 80M capacity for <60M market).</li>\n<li><strong>9. Minimize Material Diversity:</strong> Limit polymer/material variations to enable clean sorting and recycling (Slide Examples: Monomaterial consumer products; IBM PC 15 screws to 1 screw).</li>\n<li><strong>10. Integrate Local Material & Energy Flows:</strong> Industrial symbiosis where byproduct of one plant feeds another (Slide Example: Local industries / Kalundborg eco-park).</li>\n<li><strong>11. Design for Commercial Afterlife:</strong> Recover functional modules for reuse (Slide Examples: Mobile phones, computers, converting old factories to housing; AT&T, GE, IBM, P&G, Whirlpool).</li>\n<li><strong>12. Renewable Rather Than Depleting:</strong> Use renewable inputs across lifecycles (Slide Examples: Solar, wind, hydro, geothermal, biomass, hydrogen fuel cells).</li>\n</ul>",
            "detailed_answer": """<div class=\"detailed-body\">
<p><strong>The Anastas & Zimmerman Framework:</strong> Formulated by Dr. Paul Anastas and Dr. Julie Zimmerman, the <strong>12 Principles of Green Engineering</strong> provide a systematic design roadmap across chemical synthesis, product manufacturing, and industrial operations. Instead of dealing with hazardous wastes after they are created, these principles force engineers to embed non-toxicity, efficiency, and circularity into the initial design of every molecule, machine, and facility.</p>

<h4>Comprehensive Breakdown of the 12 Principles with Slide Examples</h4>
<ol>
<li><strong>Principle 1: Inherent Rather Than Circumstantial (Slide 7)</strong>
<br><em>Official Definition:</em> \"Designers should evaluate the inherent nature of the selected material and energy inputs to ensure that they are as benign as possible as a first step toward a sustainable product, process, or system.\"
<br><em>Engineering Rationale:</em> Traditional safety engineering relies on circumstantial controls (blast containment, scrubbers, personal protective respirators) to manage lethal substances. If the circumstantial apparatus fails, catastrophe occurs. Green engineering designs the hazard out entirely by choosing inherently non-toxic feedstocks.
<br><em>Slide Example:</em> <strong>Dichloromethane (\(\text{CH}_2\text{Cl}_2\))</strong>—a volatile, carcinogenic organochlorine solvent widely used in paint strippers and extraction. Circumstantial exhaust hoods do not eliminate worker exposure or environmental emissions; green engineering substitutes it with non-toxic, bio-based alternatives.</li>

<li><strong>Principle 2: Prevention Rather Than Treatment (Slide 8)</strong>
<br><em>Official Definition:</em> \"It is better to prevent waste than to treat or clean up waste after it is formed.\"
<br><em>Engineering Rationale:</em> Facilities spend tremendous financial resources on waste treatment, hazardous waste transport, deep-well disposal, and Superfund-style remediation. Preventing waste at the source completely eliminates these non-productive capital overheads.
<br><em>Slide Implementation Strategies:</em>
  <ul>
    <li>Implementation of breakthrough green technologies.</li>
    <li>Solvent substitution (replacing toxic organic solvents with supercritical \(\text{CO}_2\) or aqueous media).</li>
    <li>Eliminating hazardous chemical intermediates in multi-step synthesis.</li>
    <li>Developing entirely new reaction pathways and catalytic green chemistry.</li>
  </ul>
</li>

<li><strong>Principle 3: Design for Separation (Slide 9)</strong>
<br><em>Official Definition:</em> \"Design strategy for separation and purification: Many traditional methods for separation require large amounts of hazardous solvents, whereas others consume large quantities of energy as heat or pressure. Appropriate upfront designs permit the self-separation of products using intrinsic physical/chemical properties.\"
<br><em>Engineering Rationale:</em> Conventional downstream purification accounts for 40–70% of total capital and energy costs in chemical plants (e.g., intensive vacuum distillations and liquid-liquid column chromatography). Upfront design engineers products to spontaneously phase-separate, precipitate, or crystallize out of solution based on intrinsic solubility or boiling differentials.</li>

<li><strong>Principle 4: Maximize Mass, Energy, Space, and Time Efficiency (Slide 10)</strong>
<br><em>Official Definition:</em> \"Products, processes, and systems should be designed to maximize mass, energy, space and time efficiency.\"
<br><em>Engineering Rationale:</em> Industrial processes must be optimized multidimensionally: maximizing atom economy and mass yield, minimizing energetic inputs (low temperatures and pressures), reducing facility footprint (space), and slashing residence cycle times through continuous-flow microreactors.</li>

<li><strong>Principle 5: Output-Pulled Rather Than Input-Pushed (Slide 11)</strong>
<br><em>Official Definition:</em> \"More energy or material ('input-pushed') can increase output, but the same output can be achieved by new designing where chemical processes are 'pulled' (e.g. removing products from reaction system) without additional energy or material.\"
<br><em>Engineering Rationale:</em> Applying Le Chatelier's dynamic equilibrium principle. In a reversible reaction, forcing conversion by blasting in excess raw materials (\"input-pushed\") creates massive unreacted waste and burns energy. Conversely, continuously harvesting product molecules as they form \"pulls\" the reaction forward to 100% completion cleanly.
<br><em>Slide Example:</em> <strong>Condensation reactions with the continuous production/removal of water</strong>. Selectively evaporating or membrane-filtering water drives esterification and polymerization forward smoothly without needing excess reagent spikes.</li>

<li><strong>Principle 6: Conserve Complexity (Slides 12, 13)</strong>
<br><em>Official Definition:</em> \"Products with high complexity should correspond to reuse, products with minimal complexity are favoured for value-conserving recycling or beneficial disposition.\"
<br><em>Engineering Rationale:</em> Complexity represents embedded capital, energy, and human organization. Melting down a highly structured, intricate product downcycles its thermodynamic value.
<br><em>Slide Comparison:</em> <strong>Computer Chip vs. Paper Bag</strong>. A silicon microprocessor embodies immense nanometer-scale complexity, ultra-high material purity, and cleanroom energy; it should be preserved through modular reuse and refurbishment. Conversely, a paper bag has minimal spatial or chemical complexity and is ideally suited for bulk pulping, recycling, or natural composting.</li>

<li><strong>Principle 7: Durability Rather Than Immortality (Slide 14)</strong>
<br><em>Official Definition:</em> \"It is therefore necessary to design products with a targeted lifetime to avoid immortality of undesirable materials in the environment. However, this strategy must be balanced with the design of products that are durable enough to withstand anticipated operating conditions.\"
<br><em>Engineering Rationale:</em> Products should endure robustly throughout their intended functional use, but must not persist indefinitely as environmental pollutants after disposal.
<br><em>Slide Example:</em> <strong>Disposable Diapers</strong>. Conventional disposable diapers are used for a few hours, yet are manufactured from synthetic polymers (polypropylene, sodium polyacrylate) that remain immortal in landfills for over 500 years. Green engineering designs diapers with targeted durability followed by rapid, benign biodegradation.</li>

<li><strong>Principle 8: Meet Need, Not Excess (Slide 15)</strong>
<br><em>Official Definition:</em> \"Design for unnecessary capacity or capability (e.g., 'one size fits all') solutions should be considered a design flaw.\"
<br><em>Engineering Rationale:</em> Over-engineering, over-sizing, and building redundant capacity wastes capital, raw materials, and operating energy.
<br><em>Slide Examples:</em>
  <ul>
    <li><em>Water-Chlorine Dosing:</em> Dosing chlorine far beyond what is chemically required to disinfect water wastes treatment chemicals and generates toxic, carcinogenic disinfection byproducts (trihalomethanes).</li>
    <li><em>Global Automotive Industry Overcapacity:</em> The worldwide automobile manufacturing sector maintains an installed production capacity of <strong>80 million vehicles/year</strong> to serve an actual global market demand of <strong>less than 60 million vehicles/year</strong>—representing massive wasted industrial capital, idling plants, and embodied resource excess.</li>
  </ul>
</li>

<li><strong>Principle 9: Minimize Material Diversity (Slides 13, 16)</strong>
<br><em>Official Definition:</em> \"Options for final disposition are increased through upfront designs that minimize material diversity yet accomplish the needed functions. Reducing multiple components in products increases the possibility of useful reuse or recyclability.\"
<br><em>Engineering Rationale:</em> When a product is made from a tangled cocktail of disparate plastics, laminates, and metallic alloys, recycling is physically impossible or economically unprofitable. Monomaterial designs enable rapid, single-stream automated sorting and high-purity recycling.
<br><em>Slide Example:</em> Consumer products and electronics. Standardizing plastic casings to a single polymer (such as pure recyclable ABS or Polypropylene) instead of blending incompatible resins.</li>

<li><strong>Principle 10: Integrate Local Material and Energy Flows (Slide 17)</strong>
<br><em>Official Definition:</em> \"Design of products, processes, and systems must include integration and interconnectivity with available energy and materials flows.\"
<br><em>Engineering Rationale:</em> Emulating biological ecosystems where no waste exists. Industrial facilities must be interconnected so that one company's effluent or rejected thermal heat becomes the valuable raw material or energy feedstock for an adjacent facility.
<br><em>Slide Example:</em> <strong>Local Industries (Industrial Symbiosis / Kalundborg Eco-Park)</strong>. Co-located manufacturing plants exchanging waste steam, cooling water, sulfur byproducts, and fly ash in closed resource loops.</li>

<li><strong>Principle 11: Design for Commercial Afterlife (Slide 18)</strong>
<br><em>Official Definition:</em> \"To reduce waste, components that remain functional and valuable can be recovered for reuse and/or reconfiguration.\"
<br><em>Engineering Rationale:</em> Products must be engineered for effortless non-destructive disassembly, maintenance, and remanufacturing rather than shredding.
<br><em>Slide Examples:</em>
  <ul>
    <li><em>Electronics:</em> Mobile phones, computers, and electrical equipment designed with modular, swappable components.</li>
    <li><em>Adaptive Architecture:</em> The architectural conversion of decommissioned historic industrial factories into vibrant residential housing and commercial spaces.</li>
    <li><em>Corporate Implementations:</em> Major industrial corporations that have integrated commercial afterlife design include <strong>AT&T, General Electric (GE), IBM, Procter & Gamble (P&G), and Whirlpool</strong>.</li>
  </ul>
</li>

<li><strong>Principle 12: Renewable Rather Than Depleting (Slide 19)</strong>
<br><em>Official Definition:</em> \"Material and energy inputs should be renewable rather than depleting.\"
<br><em>Engineering Rationale:</em> Finite fossil and mineral reserves must not be depleted; resource availability must be preserved for future generations.
<br><em>Slide Examples:</em> Powering industrial processes via renewable energy inputs: <strong>solar, wind, hydroelectric, geothermal, biomass, and hydrogen (fuel cells)</strong>.</li>
</ol>
<p><em>Slide Reference: Class 15, Slides 6–20.</em></p>
</div>"""
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
            "prompt": "Explain the impact of Denim manufacturing on water consumption and pollution, worker health hazards, and greenhouse gas emissions as presented in the lecture.",
            "key_answer_points": "<ul>\n<li><strong>Three Stages of Water Pollution:</strong> 1) <em>Growing of raw cotton:</em> massive agricultural freshwater irrigation and pesticide runoff; 2) <em>Dyeing and finishing the material:</em> intensive synthetic chemical dye baths; 3) <em>Texturizing and finishing the product:</em> multiple post-fabric chemical wash cycles.</li>\n<li><strong>Chemical Dyeing & River Devastation:</strong> Producing 'distressed' vintage denim requires intensive synthetic indigo dyes, heavy chemical washes, and toxic spray-applied 'acid washes'. Chemical run-offs dumped untreated into natural water systems turn entire rivers completely indigo-blue (Slide Example: The <em>Pearl River in China</em>).</li>\n<li><strong>Denim Sandblasting & Fatal Worker Health Hazard:</strong> High-pressure airguns spray fine sand against denim fabric to create an artificial worn, vintage look; the primary ingredient, <em>silica dust</em>, causes severe, incurable, and fatal respiratory disease (silicosis) in factory garment workers.</li>\n<li><strong>Severe Carbon Footprint:</strong> A lifecycle study by a leading apparel company revealed that manufacturing a single pair of denim jeans generates <strong>44 pounds of greenhouse gas emissions</strong>—directly equivalent to burning over <strong>21 pounds of coal</strong>.</li>\n<li><strong>Green Engineering Relevance:</strong> Serves as the premier textbook example of flawed linear manufacturing ('take-make-waste') demonstrating why upstream green design (Principle 1 Inherent Safety, Principle 2 Waste Prevention) is vital to replace toxic chemical washes with benign alternatives (e.g., laser abrading, ozone fading).</li>\n</ul>",
            "detailed_answer": """<div class=\"detailed-body\">
<p><strong>The Fast-Fashion Reality Check:</strong> To illustrate why Green Engineering is urgently required in modern industrial practice, Class 15 opens with an in-depth lifecycle analysis of an everyday consumer product: a standard pair of distressed blue jeans (Slide 3). The global denim industry exemplifies the catastrophic environmental and human health costs of a traditional linear economy that designs products for aesthetic consumer trends without considering toxic inputs, water consumption, worker safety, or carbon emissions.</p>

<h4>1. The Three Critical Stages of Water Pollution</h4>
<p>The curriculum explicitly identifies the <strong>three industrial processes</strong> in denim production that drive massive aquatic pollution and depletion:</p>
<ol>
<li><strong>Growing of Cotton:</strong> Cultivating virgin cotton requires intensive agricultural freshwater irrigation (thousands of liters per kilogram of lint) combined with aggressive application of synthetic pesticides and fertilizers that leach into surrounding aquifers.</li>
<li><strong>Dyeing and Finishing the Material:</strong> Raw yarn and fabric undergo multiple chemical pretreatment baths, caustic scouring, and synthetic indigo dyeing. Synthetic indigo is water-insoluble and requires harsh reducing agents and alkalis to dissolve and bind to the cellulose fibers.</li>
<li><strong>Texturizing and Finishing the Product:</strong> To achieve commercial fashion finishes, the woven denim fabric is subjected to numerous mechanical abrasions, enzymatic treatments, detergent rinses, and chemical washes.</li>
</ol>

<h4>2. Intensive Chemical Dyes, Acid Washes & River System Collapse</h4>
<p>Modern fashion demands pre-faded, \"distressed\", and vintage-look denim garments. Achieving these cosmetic effects requires extraordinarily intensive chemical treatments:</p>
<ul>
<li><strong>Repeated Chemical Washes:</strong> Garments are repeatedly submerged in multi-stage chemical wash cycles to strip color and soften stiff denim fibers.</li>
<li><strong>Worker Spray Exposure:</strong> In pursuit of an \"acid wash\" look, harmful oxidizers and chemicals are sprayed directly onto the denim material. This creates severe, direct health risks for garment workers through toxic inhalation and dermal absorption.</li>
<li><strong>Indigo-Blue River Contamination:</strong> Industrial manufacturers routinely dump untreated or poorly treated chemical effluent directly into municipal and natural drainage basins. In major manufacturing hubs, these toxic chemical run-offs turn entire river systems completely indigo-blue. The curriculum highlights the real-world devastation of the <strong>Pearl River in Guangdong, China</strong>, where denim finishing factories turned vast stretches of the river opaque blue, suffocating aquatic life and destroying downstream drinking water sources.</li>
</ul>

<h4>3. Denim Sandblasting: Severe Occupational Silica Hazards</h4>
<p>Slide 3 specifically documents the destructive practice of <strong>Denim Sandblasting</strong>:</p>
<ul>
<li><strong>The Mechanical Process:</strong> Fine sand is loaded into pneumatic airguns and blasted at extreme high pressure directly against the denim fabric. The abrasive impact abrades the surface cotton fibers, creating an instant worn, faded, vintage appearance.</li>
<li><strong>Economic Motivation:</strong> Apparel manufacturers favor sandblasting because it is a cheap, fast, and simple mechanical shortcut to manipulate garments without purchasing expensive specialized machinery.</li>
<li><strong>Worker Health Pathology:</strong> The primary ingredient in sandblasting grit is <strong>silica (crystalline quartz, \(\text{SiO}_2\))</strong>. Blasting denim atomizes silica particles into microscopic respirable dust. Garment workers operating in poorly ventilated facilities inhale these sharp mineral particles, which lodge permanently in the lung alveoli, causing progressive pulmonary fibrosis, severe respiratory failure, and incurable, fatal <strong>silicosis</strong>.</li>
</ul>

<h4>4. Carbon Footprint and Equivalent Energy Cost</h4>
<p>Beyond water consumption and chemical poisoning, denim manufacturing carries a massive fossil fuel and greenhouse gas footprint:</p>
<div class=\"formula-box\">
<p style=\"text-align:center; font-weight:600; font-size:1.05rem; margin:0.3rem 0;\">1 Pair of Denim Jeans = 44 Pounds (\(\approx 20\text{ kg}\)) of Greenhouse Gas Emissions</p>
<p style=\"text-align:center; font-style:italic; margin:0.3rem 0;\">Directly equivalent to burning over 21 pounds (\(\approx 9.5\text{ kg}\)) of coal!</p>
</div>
<p>This staggering carbon toll stems from the combined thermal and electrical energy demanded by coal-fired captive power plants supplying textile mills: pumping massive water volumes, heating multi-stage boiling dye baths, running energy-intensive mechanical drying drums, and transporting heavy fabrics across global supply chains.</p>

<h4>5. The Green Engineering Contrast</h4>
<p>The denim crisis provides the ultimate benchmark for why the <strong>12 Principles of Green Engineering</strong> must replace traditional textile engineering:</p>
<ul>
<li><em>Principle 1 (Inherent Safety):</em> Eliminating silica sandblasting and replacing toxic acid-spray chemicals with benign physical or biochemical agents (e.g., precision computerized laser distressing and closed-loop ozone fading).</li>
<li><em>Principle 2 (Prevention over Treatment):</em> Preventing effluent formation at source through digital waterless dyeing technologies rather than building multi-million dollar wastewater treatment plants to neutralize indigo runoff.</li>
<li><em>Principle 4 (Maximize Efficiency):</em> Slashing water and thermal energy consumption per garment through closed-loop water recycling.</li>
</ul>
<p><em>Slide Reference: Class 15, Slide 3.</em></p>
</div>"""
        },
        {
            "id": "EQB-15-05",
            "class_id": 15,
            "class_name": "Green Engineering & Industrial Ecology",
            "topic": "Industrial Symbiosis, Material Diversity & Green Building Architecture",
            "category": "Descriptive & Case Study",
            "exams": [
                {"paper": "End Exam 2022", "section": "Section III, Q1", "marks": "1M"}
            ],
            "marks": "1M – 5M",
            "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
            "prompt": "An example of \"Local industries\" was taken to discuss which principle of green engineering? Explain this principle in detail along with Material Diversity, and describe the landmark Green Building architectural examples (One Central Park, Bahrain WTC, Suzlon One Earth) presented in the lecture.",
            "key_answer_points": "<ul>\n<li><strong>1-Mark Direct Exam Answer:</strong> Principle 10: <strong>\"Integrate Local Material and Energy Flows\"</strong> (Slide 17).</li>\n<li><strong>Principle 10 Core Concept (Industrial Symbiosis):</strong> Designing industrial clusters where the waste heat, steam, effluent, or byproducts of one plant become the valuable raw material/energy input for an adjacent facility, creating a closed-loop eco-industrial ecosystem (e.g., Kalundborg Eco-Park).</li>\n<li><strong>Material Diversity & IBM PC Case Study (Principle 9 & Slide 13):</strong> Upfront design that minimizes material types; Diana Bendz (IBM, 2000 ND Talk) demonstrated reducing 15 different types of screws in IBM PCs down to 1 uniform screw type, making computers easy to disassemble, modularly upgrade, and recycle.</li>\n<li><strong>One Central Park (Sydney, Australia - Slide 26):</strong> Iconic green architecture featuring extensive vertical gardens (living green walls) and a monumental cantilevered heliostat with motorized mirrors directing reflected sunlight into shaded parks and retail atriums.</li>\n<li><strong>Bahrain World Trade Center (Manama, Bahrain - Slide 27):</strong> Aerodynamically sculpted funnel-shaped twin towers that channel onshore desert and sea breezes into three massive horizontal-axis wind turbines mounted on skybridges between the towers.</li>\n<li><strong>Suzlon One Earth (Pune, India - Slide 28):</strong> Corporate headquarters built exclusively from recycled and non-toxic materials, architecturally engineered to let in abundant fresh air and natural daylight across all campus spaces.</li>\n</ul>",
            "detailed_answer": """<div class=\"detailed-body\">
<p><strong>Direct Exam Answer:</strong> In the official curriculum slides, the specific example of <strong>\"Local industries\"</strong> was presented to illustrate <strong>Principle 10: Integrate Local Material and Energy Flows</strong> (Slide 17).</p>

<h4>1. Principle 10: Integrate Local Material and Energy Flows (Industrial Symbiosis)</h4>
<p>Slide 17 establishes the official principle definition:</p>
<div class=\"formula-box\">
<p style=\"text-align:center; font-style:italic; font-size:1.02rem; margin:0.3rem 0;\">\"Design of products, processes, and systems must include integration and interconnectivity with available energy and materials flows.\"</p>
</div>
<p>In traditional industrial design, manufacturing plants operate as isolated linear entities: each plant purchases fresh energy and raw materials from the outside, runs its internal process, and dumps residual waste heat, combustion flue gases, wastewater, and solid byproducts into the environment. Principle 10 replaces this linear isolation with <strong>Industrial Ecology (Industrial Symbiosis)</strong>:</p>
<ul>
<li><strong>Local Industry Interconnectivity:</strong> By physically co-locating diverse industrial operations, the rejected byproduct of one facility serves as the direct operational feedstock or energy source for a neighboring facility.</li>
<li><strong>The Kalundborg Model:</strong> The world's classic benchmark of this principle (and standard curriculum reference) is the <strong>Kalundborg Eco-Industrial Park in Denmark</strong>:
  <ul>
    <li>Waste thermal steam from a 1,500 MW power station is piped to provide district heating for the entire municipality and process heat for an adjacent Novo Nordisk pharmaceutical plant and Equinor oil refinery.</li>
    <li>Sulfur dioxide gas trapped by the power station's flue-gas desulfurization scrubbers reacts with limestone to produce pure synthetic gypsum (\(\text{CaSO}_4\cdot 2\text{H}_2\text{O}\)), which is piped directly to a neighboring Gyproc wallboard factory, eliminating the need to mine natural gypsum.</li>
    <li>Fly ash and clinker from combustion boilers are delivered to cement manufacturing plants for concrete synthesis, closing all solid waste loops.</li>
  </ul>
</li>
</ul>

<h4>2. Principle 9 & Slide 13: Minimizing Material Diversity (The IBM Modular PC)</h4>
<p>Slide 16 defines Principle 9: <em>\"Options for final disposition are increased through upfront designs that minimize material diversity yet accomplish the needed functions. Reducing multiple components in products increases the possibility of useful reuse or recyclability.\"</em></p>
<p>To demonstrate this in mass electronics, the lecture presents the landmark case study of <strong>Diana Bendz from IBM</strong> (Talk at Notre Dame, 2000, Slide 13):</p>
<ul>
<li><strong>The Unnecessary Complexity Problem:</strong> Early IBM personal computers were assembled using <strong>15 different types of screws</strong>, alongside a chaotic mix of incompatible plastic resins (PVC, polycarbonate, ABS, polystyrene). Servicing or disassembling a discarded PC required a technician to keep a dozen distinct screwdrivers on hand and spend exorbitant manual labor sorting components. As a result, recycling was economically impossible, and discarded computers were simply dumped in landfills.</li>
<li><strong>The Green Engineering Redesign:</strong> IBM replaced the 15 screw variants with <strong>1 single standardized type of screw</strong> (and tool-less snap-fits), while standardizing plastic housings to single-polymer recyclable resins. Disassembly time dropped from tens of minutes to seconds.</li>
<li><strong>Why Not Reuse Computers?</strong> Slide 13 poses the critical green engineering question: Rather than shredding an entire computer, why not modularize it? By designing modular architectures, users can swap out the central processor (CPU) or memory (RAM) as technology advances while preserving the chassis, power supply, and passive metal frame—conserving embedded complexity (Principle 6) and commercial afterlife (Principle 11).</li>
</ul>

<h4>3. Radical Sustainable Architecture: The Three Slide Case Studies</h4>
<p>Slides 21, 26, 27, and 28 highlight how green engineering transcends industrial chemistry to transform the built environment—creating resource-efficient structures throughout their lifecycle from design and construction to operation:</p>
<ol>
<li><strong>One Central Park (Sydney, Australia - Slide 26):</strong>
  <br>Designed by Pritzker Prize architect Jean Nouvel and French botanist Patrick Blanc, this urban mixed-use landmark incorporates two high-rise towers wrapped in living architecture.
  <ul>
    <li><em>Vertical Gardens:</em> Lush vertical hanging gardens comprising over 35,000 individual plants cover the exterior facades, providing biological thermal insulation, capturing urban airborne particulates, and cooling the surrounding microclimate.</li>
    <li><em>Cantilevered Heliostat:</em> A massive monumental reflector frame cantilevers out from the 28th floor of the taller tower, carrying 320 motorized sun-tracking heliostat mirrors. These mirrors capture sunlight that would otherwise be blocked by the tower and redirect it down into shadowed retail atriums and the adjacent public parkland below. At night, the heliostat transforms into a monumental LED light artwork by Yann Kersalé.</li>
  </ul>
</li>
<li><strong>Bahrain World Trade Center (Manama, Bahrain - Slide 27):</strong>
  <br>Located on the Persian Gulf coast, this 240-meter (787-foot) twin-tower commercial complex represents the world's first large-scale skyscraper to integrate wind turbine electricity generation directly into its architectural form.
  <ul>
    <li><em>Aerodynamic Funneling Design:</em> The two identical towers are aerodynamically sculpted like twin maritime sails. As onshore desert and ocean winds strike the complex, the converging curved glass towers act as a giant funnel, accelerating wind velocity by up to 30% through the central gap.</li>
    <li><em>Integrated Wind Turbines:</em> Three massive steel skybridges span the void between the towers, each supporting a <strong>225 kW horizontal-axis wind turbine with 29-meter diameter rotor blades</strong>. Together, the three turbines generate 1.1 to 1.3 million kWh of clean electricity annually—supplying 11% to 15% of the twin towers' entire operational electrical demand.</li>
  </ul>
</li>
<li><strong>Suzlon One Earth (Pune, India - Slide 28):</strong>
  <br>The global corporate headquarters of Suzlon Energy in Pune, India, designed by architect Christopher Benninger, is recognized as one of the greenest corporate campuses in the world (LEED Platinum and GRIHA 5-star certified).
  <ul>
    <li><em>100% Recycled & Non-Toxic Materials:</em> The entire campus was built exclusively utilizing recycled, locally sourced, and non-toxic materials—eliminating VOC-emitting paints, hazardous adhesives, and high-embodied-energy components.</li>
    <li><em>Passive Daylighting & Fresh Air Ventilation:</em> The architectural layout arranges low-rise office blocks around central landscaped courtyards (\"water courts\"), deep overhangs, and high-performance glazed facades. This orientation ensures that <strong>fresh air and abundant natural daylight penetrate into 90% of all campus workspaces</strong>, dramatically cutting HVAC cooling loads and artificial lighting demand, with net-zero operations powered by on-site photovoltaic panels and wind turbines.</li>
  </ul>
</li>
</ol>

<h4>4. Extended Cleantech Ecosystems in Class 15</h4>
<p>Slides 21 to 24 document additional systemic dimensions of green engineering in society:</p>
<ul>
<li><strong>Green Transport (Slide 21):</strong> Transportation systems with low environmental impact, specifically walking, cycling, carpooling, car sharing, and electric/hybrid green vehicles.</li>
<li><strong>Green Skills (Slide 21):</strong> Defined by Cedefop (2012) as the technical knowledge, abilities, values, and attitudes required to live in, develop, and support a resource-efficient society.</li>
<li><strong>Green Audit (Slide 22):</strong> The systematic identification, quantification, recording, reporting, and analysis of environmental diversity components within and outside institutional establishments to evaluate eco-friendly ambience.</li>
<li><strong>Green Banking (Slides 22, 23):</strong> Developing sustainable banking strategies combining operational improvements, financial technology, and client habits. Key Indian implementations include:
  <ul>
    <li><em>State Bank of India (SBI):</em> Direct generation of green power by installing captive commercial windmills.</li>
    <li><em>Punjab National Bank (PNB):</em> Systematically reducing internal emissions and energy usage.</li>
    <li><em>Bank of Baroda (BOB):</em> Giving financing preference to cleantech projects that earn certified carbon credits (e.g., utility solar).</li>
    <li><em>Dedicated Clean Energy Financial Institutions:</em> <strong>Indian Renewable Energy Development Agency (IREDA)</strong> and <strong>Tata Cleantech Capital Limited (TCCL)</strong>.</li>
  </ul>
</li>
<li><strong>Green Certificates & Energy Corridors (Slide 24):</strong> Tradable market assets certifying that electricity was generated by renewable sources, integrated into national grids via the <strong>Green Energy Corridor (GEC)</strong> to synchronize fluctuating solar and wind electricity with conventional base-load power stations.</li>
</ul>
<p><em>Slide Reference: Class 15, Slides 13, 16, 17, 21, 22, 24, 26, 27, 28.</em></p>
</div>"""
        }
    ]

if __name__ == "__main__":
    qs = get_class15_grounded_questions()
    print(f"Successfully loaded {len(qs)} slide-grounded questions for Class 15.")
    for q in qs:
        print(f"[{q['id']}] {q['topic']} ({q['marks']}) - Prompt: {q['prompt'][:60]}...")
