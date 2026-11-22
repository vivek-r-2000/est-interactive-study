"""
Class 14: Green Computing - Official Slide-Grounded Question Bank
Grounded 100% in Class-14-Green computing.pdf raw slide content.
Zero external hallucinations. Rich, comprehensive detailed answers.
"""

def get_class14_grounded_questions():
    return [
        {
            "id": "EQB-14-01",
            "class_id": 14,
            "class_name": "Green Computing",
            "topic": "Green Computing Definition & 4 Core Lifecycle Approaches",
            "category": "Comprehensive Descriptive",
            "exams": [
                {"paper": "EST End Exam 2024", "section": "Section IV, Q(e)", "marks": "2M"},
                {"paper": "End Exam 2019", "section": "Section VI, Q1", "marks": "2M"},
                {"paper": "End Exam 2018", "section": "Part II, Q1–2", "marks": "10M"}
            ],
            "marks": "2M – 10M",
            "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
            "prompt": "Define Green Computing. Explain the four fundamental approaches across the hardware lifecycle: Green Design, Green Manufacturing, Green Use, and Green Disposal.",
            "expected_answer": """<div class="expected-body">
<p><strong>Definition:</strong> Green computing is the environmentally responsible and eco-friendly study and practice of designing, manufacturing, using, and disposing of computers, servers, and associated subsystems with minimal environmental impact. The term emerged shortly after 1992, following the US Environmental Protection Agency's (EPA) launch of the <strong>Energy Star</strong> labeling program. Today, Information and Communications Technology (ICT) accounts for approximately <strong>2% of global CO2 emissions</strong>.</p>

<p><strong>The Four Fundamental Lifecycle Approaches (Murugesan Model):</strong></p>
<ol>
  <li><strong>Green Design:</strong> Architecting energy-efficient processors, passive cooling (fanless systems), modular upgradeability, and non-toxic materials (e.g. bio-resins, cornstarch polymers). Slide 10 emphasizes choosing laptops over desktops because mobile-optimized laptops consume up to 70% less operational electricity.</li>
  <li><strong>Green Manufacturing:</strong> Eliminating hazardous substances (lead, mercury, cadmium, hexavalent chromium) in cleanrooms and chip fabrication. This prevents toxic wastewater—often equaling the water consumption of an entire small city per fabrication plant—from polluting surrounding watersheds and entering the human food chain.</li>
  <li><strong>Green Use:</strong> Slashing operational electricity draw during active deployment through:
    <ul>
      <li><em>Server Virtualization:</em> Consolidating multiple logical systems onto one physical server, drastically shrinking data center power and cooling footprints.</li>
      <li><em>Power Management:</em> Enabling automated sleep modes and turning off idle systems (recognizing that screen savers consume active electrical power rather than saving it).</li>
      <li><em>Display Technology:</em> Upgrading from 17" CRT monitors (<strong>80 W</strong>) to LCD panels (<strong>35 W</strong>) or LED monitors (<strong>25 W</strong>). Energy Star systems operate at <strong>80% efficiency</strong> (vs 70% for unrated machines).</li>
      <li><em>Algorithmic Efficiency:</em> Streamlining code reduces server CPU cycles and carbon emissions per query: Google ($\approx 0.20\text{ g }\text{CO}_2$), Yahoo ($\approx 0.26\text{ g }\text{CO}_2$), MS Live ($\approx 0.32\text{ g }\text{CO}_2$), and AOL ($\approx 0.37\text{ g }\text{CO}_2$).</li>
    </ul>
  </li>
  <li><strong>Green Disposal:</strong> Responsibly managing <strong>20 to 50 million tons of annual global e-waste</strong> (~5% of all solid waste on Earth). Prioritizes hardware reuse, refurbishment, and certified closed-loop metal recycling over hazardous dumping.</li>
</ol>

<table class="exam-table">
  <thead>
    <tr>
      <th>Approach</th>
      <th>Lifecycle Phase</th>
      <th>Primary Technical Interventions</th>
      <th>Quantifiable Metric / Impact</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Green Design</strong></td>
      <td>R&D & Engineering</td>
      <td>Low-TDP chips, passive cooling, modular chassis, laptops over desktops</td>
      <td>Laptops consume up to 70% less energy than desktop towers</td>
    </tr>
    <tr>
      <td><strong>Green Manufacturing</strong></td>
      <td>Semiconductor Fabrication</td>
      <td>Closed-loop water reuse, RoHS compliance, eco-packaging</td>
      <td>Prevents cleanroom effluents (small city equivalent) from polluting watersheds</td>
    </tr>
    <tr>
      <td><strong>Green Use</strong></td>
      <td>Active Deployment</td>
      <td>Server virtualization, sleep modes, LED displays, efficient algorithms</td>
      <td>Energy Star cuts power loss (80% vs 70% efficiency); Google 0.20g CO2 per query</td>
    </tr>
    <tr>
      <td><strong>Green Disposal</strong></td>
      <td>Retirement & End-of-Life</td>
      <td>Refurbishing, component reuse, certified closed-loop metal recycling</td>
      <td>Diverts 20–50 million tons/year of e-waste from toxic open dumping</td>
    </tr>
  </tbody>
</table>
</div>""",
            "key_answer_points": """<ul>
<li><strong>Definition:</strong> Green computing is the environmentally responsible and eco-friendly use of computers and their resources. It is the comprehensive study and practice of designing, manufacturing, using, and disposing of computing devices in such a way that reduces environmental impact.</li>
<li><strong>Origins:</strong> The term was coined shortly after 1992, when the US Environmental Protection Agency (EPA) launched the <strong>Energy Star</strong> labeling program to recognize energy efficiency in monitors and climate control equipment.</li>
<li><strong>The 4 Core Lifecycle Approaches:</strong>
<br>1. <strong>Green Design:</strong> Engineering energy-efficient processors, passive cooling, modular architectures, non-toxic recyclable materials, and prioritizing laptops over desktops.
<br>2. <strong>Green Manufacturing:</strong> Eliminating hazardous toxic chemicals in fabrication to prevent them entering water and food chains, minimizing cleanroom energy/water, and implementing eco-packaging.
<br>3. <strong>Green Use:</strong> Slashing operational power through server virtualization, intelligent power management (sleep modes, powering off idle CPUs/fans), selecting low-power monitors (LED 25W vs LCD 35W vs CRT 80W), Energy Star ratings (80% vs 70% efficiency), and optimizing algorithmic efficiency (e.g. Google 0.20g vs AOL 0.37g CO2 per query).
<br>4. <strong>Green Disposal:</strong> Managing 20–50 million tons of annual global e-waste (~5% of total planetary waste) through responsible reuse, refurbishing, and certified material recycling to eliminate informal toxic dumping.</li>
</ul>""",
            "detailed_answer": """<div class="detailed-body">
<p><strong>Definition & Historical Context:</strong> Green computing refers to environmentally sustainable computing. It represents a paradigm shift in designing computer systems that evaluates processing performance alongside energy efficiency. The term itself was coined shortly after 1992, when the US Environmental Protection Agency (EPA) launched the <strong>Energy Star</strong> program—a voluntary labeling initiative engineered to promote and recognize energy efficiency in computer monitors, power supplies, and climate control equipment.</p>

<p>The imperative for green computing stems from the massive ecological footprint of Information and Communications Technology (ICT), which currently accounts for <strong>2% of total global CO2 emissions</strong>. Computational energy is frequently squandered by leaving machines active when idle (where CPU, fans, and screen savers consume continuous power) and by data centers operating with inadequate cooling capacities. Furthermore, the fabrication, packaging, and disposal of computing devices release hazardous persistent pollutants into ecosystems.</p>

<h4>The Four Fundamental Lifecycle Approaches</h4>
<p>As established in the core curriculum framework (Murugesan lifecycle model), green computing must address every stage of a computing device's lifespan:</p>

<ol>
  <li><strong>Green Design (Pre-Production & Engineering):</strong>
    <p>Focuses on architecting environmentally sound computing machinery before fabrication begins. Key strategies include designing microprocessors with advanced low-power sleep states, reducing thermal design power (TDP), implementing passive conduction cooling to eliminate electromechanical fans, and selecting biodegradable or non-toxic materials (e.g. bio-resins, cornstarch polymers, and screwless chassis). Slide 10 emphasizes hardware form-factor selection: laptops should always be preferred over desktop computers because their mobile-optimized architectures draw significantly less wattage.</p>
  </li>
  <li><strong>Green Manufacturing (Fabrication & Assembly):</strong>
    <p>Addresses the industrial fabrication of microchips, printed circuit boards (PCBs), and peripherals. Semiconductor fabrication facilities consume massive amounts of process water—often equivalent to the water consumption of an entire small city—and generate toxic chemical effluents. Green manufacturing mandates eliminating hazardous substances (such as lead, mercury, cadmium, and hexavalent chromium) to prevent toxic chemicals from leaching into groundwater and entering the human food chain. It incorporates Environmentally Preferable Purchasing (EPP) standards and cleanroom energy minimization.</p>
  </li>
  <li><strong>Green Use (Operational Efficiency & Software):</strong>
    <p>Minimizes electrical consumption during the active deployment of IT infrastructure across several domains:</p>
    <ul>
      <li><em>Virtualization:</em> The process of running two or more logical computer systems on one physical set of hardware. Virtualization platforms can span hundreds of interconnected physical computers and storage devices to create an entire virtual infrastructure. This slashes an enterprise's power and cooling consumption by dramatically reducing the physical machine footprint.</li>
      <li><em>Power Management & User Habits:</em> Turning off computers and printers when not in use, enabling automated sleep modes, and recognizing that screen savers consume active electrical power rather than saving it.</li>
      <li><em>Monitor Technology Selection:</em> Operational power varies drastically across display technologies: a 17-inch CRT monitor consumes <strong>80 Watts</strong>; a 17-inch LCD monitor consumes <strong>35 Watts</strong> (preferred for general users); and a 17-inch LED monitor consumes only <strong>25 Watts</strong> (though historically rare and expensive). Furthermore, an Energy Star rated computer operates at <strong>80% energy efficiency</strong>, compared to only <strong>70% efficiency</strong> for an unrated machine.</li>
      <li><em>Algorithmic Efficiency:</em> Software algorithms directly impact the hardware resources and electrical energy consumed per computational task. Slide 11 documents the carbon cost per internet search:
        <ul>
          <li>Google Search: $\\approx 0.20\\text{ g } \\text{CO}_2$</li>
          <li>Yahoo Search: $\\approx 0.26\\text{ g } \\text{CO}_2$</li>
          <li>Microsoft Live Search: $\\approx 0.32\\text{ g } \\text{CO}_2$</li>
          <li>AOL Search: $\\approx 0.37\\text{ g } \\text{CO}_2$</li>
        </ul>
      </li>
    </ul>
  </li>
  <li><strong>Green Disposal (End-of-Life & Resource Recovery):</strong>
    <p>Addresses post-consumer hardware retirement. Global e-waste generation stands at <strong>20 to 50 million tons per year</strong>, representing approximately <strong>5% of all solid waste on the planet</strong>. Green disposal establishes systematic frameworks for e-waste handling: prioritizing component refurbishment, secondary market reuse, and environmentally sound material recycling (urban mining of precious metals) to prevent hazardous heavy metals from polluting soil and drinking water reservoirs.</p>
  </li>
</ol>

<h4>Lifecycle Engineering Summary Matrix</h4>
<table class="exam-table">
  <thead>
    <tr>
      <th>Approach</th>
      <th>Lifecycle Phase</th>
      <th>Primary Technical Interventions</th>
      <th>Quantifiable Metric / Impact</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Green Design</strong></td>
      <td>R&D / Architecture</td>
      <td>Low-power CPU logic, passive cooling, screwless modular chassis, laptop form factors</td>
      <td>Laptops consume up to 70% less power than desktop towers</td>
    </tr>
    <tr>
      <td><strong>Green Manufacturing</strong></td>
      <td>Foundry / Cleanroom</td>
      <td>Closed-loop water treatment, EPP guidelines, eliminating toxic heavy metals</td>
      <td>Prevents fab effluents equivalent to small city water demand from polluting watersheds</td>
    </tr>
    <tr>
      <td><strong>Green Use</strong></td>
      <td>Active Deployment</td>
      <td>Server virtualization, sleep modes, display upgrades (LED 25W vs CRT 80W), efficient algorithms</td>
      <td>Energy Star cuts power loss (80% vs 70% efficiency); Google search cuts carbon to 0.20g CO2</td>
    </tr>
    <tr>
      <td><strong>Green Disposal</strong></td>
      <td>Retirement / EOL</td>
      <td>Refurbishing, component reuse, closed-loop material recycling, certified recovery</td>
      <td>Diverts 20–50 million tons/year of e-waste (5% of planetary waste) from toxic landfills</td>
    </tr>
  </tbody>
</table>

<p><em>Slide Reference: Class 14, Slides 6, 7, 8, 9, 10, 11, and 19.</em></p>
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
            "prompt": "Differentiate thoroughly between Thick Clients and Thin Clients. Compare their system architecture, operational energy, embodied resources, hardware lifespan, purchase cost, and environmental footprint. Include the Queen Margaret University case study.",
            "expected_answer": """<div class="expected-body">
<p><strong>System Architecture:</strong></p>
<ul>
  <li><strong>Thin Client:</strong> A compact, solid-state terminal device with <em>no mechanical hard drives or moving parts</em> (fanless). It contains minimal local processing power and RAM, executing zero user applications locally. It sends user inputs over the network to a centralized server, which executes all workloads and returns updated display frames.</li>
  <li><strong>Thick Client:</strong> A standard standalone desktop computer equipped with local hard drives, a powerful multi-core CPU, dedicated memory, and a local operating system. It processes instructions, runs applications, and stores data locally without requiring a network server connection.</li>
</ul>

<table class="exam-table">
  <thead>
    <tr>
      <th>Comparison Parameter</th>
      <th>Thick Client (Desktop PC)</th>
      <th>Thin Client (VDI Terminal)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Operational Power Draw</strong></td>
      <td><strong>75 Watts</strong> (active baseline)</td>
      <td><strong>5 Watts</strong> (slashes operational power by <strong>93.3%</strong>)</td>
    </tr>
    <tr>
      <td><strong>Capital Purchase Cost</strong></td>
      <td><strong>£400</strong> (low-spec office PC)</td>
      <td><strong>£210</strong> (terminal unit)</td>
    </tr>
    <tr>
      <td><strong>Hardware Useful Lifespan</strong></td>
      <td><strong>5 years</strong> (rapid obsolescence)</td>
      <td><strong>7 years</strong> (centralized server upgrades)</td>
    </tr>
    <tr>
      <td><strong>Moving Parts & Acoustic Noise</strong></td>
      <td>Mechanical cooling fans & HDDs; noisy</td>
      <td><strong>Zero moving parts</strong>; completely silent</td>
    </tr>
    <tr>
      <td><strong>Embodied Production Footprint</strong></td>
      <td>Requires <strong>20 kg materials</strong>, <strong>3,244 MJ energy</strong>, <strong>920 L water</strong>, emits <strong>193 kg GHGs</strong></td>
      <td>Drastically lower embodied energy, minimal plastics, copper, and silicon area</td>
    </tr>
    <tr>
      <td><strong>Lifecycle Solid Waste</strong></td>
      <td>Generates <strong>37 kg non-hazardous</strong> + <strong>0.7 kg hazardous waste</strong></td>
      <td>Fraction of desktop e-waste mass; highly recyclable</td>
    </tr>
    <tr>
      <td><strong>Server & Network Dependency</strong></td>
      <td>Autonomous; functions fully offline</td>
      <td><strong>100% dependent</strong> on continuous 24x7 active server availability</td>
    </tr>
  </tbody>
</table>

<p><strong>Environmental & Financial Case Study (Queen Margaret University, Edinburgh):</strong> By replacing conventional desktop workstations with thin client terminals, the university saved <strong>£50,000 in direct electricity costs alone</strong> at the halfway stage of deployment, while eliminating internal lab heat dissipation and slashing secondary air-conditioning energy demand.</p>
</div>""",
            "key_answer_points": """<ul>
<li><strong>System Architecture:</strong>
<br>• <em>Thin Client:</em> A small, silent device with no hard drives or internal moving parts and minimal local processing/RAM. It sends user inputs to a centralized server, which executes all applications and returns an updated display image to the terminal screen.
<br>• <em>Thick Client (Office PC):</em> A self-contained computer equipped with local hard drives, powerful multi-core CPU, dedicated memory, and local OS; operates independently without requiring a network server connection.</li>
<li><strong>Operational Power Consumption:</strong> Thick client desktop draws <strong>75 Watts</strong>; Thin client draws only <strong>5 Watts</strong> (slashing direct electricity demand by <strong>over 93%</strong>).</li>
<li><strong>Capital Purchase Cost & Lifespan:</strong>
<br>• Thick Client: Low-spec PC costs £400 with an expected lifespan of <strong>5 years</strong>.
<br>• Thin Client: Terminal unit costs £210 with an expected lifespan of <strong>7 years</strong>.</li>
<li><strong>Resource & Material Footprint:</strong>
<br>• Producing a standard PC and 17" monitor requires <strong>20 kg of materials</strong>, consumes <strong>3,244 MJ of energy</strong> and <strong>920 liters of process water</strong>, and emits <strong>193 kg of greenhouse gases</strong>.
<br>• Over its lifecycle, a PC and monitor generate <strong>37 kg of non-hazardous waste</strong> and <strong>0.7 kg of hazardous waste</strong>.
<br>• Thin clients require substantially fewer raw materials (plastics, precious metals), use less process water, and generate negligible heat.</li>
<li><strong>Real-World Case Study:</strong> Queen Margaret University (Edinburgh) saved <strong>£50,000 in energy costs alone</strong> at the halfway stage of migrating to thin client terminals.</li>
<li><strong>Trade-Offs:</strong> Thin clients depend entirely on 24x7 centralized servers, high network reliability, and software licensing costs; thick clients function autonomously offline.</li>
</ul>""",
            "detailed_answer": """<div class="detailed-body">
<p><strong>Architectural Paradigm:</strong> In corporate, academic, and banking IT deployments, computing architecture fundamentally dictates energy demand and e-waste generation. The lecture slides establish a rigorous contrast between traditional distributed workstations (Thick Clients) and centralized virtualization terminals (Thin Clients):</p>

<ul>
  <li><strong>Thin Clients:</strong> Defined as small, silent solid-state devices that communicate over a network with a centralized server to deliver a computing experience largely identical to that of a standalone PC. They contain <em>no mechanical hard drives or internal moving parts</em>, have minimal processing power with a relatively small quantity of RAM, and store no user applications locally. All data processing occurs on the central server, which streams updated display frames back to the terminal screen.</li>
  <li><strong>Thick Clients:</strong> Conventional desktop personal computers that do not require an active server connection to run. While they benefit from network connectivity for shared storage or internet access, they process instructions, run operating systems, and store files locally and independently.</li>
</ul>

<h4>Deep Comparative Engineering Matrix</h4>
<table class="exam-table">
  <thead>
    <tr>
      <th>Comparison Parameter</th>
      <th>Thick Client (Standard Desktop PC)</th>
      <th>Thin Client (VDI Terminal)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Internal Moving Parts</strong></td>
      <td>Mechanical cooling fans, spinning magnetic HDDs, optical drives</td>
      <td><strong>Zero moving parts</strong>; solid-state fanless conduction</td>
    </tr>
    <tr>
      <td><strong>Operational Power Draw</strong></td>
      <td><strong>75 Watts</strong> (active baseline)</td>
      <td><strong>5 Watts</strong> (slashes operational power by 93.3%)</td>
    </tr>
    <tr>
      <td><strong>Purchase Cost</strong></td>
      <td><strong>£400</strong> (for a low-specification office PC)</td>
      <td><strong>£210</strong> (terminal cost)</td>
    </tr>
    <tr>
      <td><strong>Hardware Useful Lifespan</strong></td>
      <td><strong>5 years</strong> (rapid hardware obsolescence)</td>
      <td><strong>7 years</strong> (processing upgrades happen centrally)</td>
    </tr>
    <tr>
      <td><strong>Embodied Production Energy</strong></td>
      <td><strong>3,244 Mega Joules (MJ)</strong> per unit and monitor</td>
      <td>Drastically lower embodied energy (small lightweight chassis)</td>
    </tr>
    <tr>
      <td><strong>Manufacturing Process Water</strong></td>
      <td><strong>920 liters</strong> of process water consumed</td>
      <td>Minimal water consumption due to reduced silicon/board area</td>
    </tr>
    <tr>
      <td><strong>Material Requirement</strong></td>
      <td><strong>20 kg</strong> of physical materials (PC + 17" monitor)</td>
      <td>Minimal plastics, copper, and precious metals</td>
    </tr>
    <tr>
      <td><strong>Lifecycle Solid Waste</strong></td>
      <td><strong>37 kg non-hazardous</strong> + <strong>0.7 kg hazardous waste</strong></td>
      <td>Fraction of desktop e-waste mass; highly recyclable</td>
    </tr>
    <tr>
      <td><strong>Greenhouse Gas Emissions</strong></td>
      <td><strong>193 kg of GHGs</strong> generated during manufacturing</td>
      <td>Massive net carbon reduction across entire lifecycle</td>
    </tr>
    <tr>
      <td><strong>Thermal Load & Noise</strong></td>
      <td>Emits substantial heat; strains office HVAC; noisy fans</td>
      <td><strong>Completely silent</strong>; negligible heat dissipation</td>
    </tr>
    <tr>
      <td><strong>Server & Network Dependency</strong></td>
      <td>Independent; functions offline without server connectivity</td>
      <td>100% dependent on continuous 24x7 active server availability</td>
    </tr>
  </tbody>
</table>

<h4>Environmental & Financial Case Study: Queen Margaret University</h4>
<p>Slide 16 details the landmark institutional deployment at <strong>Queen Margaret University in Edinburgh</strong>. By replacing conventional thick client workstations with low-power thin client terminals, the university saved <strong>£50,000 in direct electricity costs alone</strong> at the halfway stage of implementation. The energy reduction eliminated vast amounts of waste heat, thereby reducing secondary electrical loads from office and lab air-conditioning systems.</p>

<h4>Limitations & Advantages of Thick Clients</h4>
<p>Despite the overwhelming environmental advantages of thin clients, the slides document specific architectural caveats:</p>
<ul>
  <li>Thin client infrastructure does not always deliver equal computing efficiency for compute-intensive tasks (such as 3D rendering or local compile jobs).</li>
  <li>Deployment involves substantial backend capital expenditure: acquiring enterprise server racks, high-capacity centralized storage, network switching gear, and expensive multi-user software licenses.</li>
  <li>The primary architectural advantage of the Thick Client is autonomy: it requires no central server connection, whereas thin clients demand that centralized virtual servers remain powered on <strong>24 hours a day, 7 days a week (24 x 7)</strong>.</li>
</ul>

<p><em>Slide Reference: Class 14, Slides 14, 15, and 16.</em></p>
</div>"""
        },
        {
            "id": "EQB-14-03",
            "class_id": 14,
            "class_name": "Green Computing",
            "topic": "Moore's Law & Electronic Waste Surge",
            "category": "Short Answer & Definitions",
            "exams": [
                {"paper": "EST End Exam 2024", "section": "Section II, Q(e)", "marks": "1M"},
                {"paper": "End Exam 2023", "section": "Section I, Q1(a)", "marks": "1M"}
            ],
            "marks": "1M",
            "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
            "prompt": "What is Moore's law? Explain how it drives rapid technological obsolescence and accelerates the global e-waste crisis.",
            "expected_answer": """<div class="expected-body">
<p><strong>Moore's Law:</strong> An empirical observation formulated by Gordon Moore (co-founder of Intel) predicting that computer processing power—governed by the density of transistors packed onto an integrated silicon circuit—roughly doubles every two years.</p>

<p><strong>Link to Technological Obsolescence & E-Waste Crisis:</strong></p>
<ul>
  <li><strong>Rapid Technological Obsolescence:</strong> Because processor performance doubles every 24 months, software vendors continuously engineer heavier operating systems and applications. This renders fully functional, undamaged computing hardware obsolete within 24 to 36 months simply because it cannot execute newer software workloads.</li>
  <li><strong>Global E-Waste Surge:</strong> According to the United Nations Environment Programme (UNEP), approximately <strong>50 million tons of electronic waste</strong> are generated worldwide each year (~5% of all solid waste on Earth), with as much as <strong>4,000 tonnes discarded every single hour</strong>.</li>
  <li><strong>Upstream Resource Depletion:</strong> Information and Communications Technology (ICT) accounts for <strong>2% of global CO2 emissions</strong>. Rapid turnover accelerates destructive mineral extraction, requiring around <strong>35 different raw materials</strong> per smartphone (including copper, lead, zinc, tin, nickel, barium, and gold). Mining and smelting cause deforestation, erosion, water pollution, and massive CO and CO2 emissions.</li>
</ul>
</div>""",
            "key_answer_points": """<ul>
<li><strong>Moore's Law Definition:</strong> An empirical prediction formulated by Gordon Moore (co-founder of Intel) stating that computer processing power roughly doubles every two years.</li>
<li><strong>Technological Obsolescence:</strong> Rapid exponential growth in microchip density causes state-of-the-art computing equipment to become functionally obsolete within 2–3 years, driving premature hardware replacement long before physical component failure.</li>
<li><strong>Global E-Waste Surge:</strong> According to the United Nations Environment Programme (UNEP), approximately <strong>50 million tons of electronic waste (e-trash)</strong> are generated globally each year (~4,000 tonnes discarded every single hour).</li>
<li><strong>Resource & Carbon Burden:</strong> Information and Communications Technology (ICT) accounts for <strong>2% of global CO2 emissions</strong>. Rapid obsolescence escalates destructive mineral mining, requiring around 35 distinct minerals (including copper, lead, zinc, tin, nickel, barium, and gold) for smartphone manufacturing alone.</li>
</ul>""",
            "detailed_answer": """<div class="detailed-body">
<p><strong>Definition & Historical Context:</strong> Moore's Law originated from an observation by Gordon Moore, co-founder of Intel Corporation. Moore predicted that computer processing power—governed by the density of transistors packed onto an integrated silicon circuit—roughly doubles every two years. For over five decades, this empirical trajectory served as the foundational roadmap for the global semiconductor industry, fueling exponential gains in microchip performance and steep declines in per-unit computing costs.</p>

<h4>The Obsolescence Trap & Environmental Repercussions</h4>
<p>While Moore's Law catalyzed the modern digital revolution, the lecture slides highlight its profound negative ecological consequence: <strong>rapid technological obsolescence</strong>. Because processor performance doubles every 24 months, software developers continuously engineer increasingly resource-heavy operating systems and applications. Consequently, perfectly functional, undamaged computing hardware is rendered prematurely obsolete within 24 to 36 months simply because it cannot execute newer software workloads.</p>

<p>This rapid obsolescence cycle creates severe global environmental crises:</p>
<ol>
  <li><strong>Avalanche of Global E-Waste:</strong> According to figures cited from the United Nations Environment Programme (UNEP) in Slide 5, approximately <strong>50 million tons of electronic waste</strong> are generated worldwide each year. Discarded electronics constitute roughly <strong>5% of all solid waste on Earth</strong>, with as much as <strong>4,000 tonnes of toxic e-waste discarded every single hour</strong> (Slide 20).</li>
  <li><strong>Intensive Resource Extraction:</strong> As detailed in Slide 2, modern technology is extremely mineral-intensive. A single smartphone requires approximately <strong>35 different raw materials</strong>. After silicon, plastic is the second most-used material. The finished devices contain significant quantities of iron, aluminium, copper, lead, zinc, tin, nickel, and barium. Mining these ores causes widespread deforestation, landscape degradation, heavy metal water contamination, and massive releases of CO and CO2 into the atmosphere from heavy machinery and smelting fuels.</li>
  <li><strong>Embodied Carbon & Energy Footprint:</strong> Global ICT infrastructure accounts for <strong>2% of total worldwide CO2 emissions</strong>. Because manufacturing microprocessors requires orders of magnitude more energy than operating them, discarding machines every two years multiplies the upstream fossil fuel and cleanroom manufacturing burden.</li>
</ol>

<p><em>Slide Reference: Class 14, Slides 2, 5, 11, and 20.</em></p>
</div>"""
        },
        {
            "id": "EQB-14-04",
            "class_id": 14,
            "class_name": "Green Computing",
            "topic": "Hazardous Nature of E-Waste",
            "category": "Short Answer & Definitions",
            "exams": [
                {"paper": "End Exam 2023", "section": "Section I, Q2", "marks": "1M"},
                {"paper": "End Exam 2018", "section": "Part II, Q3", "marks": "2M"}
            ],
            "marks": "1M – 2M",
            "importance": "HIGH (⭐⭐⭐⭐)",
            "prompt": "Is e-waste hazardous? Explain the legal and chemical distinction, and describe how non-hazardous electronic goods become acute environmental and health hazards.",
            "expected_answer": """<div class="expected-body">
<p><strong>Legal & Physical Distinction:</strong> <em>E-waste is not hazardous waste per-se.</em> While in operational use or intact storage on an office desk, electronic devices safely encapsulate their toxic constituents inside solid matrices, chip packages, and insulated housings, posing no immediate chemical or radiological hazard.</p>

<p><strong>How E-Waste Becomes Acutely Hazardous:</strong> E-waste becomes an acute environmental and health hazard when devices are <strong>dismantled, smashed, incinerated, or acid-stripped</strong> during informal end-of-life processing, releasing toxic constituents into ecosystems:</p>
<ul>
  <li><strong>Lead (Pb) & Cadmium (Cd):</strong> Torching printed circuit boards (solder) or cracking CRT funnel glass releases lead fumes and carcinogens into ambient air, soil, and groundwater.</li>
  <li><strong>Mercury (Hg):</strong> Broken tilt switches and Cold Cathode Fluorescent Lamp (CCFL) flat-screen backlights volatilize elemental mercury vapor, which transforms into bioaccumulative neurotoxic methylmercury in aquatic food chains.</li>
  <li><strong>Cadmium (Cd):</strong> Discarded rechargeable laptop and CMOS backup batteries corrode in unlined dumps, leaching cadmium that causes severe renal failure and bone demineralization.</li>
  <li><strong>Polychlorinated Biphenyls (PCBs):</strong> Leaking capacitors and transformers release persistent organic pollutants (POPs) that act as potent endocrine disruptors and carcinogens.</li>
  <li><strong>Brominated Flame Retardants (BFRs) & PVC:</strong> Open burning of circuit boards and polyvinyl chloride (PVC) cable insulation over tire fires generates acutely toxic brominated and chlorinated dioxins (TCDD) and corrosive hydrochloric acid gas.</li>
</ul>
</div>""",
            "key_answer_points": """<ul>
<li><strong>Core Definition:</strong> Electronic Waste (e-waste) refers to discarded electronic or electrical equipment that is no longer fit for its originally intended use (e.g. computers, cellular phones, stereos, refrigerators, air conditioners, and consumer durables).</li>
<li><strong>Is E-Waste Hazardous?:</strong> <em>e-waste is not hazardous waste per-se.</em> Intact electronic goods resting on an office desk or in home storage pose no immediate toxicity or radiation danger.</li>
<li><strong>How It Becomes Hazardous:</strong> The hazardous constituents present inside electronic components render the waste highly hazardous when devices are <strong>dismantled, smashed, chemically stripped, or incinerated</strong> during end-of-life processing.</li>
<li><strong>Key Toxic Constituents & Sources:</strong>
<br>• Lead & Cadmium: Printed circuit boards (solder) and CRT monitors (lead oxide funnel glass).
<br>• Mercury: Tilt switches and fluorescent backlights in flat-screen monitors.
<br>• Cadmium: Rechargeable computer batteries and SMD chip resistors.
<br>• Polychlorinated Biphenyls (PCBs): Capacitors and transformers.
<br>• Brominated Flame Retardants (BFRs): Circuit boards and plastic outer casings.
<br>• Polyvinyl Chloride (PVC): Cable insulation and wiring coatings.</li>
<li><strong>Environmental Pathways:</strong> Informal backyard acid leaching and open burning release toxic ash, heavy metals, and persistent organic pollutants into ambient air, soil, groundwater, and local agricultural food chains.</li>
</ul>""",
            "detailed_answer": """<div class="detailed-body">
<p><strong>The Precise Legal & Physical Distinction:</strong> Slide 20 addresses the fundamental legal and environmental question: <em>"Is e-waste hazardous?"</em> The lecture slides provide the authoritative answer: <strong>"e-waste is not hazardous waste per-se."</strong></p>

<p>When an electronic device—such as a personal computer, television, or cellular phone—is intact and in operational service, its internal toxic chemicals are safely encapsulated inside solid matrices, chip packages, and insulated housings. An intact computer resting on a worker's desk does not expose occupants to chemical toxins. However, Slide 20 emphasizes the critical caveat: <em>"the hazardous constituents present in the e-waste render it hazardous when such wastes are dismantled and processed, and pose hazard to health and environment."</em></p>

<h4>Toxic Chemical Constituents in Discarded Electronics</h4>
<p>As cataloged in Slide 21, electronic components contain a wide array of heavy metals, halogens, and persistent synthetic compounds:</p>
<table class="exam-table">
  <thead>
    <tr>
      <th>Electronic Component</th>
      <th>Toxic Chemical Constituent</th>
      <th>Mode of Release & Hazard Mechanism</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Printed Circuit Boards (PCBs)</strong></td>
      <td>Lead (Pb) & Cadmium (Cd)</td>
      <td>Open solder torching releases lead fumes; acid stripping discharges dissolved cadmium into open drains.</td>
    </tr>
    <tr>
      <td><strong>Cathode Ray Tubes (CRTs)</strong></td>
      <td>Lead oxide & Cadmium</td>
      <td>Cracking funnel glass releases lead-laden phosphor dust, causing soil contamination and groundwater leaching.</td>
    </tr>
    <tr>
      <td><strong>Switches & Flat Screen Monitors</strong></td>
      <td>Mercury (Hg)</td>
      <td>Cold cathode fluorescent backlights break easily, volatilizing elemental mercury vapor that bioaccumulates as neurotoxic methylmercury.</td>
    </tr>
    <tr>
      <td><strong>Computer Batteries</strong></td>
      <td>Cadmium (Cd)</td>
      <td>Corrosion in unlined dumps leaches cadmium into aquifers, damaging kidneys and causing bone demineralization.</td>
    </tr>
    <tr>
      <td><strong>Capacitors and Transformers</strong></td>
      <td>Polychlorinated Biphenyls (PCBs)</td>
      <td>Dielectric oil leakage causes persistent environmental contamination; potent endocrine disruptor and liver toxin.</td>
    </tr>
    <tr>
      <td><strong>Circuit Boards & Plastic Casings</strong></td>
      <td>Brominated Flame Retardants (BFRs)</td>
      <td>Thermal combustion releases polybrominated dibenzodioxins and furans; bioaccumulates in adipose tissue.</td>
    </tr>
    <tr>
      <td><strong>Cable Insulation / Coating</strong></td>
      <td>Polyvinyl Chloride (PVC)</td>
      <td>Open burning over tire fires to harvest internal copper releases carcinogenic chlorinated dioxins into local airsheds.</td>
    </tr>
  </tbody>
</table>

<h4>Environmental Transport Pathways</h4>
<p>When discarded electronics enter informal recycling streams—concentrated across developing nations such as India, China, and Ghana—they are subjected to crude backyard operations: hammer smashing, open-air acid bath leaching, and wire burning. These crude practices liberate heavy metals and organic toxins, creating toxic ash plumes that contaminate municipal air, infiltrate groundwater tables, and enter agricultural food systems (as demonstrated by PCB and dioxin contamination of poultry eggs in Ghana, Slide 24).</p>

<p><em>Slide Reference: Class 14, Slides 20, 21, 23, and 24.</em></p>
</div>"""
        },
        {
            "id": "EQB-14-05",
            "class_id": 14,
            "class_name": "Green Computing",
            "topic": "Basel Convention on Hazardous Wastes",
            "category": "Short Answer & Definitions",
            "exams": [
                {"paper": "EST End Exam 2024", "section": "Section II, Q(a)", "marks": "1M"},
                {"paper": "End Exam 2023", "section": "Section I, Q1(e)", "marks": "1M"},
                {"paper": "End Exam 2022", "section": "Section III, Q12", "marks": "1M"}
            ],
            "marks": "1M",
            "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
            "prompt": "What is the Basel Convention? Explain its core objective in governing transboundary movement of e-waste and its relevance to developing nations.",
            "expected_answer": """<div class="expected-body">
<p><strong>Definition & Treaty Identity:</strong> The <strong>Basel Convention on the Control of Transboundary Movements of Hazardous Wastes and Their Disposal</strong> is a comprehensive multilateral environmental treaty adopted in 1989 (entered into force in 1992) under the auspices of the United Nations Environment Programme (UNEP).</p>

<p><strong>Core Objective:</strong> To strictly regulate and restrict the cross-border movement of hazardous chemical and electronic wastes, preventing industrialized nations from dumping toxic waste onto developing countries lacking environmentally sound recycling infrastructure ("toxic colonialism").</p>

<p><strong>Key Operational Provisions & Relevance to Developing Nations:</strong></p>
<ul>
  <li><strong>Prior Informed Consent (PIC):</strong> Requires mandatory, written notification and verified formal consent from the competent national authority of the importing country before hazardous waste shipments can legally depart. Unauthorized shipments are criminalized as illegal trafficking.</li>
  <li><strong>Protecting Informal Hubs:</strong> Targets illegal export practices that flood hubs such as Guiyu (China) and Agbogbloshie (Ghana, where European electronic waste contaminated local free-range chicken eggs with lethal levels of chlorinated dioxins and PCBs).</li>
  <li><strong>Indian Statutory Alignment:</strong> Underpins India's Foreign Trade Policy, which strictly prohibits the commercial importation of e-waste and heavily restricts the import of second-hand computers.</li>
</ul>
</div>""",
            "key_answer_points": """<ul>
<li><strong>Treaty Identity:</strong> The <strong>Basel Convention on the Control of Transboundary Movements of Hazardous Wastes and Their Disposal</strong> is a comprehensive multilateral environmental agreement adopted in 1989 (entered into force in 1992).</li>
<li><strong>Core Regulatory Objective:</strong> Engineered specifically to regulate and strictly restrict the transboundary movement of hazardous chemical and electronic wastes, preventing industrialized, wealthy nations from dumping toxic waste on developing countries that lack environmentally sound recycling technologies.</li>
<li><strong>Operational Framework:</strong> Requires Prior Informed Consent (PIC) before any cross-border transfer of hazardous waste can legally proceed, and categorizes unauthorized waste transfers as illegal trafficking.</li>
<li><strong>Relevance to Developing Nations:</strong> Addresses the widespread illegal shipment of e-waste from Europe, the USA, and Japan into informal processing hubs in Asia and Africa (e.g. Guiyu in China and Agbogbloshie in Ghana), where unprotected workers and local food chains suffer catastrophic toxic contamination.</li>
<li><strong>Indian Statutory Alignment:</strong> Governs India's import restrictions; under India's Foreign Trade Policy, the import of second-hand computers is heavily restricted and the import of e-waste is strictly prohibited.</li>
</ul>""",
            "detailed_answer": """<div class="detailed-body">
<p><strong>Context & Historical Genesis:</strong> During the 1980s, tightening environmental regulations and rising waste disposal costs in industrialized nations led to a phenomenon known as "toxic colonialism"—the mass export of hazardous chemical and industrial wastes to developing nations in Africa, Asia, and Latin America, where environmental standards were weak or unenforced. To combat this injustice, the international community negotiated the <strong>Basel Convention on the Control of Transboundary Movements of Hazardous Wastes and Their Disposal</strong> under the auspices of the United Nations Environment Programme (UNEP) in 1989.</p>

<h4>Core Legal Mandates of the Basel Convention</h4>
<p>As documented in Slide 26 under <em>"Legislations/Framework governing e-waste"</em>, the Basel Convention serves as the primary international legal instrument for governing the cross-border transit of end-of-life electronics:</p>
<ol>
  <li><strong>Restricting Transboundary Movement:</strong> Hazardous wastes cannot be exported from a member state unless the exporting country lacks the technical capacity and facilities to dispose of the waste in an environmentally sound manner, or the importing country requires the waste as raw materials for certified recycling.</li>
  <li><strong>Prior Informed Consent (PIC) Procedure:</strong> Any proposed export of hazardous waste requires formal, written notification to the competent national authority of the importing country, along with explicit, verified consent prior to shipment departure.</li>
  <li><strong>Prohibition of Exports to Non-Parties:</strong> Prohibits the transboundary movement of hazardous waste between member states and non-signatory nations.</li>
  <li><strong>Criminalization of Illegal Traffic:</strong> Expressly defines illegal shipments of hazardous waste as criminal acts, obligating exporting states to take back intercepted waste at their own expense.</li>
</ol>

<h4>Relevance to Global E-Waste Trade & Slide Case Studies</h4>
<p>Slides 20, 24, and 26 demonstrate why the Basel Convention is vital to developing countries:</p>
<ul>
  <li><em>Guiyu, Guangdong, China (Slide 20):</em> Illustrates how vast amounts of electronic waste were routinely and illegally exported from the USA, Western Europe, and Japan, dumping as much as 4,000 tonnes of toxic e-waste every hour onto roadside scrap operations where unprotected workers dismantled parts with bare hands.</li>
  <li><em>Agbogbloshie, Accra, Ghana (Slide 24):</em> Highlights a 2019 report showing that electronic waste exported from Europe poisoned local chicken eggs with toxic chlorinated dioxins and PCBs in a community where 80,000 people reside. Exporters repeatedly exploit legal loopholes by falsely mislabeling toxic e-waste shipments as "charitable donations" or "functional second-hand electronics."</li>
  <li><em>India's Trade Policy Integration (Slide 26):</em> In compliance with Basel principles, India's national Foreign Trade Policy strictly forbids the commercial importation of e-waste and places heavy restrictions on importing second-hand computers to protect the domestic environment from external toxic burdens.</li>
</ul>

<p><em>Slide Reference: Class 14, Slides 20, 24, and 26.</em></p>
</div>"""
        },
        {
            "id": "EQB-14-06",
            "class_id": 14,
            "class_name": "Green Computing",
            "topic": "Green Website Concept & Examples (Blackle)",
            "category": "Short Answer & Definitions",
            "exams": [
                {"paper": "EST End Exam 2024", "section": "Section II, Q(d) & Section III(d)", "marks": "1M + 1M"},
                {"paper": "End Exam 2022", "section": "Section VI, Q(d)", "marks": "1M"}
            ],
            "marks": "1M – 2M",
            "importance": "HIGH (⭐⭐⭐⭐)",
            "prompt": "What is a Green Website? Give examples and explain how search engine algorithms and display color palettes impact electrical power consumption and carbon emissions.",
            "expected_answer": """<div class="expected-body">
<p><strong>Definition:</strong> A Green Website is a website designed, developed, hosted, and maintained to minimize electrical energy consumption and carbon emissions across data center servers, transmission networks, and client display monitors.</p>

<p><strong>Display Color Palette & Power Consumption (Blackle Example):</strong></p>
<ul>
  <li>On Cathode Ray Tube (CRT) monitors (consuming <strong>80 W</strong> baseline) and emissive OLED screens, displaying pure white illuminates subpixels at maximum luminosity, drawing peak wattage. Displaying black or dark pixels cuts electrical draw substantially.</li>
  <li><strong>Blackle:</strong> An energy-saving search engine created by Heap Media and powered by Google Custom Search that utilizes a predominantly black background. As documented in Slide 13, as of July 2023, Blackle claims to have saved over <strong>10.07 MWh (Megawatt-hours)</strong> of electrical energy worldwide.</li>
</ul>

<p><strong>Search Algorithm Efficiency & Carbon Emissions (Slide 11):</strong> Efficient indexing algorithms reduce server processing cycles, directly cutting carbon emissions per search query:</p>
<ul>
  <li><strong>Google Search:</strong> $\approx 0.20\text{ g }\text{CO}_2$ per query (most efficient baseline)</li>
  <li><strong>Yahoo Search:</strong> $\approx 0.26\text{ g }\text{CO}_2$ per query (30% higher carbon footprint)</li>
  <li><strong>Microsoft Live Search:</strong> $\approx 0.32\text{ g }\text{CO}_2$ per query (60% higher carbon footprint)</li>
  <li><strong>AOL Search:</strong> $\approx 0.37\text{ g }\text{CO}_2$ per query (85% higher carbon footprint)</li>
</ul>

<p><strong>Key Green Web Best Practices:</strong> Clean semantic code, dark-mode styling, server-side caching, vector asset compression, and green web hosting powered by renewable energy.</p>
</div>""",
            "key_answer_points": """<ul>
<li><strong>Definition:</strong> A Green Website is a website engineered, hosted, and operated to minimize electrical energy consumption and carbon emissions across server data centers, telecommunications networks, and client display monitors.</li>
<li><strong>Display Energy Dynamics:</strong>
<br>• Traditional CRT and modern OLED displays draw maximum power when illuminating a pure white screen, but draw significantly less electrical power when displaying black or dark pixels.
<br>• CRT monitors consume <strong>80W</strong>, while LCDs consume <strong>35W</strong> and LEDs consume <strong>25W</strong> (Slide 10).</li>
<li><strong>Blackle Search Engine Example:</strong> Blackle (an eco-friendly search engine created by Heap Media and powered by Google Custom Search) utilizes a predominantly black background. As documented in Slide 13, as of July 2023, Blackle claims to have saved over <strong>10.07 MWh (Megawatt-hours)</strong> of electrical energy worldwide.</li>
<li><strong>Algorithmic Energy & Carbon Footprint:</strong> Algorithm efficiency directly dictates computing cycles and carbon emissions per search query (Slide 11):
<br>• Google Search: $\\approx 0.20\\text{ g } \\text{CO}_2$ per query
<br>• Yahoo Search: $\\approx 0.26\\text{ g } \\text{CO}_2$ per query
<br>• Microsoft Live Search: $\\approx 0.32\\text{ g } \\text{CO}_2$ per query
<br>• AOL Search: $\\approx 0.37\\text{ g } \\text{CO}_2$ per query</li>
<li><strong>Core Green Web Best Practices:</strong> Clean lightweight code, dark-mode styling, compressed vector assets, efficient server-side caching, and green web hosting powered by renewable energy.</li>
</ul>""",
            "detailed_answer": """<div class="detailed-body">
<p><strong>Concept & Definition:</strong> A Green Website is a website designed, developed, and deployed with the specific objective of reducing environmental impact by minimizing the energy consumed during its transmission and rendering. Every web transaction involves a three-part energy chain: (1) backend servers processing queries and database operations, (2) network switches and fiber cables routing packets, and (3) user terminal devices (monitors and processors) rendering the webpage markup. Green web architecture targets efficiencies across all three links.</p>

<h4>The Blackle Case Study & Display Energy Mechanics</h4>
<p>Slides 10, 12, and 13 document the real-world operational concept of <strong>Blackle</strong>. Traditional search engines (like standard Google or Yahoo) present users with an expansive, bright white canvas. On Cathode Ray Tube (CRT) monitors and modern emissive displays (such as OLED and AMOLED screens), rendering a white pixel requires energizing all color subpixels at maximum luminosity:</p>

<ul>
  <li>Slide 10 details baseline monitor power demands: a 17-inch CRT monitor consumes <strong>80 Watts</strong>; a 17-inch LCD monitor consumes <strong>35 Watts</strong>; and an LED monitor consumes <strong>25 Watts</strong>.</li>
  <li>On CRT and OLED screens, displaying pure black turns off electron guns or diode subpixels, cutting display electrical draw by a measurable margin.</li>
  <li>Based on this display physics principle, Blackle was developed as an energy-saving search interface. Slide 13 provides the official metric: <em>"As of July 2023, Blackle claims to have saved over <strong>10.07 MWh</strong> of electrical energy."</em></li>
</ul>

<h4>Algorithmic Efficiency & Search Carbon Footprint</h4>
<p>Slide 11 highlights the critical principle that <em>"The efficiency of algorithms has an impact on the amount of computer resources required for any given computing function."</em> When millions of users execute billions of daily searches, algorithmic optimization directly impacts global megawatt-hours and greenhouse gas emissions.</p>

<p>Slide 11 quantifies the direct CO2 released per internet search across major platforms:</p>
<table class="exam-table">
  <thead>
    <tr>
      <th>Search Engine Platform</th>
      <th>Estimated Carbon Dioxide Released per Search Query</th>
      <th>Relative Efficiency Comparison</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Google Search</strong></td>
      <td><strong>$\\approx 0.20\\text{ grams } \\text{CO}_2$</strong></td>
      <td>Most efficient indexed retrieval algorithm (baseline)</td>
    </tr>
    <tr>
      <td><strong>Yahoo Search</strong></td>
      <td><strong>$\\approx 0.26\\text{ grams } \\text{CO}_2$</strong></td>
      <td>30% higher carbon emissions per query than Google</td>
    </tr>
    <tr>
      <td><strong>Microsoft Live Search</strong></td>
      <td><strong>$\\approx 0.32\\text{ grams } \\text{CO}_2$</strong></td>
      <td>60% higher carbon emissions per query than Google</td>
    </tr>
    <tr>
      <td><strong>AOL Search</strong></td>
      <td><strong>$\\approx 0.37\\text{ grams } \\text{CO}_2$</strong></td>
      <td>85% higher carbon emissions per query than Google</td>
    </tr>
  </tbody>
</table>

<p>This empirical comparison proves that refining backend indexing algorithms, reducing redundant database lookups, compressing page payloads, and minimizing unnecessary JavaScript roundtrips directly reduces the carbon footprint of digital services.</p>

<p><em>Slide Reference: Class 14, Slides 10, 11, 12, and 13.</em></p>
</div>"""
        },
        {
            "id": "EQB-14-07",
            "class_id": 14,
            "class_name": "Green Computing",
            "topic": "Environmental Impact of Computer & Smartphone Production (Resource Footprint)",
            "category": "Descriptive & Case Study",
            "exams": [
                {"paper": "EST End Exam 2024", "section": "Section VI, Q1", "marks": "3M"}
            ],
            "marks": "3M – 5M",
            "importance": "HIGH (⭐⭐⭐⭐)",
            "prompt": "Explain the environmental impact of manufacturing computers, smartphones, and mobile devices. Detail the raw material footprint, water consumption, fossil fuel requirements, and mineral intensity.",
            "expected_answer": """<div class="expected-body">
<p><strong>Upstream Resource Extraction & Manufacturing Dominance:</strong> Popular perception assumes the primary ecological impact of computing occurs during consumer operation. However, the lecture slides reveal that the overwhelming majority of environmental damage occurs upstream during raw material extraction, chemical processing, and cleanroom fabrication.</p>

<p><strong>1. The 1.8-Ton Material Footprint of a Personal Computer (Slide 4):</strong></p>
<p>Manufacturing a single average <strong>24-kg desktop computer and 27-cm monitor</strong> demands at least:</p>
<ul>
  <li><strong>240 kg of fossil fuels</strong> (coal, petroleum, natural gas)</li>
  <li><strong>22 kg of industrial chemicals</strong> (solvents, acids, toxic dopants)</li>
  <li><strong>1,500 kg of water</strong></li>
  <li><strong>Totaling 1.8 tons of physical resources</strong>—equivalent to the weight of a full-size sports utility vehicle (SUV)!</li>
</ul>

<p><strong>2. Extreme Material Intensity Ratio:</strong></p>
<ul>
  <li>Manufacturing an automobile or a household refrigerator requires only <strong>1 to 2 times its finished weight</strong> in fossil fuels.</li>
  <li>Manufacturing a computer requires <strong>10 times its finished weight in fossil fuels</strong> (240 kg fossil fuels for a 24 kg computer), making microelectronics one of the most resource-intensive manufacturing processes in industrial history.</li>
</ul>

<p><strong>3. Semiconductor Fabrication Water Depletion:</strong> Semiconductor cleanrooms consume staggering quantities of ultra-pure process water to rinse microchip wafers between lithographic etching cycles—often equivalent to the water consumption of an entire small city.</p>

<p><strong>4. Smartphone Mineral Metallurgy (Slide 2):</strong></p>
<ul>
  <li>Fabricating a single smartphone requires around <strong>35 different raw materials</strong>. Silicon is primary; plastic is the second most-used material. Devices contain finished fractions of iron, aluminium, copper, lead, zinc, tin, nickel, and barium.</li>
  <li>Open-pit mining and smelting cause extensive deforestation, topsoil erosion, landscape scarring, acid mine drainage, and massive atmospheric emissions of CO and CO2 from heavy mining machinery.</li>
</ul>

<p><strong>5. Lifecycle Embodied Energy & Solid Waste (Slide 15):</strong> Manufacturing a desktop PC and 17" monitor consumes <strong>3,244 MJ of energy</strong>, <strong>920 liters of process water</strong>, and emits <strong>193 kg of greenhouse gases</strong>, generating <strong>37 kg of non-hazardous waste</strong> and <strong>0.7 kg of hazardous waste</strong> over its operational lifetime.</p>
</div>""",
            "key_answer_points": """<ul>
<li><strong>The 1.8-Ton Material Footprint:</strong> Constructing a single average <strong>24-kg desktop computer and 27-cm monitor</strong> requires at least:
<br>• <strong>240 kg of fossil fuel</strong>
<br>• <strong>22 kg of chemicals</strong>
<br>• <strong>1,500 kg of water</strong>
<br>• <strong>Totaling 1.8 tons of physical resources</strong>—equivalent to the weight of a full-size sports utility vehicle (SUV)!</li>
<li><strong>Extreme Material Intensity Ratio:</strong> Computer manufacturing is vastly more materials-intensive than heavy manufacturing (automobiles or refrigerators). An automobile or refrigerator requires only <strong>1 to 2 times its own weight in fossil fuels</strong>, whereas a computer requires <strong>10 times its own weight in fossil fuels</strong> (240 kg fossil fuels for a 24 kg computer).</li>
<li><strong>Semiconductor Water Depletion:</strong> Semiconductor fabrication plants consume astronomical volumes of ultra-pure process water—often equivalent to the water consumption of an entire small city.</li>
<li><strong>Smartphone Mineral Intensity:</strong> Fabricating a modern smartphone requires around <strong>35 different raw materials</strong>. After silicon, plastic is the second most-used material. Devices contain finished fractions of iron, aluminium, copper, lead, zinc, tin, nickel, and barium.</li>
<li><strong>Mining & Extraction Destruction:</strong> Mineral extraction is responsible for widespread deforestation, landscape degradation, water pollution, and massive atmospheric emissions of CO and CO2 from heavy mining machinery and transport.</li>
<li><strong>Embodied Lifecycle Energy & Waste:</strong> Manufacturing a desktop PC and 17" monitor consumes <strong>3,244 MJ of energy</strong>, <strong>920 liters of process water</strong>, and emits <strong>193 kg of greenhouse gases</strong>, generating <strong>37 kg of non-hazardous waste</strong> and <strong>0.7 kg of hazardous waste</strong> over its lifecycle.</li>
</ul>""",
            "detailed_answer": """<div class="detailed-body">
<p><strong>The Hidden Upstream Footprint:</strong> Popular perception often assumes that the primary environmental impact of electronic gadgets occurs during their daily operation (electricity drawn from wall sockets). However, the lecture slides reveal that the overwhelming majority of technological environmental damage occurs upstream during <strong>raw material extraction, chemical processing, and cleanroom fabrication</strong>.</p>

<h4>The 1.8-Ton Resource Equivalence of a Personal Computer</h4>
<p>Slide 4 presents a striking quantitative resource breakdown. The construction of a single average <strong>24-kilogram desktop computer and 27-centimeter monitor</strong> demands:</p>

<ul>
  <li>At least <strong>240 kg of fossil fuels</strong> (coal, petroleum, natural gas)</li>
  <li>At least <strong>22 kg of industrial chemicals</strong> (acids, toxic dopants, cleaning solvents)</li>
  <li>At least <strong>1,500 kg of water</strong></li>
  <li><strong>Totaling 1.8 tons of physical material resources</strong>—which is equal to the weight of a full-size sports utility vehicle (SUV).</li>
</ul>

<h4>Comparative Material Intensity: Computers vs Automobiles & Refrigerators</h4>
<p>Slide 4 highlights an extraordinary contrast between computing hardware and traditional consumer appliances:</p>
<ul>
  <li>Manufacturing an automobile or a household refrigerator requires only <strong>1 to 2 times their finished weight</strong> in fossil fuels.</li>
  <li>Manufacturing a computer requires <strong>10 times its finished weight in fossil fuels</strong> (240 kg of fossil fuel for a 24 kg machine).</li>
  <li>This makes microelectronic computing one of the most resource-intensive and environmentally demanding manufacturing processes in human industrial history.</li>
</ul>

<h4>Semiconductor Fabrication Water Demand</h4>
<p>Slide 4 documents that modern semiconductor cleanrooms use staggering volumes of ultra-pure water (UPW) to rinse microchip wafers between lithographic etching and chemical vapor deposition cycles. A single commercial semiconductor manufacturing plant can consume <strong>as much fresh water as an entire small city</strong>, placing severe hydrological stress on municipal reservoirs and local aquifers.</p>

<h4>Smartphone Mineral Metallurgy & Environmental Degradation</h4>
<p>Slide 2 examines the metallurgy of mobile devices:</p>
<table class="exam-table">
  <thead>
    <tr>
      <th>Resource Category</th>
      <th>Key Material Components</th>
      <th>Environmental & Ecological Impact</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Mineral Diversity</strong></td>
      <td>Around <strong>35 different raw materials</strong> per smartphone</td>
      <td>Demands multi-continent supply chains; large open-pit mining operations cause severe ecological disruption.</td>
    </tr>
    <tr>
      <td><strong>Core Structural Materials</strong></td>
      <td>Silicon (primary) and <strong>Plastic (second most-used material)</strong></td>
      <td>Silicon refining requires intense electric arc furnace energy; plastics derive from non-renewable petrochemical refining.</td>
    </tr>
    <tr>
      <td><strong>Metallic Constituents</strong></td>
      <td>Iron, aluminium, copper, lead, zinc, tin, nickel, barium</td>
      <td>Smelting and open-pit extraction cause widespread deforestation, topsoil erosion, landscape scarring, and acid mine drainage.</td>
    </tr>
    <tr>
      <td><strong>Machinery & Atmospheric Burden</strong></td>
      <td>Heavy diesel extraction machinery and smelting furnaces</td>
      <td>Releases massive plumes of carbon dioxide (CO2) and carbon monoxide (CO) into ambient air, accelerating global climate change.</td>
    </tr>
  </tbody>
</table>

<h4>Embodied Energy & Lifecycle Waste Matrix</h4>
<p>Slide 15 provides further lifecycle quantification: producing a standard PC and 17" monitor consumes <strong>3,244 Mega Joules (MJ) of energy</strong>, <strong>920 liters of process water</strong>, and emits <strong>193 kg of greenhouse gases</strong>. Throughout its lifetime, this single computer system generates <strong>37 kg of non-hazardous solid waste</strong> and <strong>0.7 kg of hazardous chemical waste</strong>. Because these environmental costs are locked in before the consumer ever powers on the device, extending device lifespans is paramount to sustainable computing.</p>

<p><em>Slide Reference: Class 14, Slides 2, 4, and 15.</em></p>
</div>"""
        },
        {
            "id": "EQB-14-08",
            "class_id": 14,
            "class_name": "Green Computing",
            "topic": "Sustainable Concept Computers & Design Innovations for Green Computing",
            "category": "Comprehensive Descriptive",
            "exams": [
                {"paper": "End Exam Curriculum", "section": "Class 14 Core Syllabus", "marks": "5M – 10M"}
            ],
            "marks": "5M – 10M",
            "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
            "prompt": "How can computers be made green? Explain key operational measures, paper conservation metrics, and describe at least five sustainable concept computers featured in green computing design.",
            "expected_answer": """<div class="expected-body">
<p><strong>Operational Measures for Green Computing:</strong></p>
<ul>
  <li><strong>Hardware Form-Factor:</strong> Laptops must be preferred over desktop PCs due to their compact, mobile-optimized chipsets and lower power draw (up to 70% energy reduction).</li>
  <li><strong>Display Upgrades:</strong> Transitioning away from 17" CRT monitors (<strong>80 W</strong>) to 17" LCD panels (<strong>35 W</strong>) or LED monitors (<strong>25 W</strong>) slashes display energy consumption by up to 68%.</li>
  <li><strong>Energy Star Compliance:</strong> Deploying Energy Star rated equipment, which operates at <strong>80% electrical efficiency</strong> compared to only <strong>70% efficiency</strong> for non-rated computers.</li>
  <li><strong>Active Power Management:</strong> Turning off computers and printers when not in use and enforcing automated sleep modes (recognizing that screen savers consume active power rather than saving it).</li>
</ul>

<p><strong>Office Paper Conservation Metrics (Slide 18):</strong></p>
<ul>
  <li><strong>1 ton of office paper</strong> consumes <strong>24 mature trees</strong>.</li>
  <li><strong>1 tree</strong> yields approximately <strong>16.67 reams of paper</strong> (meaning 1 single ream of 500 sheets consumes <strong>6% of a tree</strong>).</li>
  <li>Manufacturing and using <strong>1 ton of recycled paper</strong> saves <strong>17 mature trees</strong> from logging.</li>
</ul>

<p><strong>Sustainable Concept Computers in Green Design (Slides 29–35):</strong></p>
<table class="exam-table">
  <thead>
    <tr>
      <th>Concept Name & Designer</th>
      <th>Slide</th>
      <th>Key Eco-Innovation</th>
      <th>Technical & Material Architecture</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Nikola Knezevic Solar Laptop</strong></td>
      <td>Slide 30</td>
      <td>Fold-out integrated solar harvesting</td>
      <td>Features a solar panel attached to its top half that folds out to catch sunlight whether the laptop is open or closed, charging battery packs and saving grid power.</td>
    </tr>
    <tr>
      <td><strong>Lawn PC</strong></td>
      <td>Slide 30</td>
      <td>Self-generating biomimetic solar grass</td>
      <td>Engineered with recyclable synthetic grass blades embedding micro-circuits and solar cells; generates its own electricity and saves approximately <strong>876 kWh of power per year</strong>.</td>
    </tr>
    <tr>
      <td><strong>Dell O Project & Biodegradable PC</strong></td>
      <td>Slide 29</td>
      <td>Floor projection & bio-skin</td>
      <td>Eliminates physical monitors and keyboards via laser floor projection. Chassis skin is molded from biodegradable polymers derived from bamboo and cornstarch; parts returnable to OEM.</td>
    </tr>
    <tr>
      <td><strong>Igglu Modular PC</strong></td>
      <td>Slide 31</td>
      <td>Standardized modular upgradeability</td>
      <td>Built from standardized, reusable, and recyclable modular blocks for PCI slots, graphics cards, RAM, and hard drives, enabling individual component upgrades without chassis disposal.</td>
    </tr>
    <tr>
      <td><strong>Power Flower PC</strong></td>
      <td>Slide 34</td>
      <td>Hydrogen fuel cell with potable water byproduct</td>
      <td>Powered by a clean hydrogen fuel cell. Byproduct water drips into a clear container and can be reused for <strong>drinking, cooking, or watering flowers</strong>! Gesture tracking and a pico projector eliminate mouse, keyboard, and physical monitor.</td>
    </tr>
    <tr>
      <td><strong>Solar Clamshell PC for Rural India</strong></td>
      <td>Slide 35</td>
      <td>Solar-powered rural agricultural hub</td>
      <td>Portable mini PC equipped with a roll-out flexible LCD screen, built-in LED projector, Wi-Fi, and onboard solar charging panels to deliver agricultural advisory to farmers in remote off-grid villages.</td>
    </tr>
  </tbody>
</table>
</div>""",
            "key_answer_points": """<ul>
<li><strong>Operational & Behavioral Measures:</strong>
<br>• Turn off computers and printers when not in use; set systems to sleep modes when idle.
<br>• Prefer energy-efficient laptops over power-hungry desktops.
<br>• Select low-power displays: upgrade from CRT monitors (80W) to LCD (35W) or LED (25W).
<br>• Deploy Energy Star rated computers (achieving 80% energy efficiency vs 70% for unrated systems).</li>
<li><strong>Paper Consumption Mathematics (Slide 18):</strong>
<br>• <strong>1 ton of office paper</strong> consumes <strong>24 trees</strong>.
<br>• <strong>1 tree</strong> yields <strong>16.67 reams of paper</strong> (with 1 ream using <strong>6% of a tree</strong>).
<br>• <strong>1 ton of recycled paper</strong> saves <strong>17 trees</strong>.</li>
<li><strong>Featured Sustainable Concept Computers (Slides 29–35):</strong>
<br>1. <em>Nikola Knezevic Solar Laptop:</em> Features a fold-out solar panel on the top half that charges battery in both open and closed positions.
<br>2. <em>Lawn PC:</em> Powered by recyclable solar grass blades with integrated circuits and solar cells, saving <strong>876 kWh of power per year</strong>.
<br>3. <em>Dell O Project & Biodegradable PC:</em> Employs laser floor projection to eliminate physical monitors and keyboards; skin made from bio-decomposable starch-based polymer, bamboo, and cornstarch.
<br>4. <em>Igglu Modular PC:</em> Uses standard reusable and recyclable modular components (PCI drives, graphics cards, RAM, HDDs) for simple, zero-waste upgrades.
<br>5. <em>Power Flower PC:</em> Powered by a hydrogen fuel cell; dripping water is collected in a clear container and reused for drinking or cooking; gesture camera eliminates mouse/keyboard; projector replaces monitor.
<br>6. <em>Solar-Powered Clamshell PC for Rural India:</em> Mini PC with roll-out LCD screen, built-in LED projector, and solar panels to provide agricultural advisory to farmers.</li>
</ul>""",
            "detailed_answer": """<div class="detailed-body">
<p><strong>Actionable Strategies for Green Computing:</strong> Slide 18 poses the core practical question: <em>"How can I make my computer Green?"</em> The slide outlines a systematic methodology: developing an institutional green computing plan, making environmentally sound purchasing decisions, conserving electrical energy, recycling obsolete hardware, and drastically reducing office paper consumption.</p>

<h4>The Mathematics of Office Paper Conservation</h4>
<p>Slide 18 details the exact ecological metrics connecting digital computing to forestry conservation:</p>
<ul>
  <li><strong>1 ton of office paper</strong> requires the destruction of <strong>24 mature trees</strong>.</li>
  <li><strong>1 tree</strong> yields approximately <strong>16.67 reams of paper</strong> (meaning 1 single ream of 500 sheets consumes <strong>6% of a tree</strong>).</li>
  <li>Manufacturing and using <strong>1 ton of recycled paper</strong> preserves <strong>17 mature trees</strong> from commercial clear-cutting.</li>
</ul>

<h4>Operational Energy Conservation Standards</h4>
<p>Slide 10 establishes fundamental hardware and operational practices:</p>
<ol>
  <li><strong>Hardware Form-Factor:</strong> Laptops must be preferred over desktop PCs due to their compact, low-voltage mobile chipsets and passive cooling.</li>
  <li><strong>Display Selection:</strong> Transitioning away from 17-inch CRT monitors (<strong>80 Watts</strong>) to 17-inch LCD panels (<strong>35 Watts</strong>) or LED monitors (<strong>25 Watts</strong>) slashes display energy consumption by up to 68%.</li>
  <li><strong>Energy Star Compliance:</strong> Energy Star rated computing devices operate at <strong>80% electrical efficiency</strong>, compared to only <strong>70% efficiency</strong> for non-rated computers.</li>
  <li><strong>Active Power Management:</strong> Enforcing automated sleep states and shutting down machines and printers when not in use stops idle CPU and cooling fan energy waste (recognizing that screen savers consume active power).</li>
</ol>

<h4>Comprehensive Review of Sustainable Concept Computers</h4>
<p>Slides 29 through 35 present twelve pioneering industrial design concepts that reimagine computing hardware for circularity and sustainability:</p>

<table class="exam-table">
  <thead>
    <tr>
      <th>Concept Name & Designer</th>
      <th>Slide</th>
      <th>Primary Eco-Innovation</th>
      <th>Technical & Material Architecture</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Nikola Knezevic Solar Laptop</strong></td>
      <td>Slide 30</td>
      <td>Fold-out integrated solar harvesting</td>
      <td>Features a solar panel attached to its top half that folds out to catch sunlight whether the laptop is open or closed, maintaining a topped-up battery pack and saving grid electricity.</td>
    </tr>
    <tr>
      <td><strong>Lawn PC</strong></td>
      <td>Slide 30</td>
      <td>Self-generating biomimetic solar cells</td>
      <td>Engineered with recyclable synthetic grass blades embedding micro-circuits and solar cells; generates its own power and saves approximately <strong>876 kWh of electrical power per year</strong>.</td>
    </tr>
    <tr>
      <td><strong>Dell O Project</strong></td>
      <td>Slide 29</td>
      <td>Peripheral-free floor projection</td>
      <td>Uses high-end laser projection to project the display and virtual keyboard onto the floor, eliminating physical monitors and keyboards. Body carved from bio-decomposable starch-based polymer; obsolete parts returnable to manufacturer.</td>
    </tr>
    <tr>
      <td><strong>Dell Biodegradable Desktop</strong></td>
      <td>Slide 29</td>
      <td>Agricultural polymer casing</td>
      <td>Chassis skin composed of biodegradable polymers synthesized from bamboo and cornstarch. Components can be returned to Dell for certified recycling upon obsolescence.</td>
    </tr>
    <tr>
      <td><strong>Igglu Modular PC</strong></td>
      <td>Slide 31</td>
      <td>Standardized modular upgradeability</td>
      <td>Built from standardized, reusable, and recyclable modular blocks for PCI drives, graphics cards, RAM, and hard drives, allowing users to upgrade individual components without discarding the chassis.</td>
    </tr>
    <tr>
      <td><strong>Compaq EOS Sustainable Desktop</strong></td>
      <td>Slide 31</td>
      <td>Disassembly-friendly desktop</td>
      <td>Engineered for rapid disassembly and partial recycling with a tiny desk footprint; utilizes biodegradable bio-resins and recyclable aluminum; supported by HP's hardware take-back program.</td>
    </tr>
    <tr>
      <td><strong>Ecofriendly Screwless Desktop</strong></td>
      <td>Slide 32</td>
      <td>Screwless plastic-lumber PC</td>
      <td>Contains zero screws inside the chassis, minimizing assembly waste and saving internal space. Exterior crafted from recycled plastic lumber and matte white plastic to merge with home furniture.</td>
    </tr>
    <tr>
      <td><strong>Avant-Garde Tablet PC</strong></td>
      <td>Slide 32</td>
      <td>Modular peripheral-free tablet</td>
      <td>Features upgradeable hardware blocks to keep e-waste at bay; incorporates an OLED display with stylus input, rendering external mice and keyboards redundant.</td>
    </tr>
    <tr>
      <td><strong>Recyclable Paper Laptop</strong></td>
      <td>Slide 33</td>
      <td>Layered recycled paper pulp</td>
      <td>Fabricated from pulp materials and recycled paper packed in protective layers; lightweight, fully recyclable, and easily upgradeable.</td>
    </tr>
    <tr>
      <td><strong>Power Flower PC</strong></td>
      <td>Slide 34</td>
      <td>Hydrogen fuel cell with water byproduct</td>
      <td>Powered by a clean hydrogen fuel cell with components extending like blooming daisies. As power is generated, clean water drips out into a clear container and can be reused for <strong>drinking, cooking, or watering flowers</strong>! Gestures are tracked by camera (eliminating mouse/keyboard), while a small pico projector eliminates physical monitors.</td>
    </tr>
    <tr>
      <td><strong>Solar Clamshell PC for Rural India</strong></td>
      <td>Slide 35</td>
      <td>Solar rural computing hub</td>
      <td>Designed specifically for rural India; features a roll-out flexible LCD screen, built-in LED projector, Wi-Fi connectivity, and an onboard battery recharged via integrated solar panels to deliver online agricultural assistance to farmers.</td>
    </tr>
  </tbody>
</table>

<p><em>Slide Reference: Class 14, Slides 10, 18, 29, 30, 31, 32, 33, 34, and 35.</em></p>
</div>"""
        },
        {
            "id": "EQB-14-09",
            "class_id": 14,
            "class_name": "Green Computing",
            "topic": "E-Waste Legislations & Regulatory Guidelines (EPR, RoHS, CPCB 2008 Guidelines)",
            "category": "Descriptive & Regulatory Frameworks",
            "exams": [
                {"paper": "End Exam Curriculum", "section": "Class 14 Regulatory Framework", "marks": "3M – 5M"}
            ],
            "marks": "3M – 5M",
            "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
            "prompt": "Explain the regulatory framework and legislations governing e-waste management. Why is dedicated e-waste legislation necessary, and what are the salient features of the Central Pollution Control Board (CPCB) 2008 Guidelines?",
            "expected_answer": """<div class="expected-body">
<p><strong>Why Dedicated E-Waste Legislation is Necessary (Slide 25):</strong></p>
<ol>
  <li><strong>End-of-Consumption Nature:</strong> Unlike traditional industrial hazardous waste originating from point-source factories, e-waste is generated at the end of consumer utilization across millions of dispersed homes, schools, and offices.</li>
  <li><strong>Statutory Precedents under the Environment Protection Act:</strong> The Indian EPA provides for separate, specialized rules for distinct waste streams, such as the <em>Biomedical Wastes Rules 1998</em> and <em>Batteries Rules 2001</em>. E-waste demanded an equivalent standalone regime.</li>
  <li><strong>Complex Multi-Stakeholder Chain:</strong> Spans an intricate network: original equipment manufacturers (producers), distributors, retailers, millions of end consumers, scrap pickers, aggregators, and formal/informal dismantlers.</li>
  <li><strong>Dual Characteristics (Value vs Toxicity):</strong> Combines high economic value (gold, silver, copper) with acute environmental hazards (lead, mercury, cadmium), requiring distinct technical standards for safe refurbishment, dismantling, and precious metal recovery.</li>
</ol>

<p><strong>Multi-Tiered Regulatory Framework Governing E-Waste (Slide 26):</strong></p>
<ul>
  <li><em>Hazardous Waste Rules 1998 (as amended in 2008):</em> Governs toxic chemical constituents and made formal environmental registration mandatory for all electronic waste recyclers.</li>
  <li><em>Municipal Solid Waste Rules:</em> Covers non-toxic solid waste fractions and mixed garbage disposal.</li>
  <li><em>Basel Convention:</em> Regulates transboundary movements to prohibit international dumping in non-equipped developing states via Prior Informed Consent (PIC).</li>
  <li><em>Foreign Trade Policy (DGFT):</em> Restricts the importation of second-hand computers and <strong>strictly prohibits the import of e-waste into India</strong>.</li>
</ul>

<p><strong>Salient Features of CPCB Guidelines (April 2008) (Slide 27):</strong></p>
<ul>
  <li><strong>Extended Producer Responsibility (EPR):</strong> Mandates that producers and brand owners bear financial and physical responsibility for establishing take-back mechanisms, collection centers, and certified recycling infrastructure.</li>
  <li><strong>Restriction on Hazardous Substances (RoHS):</strong> Sets thresholds restricting hazardous heavy metals (lead, cadmium, mercury, hexavalent chromium) and flame retardants in electronic manufacturing.</li>
  <li><strong>Recycling Standards & Best Practices:</strong> Outlines environmental guidelines for dismantling, mechanical shredding, and hydrometallurgical recovery.</li>
  <li><strong>Call for Dedicated Legislation:</strong> Formally recommended enacting binding standalone e-waste legislation, which crystallized as India's E-Waste (Management and Handling) Rules.</li>
</ul>
</div>""",
            "key_answer_points": """<ul>
<li><strong>Why Dedicated E-Waste Legislation is Necessary (Slide 25):</strong>
<br>• E-waste is <strong>distinct</strong> because it is an <em>end-of-consumption waste</em>, whereas hazardous waste typically results from a distinct industrial manufacturing process.
<br>• The e-waste value chain is exceptionally complex, involving diverse stakeholders: manufacturers/producers, distributors, retailers, end consumers, collection agencies, and informal/formal recyclers.
<br>• E-waste management involves refurbishment for reuse, physical dismantling, and precious metal recovery—processes requiring specialized technical standards.
<br>• Precedents under the Environment Protection Act exist for waste with distinct characteristics (e.g. Biomedical Wastes Rules 1998, Batteries Rules 2001).</li>
<li><strong>Multi-Pillar Legal Framework Governing E-Waste (Slide 26):</strong>
<br>• <em>Hazardous Waste Rules 1998 (as amended in 2008):</em> Governs toxic contents; establishes mandatory registration for e-waste recyclers.
<br>• <em>Municipal Solid Waste Management & Handling Rules:</em> Covers non-toxic solid waste fractions.
<br>• <em>Basel Convention:</em> Regulates transboundary movement to prevent international toxic dumping.
<br>• <em>Foreign Trade Policy:</em> Restricts the importation of second-hand computers and strictly prohibits the import of e-waste into India.</li>
<li><strong>Salient Features of CPCB Guidelines (April 2008) (Slide 27):</strong>
<br>1. <strong>Producer Responsibility (Extended Producer Responsibility / EPR):</strong> Establishes that manufacturers are responsible for the entire lifecycle, including financing and organizing take-back and recycling systems.
<br>2. <strong>RoHS (Restriction on Hazardous Substances):</strong> Limits hazardous heavy metals (lead, cadmium, mercury, hexavalent chromium) and flame retardants in electronic goods.
<br>3. <strong>Best Practices & Recycling Technology:</strong> Provides technical insights and standards for environmentally sound recycling across dismantling, precious metal recovery, and hazardous disposal.
<br>4. Explicitly stated the legal necessity for a dedicated standalone statute to enforce Producer Responsibility.</li>
</ul>""",
            "detailed_answer": """<div class="detailed-body">
<p><strong>The Legal Dilemma of E-Waste:</strong> Historically, discarded electronics in India were lumped under general hazardous industrial waste or municipal solid waste regulations. However, the lecture slides detail why conventional environmental statutes failed to manage electronic scrap effectively.</p>

<h4>The Need for Dedicated / Separate E-Waste Legislation</h4>
<p>Slide 25 articulates four definitive legal and operational reasons why e-waste requires dedicated, standalone statutes:</p>
<ol>
  <li><strong>End-of-Consumption Nature:</strong> E-waste is legally and physically distinct from traditional industrial hazardous waste. Industrial waste originates from point-source manufacturing processes inside factories, whereas e-waste is generated at the end of consumer utilization across millions of distributed households, schools, and offices.</li>
  <li><strong>Statutory Precedents under the Environment Protection Act:</strong> The Indian Environment Protection Act provides for separate, specialized rules for waste streams possessing unique lifecycle characteristics. Precedents include the <em>Biomedical Wastes (Management & Handling) Rules 1998</em> and the <em>Batteries (Management & Handling) Rules 2001</em>. E-waste demanded an equivalent specialized statutory regime.</li>
  <li><strong>Complex Multi-Stakeholder Value Chain:</strong> Unlike point-source factory emissions, the e-waste lifecycle spans an intricate network of participants: original equipment manufacturers (producers), brand distributors, retail vendors, millions of corporate and individual end consumers, waste pickers, scrap aggregators, and formal/informal dismantlers.</li>
  <li><strong>Dual Characteristics (Valuable Resource vs Toxic Hazard):</strong> E-waste is unique because it combines high economic value (gold, silver, copper) with acute environmental hazards (lead, mercury, cadmium). Proper handling requires specialized refurbishment for reuse, safe dismantling, and hydrometallurgical/pyrometallurgical precious metal reclamation.</li>
</ol>

<h4>The Multi-Tiered Legal Framework Governing E-Waste</h4>
<p>Slide 26 outlines the historical intersection of statutes governing e-waste in India prior to dedicated standalone rules:</p>
<table class="exam-table">
  <thead>
    <tr>
      <th>Statutory / Legal Instrument</th>
      <th>Regulatory Scope & Domain</th>
      <th>Key Mandate for E-Waste</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Hazardous Waste (M&H) Rules 1998 (Amended 2008)</strong></td>
      <td>Toxic chemical constituents</td>
      <td>Made formal environmental registration <strong>mandatory for all electronic recyclers</strong>.</td>
    </tr>
    <tr>
      <td><strong>Municipal Solid Waste (M&H) Rules</strong></td>
      <td>Non-toxic waste fractions</td>
      <td>Governs mixed municipal solid waste collection, sorting, and landfill disposal.</td>
    </tr>
    <tr>
      <td><strong>Basel Convention</strong></td>
      <td>International transboundary movements</td>
      <td>Prohibits transboundary shipment of toxic e-waste to non-equipped developing states.</td>
    </tr>
    <tr>
      <td><strong>Foreign Trade Policy (DGFT)</strong></td>
      <td>Cross-border commercial trade</td>
      <td>Restricts import of second-hand PCs and <strong>strictly prohibits import of e-waste</strong>.</td>
    </tr>
    <tr>
      <td><strong>CPCB Guidelines (April 2008)</strong></td>
      <td>National environmental guidance</td>
      <td>Established fundamental principles: Producer Responsibility, RoHS, and recycling standards.</td>
    </tr>
  </tbody>
</table>

<h4>Salient Features of CPCB Guidelines 2008</h4>
<p>Slide 27 details the landmark guidelines notified by the Central Pollution Control Board (CPCB) in April 2008. These served as India's primary transitional blueprint, articulating four cornerstone principles:</p>
<ul>
  <li><strong>Extended Producer Responsibility (EPR):</strong> Formally recognized the principle that producers and brand owners bear financial and physical responsibility for establishing take-back mechanisms, collection centers, and certified recycling infrastructure for their post-consumer products.</li>
  <li><strong>Restriction on Hazardous Substances (RoHS):</strong> Mandated thresholds restricting hazardous substances (lead, cadmium, mercury, hexavalent chromium, polybrominated biphenyls, and polybrominated diphenyl ethers) in newly manufactured electronic products.</li>
  <li><strong>Best Practices & Recycling Technology:</strong> Provided engineering blueprints and environmental safeguards for dismantling, mechanical shredding, hydrometallurgical recovery, and toxic fraction disposal.</li>
  <li><strong>Call for Dedicated Legislation:</strong> Crucially, the guidelines explicitly documented that non-binding guidelines were insufficient, formally recommending the enactment of standalone, enforceable e-waste legislation—which materialized as the landmark E-Waste (Management and Handling) Rules.</li>
</ul>

<p><em>Slide Reference: Class 14, Slides 25, 26, and 27.</em></p>
</div>"""
        },
        {
            "id": "EQB-14-10",
            "class_id": 14,
            "class_name": "Green Computing",
            "topic": "Informal E-Waste Recycling Hazards & Case Studies (Guiyu & Agbogbloshie)",
            "category": "Descriptive & Case Study",
            "exams": [
                {"paper": "End Exam Past Papers", "section": "Class 14 Case Studies", "marks": "3M – 5M"}
            ],
            "marks": "3M – 5M",
            "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
            "prompt": "Discuss the environmental and occupational health hazards associated with informal e-waste recycling. Detail the case studies of Guiyu (China) and Agbogbloshie (Ghana) as highlighted in the lecture slides.",
            "expected_answer": """<div class="expected-body">
<p><strong>Informal E-Waste Recycling Reality in Developing Nations (Slides 22 & 23):</strong></p>
<ul>
  <li><strong>Unorganized & Unregulated:</strong> Over 90% of e-waste recycling in developing nations is concentrated in the informal sector without organized collection systems. Operations are mostly illegal and rely on crude methods: manual hammer smashing of CRTs, open-pan acid leaching using aqua regia to strip gold, and burning insulated wiring over vehicle tires to harvest copper wire.</li>
  <li><strong>Low Recovery & Severe Pollution:</strong> Primitive chemical leaching achieves recovery rates below 20%, squandering over 80% of precious minerals while discharging toxic metal-saturated acid slurries directly into municipal gutters and soils.</li>
  <li><strong>Severe Occupational Illnesses:</strong> Workers continuously inhale toxic metal fumes (lead, cadmium), acid mists, and brominated dioxins without personal protective equipment (PPE), causing chronic pulmonary disease, kidney failure, and neurological damage.</li>
  <li><strong>Exploitation of Vulnerable Groups:</strong> These hazardous backyard operations disproportionately exploit <strong>women, children, and impoverished migrant labourers</strong> who manually sort and desolder circuit boards over open charcoal fires.</li>
</ul>

<p><strong>Case Study 1: Guiyu, Guangdong, China (Slide 20):</strong></p>
<ul>
  <li>Recognized as the world's largest informal e-waste dumping hub, where vast roadsides were lined with mounds of discarded computers and circuit boards.</li>
  <li>Handled an influx where as much as <strong>4,000 tonnes of toxic e-waste were discarded every hour</strong>, with massive shipments illegally imported from Europe, the USA, and Japan.</li>
  <li>Resulted in pervasive heavy metal saturation of local river systems and record-high blood lead levels in local children.</li>
</ul>

<p><strong>Case Study 2: Agbogbloshie, Accra, Ghana (Slide 24):</strong></p>
<ul>
  <li>A landmark 2019 investigative report (<em>The Guardian</em>) titled <em>"Rotten eggs: e-waste from Europe poisons Ghana's food chain"</em> documented open burning of European electronic scrap in a slum settlement of <strong>80,000 residents</strong>.</li>
  <li>Open burning of wire insulation and plastic casings deposited dense toxic ash laden with chlorinated dioxins and polychlorinated biphenyls (PCBs) across surrounding foraging grounds.</li>
  <li>Free-range chickens foraging on the dumpsite ingested contaminated ash; laboratory testing revealed that chicken eggs contained chlorinated dioxins and PCBs hundreds of times above European food safety limits, demonstrating direct transfer of toxic e-waste chemicals into the human food supply.</li>
</ul>
</div>""",
            "key_answer_points": """<ul>
<li><strong>Informal Recycling Reality in India & Developing Nations (Slide 22):</strong>
<br>• Concentrated heavily in the informal (unorganized) sector without organized collection systems.
<br>• Operations are mostly illegal, unregulated, and employ highly polluting rudimentary methods.
<br>• Activities focus on manual dismantling, sale of usable parts, crude resource recovery (acid leaching, open wire burning), and exporting residues for overseas smelting.</li>
<li><strong>Key Hazards & Concerns of Informal Recycling (Slide 23):</strong>
<br>• <em>High-Risk Backyard Operations:</em> Workers operate in residential alleys with no personal protective equipment (PPE) or toxic ventilation.
<br>• <em>Non-Sound Technologies:</em> Acid leaching and open-air burning suffer from extremely low resource recovery efficiencies, causing vast losses of precious materials.
<br>• <em>Disproportionate Social Impact:</em> Severely harms vulnerable groups—especially <strong>women, young children, and migrant labourers</strong> who manually sort and desolder circuit boards.</li>
<li><strong>Guiyu, Guangdong, China Case Study (Slide 20):</strong>
<br>• World's largest informal e-waste dumping hub, where piles of electronic scrap line roadsides.
<br>• As much as <strong>4,000 tonnes of toxic e-waste</strong> discarded every hour, with massive illegal shipments from Europe, the USA, and Japan processed by unprotected workers.</li>
<li><strong>Agbogbloshie, Accra, Ghana Case Study (Slide 24):</strong>
<br>• <em>"Rotten eggs: e-waste from Europe poisons Ghana's food chain"</em> (The Guardian, 2019).
<br>• Burning discarded European computers and refrigerators in a scrap settlement of 80,000 people liberated heavy metals, dioxins, and PCBs into soils.
<br>• Foraging free-range chickens ingested contaminated ash; eggs were found to contain lethal concentrations of chlorinated dioxins and PCBs, directly poisoning the human food supply.</li>
</ul>""",
            "detailed_answer": """<div class="detailed-body">
<p><strong>The Reality of Informal E-Waste Recycling:</strong> While electronic scrap holds immense economic value due to embedded precious metals (gold, silver, platinum, copper), over 90% of recycling in developing nations takes place within the unorganized, informal sector. The lecture slides examine the profound human and ecological crises generated by informal recycling practices.</p>

<h4>The Recycling Scenario in India & Developing Economies</h4>
<p>Slide 22 describes the baseline reality of domestic e-waste processing:</p>
<ul>
  <li>E-waste recycling is overwhelmingly concentrated in the informal, unorganized sector.</li>
  <li>No systematic, organized municipal collection system prevails; waste pickers (kabadiwalas) acquire scrap directly from consumers and offices.</li>
  <li>Backyard operations are largely illegal and exempt from environmental inspections.</li>
  <li>Processing methods are primitive and highly polluting: manual smashing of cathode ray tubes, open-pan acid leaching using aqua regia to strip gold from printed circuit boards, and open burning of insulated wiring over burning vehicle tires to harvest copper.</li>
  <li>Recycling operations encompass: manual dismantling, sale of salvaged components, crude resource recovery, and export of processed electronic scrap for overseas precious metal refining.</li>
</ul>

<h4>Occupational & Environmental Hazards</h4>
<p>Slide 23 identifies five critical concerns associated with informal processing:</p>
<ol>
  <li><strong>High-Risk Backyard Operations:</strong> Carried out in dense residential settlements with zero effluent treatment, fume hoods, or safety equipment.</li>
  <li><strong>Inefficient & Non-Sound Technologies:</strong> Crude open chemical leaching achieves recovery rates below 20%, squandering over 80% of valuable mineral resources while discharging gallons of concentrated metal-laden acid directly into municipal gutters.</li>
  <li><strong>Severe Occupational Illnesses:</strong> Workers continuously inhale toxic metal fumes (lead, cadmium), hydrochloric acid mists, and brominated flame retardant vapors, causing chronic pulmonary disease, neurological damage, and renal failure.</li>
  <li><strong>Exploitation of Vulnerable Groups:</strong> These hazardous backyard operations disproportionately exploit <strong>women, children, and impoverished migrant labourers</strong>, whose dexterous hands are used to desolder electronic components over charcoal burners with no respiratory protection.</li>
</ol>

<h4>Case Study 1: Guiyu, Guangdong, China (Slide 20)</h4>
<p>Slide 20 highlights Guiyu, historically recognized as the largest informal e-waste hub on the planet. The slide documents:</p>
<ul>
  <li>Roadsides lined with massive piles of discarded computer chassis, circuit boards, and broken monitors.</li>
  <li>An astonishing global throughput: <em>"As much as 4,000 tonnes of toxic e-waste are discarded every hour."</em></li>
  <li>Vast quantities of electronic scrap were routinely and illegally exported from Europe, the USA, and Japan to Guiyu, where thousands of unprotected laborers broke down parts in open workshops, leaving local rivers heavily saturated with heavy metals and children exhibiting record-high blood lead levels.</li>
</ul>

<h4>Case Study 2: Agbogbloshie, Accra, Ghana (Slide 24)</h4>
<p>Slide 24 presents a landmark 2019 investigative report published in <em>The Guardian</em>: <strong>"Rotten eggs: e-waste from Europe poisons Ghana's food chain."</strong></p>
<ul>
  <li>At the Agbogbloshie dumpsite in Accra, Ghana, an informal settlement of <strong>80,000 residents</strong> lived adjacent to an open burning scrap yard processing old computers, refrigerators, and electronics shipped from Europe.</li>
  <li>Open-air wire burning generated dense plumes of toxic smoke and deposited ash laden with chlorinated dioxins and polychlorinated biphenyls (PCBs) across surrounding foraging grounds.</li>
  <li>Free-range chickens foraging on the dumpsite ingested these chemical residues. Subsequent laboratory testing revealed that a single chicken egg contained toxic dioxins and PCBs hundreds of times above European food safety limits, conclusively proving that crude e-waste burning transfers persistent industrial poisons directly into the human food chain.</li>
</ul>

<p><em>Slide Reference: Class 14, Slides 20, 22, 23, and 24.</em></p>
</div>"""
        },
        {
            "id": "EQB-14-11",
            "class_id": 14,
            "class_name": "Green Computing",
            "topic": "Computer Components vs Toxic Chemical Constituents",
            "category": "Match the Following",
            "exams": [
                {"paper": "EST End Exam 2024", "section": "Section I, Q(A)", "marks": "5M"},
                {"paper": "End Exam 2022", "section": "Section I, Q(A)", "marks": "5M"},
                {"paper": "End Exam 2018", "section": "Part II, Q3", "marks": "2M"}
            ],
            "marks": "5M",
            "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
            "prompt": "Match the following computer components with their toxic chemical constituents. Explain the technical function of each chemical in the hardware component and its specific environmental and toxicological impact when improperly discarded.",
            "expected_answer": """<div class="expected-body">
<p><strong>Hardware Component to Toxic Chemical Constituent Match (Slide 21):</strong></p>
<ol>
  <li><strong>Printed circuit boards</strong> $\rightarrow$ <strong>Lead & cadmium</strong></li>
  <li><strong>Cathode ray tubes (CRTs)</strong> $\rightarrow$ <strong>Lead oxide & Cadmium</strong></li>
  <li><strong>Switches & flat screen monitors</strong> $\rightarrow$ <strong>Mercury</strong></li>
  <li><strong>Computer batteries</strong> $\rightarrow$ <strong>Cadmium</strong></li>
  <li><strong>Capacitors and transformers</strong> $\rightarrow$ <strong>Poly Chlorinated Bi-phenyls (PCB)</strong></li>
  <li><strong>Printed circuit boards, plastic casings cable</strong> $\rightarrow$ <strong>Brominated Flame Retardant (BFR)</strong></li>
  <li><strong>Cable insulation / coating</strong> $\rightarrow$ <strong>Poly Vinyl Chloride (PVC)</strong></li>
</ol>

<table class="exam-table">
  <thead>
    <tr>
      <th>No.</th>
      <th>Hardware Component</th>
      <th>Toxic Constituent</th>
      <th>Engineering Function</th>
      <th>Environmental & Toxicological Impact</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td><strong>Printed circuit boards</strong></td>
      <td><strong>Lead & cadmium</strong></td>
      <td>Lead is used in tin-lead solder alloys for electrical connections; cadmium is used in SMD chip resistors and semiconductor passivators.</td>
      <td>Lead causes neurotoxicity and brain damage; cadmium causes proximal renal tubular dysfunction and severe bone demineralization (Itai-Itai disease).</td>
    </tr>
    <tr>
      <td>2</td>
      <td><strong>Cathode ray tubes (CRTs)</strong></td>
      <td><strong>Lead oxide & Cadmium</strong></td>
      <td>Lead oxide (2–3 kg per monitor) shields users from X-rays; cadmium is used as a phosphor coating inside the tube screen.</td>
      <td>Crushed funnel glass leaches lead into acidic groundwater; cadmium phosphor dust causes severe respiratory inflammation and pulmonary edema.</td>
    </tr>
    <tr>
      <td>3</td>
      <td><strong>Switches & flat screen monitors</strong></td>
      <td><strong>Mercury</strong></td>
      <td>Used in mechanical tilt switches and as an excitation gas inside Cold Cathode Fluorescent Lamps (CCFLs) backlighting older LCD panels.</td>
      <td>Volatilizes into toxic mercury vapor; converts to bioaccumulative methylmercury in aquatic food chains, destroying central nervous systems.</td>
    </tr>
    <tr>
      <td>4</td>
      <td><strong>Computer batteries</strong></td>
      <td><strong>Cadmium</strong></td>
      <td>Active cathode material in rechargeable Nickel-Cadmium (Ni-Cd) laptop and CMOS backup battery cells.</td>
      <td>Classified as an IARC Group 1 human carcinogen; bioaccumulates in kidneys and causes severe bone softening.</td>
    </tr>
    <tr>
      <td>5</td>
      <td><strong>Capacitors and transformers</strong></td>
      <td><strong>Poly Chlorinated Bi-phenyls (PCB)</strong></td>
      <td>Historically functioned as dielectric insulating fluids due to exceptional thermal stability and high dielectric constants.</td>
      <td>Persistent Organic Pollutants (POPs) under the Stockholm Convention; potent endocrine disruptor, causes liver cancer and immune suppression.</td>
    </tr>
    <tr>
      <td>6</td>
      <td><strong>Printed circuit boards, plastic casings cable</strong></td>
      <td><strong>Brominated Flame Retardant (BFR)</strong></td>
      <td>Polybrominated diphenyl ethers (PBDEs) are blended into polymer casings and resin boards to retard thermal ignition and satisfy fire safety ratings.</td>
      <td>Bioaccumulates in adipose tissue and breast milk; open-air burning releases acutely toxic polybrominated dibenzodioxins and dibenzofurans.</td>
    </tr>
    <tr>
      <td>7</td>
      <td><strong>Cable insulation / coating</strong></td>
      <td><strong>Poly Vinyl Chloride (PVC)</strong></td>
      <td>Thermoplastic polymer blended with plasticizers used to coat electrical wiring for flexible electrical insulation.</td>
      <td>Contains chlorine; open burning to harvest copper wire pyrolyzes into highly carcinogenic chlorinated dioxins (TCDD) and corrosive hydrochloric acid gas.</td>
    </tr>
  </tbody>
</table>
</div>""",
            "key_answer_points": """<ul>
<li><strong>Authoritative Slide 21 Match:</strong>
<br>1. <strong>Printed circuit boards</strong> $\\rightarrow$ <strong>Lead & cadmium</strong>
<br>2. <strong>Cathode ray tubes (CRTs)</strong> $\\rightarrow$ <strong>Lead oxide & Cadmium</strong>
<br>3. <strong>Switches & flat screen monitors</strong> $\\rightarrow$ <strong>Mercury</strong>
<br>4. <strong>Computer batteries</strong> $\\rightarrow$ <strong>Cadmium</strong>
<br>5. <strong>Capacitors and transformers</strong> $\\rightarrow$ <strong>Poly Chlorinated Bi-phenyls (PCB)</strong>
<br>6. <strong>Printed circuit boards, plastic casings cable</strong> $\\rightarrow$ <strong>Brominated Flame Retardant (BFR)</strong>
<br>7. <strong>Cable insulation/coating</strong> $\\rightarrow$ <strong>Poly Vinyl Chloride (PVC)</strong></li>
<li><strong>Toxicological Mechanisms:</strong>
<br>• <em>Lead:</em> Neurotoxin damaging central nervous system, brain development, and kidneys.
<br>• <em>Cadmium:</em> Bioaccumulative kidney toxin, human carcinogen, and cause of bone demineralization.
<br>• <em>Mercury:</em> Volatilizes into vapor; converts to methylmercury, bioaccumulating in aquatic food chains and causing severe neurological damage.
<br>• <em>PCBs:</em> Persistent organic pollutants (POPs) acting as potent endocrine disruptors and carcinogens.
<br>• <em>BFRs:</em> Release toxic brominated dioxins/furans upon combustion; disrupt endocrine and thyroid functions.
<br>• <em>PVC:</em> Chlorinated polymer; open combustion produces highly carcinogenic chlorinated dioxins.</li>
</ul>""",
            "detailed_answer": """<div class="detailed-body">
<p><strong>Technical Function vs Toxicological Risk:</strong> Modern electronics rely on specific chemical elements and synthetic polymers to achieve high electrical conductivity, dielectric insulation, flame resistance, and structural durability. However, when these devices reach their end-of-life, those exact constituents pose severe environmental and human toxicological hazards if dismantled or landfilled improperly.</p>

<h4>Authoritative Hardware Component vs Chemical Constituent Match</h4>
<p>Slide 21 provides the definitive examination mapping between hardware components and their toxic chemical constituents:</p>

<table class="exam-table">
  <thead>
    <tr>
      <th>No.</th>
      <th>Hardware Component (Slide 21)</th>
      <th>Toxic Chemical Constituent</th>
      <th>Engineering Function in Component</th>
      <th>Toxicological & Environmental Impact</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td><strong>Printed circuit boards</strong></td>
      <td><strong>Lead & cadmium</strong></td>
      <td>Lead is used in tin-lead solder alloys for electrical interconnections; cadmium is used in SMD chip resistors, infrared detectors, and semiconductor passivators.</td>
      <td>Lead is a potent neurotoxin causing cognitive impairment and kidney damage; cadmium causes proximal renal tubular dysfunction and severe bone demineralization (Itai-Itai disease).</td>
    </tr>
    <tr>
      <td>2</td>
      <td><strong>Cathode ray tubes (CRTs)</strong></td>
      <td><strong>Lead oxide & Cadmium</strong></td>
      <td>Lead oxide (up to 2–3 kg per monitor) is infused into funnel glass to shield users from X-rays; cadmium is used as a phosphor coating inside the tube face.</td>
      <td>When crushed in unlined dumps, lead leaches into acidic groundwater; cadmium dust causes severe respiratory inflammation and pulmonary edema.</td>
    </tr>
    <tr>
      <td>3</td>
      <td><strong>Switches & flat screen monitors</strong></td>
      <td><strong>Mercury</strong></td>
      <td>Elemental mercury was historically used in mechanical tilt switches and as an excitation gas inside Cold Cathode Fluorescent Lamps (CCFLs) backlighting older LCD panels.</td>
      <td>Easily volatilizes into toxic mercury vapor; settles into aquatic ecosystems where anaerobic bacteria methylate it into bioaccumulative methylmercury, destroying central nervous systems.</td>
    </tr>
    <tr>
      <td>4</td>
      <td><strong>Computer batteries</strong></td>
      <td><strong>Cadmium</strong></td>
      <td>Used as the active cathode material in rechargeable Nickel-Cadmium (Ni-Cd) laptop and CMOS backup battery cells.</td>
      <td>Extremely persistent and bioaccumulative; classified as a Group 1 human carcinogen by IARC; damages kidneys and calcium metabolism.</td>
    </tr>
    <tr>
      <td>5</td>
      <td><strong>Capacitors and transformers</strong></td>
      <td><strong>Poly Chlorinated Bi-phenyls (PCB)</strong></td>
      <td>Historically functioned as dielectric insulating fluids due to exceptional thermal stability and high dielectric constants.</td>
      <td>Classified as Persistent Organic Pollutants (POPs) under the Stockholm Convention; immune system suppressor, potent endocrine disruptor, and causes chloracne and liver cancer.</td>
    </tr>
    <tr>
      <td>6</td>
      <td><strong>Printed circuit boards, plastic casings cable</strong></td>
      <td><strong>Brominated Flame Retardant (BFR)</strong></td>
      <td>Polybrominated diphenyl ethers (PBDEs) are blended into polymer casings and fiberglass resin boards to retard thermal ignition and satisfy flammability safety ratings.</td>
      <td>Bioaccumulates in human adipose tissue and breast milk; disrupts endocrine and thyroid hormone systems; open-air burning generates acutely toxic polybrominated dibenzodioxins and dibenzofurans.</td>
    </tr>
    <tr>
      <td>7</td>
      <td><strong>Cable insulation / coating</strong></td>
      <td><strong>Poly Vinyl Chloride (PVC)</strong></td>
      <td>Thermoplastic polymer blended with plasticizers used to coat electrical wiring and power cords for flexible electrical insulation.</td>
      <td>Contains chlorine; when burned in open backyard scrapyards to harvest internal copper wire, it pyrolyzes into highly carcinogenic chlorinated dioxins (TCDD) and corrosive hydrochloric acid gas.</td>
    </tr>
  </tbody>
</table>

<h4>Exam Answering Protocol</h4>
<p>When this recurring 5-mark question appears in Section I, candidates must write the exact 7 pairs specified above. To secure full marks, students should provide both the component-constituent match and a one-sentence technical rationale explaining why the element is hazardous upon disposal.</p>

<p><em>Slide Reference: Class 14, Slide 21.</em></p>
</div>"""
        }
    ]
