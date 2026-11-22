import json
import os

# Build complete dataset for Classes 11-19
# Covering all past exam papers (2018-2024 End-Sems, Mid-Sems, Quizzes)

def get_class11_questions():
    return [
        {
            "id": "EQB-11-01",
            "class_id": 11,
            "class_name": "Climate Change Technology Solutions",
            "topic": "Air-to-Diamond Synthesis (Aether Diamonds)",
            "category": "Descriptive & Case Study",
            "exams": [
                {"paper": "End Exam 2023", "section": "Section III, Q5", "marks": "3M"},
                {"paper": "End Exam 2022", "section": "Section X, Q(b)", "marks": "5M"}
            ],
            "marks": "3M – 5M",
            "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
            "prompt": "Explain the process of diamond manufacturing by Aether (only the process).",
            "key_answer_points": "<ul>\n<li><strong>Direct Air Capture:</strong> Ambient atmospheric \\(\\text{CO}_2\\) is captured from air in Europe using Climeworks collector fans and solid amine filters.</li>\n<li><strong>Methane Synthesis (Sabatier Reaction):</strong> Captured \\(\\text{CO}_2\\) is mixed with green electrolytic hydrogen over a catalyst at \\(300–400^\\circ\\text{C}\\) to produce high-purity methane: \\(\\text{CO}_2 + 4\\text{H}_2 \\rightarrow \\text{CH}_4 + 2\\text{H}_2\\text{O}\\).</li>\n<li><strong>CVD Plasma Growth:</strong> Methane is pumped into Chemical Vapor Deposition (CVD) vacuum chambers and heated by microwaves into plasma (\\(>2,000^\\circ\\text{C}\\)). Carbon atoms deposit onto diamond seed plates atom-by-atom over 3–4 weeks.</li>\n<li><strong>100% Clean Energy:</strong> The entire process runs strictly on certified solar and nuclear power.</li>\n<li><strong>Surat Cutting Hub:</strong> Rough synthetic diamonds are sent to Surat, Gujarat, India for laser cutting and faceting by master polishers.</li>\n<li><strong>Environmental Savings:</strong> Offsets <strong>20 tonnes of \\(\\text{CO}_2\\) per carat</strong>, uses zero net water (saves 127 gallons), and requires no open-pit mining.</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>The Big Picture:</strong> Traditional diamond mining moves over 250 tonnes of earth per carat and burns huge amounts of diesel. Aether Diamonds developed a cleantech solution: pulling carbon pollution straight out of the atmosphere and turning it into genuine gem-grade diamonds.</p>\n<h4>Step-by-Step: How It Works</h4>\n<ol>\n<li><strong>Pulling \\(\\text{CO}_2\\) from Air:</strong> Climeworks facilities in Switzerland and Iceland use giant fans with chemical filters to capture ambient carbon dioxide, compressing it into pure gas.</li>\n<li><strong>Making Methane (Sabatier Reaction):</strong> Pure \\(\\text{CO}_2\\) cannot form a diamond crystal directly. It is combined with green hydrogen from water electrolysis over a nickel catalyst:\n<div class=\"formula-box\">$$\\text{CO}_2 + 4\\text{H}_2 \\xrightarrow{\\text{Catalyst, } \\Delta} \\text{CH}_4 + 2\\text{H}_2\\text{O}$$</div>\nThis produces ultra-pure methane gas (\\(\\text{CH}_4\\)).</li>\n<li><strong>Growing Crystals in Plasma (CVD):</strong> Methane is injected into a vacuum chamber and microwaved into plasma hotter than the sun (\\(>2,000^\\circ\\text{C}\\)). Carbon atoms break free from hydrogen and stack onto diamond seed plates in a tetrahedral crystal lattice.</li>\n<li><strong>Zero-Carbon Power:</strong> Aether uses only certified solar and nuclear power to avoid fossil grid emissions.</li>\n<li><strong>Faceting in Surat, India:</strong> Rough stones are flown to Surat, Gujarat—the global diamond polishing hub—where gemologists laser-cut and polish them into brilliant gems. Certified by IGI as genuine Type IIa diamonds.</li>\n</ol>\n<p><em>Slide Reference: Class 11 Slides 23–27.</em></p>\n</div>"
        },
        {
            "id": "EQB-11-02",
            "class_id": 11,
            "class_name": "Climate Change Technology Solutions",
            "topic": "Eco-friendly Carbon-Negative Cement (Novacem vs Portland)",
            "category": "Differentiate Between",
            "exams": [
                {"paper": "End Exam 2023", "section": "Section III, Q7", "marks": "3M"},
                {"paper": "End Exam 2019", "section": "Section IV, Q1(d)", "marks": "3M"},
                {"paper": "Mid-2 2018", "section": "Q8(b)", "marks": "1.5M"}
            ],
            "marks": "3M",
            "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
            "prompt": "Difference between Portland and Novacem cement.",
            "key_answer_points": "<ul>\n<li><strong>Raw Mineral Feedstock:</strong> Portland cement uses limestone (\\(\\text{CaCO}_3\\)); Novacem uses magnesium silicates (olivine or serpentine, \\(\\text{MgSiO}_3\\)).</li>\n<li><strong>Kiln Temperature:</strong> Portland requires \\(1,450^\\circ\\text{C}\\) (burning fossil coal); Novacem requires only \\(650^\\circ\\text{C}\\) (compatible with biomass or green electricity).</li>\n<li><strong>Manufacturing Reaction:</strong>\n<br>• Portland: \\(\\text{CaCO}_3 \\xrightarrow{1450^\\circ\\text{C}} \\text{CaO} + \\text{CO}_2\\uparrow\\) (unavoidable release of mineral \\(\\text{CO}_2\\)).\n<br>• Novacem: \\(\\text{MgSiO}_3 \\xrightarrow{650^\\circ\\text{C}} \\text{MgO} + \\text{SiO}_2\\) (zero mineral \\(\\text{CO}_2\\) emitted).</li>\n<li><strong>Curing / Hardening Reaction:</strong>\n<br>• Portland cures strictly by water hydration: \\(\\text{CaO}\\cdot\\text{SiO}_2 + \\text{H}_2\\text{O} \\rightarrow \\text{C-S-H}\\).\n<br>• Novacem cures by actively absorbing ambient \\(\\text{CO}_2\\) from outdoor air: \\(\\text{MgO} + \\text{CO}_2 + 3\\text{H}_2\\text{O} \\rightarrow \\text{MgCO}_3\\cdot 3\\text{H}_2\\text{O}\\).</li>\n<li><strong>Net Carbon Balance:</strong> Portland emits <strong>+800 to +1,000 kg \\(\\text{CO}_2\\) per tonne</strong> (~8% of global emissions); Novacem is carbon-negative, storing <strong>-100 kg \\(\\text{CO}_2\\) net per tonne</strong>.</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>Why This Matters:</strong> Concrete is the second most consumed material on Earth. Traditional Portland cement releases massive \\(\\text{CO}_2\\) from limestone heating. Novacem uses magnesium silicates that contain no carbonate ions, absorbing carbon from air as the concrete hardens.</p>\n<h4>Side-by-Side Comparison</h4>\n<table class=\"exam-table\">\n<thead><tr><th>Parameter</th><th>Ordinary Portland Cement (OPC)</th><th>Novacem Cement</th></tr></thead>\n<tbody>\n<tr><td>Raw Mineral</td><td>Limestone (\\(\\text{CaCO}_3\\))</td><td>Magnesium Silicate (\\(\\text{MgSiO}_3\\))</td></tr>\n<tr><td>Kiln Temp</td><td>\\(1,450^\\circ\\text{C}\\) (coal combustion)</td><td>\\(650^\\circ\\text{C}\\) (electric/biomass)</td></tr>\n<tr><td>Process Emission</td><td>Emits 0.53 t \\(\\text{CO}_2\\) / t clinker chemically</td><td>Zero chemical mineral \\(\\text{CO}_2\\) release</td></tr>\n<tr><td>Hardening</td><td>Hydration forming C-S-H gel</td><td>Carbonation absorbing ambient air \\(\\text{CO}_2\\)</td></tr>\n<tr><td>Carbon Balance</td><td>Net positive: +0.8 to +1.0 t \\(\\text{CO}_2\\)/t</td><td><strong>Net negative: -0.1 t \\(\\text{CO}_2\\)/t (-100 kg/t)</strong></td></tr>\n</tbody>\n</table>\n<p><em>Slide Reference: Class 11 Slides 42–46.</em></p>\n</div>"
        },
        {
            "id": "EQB-11-03",
            "class_id": 11,
            "class_name": "Climate Change Technology Solutions",
            "topic": "Blue Carbon Definition & Ecosystem Benefits",
            "category": "Short Answer & Definitions",
            "exams": [
                {"paper": "End Exam 2023", "section": "Section I, Q1(g)", "marks": "1M"},
                {"paper": "End Exam 2022", "section": "Section V, Q(e) & Section IX(e)", "marks": "1M + 2M"},
                {"paper": "End Exam 2019", "section": "Section X, Q1(c)", "marks": "1M"},
                {"paper": "End Exam 2018", "section": "Part IV, Q3", "marks": "2M"}
            ],
            "marks": "1M – 2M",
            "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
            "prompt": "What is Blue Carbon? State the advantages of blue carbon habitat restoration [3 points].",
            "key_answer_points": "<ul>\n<li><strong>Definition:</strong> Blue Carbon is the carbon captured and stored by coastal and marine ecosystems—mainly <strong>mangroves, tidal salt marshes, and seagrass meadows</strong>.</li>\n<li><strong>Advantage 1 (Fast & Long-Term Storage):</strong> Sequesters carbon <strong>3 to 5 times faster</strong> than terrestrial tropical forests, locking it into waterlogged, oxygen-poor mud for millennia without saturating.</li>\n<li><strong>Advantage 2 (Storm & Flood Defense):</strong> Dense root networks cut down wave force, buffering coastal communities against cyclones, storm surges, and sea level rise.</li>\n<li><strong>Advantage 3 (Fisheries & Biodiversity Nursery):</strong> Provides shelter and breeding grounds for over 75% of commercial fish and shellfish species.</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>The Big Picture:</strong> Terrestrial forests can easily lose stored carbon to wildfires or rot. Blue carbon soils are permanently saturated with saltwater, preventing oxygen from reaching microbes. This stops decomposition and locks carbon away for geological timescales.</p>\n<p><em>Slide Reference: Class 11 Slides 8–12.</em></p>\n</div>"
        },
        {
            "id": "EQB-11-04",
            "class_id": 11,
            "class_name": "Climate Change Technology Solutions",
            "topic": "Livestock Enteric Methane Mitigation",
            "category": "Short Answer & Definitions",
            "exams": [
                {"paper": "End Exam 2022", "section": "Section III, Q15", "marks": "1M"},
                {"paper": "Mid-2 2018", "section": "Q1(c)", "marks": "1M"}
            ],
            "marks": "1M",
            "importance": "HIGH (⭐⭐⭐⭐)",
            "prompt": "How can methane reduction from livestock be achieved? (Explain red seaweed additive and wearable devices).",
            "key_answer_points": "<ul>\n<li><strong>The Problem:</strong> Cattle burps (enteric fermentation) contribute ~14.5% of total global human greenhouse gas emissions.</li>\n<li><strong>Solution 1 (Red Seaweed Additive):</strong> Feeding cattle small amounts (0.2–0.5% of feed) of the red seaweed <em>Asparagopsis taxiformis</em> blocks the enzyme in rumen gut microbes, cutting methane by <strong>up to 80–90%</strong>.</li>\n<li><strong>Solution 2 (Zelp Wearable Halter):</strong> A smart nose halter detects methane from cattle exhales and oxidizes it via a catalytic filter into water and less-potent \\(\\text{CO}_2\\) (reducing warming impact by 53%).</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>The Biological Mechanism:</strong> Methanogens in the cow's rumen generate methane during digestion. The natural bromoform compounds in Asparagopsis seaweed react with vitamin B12 in gut microbes to halt methane synthesis safely.</p>\n<p><em>Slide Reference: Class 11 Slides 13–17.</em></p>\n</div>"
        },
        {
            "id": "EQB-11-05",
            "class_id": 11,
            "class_name": "Climate Change Technology Solutions",
            "topic": "Direct Air Capture (DAC) Companies & Contactor Physics",
            "category": "Short Answer & Definitions",
            "exams": [
                {"paper": "End Exam 2022", "section": "Section VI, Q(c)", "marks": "1M"},
                {"paper": "End Exam 2019", "section": "Section II, Q6", "marks": "2M"}
            ],
            "marks": "1M – 2M",
            "importance": "HIGH (⭐⭐⭐⭐)",
            "prompt": "Name leading commercial Direct Air Capture (DAC) companies and explain solid vs liquid contactor physics.",
            "key_answer_points": "<ul>\n<li><strong>Commercial DAC Pioneers:</strong> <strong>Climeworks</strong> (Switzerland/Iceland), <strong>Carbon Engineering</strong> (Canada/USA), and <strong>Global Thermostat</strong> (USA).</li>\n<li><strong>Solid Sorbent DAC (Climeworks):</strong> Uses chemical sponge filters with amine groups. Saturated filters are heated to <strong>\\(100^\\circ\\text{C}\\)</strong> using geothermal or waste heat to release pure \\(\\text{CO}_2\\).</li>\n<li><strong>Liquid Solvent DAC (Carbon Engineering):</strong> Uses liquid potassium hydroxide (\\(\\text{KOH}\\)) spray contactors: \\(2\\text{KOH} + \\text{CO}_2 \\rightarrow \\text{K}_2\\text{CO}_3 + \\text{H}_2\\text{O}\\). Releasing the carbon requires heating pellets in a natural gas kiln to <strong>\\(900^\\circ\\text{C}\\)</strong>.</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>Contactor Comparison:</strong> Solid sorbents require lower heat (\\(100^\\circ\\text{C}\\)) and produce water as a byproduct, making them ideal for geothermal sites like Iceland. Liquid systems can be built at massive megaton scale but require intense kiln heat (\\(900^\\circ\\text{C}\\)).</p>\n<p><em>Slide Reference: Class 11 Slides 18–22.</em></p>\n</div>"
        },
        {
            "id": "EQB-11-06",
            "class_id": 11,
            "class_name": "Climate Change Technology Solutions",
            "topic": "Wild Me AI Platform",
            "category": "Short Answer & Definitions",
            "exams": [
                {"paper": "End Exam 2023", "section": "Section I, Q1(c)", "marks": "1M"},
                {"paper": "End Exam 2022", "section": "Section III, Q6", "marks": "1M"}
            ],
            "marks": "1M",
            "importance": "HIGH (⭐⭐⭐⭐)",
            "prompt": "What is Wild Me?",
            "key_answer_points": "<ul>\n<li><strong>Definition:</strong> <strong>Wild Me</strong> is an open-source non-profit platform that uses computer vision and machine learning to identify, track, and monitor individual wild animals.</li>\n<li><strong>Mechanism:</strong> Scans photos taken by researchers and tourists, recognizing unique natural patterns like whale shark spots, zebra stripes, or giraffe coats—acting like facial recognition for animals.</li>\n<li><strong>Benefit:</strong> Replaces invasive tagging, radio-collars, or ear notching with non-invasive automated population counts and anti-poaching monitoring.</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>AI for Ecology:</strong> Machine learning turns crowd-sourced wildlife photography from safari tourists and camera traps into real-time biological population censuses.</p>\n<p><em>Slide Reference: Class 11 Slide 52.</em></p>\n</div>"
        },
        {
            "id": "EQB-11-07",
            "class_id": 11,
            "class_name": "Climate Change Technology Solutions",
            "topic": "TRASE Supply Chain Platform",
            "category": "Short Answer & Definitions",
            "exams": [
                {"paper": "End Exam 2022", "section": "Section III, Q14", "marks": "1M"}
            ],
            "marks": "1M",
            "importance": "MEDIUM (⭐⭐⭐)",
            "prompt": "What is the TRASE platform?",
            "key_answer_points": "<ul>\n<li><strong>Definition:</strong> <strong>TRASE</strong> (Transparency for Sustainable Economies) is a supply-chain mapping platform by the Stockholm Environment Institute and Global Canopy.</li>\n<li><strong>Function:</strong> Combines customs manifests, shipping logs, and satellite deforestation imagery to trace global agricultural commodities (beef, soy, palm oil, cocoa) from importing companies straight back to specific deforestation zones.</li>\n<li><strong>Goal:</strong> Enables companies, investors, and regulators to verify deforestation-free supply chains.</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>Supply Chain Transparency:</strong> Bridges the information gap between consumer supermarkets and tropical forest loss on the ground.</p>\n<p><em>Slide Reference: Class 11 Slide 53.</em></p>\n</div>"
        },
        {
            "id": "EQB-11-08",
            "class_id": 11,
            "class_name": "Climate Change Technology Solutions",
            "topic": "Tree Biomass Carbon Calculation",
            "category": "MCQ & Objective",
            "exams": [
                {"paper": "End Exam 2022", "section": "Section III, Q13", "marks": "1M"},
                {"paper": "End Exam 2019", "section": "Section II, Q1", "marks": "0.5M"}
            ],
            "marks": "1M",
            "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
            "prompt": "If the dry biomass of a tree is 2 tons, then it contains around ______ tons of carbon.",
            "key_answer_points": "<ul>\n<li><strong>Answer:</strong> <strong>ONE ton</strong> (or <strong>1 ton</strong>).</li>\n<li><strong>Scientific Rule:</strong> In forest ecology, dry wood biomass is universally calculated as <strong>50% elemental carbon by weight</strong> (\\(0.50 \\times \\text{Dry Biomass}\\)).</li>\n<li><strong>Calculation:</strong> \\(2 \\text{ tons dry biomass} \\times 50\\% = 1.0 \\text{ ton of carbon}\\).</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>Why 50%?:</strong> Wood is composed of cellulose, hemicellulose, and lignin, which average 50% carbon content by mass across nearly all tree species (standard IPCC forestry metric).</p>\n<p><em>Slide Reference: Class 11 Slide 7 & Class 9 Slide 14.</em></p>\n</div>"
        },
        {
            "id": "EQB-11-09",
            "class_id": 11,
            "class_name": "Climate Change Technology Solutions",
            "topic": "Ocean Carbon Sequestration Risks (Iron & Urea)",
            "category": "Descriptive & Case Study",
            "exams": [
                {"paper": "End Exam 2023", "section": "Section III, Q6", "marks": "3M"},
                {"paper": "End Exam 2019", "section": "Section IV, Q1(a,b)", "marks": "6M"}
            ],
            "marks": "3M – 6M",
            "importance": "HIGH (⭐⭐⭐⭐)",
            "prompt": "Explain the Iron Hypothesis and Urea fertilization for ocean carbon sequestration, and explain the negative impacts of ocean fertilization in the Sulu Sea.",
            "key_answer_points": "<ul>\n<li><strong>Iron Hypothesis (John Martin):</strong> In High-Nutrient Low-Chlorophyll (HNLC) ocean zones, adding trace iron sulfate (\\(\\text{FeSO}_4\\)) triggers massive phytoplankton blooms that take up \\(\\text{CO}_2\\) and sink to the deep sea bed upon death.</li>\n<li><strong>Urea Fertilization:</strong> Spreads nitrogen-rich urea into warm, nitrogen-poor tropical waters to stimulate algae growth.</li>\n<li><strong>Negative Impacts (Sulu Sea Incident):</strong>\n<br>• <strong>Marine Dead Zones (Hypoxia):</strong> Sinking algae rot, consuming dissolved oxygen and suffocating marine life.\n<br>• <strong>Toxic Algae Blooms:</strong> Favors neurotoxin-producing algae that poison local fisheries.\n<br>• <strong>Greenhouse Gas Production:</strong> Anoxic deep waters release <strong>methane (\\(\\text{CH}_4\\))</strong> and <strong>nitrous oxide (\\(\\text{N}_2\\text{O}\\))</strong>—a gas 273 times more potent than \\(\\text{CO}_2\\).</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>The Geoengineering Risk:</strong> Dumping nutrients into oceans can backfire. In the 2007 Sulu Sea experiment, rotting algae stripped oxygen from deeper layers, threatening coral reefs and generating powerful warming gases.</p>\n<p><em>Slide Reference: Class 11 Slides 36–41.</em></p>\n</div>"
        },
        {
            "id": "EQB-11-10",
            "class_id": 11,
            "class_name": "Climate Change Technology Solutions",
            "topic": "Arctic Summer Sea Ice Loss",
            "category": "Short Answer & Definitions",
            "exams": [
                {"paper": "End Exam 2023", "section": "Section II, Q19", "marks": "2M"}
            ],
            "marks": "2M",
            "importance": "HIGH (⭐⭐⭐⭐)",
            "prompt": "Why is melting of Arctic summer ice considered to be the single greatest threat?",
            "key_answer_points": "<ul>\n<li><strong>Albedo Flip:</strong> White sea ice reflects <strong>85% of solar heat</strong>. Dark open ocean reflects only <strong>10%</strong>, absorbing 90% of heat and creating an unstoppable runaway warming loop (ice-albedo feedback).</li>\n<li><strong>Permafrost Thaw:</strong> Warmer Arctic temperatures thaw tundra permafrost, threatening to release up to <strong>1,500 billion tonnes</strong> of trapped ancient carbon as methane and \\(\\text{CO}_2\\).</li>\n<li><strong>Jet Stream Destabilization:</strong> Weakens the polar vortex, locking weather systems in place to cause catastrophic prolonged heatwaves, floods, and winter freezes worldwide.</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>Earth's Mirror:</strong> The Arctic functions as our global planetary heat shield. Losing summer ice turns that shield into a heat absorber.</p>\n<p><em>Slide Reference: Class 11 Slides 5–6 & Class 8 Slides 12–15.</em></p>\n</div>"
        },
        {
            "id": "EQB-11-11",
            "class_id": 11,
            "class_name": "Climate Change Technology Solutions",
            "topic": "Ocean Acidification & Small pH Changes",
            "category": "Short Answer & Definitions",
            "exams": [
                {"paper": "End Exam 2023", "section": "Section II, Q12", "marks": "2M"}
            ],
            "marks": "2M",
            "importance": "HIGH (⭐⭐⭐⭐)",
            "prompt": "Why be concerned with a small change in Ocean pH?",
            "key_answer_points": "<ul>\n<li><strong>Logarithmic Scale:</strong> A drop of just <strong>0.1 pH units</strong> represents a massive <strong>30% surge in hydrogen ion concentration</strong> (\\([\\text{H}^+]\\)).</li>\n<li><strong>Dissolves Shells & Coral Skeletons:</strong> Extra \\(\\text{H}^+\\) ions bind with carbonate ions (\\(\\text{CO}_3^{2-}\\)), starving corals and shellbuilders of the building blocks needed to make calcium carbonate (\\(\\text{CaCO}_3\\)).</li>\n<li><strong>Marine Food Web Disruption:</strong> Dissolves shells of tiny sea butterflies (pteropods), which form the foundational diet for commercial fish like salmon, mackerel, and cod.</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>The Chemistry:</strong> Absorbed \\(\\text{CO}_2\\) forms carbonic acid (\\(\\text{H}_2\\text{CO}_3\\)), releasing \\(\\text{H}^+\\) that robs calcifying organisms of carbonate ions.</p>\n<p><em>Slide Reference: Class 11 Slides 34–35 & Class 10 Slides 18–21.</em></p>\n</div>"
        },
        {
            "id": "EQB-11-12",
            "class_id": 11,
            "class_name": "Climate Change Technology Solutions",
            "topic": "Hypercane & Ozone Layer Impact",
            "category": "Short Answer & Definitions",
            "exams": [
                {"paper": "End Exam 2023", "section": "Section I, Q3", "marks": "1M"},
                {"paper": "End Exam 2022", "section": "Section III, Q4", "marks": "1M"}
            ],
            "marks": "1M",
            "importance": "MEDIUM (⭐⭐⭐)",
            "prompt": "How hypercane impacts Earth's Ozone layer?",
            "key_answer_points": "<ul>\n<li><strong>Definition:</strong> A hypothetical mega-cyclone forming if oceans reach extreme temperatures of <strong>\\(50^\\circ\\text{C}\\)</strong>.</li>\n<li><strong>Ozone Destruction:</strong> Its massive updrafts would blast clouds of water vapor and sea salt <strong>30 km high into the stratosphere</strong>, triggering chemical reactions that break down the protective ozone shield and expose Earth to lethal UV radiation.</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>Stratospheric Injection:</strong> Standard hurricanes stay within the troposphere (under 15 km). Hypercanes would penetrate deep into the stratosphere, injecting water vapor that catalytically destroys ozone.</p>\n<p><em>Slide Reference: Class 11 Slide 54.</em></p>\n</div>"
        },
        {
            "id": "EQB-11-13",
            "class_id": 11,
            "class_name": "Climate Change Technology Solutions",
            "topic": "Lightning Increase in Climate Change",
            "category": "Short Answer & Definitions",
            "exams": [
                {"paper": "End Exam 2022", "section": "Section IX, Q(a)", "marks": "2M"}
            ],
            "marks": "2M",
            "importance": "MEDIUM (⭐⭐⭐)",
            "prompt": "Why there will be more lightning process in the event of climate change?",
            "key_answer_points": "<ul>\n<li><strong>Physics:</strong> Lightning is generated when strong convective updrafts cause ice particles to collide and build up electrical charges inside storm clouds.</li>\n<li><strong>Higher Moisture & Heat:</strong> Warmer air holds ~7% more moisture per \\(^\\circ\\text{C}\\) and fuels stronger convective energy.</li>\n<li><strong>12% Spike per Degree:</strong> Climate models project about a <strong>12% increase in lightning strikes for every \\(1^\\circ\\text{C}\\) of global warming</strong>, greatly increasing forest wildfire ignitions.</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>Wildfire Risk:</strong> More frequent lightning strikes dry northern boreal forests, sparking massive wildfires that release more stored carbon.</p>\n<p><em>Slide Reference: Class 11 Slide 55.</em></p>\n</div>"
        },
        {
            "id": "EQB-11-14",
            "class_id": 11,
            "class_name": "Climate Change Technology Solutions",
            "topic": "Afforestation vs Reforestation & Forest Saturation",
            "category": "Differentiate Between",
            "exams": [
                {"paper": "End Exam 2019", "section": "Section II, Q4, Q6", "marks": "3M"}
            ],
            "marks": "3M",
            "importance": "HIGH (⭐⭐⭐⭐)",
            "prompt": "Differentiate between afforestation and reforestation. In natural forests, there is a net addition to standing biomass leading to carbon storage only until maturity – why not later?",
            "key_answer_points": "<ul>\n<li><strong>Afforestation:</strong> Planting trees on land that has historically never had forest cover (or has been barren for 50+ years).</li>\n<li><strong>Reforestation:</strong> Replanting trees on recently cleared, logged, or deforested land.</li>\n<li><strong>Why Carbon Addition Stops at Maturity:</strong> Young forests add biomass rapidly. When a forest reaches old-growth maturity, <strong>photosynthesis (Gross Primary Productivity) balances out with ecosystem respiration</strong> (plant respiration plus microbial decay of fallen wood). Net Ecosystem Productivity (NEP) drops to zero (steady-state equilibrium).</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>Stock vs Flux:</strong> While a mature forest stops adding <em>new</em> carbon each year, it maintains an enormous permanent <em>stock</em> of carbon that must not be cleared.</p>\n<p><em>Slide Reference: Class 11 Slide 7 & Class 9 Slides 8–12.</em></p>\n</div>"
        },
        {
            "id": "EQB-11-15",
            "class_id": 11,
            "class_name": "Climate Change Technology Solutions",
            "topic": "Agroforestry for Carbon Mitigation",
            "category": "Descriptive & Case Study",
            "exams": [
                {"paper": "End Exam 2019", "section": "Section II, Q5", "marks": "3.5M"}
            ],
            "marks": "3.5M",
            "importance": "HIGH (⭐⭐⭐⭐)",
            "prompt": "What is Agroforestry? Why it is an attractive option for carbon mitigation?",
            "key_answer_points": "<ul>\n<li><strong>Definition:</strong> An integrated farming system combining trees and woody shrubs with food crops and/or livestock on the same land.</li>\n<li><strong>Dual Carbon Storage:</strong> Traps carbon in tree trunks above ground and deep soil root layers below ground without sacrificing crop yields.</li>\n<li><strong>Climate Resilience:</strong> Deep roots prevent soil erosion, retain water during dry spells, and fix nitrogen in soils.</li>\n<li><strong>Economic Diversification:</strong> Provides farmers with fruit, timber, nuts, and fodder alongside standard annual crops.</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>Farming with Trees:</strong> Agroforestry turns working agricultural land into productive carbon sinks while improving soil health and food security.</p>\n<p><em>Slide Reference: Class 11 Slide 13 & Class 9 Slide 19.</em></p>\n</div>"
        },
        {
            "id": "EQB-11-16",
            "class_id": 11,
            "class_name": "Climate Change Technology Solutions",
            "topic": "Conservation Agricultural Tillage",
            "category": "Short Answer & Definitions",
            "exams": [
                {"paper": "End Exam 2023", "section": "Section II, Q16", "marks": "2M"}
            ],
            "marks": "2M",
            "importance": "MEDIUM (⭐⭐⭐)",
            "prompt": "Conservation agricultural tillage and its uses.",
            "key_answer_points": "<ul>\n<li><strong>Definition:</strong> Farming that minimizes or avoids mechanical plowing (no-till or reduced-till), leaving at least 30% of soil covered with crop residue.</li>\n<li><strong>Protects Soil Carbon:</strong> Plowing exposes underground organic matter to oxygen, turning soil carbon into \\(\\text{CO}_2\\). No-till keeps carbon trapped underground.</li>\n<li><strong>Saves Water & Soil:</strong> Surface crop residue acts as mulch, cutting evaporation by 50% and protecting topsoil from water and wind erosion.</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>Living Soil:</strong> Deep plowing breaks down soil microbiomes and causes erosion (like the 1930s Dust Bowl). Conservation tillage preserves soil moisture and microbial life.</p>\n<p><em>Slide Reference: Class 11 Slide 14 & Class 9 Slide 22.</em></p>\n</div>"
        }
    ]

if __name__ == "__main__":
    qs = get_class11_questions()
    print(f"Class 11: {len(qs)} questions ready.")
