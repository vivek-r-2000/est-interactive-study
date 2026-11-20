import json
from pathlib import Path

cards = [
    {
        "card_num": 1,
        "title": "Negative Emissions Framework, Afforestation & Pyrolysis Biochar",
        "act": "ACT I: NATURE-BASED & BIOSPHERIC SINKS",
        "slides_covered": [1, 2, 3],
        "slides_label": "Slides 1, 2, 3",
        "exam_rating": {
            "tier": "HIGH (⭐⭐⭐⭐)",
            "stars": 4,
            "badge_class": "badge-high",
            "frequency_count": "3 appearances in past exams",
            "recent_papers": ["Mid-1 2022 (Q3)", "Quiz-3 2020 (Q1b)", "End Exam 2019 (Sec II)"],
            "exam_tip": "Exams test the core rationale: why emission reduction alone is insufficient to reach net-zero (residual hard-to-abate sectors demand Negative Emission Technologies / NETs). Be ready to contrast A/R costs with biochar durability."
        },
        "eli15_takeaway": "Cutting future emissions isn't enough to stay below 1.5°C; we must actively suck historical CO2 out of the atmosphere. Biochar does this by cooking organic plant waste without oxygen into pure carbon sponge that locks into soil for centuries.",
        "key_facts": [
            "<strong>Slide 2 — Paris Agreement (COP21) Target:</strong> Aims to limit global surface warming to 1.5°C. To reach true net-zero, humanity requires Negative Emissions Technologies (NETs) to counterbalance residual emissions from heavy transport, industry, and agriculture.",
            "<strong>Slide 2 — Afforestation & Reforestation (A/R) Metrics:</strong> Sequestration rate of <strong>3.7 tonnes CO2 / hectare / year</strong> at an operating cost of <strong>$20–$100 per tonne</strong>. Major obstacles: land-use competition with agriculture, vulnerability to forest fires (permanence risk), water consumption, and albedo changes in snowy latitudes.",
            "<strong>Slide 3 — Biochar Sequestration Capacity:</strong> Holds the technical potential to sequester up to <strong>4.8 billion tonnes (4.8 Gt) of CO2 per year</strong> globally.",
            "<strong>Slide 3 — Pyrolysis Production Mechanism:</strong> Produced by heating renewable biomass at high temperatures (400–700°C) in an oxygen-limited or oxygen-free environment. Without pyrolysis, raw agricultural biomass either decomposes or is burned openly in fields, releasing methane and CO2 rapidly.",
            "<strong>Slide 3 — Agricultural & Soil Co-benefits:</strong> Biochar converts labile plant carbon into a recalcitrant aromatic carbon matrix that resists microbial decay for centuries, while significantly enhancing soil fertility, cation exchange capacity, and soil moisture retention."
        ],
        "mental_model": "Think of afforestation as borrowing carbon from the atmosphere on a 50-year lease that a wildfire can cancel tomorrow, whereas biochar is burning that carbon into an inert charcoal sponge and burying it permanently in an underground bank vault.",
        "checkpoint": {
            "question": "Why is biochar considered significantly more permanent than conventional afforestation for carbon removal?",
            "options": [
                "Biochar undergoes natural nuclear fusion in the topsoil",
                "Pyrolysis alters the organic carbon into a stable aromatic structure resistant to microbial decomposition for hundreds of years",
                "Biochar evaporates into the stratosphere where it blocks solar radiation",
                "Biochar absorbs oxygen from the soil to prevent plant roots from decomposing"
            ],
            "correct": 1,
            "explanation": "Pyrolysis transforms perishable cellulosic biomass into highly recalcitrant aromatic carbon networks that soil microbes cannot readily break down, storing carbon safely for centuries while improving soil quality."
        }
    },
    {
        "card_num": 2,
        "title": "Blue Carbon: Coastal Ocean Super-Sinks (Mangroves & Salt Marshes)",
        "act": "ACT I: NATURE-BASED & BIOSPHERIC SINKS",
        "slides_covered": [4],
        "slides_label": "Slide 4 (Standalone Core Topic)",
        "exam_rating": {
            "tier": "CRITICAL (⭐⭐⭐⭐⭐)",
            "stars": 5,
            "badge_class": "badge-critical",
            "frequency_count": "5 appearances in past exams (Highest Recurrence)",
            "recent_papers": ["End Exam 2023 (Q2a, 3M)", "End Exam 2022 (Q1, 4M)", "End Exam 2019 (Q1b)", "End Exam 2018 (Q3)"],
            "exam_tip": "High-yield exam staple. Always state the three essential points: (1) 3–19% of global deforestation emissions originate from degraded coastal habitats; (2) Mangroves sequester carbon 10–40x faster than terrestrial rainforests in anoxic mud; (3) Multi-hazard coastal defense against cyclones and tidal surges."
        },
        "eli15_takeaway": "Blue carbon is carbon captured by coastal marine ecosystems (mangroves, tidal salt marshes, seagrass meadows). These coastal wetlands bury organic carbon deep in waterlogged, oxygen-deprived mud where it never rots, trapping carbon 40 times faster than tropical jungles.",
        "key_facts": [
            "<strong>Slide 4 — Definition of Blue Carbon:</strong> Biologically driven carbon flux and storage in coastal and marine habitats, dominated by mangroves, tidal marshes, and seagrass meadows.",
            "<strong>Slide 4 — High Degradation Emissions:</strong> Destroying and draining coastal wetlands accounts for an estimated <strong>3% to 19% of total global deforestation emissions</strong>, despite covering less than 0.5% of the sea floor.",
            "<strong>Mechanism — Anoxic Sediment Trapping:</strong> Coastal wetland roots trap organic sediment in permanently waterlogged, saline, oxygen-depleted (anoxic) mud. Because aerobic bacteria cannot survive without oxygen, organic matter is preserved without decomposing, locking carbon away for millennia.",
            "<strong>Volumetric Rate vs Terrestrial Forests:</strong> Mangrove sediments accumulate and bury carbon at rates <strong>10 to 40 times faster</strong> than terrestrial tropical rainforests per unit area.",
            "<strong>Multi-Hazard Ecosystem Services:</strong> Mangrove root complexes attenuate up to 66% of wave energy within 100 meters, serving as physical storm-surge buffers against cyclones while acting as critical nursery grounds for 75% of commercial tropical fish species."
        ],
        "mental_model": "Terrestrial forests store carbon in tree trunks above ground where fire or termites can quickly release it. Blue carbon ecosystems push carbon deep into a salty, airless underwater swamp where no microbe can breathe to burn it.",
        "checkpoint": {
            "question": "What is the primary biogeochemical reason why blue carbon habitats sequester carbon for thousands of years without releasing it?",
            "options": [
                "High salinity dissolves carbon dioxide directly into limestone crystals",
                "Waterlogged, oxygen-poor (anoxic) mud prevents aerobic microorganisms from decomposing trapped organic matter",
                "Ocean waves continuously compress carbon into crude oil",
                "Mangrove leaves reflect 100% of incoming sunlight preventing cellular respiration"
            ],
            "correct": 1,
            "explanation": "Because coastal soils are permanently submerged and waterlogged, they are anoxic (deprived of oxygen), which halts aerobic microbial decay and preserves organic carbon in thick sediment layers for thousands of years."
        }
    },
    {
        "card_num": 3,
        "title": "Building with Biomass: CLT Timber, Hemp & Embodied Carbon Inversion",
        "act": "ACT I: NATURE-BASED & BIOSPHERIC SINKS",
        "slides_covered": [5],
        "slides_label": "Slide 5 (Standalone Focus)",
        "exam_rating": {
            "tier": "HIGH (⭐⭐⭐⭐)",
            "stars": 4,
            "badge_class": "badge-high",
            "frequency_count": "2 appearances in past exams",
            "recent_papers": ["Mid-1 2022 (Q3c)", "Quiz-3 2020 (Q2)"],
            "exam_tip": "Focus on the shift from 'operational emissions' to 'embodied emissions' in architecture: replacing carbon-intensive Portland cement and steel with photosynthetic structural biomass turns cities from carbon emitters into carbon vaults."
        },
        "eli15_takeaway": "Instead of constructing skyscrapers with steel and cement that dump gigatons of CO2 into the sky, we can build tall buildings using compressed cross-laminated timber, hemp-lime walls, and sheep wool insulation, locking forest carbon into urban buildings for over a century.",
        "key_facts": [
            "<strong>Slide 5 — Structural Elements:</strong> Utilizing engineered <strong>Cross-Laminated Timber (CLT)</strong> and structural bamboo in place of reinforced concrete beams and structural steel columns.",
            "<strong>Slide 5 — Natural Insulation Materials:</strong> Replacing petroleum-based polyurethane and fiberglass foam insulation with agricultural <strong>hemp fibers and sheep's wool</strong>, drastically lowering manufacturing energy footprints.",
            "<strong>Slide 5 — Carbon-Negative Walling (Hemp-Lime):</strong> Using hempcrete (a composite of industrial hemp woody core/shiv and hydraulic lime binder) for monolithic, breathable, fire-resistant exterior walls.",
            "<strong>Embodied Carbon Inversion:</strong> Conventional construction materials account for ~11% of global carbon emissions through high-temperature calcination and smelting. Biomass buildings act as net carbon sinks, sequestering ~1 tonne of atmospheric CO2 in every cubic meter of engineered timber for 50–100+ years.",
            "<strong>Circular Lifecycle Durability:</strong> Engineered mass timber exhibits high fire resistance (forming a predictable char layer that insulates the internal structural core) while maintaining high strength-to-weight ratios."
        ],
        "mental_model": "A conventional concrete building is an enormous smokestack frozen in time. A cross-laminated timber building is a captured forest standing in the middle of a downtown city street.",
        "checkpoint": {
            "question": "How does using Cross-Laminated Timber (CLT) and hemp-lime walling achieve 'embodied carbon inversion' in urban construction?",
            "options": [
                "They generate electricity when compressed by structural loads",
                "They actively absorb sunlight to generate synthetic biofuels for the building",
                "They replace carbon-intensive concrete/steel with photosynthetic biomass that safely locks absorbed atmospheric CO2 into structural materials for decades",
                "They dissolve atmospheric nitrogen to fertilize surrounding city parks"
            ],
            "correct": 2,
            "explanation": "Mass timber and hemp-lime lock away the biogenic carbon captured by living plants during photosynthesis, storing it in permanent building structures and displacing fossil-fuel-intensive cement and steel production."
        }
    },
    {
        "card_num": 4,
        "title": "Earth-Scale Chemistry: Cloud Alkali Treatment & Enhanced Rock Weathering",
        "act": "ACT II: GEOCHEMICAL & ATMOSPHERIC INTERVENTIONS",
        "slides_covered": [6, 7],
        "slides_label": "Slides 6, 7",
        "exam_rating": {
            "tier": "MEDIUM-HIGH (⭐⭐⭐)",
            "stars": 3,
            "badge_class": "badge-medium",
            "frequency_count": "2 appearances in past exams",
            "recent_papers": ["Mid-1 2024 (Q2)", "Quiz-1 2023 (Q3)"],
            "exam_tip": "Expect numerical and chemical questions on Enhanced Weathering: natural silicate dissolution absorbs 3% of fossil emissions; grinding basalt expands surface area to absorb up to 3.7 Gt CO2eq/yr while actively counteracting ocean acidification."
        },
        "eli15_takeaway": "Over millions of years, rain and rocks naturally dissolve atmospheric CO2 and wash it into the oceans. Enhanced weathering supercharges this process by crushing volcanic rocks into fine dust and spreading it on croplands to capture CO2 in weeks instead of centuries.",
        "key_facts": [
            "<strong>Slide 6 — Cloud & Ocean Treatment with Alkali:</strong> Offsetting global emissions by dispersing <strong>56 million tonnes of potassium hydroxide (KOH)</strong> into clouds across 0.4% of Earth's surface (an area equivalent to the Greenland ice sheet).",
            "<strong>Slide 6 — Ocean Liming Scale:</strong> Counteracting ocean acidification requires adding approximately <strong>2.5 billion tonnes of limestone</strong>, scaling up to <strong>8 billion tonnes per year</strong> to neutralize carbonic acid in marine waters.",
            "<strong>Slide 7 — Baseline Natural Rock Weathering:</strong> Natural chemical weathering of silicate rocks currently absorbs approximately <strong>3% of global fossil fuel CO2 emissions</strong> each year via slow geologic cycles.",
            "<strong>Slide 7 — Enhanced Weathering (EW) Mechanism:</strong> Pulverizing reactive silicate rocks (such as volcanic basalt or olivine) into fine micron-sized powder multiplies surface area exponentially, accelerating the mineral dissolution reaction: CaSiO3 + 2CO2 + H2O → Ca²⁺ + 2HCO3⁻ + SiO2.",
            "<strong>Slide 7 — Sequestration Potential & Ocean Co-benefit:</strong> Enhanced weathering could capture up to <strong>3.7 billion tonnes of CO2eq per year</strong> globally while releasing bicarbonate ions into waterways, directly counteracting ocean acidification."
        ],
        "mental_model": "Think of natural rock weathering as an ant drinking a gallon of water drop by drop over a million years. Enhanced weathering grinds the rock into billions of microscopic grains so a billion ants drink the entire gallon in one afternoon.",
        "checkpoint": {
            "question": "What is the primary chemical product formed when pulverized basalt undergoes enhanced weathering with atmospheric carbon dioxide and rainwater?",
            "options": [
                "Gaseous methane (CH4) vented into the upper atmosphere",
                "Soluble bicarbonate ions (HCO3⁻) that safely wash into oceans and buffer marine acidity",
                "Solid sulfuric acid crystals that acidify topsoil",
                "Pure liquid carbon monoxide (CO)"
            ],
            "correct": 1,
            "explanation": "Silicate weathering converts dissolved CO2 and water into stable, soluble bicarbonate ions (HCO3⁻) and silica, which travel via river networks into oceans where they safely buffer acidification for over 100,000 years."
        }
    },
    {
        "card_num": 5,
        "title": "Direct Air Capture (DAC): Physics, Contactors, Liquid vs Solid Sorbents & BIGs",
        "act": "ACT II: GEOCHEMICAL & ATMOSPHERIC INTERVENTIONS",
        "slides_covered": [8, 9, 10, 12, 13],
        "slides_label": "Slides 8, 9, 10, 12, 13",
        "exam_rating": {
            "tier": "HIGH (⭐⭐⭐⭐)",
            "stars": 4,
            "badge_class": "badge-high",
            "frequency_count": "4 appearances in past exams",
            "recent_papers": ["End Exam 2023 (Q2b)", "Mid-1 2024 (Q4)", "Quiz-4 2020 (Q2)", "End Exam 2019 (Sec I)"],
            "exam_tip": "Memorize the contrast between high-temperature liquid hydroxide systems (Carbon Engineering calciner at 900°C) and low-temperature solid guanidines/BIGs (120°C mild heating). Be prepared to state the primary bottleneck: massive energetic penalty per ton of CO2 captured."
        },
        "eli15_takeaway": "Direct Air Capture uses giant fans to suck ambient air through chemical filters that grab CO2 like a molecular sponge. The biggest challenge is energy: air contains only 0.04% CO2, so scrubbing a single ton requires processing millions of cubic meters of air.",
        "key_facts": [
            "<strong>Slide 8 — DAC Plant Architectures:</strong> Two core deployment paradigms: (1) Standalone DAC coupled to deep geologic storage (permanent CDR); (2) DAC coupled to Enhanced Oil Recovery (EOR - controversial fossil utilization).",
            "<strong>Slide 9 — Air-to-Fuels Plants (Carbon Engineering):</strong> Utilizes captured atmospheric CO2 and electrolytic hydrogen (H2 from water splitting using renewable electricity) to synthesize drop-in hydrocarbons: low-carbon aviation jet fuel (Jet-A), diesel, and gasoline.",
            "<strong>Slide 10 — Closed-Loop Chemical Cycle:</strong> Ambient air passes through an air contactor with potassium hydroxide (KOH) spray → forms potassium carbonate (K2CO3) → reacts in a pellet reactor with calcium hydroxide to precipitate calcium carbonate (CaCO3) pellets → heated in an oxy-fired calciner at ~900°C to release pure CO2 → calcium oxide (CaO) is hydrated in a slaker to regenerate the sorbent.",
            "<strong>Slide 12 — Gigatonne-Scale Energy Penalties:</strong> Scrubbing ambient air (at 420 ppm / 0.042% concentration) requires massive parasitic energy loads: 1,500–2,500 kWh of thermal energy plus 300–500 kWh of electrical energy per tonne of CO2, creating major supply chain and clean grid bottlenecks.",
            "<strong>Slide 13 — Bis-iminoguanidines (BIGs) Low-Temperature Scrubbers:</strong> Oak Ridge National Laboratory discovery: Guanidine-based crystallization agents scrub CO2 like scuba rebreathers. BIGs selectively bind bicarbonate from aqueous solution; heating the solid to just <strong>~120°C (mild heating)</strong> releases pure CO2 gas (trapped in collection vessels) while water vapors condense in ice-cooled tubes, cutting regeneration thermal energy by over 60% compared to traditional calciners."
        ],
        "mental_model": "Filtering carbon from a coal smokestack is like catching fish in a crowded hatchery (15% CO2). Direct air capture is like catching a specific minnow swimming in Lake Superior (0.04% CO2) — you have to pump and strain millions of liters of water to find one fish.",
        "checkpoint": {
            "question": "What is the key thermodynamic advantage of Bis-iminoguanidines (BIGs) over traditional industrial calcium hydroxide/calcination cycles for CO2 stripping?",
            "options": [
                "BIGs release CO2 under mild heating at ~120°C instead of requiring energy-intensive calciners operating at ~900°C",
                "BIGs convert carbon directly into enriched uranium",
                "BIGs eliminate the need for ambient air contactor fans completely",
                "BIGs operate exclusively underwater inside ocean trenches"
            ],
            "correct": 0,
            "explanation": "Traditional calciners require extreme temperatures (~900°C) to break calcium carbonate bonds, requiring massive fossil or oxy-fuel combustion. BIGs release pure CO2 at a gentle ~120°C, vastly reducing thermal energy inputs."
        }
    },
    {
        "card_num": 6,
        "title": "Industrial DAC Global Deployments & Deep Geological Storage",
        "act": "ACT II: GEOCHEMICAL & ATMOSPHERIC INTERVENTIONS",
        "slides_covered": [11, 14, 16],
        "slides_label": "Slides 11, 14, 16",
        "exam_rating": {
            "tier": "HIGH (⭐⭐⭐⭐)",
            "stars": 4,
            "badge_class": "badge-high",
            "frequency_count": "3 appearances in past exams",
            "recent_papers": ["End Exam 2024 (Q1c)", "End Exam 2023 (Q2c)", "Quiz-2 2020 (Q4)"],
            "exam_tip": "Focus on the real-world operational scale: current commercial capture capacity is ~8,000 tCO2/yr across 18 plants globally. Master the CarbFix basalt mineralization mechanism in Iceland and the Net Zero Teesside (NZT) offshore North Sea saline storage model."
        },
        "eli15_takeaway": "Once CO2 is pulled from thin air, where does it go? Leading facilities in Iceland dissolve the gas in water and pump it deep into volcanic basalt, where chemical reactions turn the gas into solid stone in under two years.",
        "key_facts": [
            "<strong>Slide 11 — Geological Storage Formations:</strong> CO2 is compressed into a supercritical fluid (>73.8 bar, >31.1°C) and injected into deep geological reservoirs: deep saline aquifers, permeable basalt formations, depleted oil/gas fields, and deep sub-seabed geological layers beneath impermeable caprocks.",
            "<strong>Slide 14 — Global Commercial Landscape:</strong> The world's leading DAC technology companies include <strong>Climeworks (Switzerland)</strong>, <strong>Carbon Engineering (Canada)</strong>, and <strong>Global Thermostat (USA)</strong>.",
            "<strong>Slide 14 — Operational Fleet Capacity:</strong> Together, these companies operate <strong>18 commercial plants</strong> ranging in unit scale from 1 tCO2/year up to 4,000 tCO2/year (Climeworks Orca plant in Iceland), capturing a global total of <strong>just under 8,000 tCO2/year</strong>.",
            "<strong>Slide 14 — Utilization vs Permanent Sequestration Split:</strong> Approximately half of captured CO2 is sequestered permanently underground (equivalent to offsetting the annual emissions of only ~870 passenger cars), while the other half is sold for commercial utilization (sparkling beverages, agricultural greenhouses, synthetic fuels).",
            "<strong>Slide 16 — Net Zero Teesside (NZT Project), UK:</strong> A massive industrial cluster decarbonization initiative in Teesside, UK. Captured CO2 from power plants and heavy industrial facilities is compressed, piped offshore, and buried securely in deep geological saline aquifers beneath the North Sea (Endurance reservoir), targeting up to 10 million tonnes of annual storage."
        ],
        "mental_model": "Deep geological mineralization (CarbFix) is like making seltzer water, injecting it deep into crushed volcanic rock, and letting the minerals react until the carbon dioxide turns into solid limestone countertops two kilometers underground.",
        "checkpoint": {
            "question": "What is the global operational capacity of commercial DAC plants today as highlighted in the course material, and how is the captured CO2 distributed?",
            "options": [
                "Over 100 million tCO2/year, all converted into synthetic gasoline",
                "Just under 8,000 tCO2/year across 18 plants; half permanently sequestered (offsetting ~870 cars) and half sold for industrial products",
                "500,000 tCO2/year, entirely vented into abandoned coal mines",
                "Zero tonnes per year because no commercial DAC facility has ever been constructed"
            ],
            "correct": 1,
            "explanation": "As documented on Slide 14, the 18 operating commercial DAC plants capture just under 8,000 tonnes of CO2 per year — roughly half is stored permanently in geology while the remaining half is utilized in commercial products."
        }
    },
    {
        "card_num": 7,
        "title": "Air-to-Luxury: Aether Diamonds from Captured Atmospheric Pollution",
        "act": "ACT III: COMMERCIAL CIRCULARITY & INDUSTRIAL CASE STUDIES",
        "slides_covered": [15],
        "slides_label": "Slide 15 (Standalone Core Case Study)",
        "exam_rating": {
            "tier": "CRITICAL (⭐⭐⭐⭐⭐)",
            "stars": 5,
            "badge_class": "badge-critical",
            "frequency_count": "2 appearances in past exams (High Mark Weight)",
            "recent_papers": ["End Exam 2023 (Q4, 3M)", "End Exam 2022 (Q5, 5M)"],
            "exam_tip": "High-yield descriptive case study. You must list all 5 steps in correct sequence: (1) DAC CO2 sourcing from Climeworks; (2) Catalytic conversion to pure methane (CH4); (3) CVD plasma diamond growth; (4) 100% clean solar/nuclear power; (5) Surat, India cutting and polishing."
        },
        "eli15_takeaway": "Aether creates real, certified vegan diamonds out of captured smog and air pollution. They take CO2 scrubbed from the air, convert it to pure methane gas, bake it into sparkling rough diamonds inside vacuum plasma chambers, and polish them in Surat, India.",
        "key_facts": [
            "<strong>Slide 15 — Step 1 (CO2 Sourcing):</strong> Aether purchases captured atmospheric CO2 directly from Climeworks' commercial DAC facilities in Europe and ships it to diamond synthesis reactors in the United States.",
            "<strong>Slide 15 — Step 2 (Methanation Reaction):</strong> The raw CO2 is processed through a proprietary catalytic methanation process (Sabatier reaction: CO2 + 4H2 → CH4 + 2H2O) to convert carbon dioxide into ultra-high-purity methane (CH4).",
            "<strong>Slide 15 — Step 3 (Chemical Vapor Deposition - CVD):</strong> The pure methane is injected into specialized diamond reactors where Chemical Vapor Deposition (CVD) heats hydrocarbon gas to extreme temperatures under near-vacuum conditions, precipitating pure carbon atoms layer by layer onto substrate seeds over several weeks.",
            "<strong>Slide 15 — Step 4 (100% Carbon-Free Power):</strong> The synthesis reactors and manufacturing stages are powered entirely by zero-emission renewable and clean energy sources (solar and nuclear power).",
            "<strong>Slide 15 — Step 5 (Surat Cutting & New York Retail):</strong> Rough crystal diamonds are shipped to Surat, Gujarat, India (the global diamond polishing hub) for precision laser cutting and facet polishing, before being sent to New York City for high-end luxury jewelry sales.",
            "<strong>Slide 15 — Environmental Metrics:</strong> Each 1-carat Aether diamond removes the equivalent of <strong>20 tonnes of atmospheric CO2</strong> (offsetting ~1.5 years of an average human's footprint), consumes half the energy of mined gems, and completely avoids the <strong>127 gallons of water</strong> traditionally wasted per mined carat."
        ],
        "mental_model": "Traditional diamond mining digs massive open-pit craters that scar the Earth and waste thousands of gallons of water. Aether catches toxic sky pollution, turns it into plasma gas, and freezes it into an eternal gem.",
        "checkpoint": {
            "question": "What are the chemical gas intermediate and manufacturing technology used to grow Aether diamonds from captured CO2?",
            "options": [
                "Carbon monoxide (CO) via blast furnace smelting",
                "High-purity methane (CH4) via Chemical Vapor Deposition (CVD) under vacuum plasma conditions",
                "Nitrous oxide (N2O) via liquid nitrogen freezing",
                "Sulfur dioxide (SO2) via high-pressure hydraulic fracturing"
            ],
            "correct": 1,
            "explanation": "Captured CO2 is catalytically converted into high-purity methane (CH4), which is fed into Chemical Vapor Deposition (CVD) plasma reactors to grow rough gem diamonds over several weeks."
        }
    },
    {
        "card_num": 8,
        "title": "Agricultural Decarbonization: Enteric Cattle Methane, Red Seaweed & Insects",
        "act": "ACT III: COMMERCIAL CIRCULARITY & INDUSTRIAL CASE STUDIES",
        "slides_covered": [17, 18, 19],
        "slides_label": "Slides 17, 18, 19",
        "exam_rating": {
            "tier": "HIGH (⭐⭐⭐⭐)",
            "stars": 4,
            "badge_class": "badge-high",
            "frequency_count": "3 appearances in past exams",
            "recent_papers": ["End Exam 2022 (Q3, 3M)", "Quiz-3 2020 (Q2)", "End Exam 2018 (Q4b)"],
            "exam_tip": "Be prepared to write down the exact scientific name of the red seaweed (Asparagopsis taxiformis) and explain how bromoform halts the microbial methanogenesis enzyme pathway. Contrast with Zelp wearable oxidation halters."
        },
        "eli15_takeaway": "Cows burping methane create nearly 15% of all human-driven greenhouse gases. Feeding them tiny pinches of red tropical seaweed cuts their burps by 80%, while replacing cattle beef with cricket burgers slashes agricultural land and water use to near zero.",
        "key_facts": [
            "<strong>Slide 17 — Meat & Dairy Global Footprint:</strong> Global meat and dairy production generates <strong>7.1 gigatons (Gt) of greenhouse gases annually</strong>, representing <strong>14.5% of total man-made global GHG emissions</strong>.",
            "<strong>Slide 17 — Enteric Fermentation Driver:</strong> The planet's 1.5 billion head of cattle produce enteric methane (CH4) during rumination, a short-lived greenhouse gas with a warming potential 28–36 times more potent than CO2 over a century.",
            "<strong>Slide 18 — Asparagopsis taxiformis Red Seaweed:</strong> Feeding cattle small dietary supplements (0.2–0.5% of feed) of tropical red seaweed (<em>Asparagopsis taxiformis</em>) reduces bovine methane emissions by up to <strong>80%</strong>. Bioactive bromoform compounds in the seaweed inhibit methyl-coenzyme M reductase in methanogenic archaea within the rumen.",
            "<strong>Slide 18 — Zelp Wearable Smart Halter (UK):</strong> A wearable cattle mask fitted with miniature fans and catalytic oxidation filters. When cattle exhale and burp (95% of cattle methane comes from burps, not flatulence!), sensors detect CH4 and channel it through a micro-catalytic converter that oxidizes methane into water vapor and trace CO2: CH4 + 2O2 → CO2 + 2H2O.",
            "<strong>Slide 19 — Alternative Insect Proteins:</strong> Breeding insects like crickets and grasshoppers for protein burgers and livestock feed delivers complete amino acids while consuming 90% less arable land, drastically reducing irrigation water, and generating zero enteric methane emissions."
        ],
        "mental_model": "A cow is essentially an enormous four-legged fermentation vat powered by bacteria that burp flammable methane. Red seaweed acts like a microbiological off-switch for those specific burp-producing microbes.",
        "checkpoint": {
            "question": "By what biochemical mechanism does the tropical red seaweed Asparagopsis taxiformis reduce enteric methane emissions in cattle by up to 80%?",
            "options": [
                "It absorbs all digestive acids so cows cease digestion entirely",
                "Bioactive bromoform compounds in the seaweed inhibit methanogenesis enzymes in rumen archaea",
                "It causes cows to exhale pure liquid oxygen",
                "It replaces stomach bacteria with photosynthetic algae"
            ],
            "correct": 1,
            "explanation": "Asparagopsis contains bromoform which binds to and inhibits the enzyme methyl-coenzyme M reductase, blocking the final metabolic step by which archaea in the cow's rumen produce methane gas."
        }
    },
    {
        "card_num": 9,
        "title": "Climate Repair & Geoengineering: Marine Cloud Brightening & Flettner Ships",
        "act": "ACT IV: PLANETARY REPAIR & MULTI-SECTOR INFRASTRUCTURE",
        "slides_covered": [20],
        "slides_label": "Slide 20 (Standalone Focus)",
        "exam_rating": {
            "tier": "MEDIUM-HIGH (⭐⭐⭐)",
            "stars": 3,
            "badge_class": "badge-medium",
            "frequency_count": "2 appearances in past exams",
            "recent_papers": ["Mid-1 2024 (Q3)", "End Exam 2022 (Q4b)"],
            "exam_tip": "Learn the 3-question governance dilemma: (1) Science: Can we do it? (2) Ethics: Should we do it? (3) Policy: How would we do it? Cite Stephen Salter's unmanned Flettner rotor ships and NASA satellite ship tracks as evidence."
        },
        "eli15_takeaway": "If polar ice melts too fast, solar radiation management proposes refreezing the poles using autonomous wind-powered ships that spray salty ocean mist into clouds, making them whiter and more reflective like giant planetary mirrors.",
        "key_facts": [
            "<strong>Slide 20 — Polar Refreezing Concept:</strong> Marine Cloud Brightening (MCB) and ocean greening have been proposed as emergency solar radiation management (SRM) tactics to cool polar ice sheets and halt runaway ice-albedo feedback loops.",
            "<strong>Slide 20 — Unmanned Flettner Rotor Vessels:</strong> Conceptual design by Stephen Salter and John MacNeill: autonomous, wind-powered, remotely controlled ships fitted with tall spinning Flettner rotors that harness the Magnus effect to sail across oceans while generating electrical power.",
            "<strong>Slide 20 — Four-Step Mist Dispersion Process:</strong> Seawater is pumped up, micro-filtered, pressurized, and sprayed through thousands of nanoscale nozzles into the marine boundary layer, creating a plume of microscopic sea-salt aerosol droplets.",
            "<strong>Slide 20 — Twomey Effect & Satellite Proof:</strong> Salt crystals act as cloud condensation nuclei (CCN). Distributing more nuclei produces smaller, more numerous water droplets, drastically increasing cloud albedo (reflectivity) to bounce solar radiation back to space. NASA satellite imagery provides direct empirical proof, capturing bright, persistent cloud trails left behind in ship tracks by commercial marine vessels.",
            "<strong>Slide 20 — Tripartite Governance Framework:</strong> Poses three fundamental questions: (1) <em>The Scientific Question:</em> Can we do it without triggering disastrous monsoonal disruptions? (2) <em>The Ethical Question:</em> Should humanity artificially manipulate the planetary climate thermostat? (3) <em>The Policy Question:</em> How would global nations govern, regulate, and avoid rogue deployment?"
        ],
        "mental_model": "Marine Cloud Brightening is like painting a dark asphalt roof white so it stops absorbing summer heat. Flettner ships spray sea salt into low clouds, turning dull grey skies into bright white mirrors that bounce sunlight away.",
        "checkpoint": {
            "question": "What observational phenomenon captured by NASA satellites provides direct empirical evidence that aerosol emissions can brighten marine clouds?",
            "options": [
                "Aurora borealis displays over northern Canada",
                "Bright reflective ship tracks created in marine stratocumulus clouds along cargo vessel shipping lanes",
                "Giant dust devils sweeping across the Sahara Desert",
                "Submarine volcanic eruptions boiling coastal surface waters"
            ],
            "correct": 1,
            "explanation": "NASA satellite images clearly reveal bright white line tracks in low clouds where sulfate and aerosol particles from ship smokestacks acted as cloud condensation nuclei, demonstrating the physical mechanism of Marine Cloud Brightening."
        }
    },
    {
        "card_num": 10,
        "title": "Clean Transport & Infrastructure: Hydrogen Ships, Tree Corridors, Electric Aviation & Floating Energy",
        "act": "ACT IV: PLANETARY REPAIR & MULTI-SECTOR INFRASTRUCTURE",
        "slides_covered": [23],
        "slides_label": "Slide 23 (Standalone Core Topic)",
        "exam_rating": {
            "tier": "CRITICAL (⭐⭐⭐⭐⭐)",
            "stars": 5,
            "badge_class": "badge-critical",
            "frequency_count": "3 appearances in past exams",
            "recent_papers": ["End Exam 2023 (Q3b)", "Mid-2 2018 (Q2)", "End Exam 2019 (Q4)"],
            "exam_tip": "High-yield multi-sector question. Memorize the exact data for all 5 sectors: (1) Hydrogen ships addressing 2.5% maritime CO2; (2) Medellín tree corridors (350,000 trees, 3°C cooling); (3) Electric aviation addressing 2% flight CO2; (4) Canada Bay of Fundy floating tidal platform; (5) South Korea 41 MW Hapcheon Dam floating solar."
        },
        "eli15_takeaway": "Deep decarbonization tackles the heavy infrastructure we rely on: zero-emission hydrogen cargo ships, electric airplanes, massive tree corridors that cool cities by 3°C, floating ocean tidal turbines, and solar panels floating on reservoirs that cool themselves while preserving land.",
        "key_facts": [
            "<strong>Slide 23 — Sector 1: Hydrogen Ships & Green Ammonia:</strong> Maritime cargo shipping generates <strong>2.5% of total global CO2 emissions</strong> burning heavy fuel oil. Transitioning to green hydrogen fuel cells and liquid ammonia propulsion eliminates sulfur oxides and carbon emissions across oceanic freight routes.",
            "<strong>Slide 23 — Sector 2: Urban Green Corridors (Medellín, Colombia):</strong> To combat severe urban heat island effects, Medellín planted more than <strong>350,000 trees and millions of plants across 30 interconnected green corridors</strong>, successfully lowering citywide ambient microclimate temperatures by up to <strong>3°C (3.5°F)</strong>.",
            "<strong>Slide 23 — Sector 3: Electric Aircraft & Sustainable Aviation:</strong> Commercial aviation generates <strong>2% of the world's carbon emissions</strong> at high cruising altitudes. Battery-electric propulsion is emerging for regional and commuter routes under 500 km, complemented by sustainable aviation fuels (SAF) for long-haul routes.",
            "<strong>Slide 23 — Sector 4: Floating Tidal Energy Platforms (Canada):</strong> Canada deployed the world's first floating tidal-energy platform in the Bay of Fundy (which possesses the world's highest tidal range of up to 16 meters), harnessing predictable, dense hydrodynamic currents to generate baseload renewable electricity.",
            "<strong>Slide 23 — Sector 5: Floating Solar Photovoltaics / FPV (South Korea):</strong> South Korea installed a massive <strong>41 MW floating solar power plant</strong> on the Hapcheon Dam reservoir. Floating panels eliminate terrestrial land acquisition costs, suppress toxic algal blooms, curb water evaporation, and benefit from natural water cooling that boosts solar photovoltaic efficiency by <strong>5% to 10%</strong>."
        ],
        "mental_model": "Rather than clearing forests to install solar panels or burning bunker fuel to move cargo, multi-sector infrastructure puts solar panels on dam reservoirs to keep water cool, and plants green tree highways right through concrete city canyons.",
        "checkpoint": {
            "question": "What dual environmental and physical benefits are achieved by South Korea's 41 MW floating solar installation on the Hapcheon Dam?",
            "options": [
                "It freezes the reservoir water completely to facilitate ice skating all year round",
                "It conserves agricultural land, suppresses water evaporation, and natural water cooling increases solar panel conversion efficiency by 5–10%",
                "It produces natural petroleum through high-voltage underwater electrolysis",
                "It converts incoming solar radiation into pressurized natural gas"
            ],
            "correct": 1,
            "explanation": "Floating solar (FPV) avoids land-use conflicts, prevents evaporation from reservoirs, and leverages the cooling effect of the water body to reduce thermal degradation and boost solar panel output by 5–10%."
        }
    },
    {
        "card_num": 11,
        "title": "Digital Earth: Remote Work, Cloud Efficiency & The 'Battle of Technologies' AI Surveillance",
        "act": "ACT V: DIGITAL SYSTEMS & CONTROLLED ENVIRONMENT AGRICULTURE",
        "slides_covered": [21, 22, 24],
        "slides_label": "Slides 21, 22, 24",
        "exam_rating": {
            "tier": "CRITICAL (⭐⭐⭐⭐⭐)",
            "stars": 5,
            "badge_class": "badge-critical",
            "frequency_count": "4 appearances in past exams",
            "recent_papers": ["End Exam 2023 (Q5b, 3M)", "End Exam 2022 (Q4, 3M)", "End Exam 2019 (Q3)", "Quiz-1 2023 (Q2)"],
            "exam_tip": "High exam probability. Wild Me and Global Forest Watch frequently appear as short notes or 2–3 mark questions. Be ready to explain how computer vision identifies animal coat patterns (like fingerprints) and how satellite RS-GPS halts illegal fishing."
        },
        "eli15_takeaway": "Technology can fight environmental crime: satellites track illegal logging in real time, drones detect poachers in African savannahs using thermal cameras, blockchain prevents illegal tuna from entering markets, and AI identifies individual endangered animals by scanning their natural stripes and spots.",
        "key_facts": [
            "<strong>Slide 21 — Remote Working & Commute Decarbonization:</strong> Telecommuting directly curtails urban transport emissions, decreases peak-hour road congestion, and enables commercial office facilities to consolidate lighting and HVAC loads.",
            "<strong>Slide 22 — Hyperscale Datacenter Efficiency:</strong> Migrating computational workloads from inefficient distributed corporate servers to centralized, energy-efficient hyperscale datacenters optimizes Power Usage Effectiveness (PUE) through liquid immersion cooling and 24/7 dedicated clean power contracts.",
            "<strong>Slide 24 — Blockchain & Commodity Supply Chains:</strong> Blockchain ledgers integrated with Remote Sensing (RS) and GPS transponders track vessel positioning and seafood origins to eradicate illegal, unreported, and unregulated (IUU) tuna fishing and stop agricultural commodity fraud.",
            "<strong>Slide 24 — Satellite Deforestation & Palm Oil Tracking:</strong> High-resolution optical and radar remote sensing satellites monitor rainforest canopies in real time, detecting illicit road carving and forest clearing for palm oil expansion across Southeast Asia and the Amazon basin.",
            "<strong>Slide 24 — Drones & WRI Global Forest Watch (GFW):</strong> Crowdsourced algorithms and autonomous drone surveillance networks detect illegal logging camps and timber transport before irreversible deforestation occurs.",
            "<strong>Slide 24 — Thermal Imaging Anti-Poaching:</strong> Night-vision thermal infrared cameras deployed in the savannahs of Kenya's National Parks detect armed poachers crossing border corridors from Tanzania under cover of darkness.",
            "<strong>Slide 24 — AI Wildlife Defense & Wild Me / DolphinGemma:</strong> Advanced computer vision models scan wildlife photographs to identify individual animals based on natural biometric markings (whisker spots in lions, stripe patterns in Chinese wild tigers, dorsal fins in dolphins), functioning like an automated biometric passport for global conservation without needing invasive physical tagging."
        ],
        "mental_model": "Wild Me is like facial recognition at airport passport control, but instead of human faces, the AI recognizes the unique geometric spot pattern on a whale shark's skin or the stripes on an endangered tiger.",
        "checkpoint": {
            "question": "How does the 'Wild Me' AI platform assist conservation biologists in tracking endangered animal populations?",
            "options": [
                "By genetically cloning extinct animal species in underground labs",
                "By using computer vision algorithms to identify individual animals from photos based on their unique biometric coat and spot patterns without invasive tags",
                "By deploying robotic predator decoys to frighten away poachers",
                "By administering tranquilizer darts using remote-controlled satellites"
            ],
            "correct": 1,
            "explanation": "Wild Me uses computer vision and machine learning (such as Wildbook algorithms) to analyze photographic sightings and distinguish individual animals by their unique natural patterns, enabling non-invasive census monitoring."
        }
    },
    {
        "card_num": 12,
        "title": "Controlled Environment Agriculture (CEA): Vertical Farming Pillars & AeroFarms",
        "act": "ACT V: DIGITAL SYSTEMS & CONTROLLED ENVIRONMENT AGRICULTURE",
        "slides_covered": [25, 26, 27],
        "slides_label": "Slides 25, 26, 27",
        "exam_rating": {
            "tier": "HIGH (⭐⭐⭐⭐)",
            "stars": 4,
            "badge_class": "badge-high",
            "frequency_count": "3 appearances in past exams",
            "recent_papers": ["End Exam 2023 (Q5a)", "Mid-1 2024 (Q5)", "Quiz-4 2020 (Q3)"],
            "exam_tip": "Be prepared to list the Four Essential Aspects of Vertical Farming: (1) Tower-like physical structure; (2) LED spectrum lighting; (3) Soilless medium (aeroponics/hydroponics); (4) 95% water reduction. Cite AeroFarms' cloth fleece and LED wavelength optimization."
        },
        "eli15_takeaway": "Vertical farming grows fresh food indoors inside stacked modular towers without sunlight or soil. Crops have their roots misted with nutrient water under specialized pink LED lights, producing 390 times more food per square foot while using 95% less water.",
        "key_facts": [
            "<strong>Slide 25 — Definition & Objectives of CEA:</strong> Vertical and greenhouse farming leverages environmentally controlled agriculture to maximize crop yields in confined, urban, or non-arable locations by artificially regulating temperature, humidity, airflow, and CO2 enrichment indoors.",
            "<strong>Slide 26 — Pillar 1 (Physical Arrangement):</strong> Crops are cultivated in vertical, multi-tiered modular racking towers that multiply production output per square meter of building footprint.",
            "<strong>Slide 26 — Pillar 2 (Lighting Optimization):</strong> Delivers precise photosynthetic active radiation (PAR) using customized solid-state LED fixtures tuned to specific chlorophyll-absorption wavelengths (predominantly red and blue spectrums) alongside natural daylight harvesting.",
            "<strong>Slide 26 — Pillar 3 (Growth Medium):</strong> Replaces natural topsoil with soilless systems: <em>Hydroponics</em> (roots submerged in aerated nutrient solution), <em>Aeroponics</em> (roots suspended in air and misted periodically), or <em>Aquaponics</em> (closed-loop symbiotic fish and plant culture), supported by inert media like sphagnum moss or coconut coir.",
            "<strong>Slide 26 & 27 — Pillar 4 (95% Water Conservation):</strong> Recirculating irrigation loops capture plant transpiration via dehumidifiers, slashing water consumption by up to <strong>95%</strong> compared to open-field agriculture while eliminating synthetic agricultural runoff.",
            "<strong>Slide 27 — Crops Best Suited:</strong> Leafy greens (lettuce, kale, spinach), culinary herbs (basil, mint), vine vegetables (tomatoes, bell peppers), broccoli, and succulents.",
            "<strong>Slide 27 — Industrial Case Study (AeroFarms, USA):</strong> Commercial pioneer using patented aeroponic misting technology. Seeds are sown on reusable cloth fleece fabric woven from recycled plastic beverage bottles; plants receive optimized LED spectra without pesticides, cutting water use by 95% across high-density facilities globally (USA, Japan, China, Singapore, South Korea, Germany, UK, Netherlands)."
        ],
        "mental_model": "Traditional farming is a two-dimensional carpet spread across millions of acres, praying for rain and sunlight. Vertical farming is a 3D skyscraper where every drop of water is recycled and every leaf receives the exact photon it needs.",
        "checkpoint": {
            "question": "What is the primary technological difference between traditional open-field farming and AeroFarms' patented aeroponic vertical farming system?",
            "options": [
                "AeroFarms grows crops entirely underwater inside deep ocean trenches",
                "AeroFarms suspends plant roots in air, misting them with nutrient water, using reusable recycled-bottle cloth, custom LED wavelengths, and cutting water use by 95%",
                "AeroFarms burns fossil fuels indoors to elevate soil temperature above 100°C",
                "AeroFarms genetic engineering makes plants grow without needing water or light"
            ],
            "correct": 1,
            "explanation": "AeroFarms utilizes indoor aeroponics where roots are suspended and sprayed with nutrient mist, supported on reusable fleece made from recycled plastic bottles under tuned LED wavelengths, reducing water consumption by 95%."
        }
    },
    {
        "card_num": 13,
        "title": "Agroecological Adaptation & Carbon Moonshots: Trap Cropping & XPRIZE",
        "act": "ACT V: DIGITAL SYSTEMS & CONTROLLED ENVIRONMENT AGRICULTURE",
        "slides_covered": [28, 29],
        "slides_label": "Slides 28, 29",
        "exam_rating": {
            "tier": "HIGH (⭐⭐⭐⭐)",
            "stars": 4,
            "badge_class": "badge-high",
            "frequency_count": "2 appearances in past exams",
            "recent_papers": ["Mid-1 2024 (Q1)", "End Exam 2022 (Q2)"],
            "exam_tip": "Master the biological pairs for trap cropping: Marigolds against root-knot nematodes and whiteflies; Italy (Brassicaceae + sugar beets vs flea beetles); China (Maize + cotton vs whiteflies). Note the $100M XPRIZE milestone for gigatonne carbon removal."
        },
        "eli15_takeaway": "Instead of spraying toxic poisons on food, trap cropping plants natural pest magnets around fields — like bright marigolds whose roots kill parasitic worms and flowers repel flies. Meanwhile, global moonshot prizes like the $100M XPRIZE fund technologies to pull gigatons of carbon from the air.",
        "key_facts": [
            "<strong>Slide 28 — Climate Trigger for Pest Proliferation:</strong> Global climate warming and rising humidity accelerate insect metabolic rates, shorten generation intervals, and expand pest geographical ranges into previously temperate croplands.",
            "<strong>Slide 28 — Trap Cropping Working Principle:</strong> Establishing perimeter borders or intercropped rows of sacrificial companion plants that are significantly more attractive to insect pests than the primary cash crop, preventing pest infestation without synthetic chemical insecticides.",
            "<strong>Slide 28 — Marigolds (Tagetes) Chemical Warfare:</strong> Marigold root systems exude natural alpha-terthienyl nematicides that kill root-knot nematodes upon penetration, while their blossoms emit volatile organic compounds that confuse and deter aphids and whiteflies.",
            "<strong>Slide 28 — Global Real-World Examples:</strong> (1) <em>Italy:</em> Planting <em>Brassicaceae</em> buffer strips around sugar beet fields to intercept flea beetles; (2) <em>China:</em> Interplanting maize border strips alongside cotton fields to attract and trap whiteflies and cotton bollworms.",
            "<strong>Slide 28 — Intensive System Optimization:</strong> Successful trap cropping requires rigorous ecological knowledge: decoding pest sensory behavior, matching plant flowering phenologies, and optimizing spatial border-to-crop ratios.",
            "<strong>Slide 29 — XPRIZE Carbon Removal ($100 Million):</strong> Launched by the Musk Foundation and XPRIZE, this competition represents the largest incentive prize in human history. It challenges innovators worldwide to demonstrate operational CDR technologies sequestering 1,000 net tonnes of CO2/year and prove a credible engineering pathway to gigatonne-scale carbon removal by 2050."
        ],
        "mental_model": "Trap cropping is like setting out a plate of sweet glazed doughnuts at the front door so unwanted guests fill their bellies on junk food and never make it into your dining room.",
        "checkpoint": {
            "question": "How do marigolds (Tagetes) act as a biological trap crop to protect primary agricultural crops?",
            "options": [
                "Their leaves release toxic chlorine gas during photosynthesis",
                "Their roots exude natural nematicidal chemicals that suppress root-knot nematodes while flower volatiles repel aphids and whiteflies",
                "They attract wild birds that consume all plant leaves in the field",
                "Their roots absorb 100% of soil moisture to dehydrate surrounding insects"
            ],
            "correct": 1,
            "explanation": "Marigolds produce alpha-terthienyl compounds in their root exudates that kill root-knot nematodes, while their floral scents emit natural insect deterrents that confuse foliar pests like aphids and whiteflies."
        }
    },
    {
        "card_num": 14,
        "title": "High-Yield Exam Spotlight: Novacem Eco-Cements vs Traditional Portland Chemistry",
        "act": "ACT VI: HIGH-YIELD EXAM QUESTION MASTERCLASS",
        "slides_covered": ["Exam Past Papers (2018, 2019, 2023)"],
        "slides_label": "Exam Question Bank Spotlight (Pillar IV)",
        "exam_rating": {
            "tier": "CRITICAL (⭐⭐⭐⭐⭐)",
            "stars": 5,
            "badge_class": "badge-critical",
            "frequency_count": "3 appearances in past exams (Must-Know Chemistry)",
            "recent_papers": ["End Exam 2023 (Q3, 3M)", "End Exam 2019 (Q2, 3M)", "Mid-2 2018 (Q1b, 1.5M)"],
            "exam_tip": "One of the most frequently asked chemical contrast questions in EST! You must write out the chemical equations: Portland cement calcination (CaCO3 → CaO + CO2 at 1450°C) versus Novacem magnesium silicate carbonation (MgO + CO2 + H2O → MgCO3) at 650°C."
        },
        "eli15_takeaway": "Traditional Portland cement is one of Earth's biggest polluters because it bakes limestone at 1,450°C, releasing tons of CO2. Novacem replaces limestone with magnesium silicates baked at just 650°C, and as it hardens, it actually drinks CO2 from the air, making it carbon-negative!",
        "key_facts": [
            "<strong>Exam Provenance & Recurrence:</strong> Asked as a 3-mark conceptual question in Endsem 2023, Endsem 2019, and Midsem-2 2018: <em>'Explain how Novacem cement differs chemically from Ordinary Portland Cement and why it is considered carbon-negative.'</em>",
            "<strong>Traditional Ordinary Portland Cement (OPC) Problem:</strong> Produces ~8% of global CO2 emissions. Manufacturing OPC requires calcining limestone (CaCO3) in high-temperature rotary kilns at <strong>1,450°C</strong>: CaCO3 → CaO + CO2. Producing 1 tonne of OPC releases approximately <strong>0.8 to 1.0 tonne of CO2</strong> (50% from limestone chemical breakdown, 50% from fossil fuel combustion to reach 1,450°C).",
            "<strong>Novacem Raw Materials & Low Temperature:</strong> Novacem uses abundant <strong>magnesium silicates (MgSiO3)</strong> instead of limestone (calcium carbonate). It manufactures magnesium oxide (MgO) at a vastly lower kiln temperature of <strong>650°C</strong>, slashing fuel combustion emissions by over 50%.",
            "<strong>Carbon-Negative Hardening (Carbonation):</strong> While traditional cement cures through hydration, Novacem mortar cures by actively absorbing atmospheric carbon dioxide to form hydrated magnesium carbonates: MgO + CO2 + H2O → MgCO3·3H2O (nesquehonite).",
            "<strong>Net Carbon Balance:</strong> For every tonne of Novacem cement manufactured, the process can absorb up to <strong>100 kg more CO2 than it emits</strong>, achieving true cradle-to-gate carbon-negative concrete."
        ],
        "mental_model": "Making traditional Portland cement is like burning a log to make ashes — you dump carbon into the air. Making Novacem is like building a coral reef in a mold — the cement cures by drinking carbon out of the atmosphere and locking it into rock.",
        "checkpoint": {
            "question": "What is the primary chemical difference that makes Novacem cement carbon-negative compared to Ordinary Portland Cement (OPC)?",
            "options": [
                "Novacem mixes powdered uranium into standard concrete to generate internal heat",
                "Novacem uses magnesium silicates processed at 650°C instead of limestone at 1,450°C, and hardens by absorbing atmospheric CO2 into magnesium carbonate",
                "Novacem is made by dissolving plastic waste in concentrated hydrochloric acid",
                "Novacem cures exclusively by evaporating liquid nitrogen"
            ],
            "correct": 1,
            "explanation": "Novacem replaces limestone with magnesium silicates calcined at a much lower temperature (650°C vs 1,450°C) and cures via carbonation (MgO + CO2 → MgCO3), absorbing more atmospheric CO2 during hardening than is emitted during manufacturing."
        }
    }
]

print(f"Total cards: {len(cards)}")
# verify slide coverage
covered = set()
for c in cards:
    for s in c["slides_covered"]:
        if isinstance(s, int):
            covered.add(s)

print(f"Covered slide integers: {sorted(list(covered))}")
missing = set(range(1, 30)) - covered
print(f"Missing slides from 1 to 29: {missing}")

# Save to Study_Material/class_11_cards.json
with open("Study_Material/class_11_cards.json", "w", encoding="utf-8") as f:
    json.dump(cards, f, indent=2)

print("Saved Study_Material/class_11_cards.json successfully.")
