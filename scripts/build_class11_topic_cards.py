import json
import os

class11_cards = [
    {
        "card_num": 1,
        "title": "Negative Emissions Framework & Nature-Based Carbon Sinks",
        "act": "Act 1: Carbon Drawdown & Natural Sinks",
        "slides_covered": [1, 2, 3, 5],
        "slides_label": "Slides 1, 2, 3, 5",
        "exam_rating": {
            "tier": "HIGH (⭐⭐⭐⭐)",
            "stars": 4,
            "badge_class": "badge-high",
            "frequency_count": "3 appearances in previous papers",
            "recent_papers": ["Mid-1 2022 (Q3)", "Quiz-3 2020 (Q1b)", "End Exam 2019 (Sec II)"],
            "exam_tip": "Exams test the fundamental distinction: emission cuts alone cannot achieve net-zero because residual hard-to-abate sectors remain. Negative Emission Technologies (NETs) are mandatory to remove atmospheric carbon."
        },
        "eli15_takeaway": "Stopping new pollution isn't enough because the bath is already overflowing. We must pull existing carbon out of the air. Nature does this using fast biological cycles (trees) and permanent geological locks (biochar baked without oxygen and timber skyscrapers).",
        "key_facts": [
            "The Net-Zero Mathematical Deficit: Residual emissions from aviation, steel, and agriculture mean reaching 1.5°C requires removing 5–10 gigatonnes of atmospheric CO2 annually by 2050.",
            "Negative Emission Technologies (NETs): Defined as physical or biological interventions that result in net removal of greenhouse gases from the atmosphere, not merely avoidance.",
            "Biochar Pyrolysis: Biomass heated to 400–700°C in an oxygen-depleted reactor (pyrolysis). Replaces fast natural rotting (which returns CO2 in 1–5 years) with recalcitrant polycyclic aromatic carbon that stays stable in soils for over 1,000 years while improving water retention and cation exchange capacity.",
            "Structural Timber (Mass Timber / Cross-Laminated Timber - CLT): Harvested timber locks ~1 tonne of CO2 per cubic metre into load-bearing skyscraper columns, preventing the 0.9 kg CO2/kg emissions from manufacturing conventional steel and Portland cement."
        ],
        "mental_model": "A sponge and a vault. Planting a standard tree is a wet sponge that leaks carbon back when it rots or burns. Biochar and mass timber turn that sponge into an iron safe, locking the carbon away for centuries.",
        "checkpoint": {
            "question": "Why is biochar biologically and chemically distinct from natural forest compost in carbon sequestration?",
            "options": [
                "Compost stores double the carbon per hectare compared to biochar",
                "Compost rapidly decomposes back to CO2 within years, while biochar's aromatic rings resist microbial decay for over 1,000 years",
                "Biochar requires high oxygen availability during creation to maximize mass",
                "Compost completely eliminates soil nitrogen volatilization"
            ],
            "correct_index": 1,
            "explanation": "Natural compost decays through microbial oxidation within 1–5 years. Biochar created via oxygen-starved pyrolysis forms recalcitrant aromatic carbon structures that microbes cannot break down, locking carbon for millennia."
        }
    },
    {
        "card_num": 2,
        "title": "Blue Carbon: Coastal Ocean Super-Sinks (Mangroves & Salt Marshes)",
        "act": "Act 1: Carbon Drawdown & Natural Sinks",
        "slides_covered": [4],
        "slides_label": "Slide 4 (Standalone)",
        "exam_rating": {
            "tier": "CRITICAL / MUST-KNOW (⭐⭐⭐⭐⭐)",
            "stars": 5,
            "badge_class": "badge-critical",
            "frequency_count": "Tested in 4 End-Semester Exams (2018, 2019, 2022, 2023)",
            "recent_papers": ["End Exam 2023 (Sec I, Q1g - 1M)", "End Exam 2022 (Sec V, Qe - 2M)", "End Exam 2019 (Sec X, Q1c - 3M)", "End Exam 2018 (Part IV, Q3 - 4M)"],
            "exam_tip": "Memorize the 3-point answer key from 2022/2023: (1) Stores 3-5x more carbon per hectare than upland tropical forests in waterlogged anoxic sediment; (2) Critical nursery grounds for commercial marine fisheries; (3) Frontline storm-surge and wave-energy buffers protecting coastal populations."
        },
        "eli15_takeaway": "Coastal ecosystems (mangroves, tidal salt marshes, and seagrasses) are the ocean's super-sponges. They trap organic mud in water without oxygen, stopping decay and locking away carbon up to 10 times faster than tropical land jungles.",
        "key_facts": [
            "Official Definition: 'Blue Carbon' is the carbon captured and stored by coastal and marine ecosystems—principally mangroves, tidal salt marshes, and seagrass meadows.",
            "Sequestration Velocity: Coastal wetlands sequester carbon at rates up to 10 times higher per hectare than mature terrestrial tropical rainforests.",
            "The Sediment Anoxia Advantage: Unlike terrestrial forest soils where microbial aerobic respiration converts leaf litter to CO2, tidal marine soils are permanently waterlogged and oxygen-depleted (anoxic), preserving sediment carbon for thousands of years.",
            "Triple Ecological Dividend: High carbon density per hectare (3–5x upland forests), severe coastal erosion/cyclone attenuation (reducing wave energy by up to 66%), and vital breeding nurseries for 75% of commercial fish and crustacean species."
        ],
        "mental_model": "Deep-freeze pantry versus a warm kitchen counter. Terrestrial soil is a warm room where food rots quickly. Anoxic mangrove mud is a deep freeze where organic carbon cannot decay because there is no oxygen for the bacteria to breathe.",
        "checkpoint": {
            "question": "What is the primary geochemical mechanism allowing mangrove sediments to store 3–5 times more carbon per hectare than terrestrial forests?",
            "options": [
                "Mangrove leaves contain zero lignin and decompose instantly into inorganic minerals",
                "Permanently waterlogged, anoxic conditions prevent microbial aerobic respiration, locking organic carbon in deep sediments without decay",
                "Saltwater instantly transforms atmospheric CO2 into solid diamond crystals",
                "Mangrove root systems absorb gaseous methane and convert it to limestone"
            ],
            "correct_index": 1,
            "explanation": "In terrestrial forests, abundant oxygen allows soil microbes to rapidly decompose organic matter into CO2. In mangrove swamps, tidal water saturation creates anoxic sediments where aerobic decomposition cannot occur, preserving organic carbon for millennia."
        }
    },
    {
        "card_num": 3,
        "title": "Earth-Scale Chemistry & Enhanced Rock Weathering",
        "act": "Act 2: Earth-Scale Chemical Interventions",
        "slides_covered": [6, 7],
        "slides_label": "Slides 6, 7",
        "exam_rating": {
            "tier": "MEDIUM-HIGH (⭐⭐⭐)",
            "stars": 3,
            "badge_class": "badge-medium",
            "frequency_count": "Tested in chemical sequestration & geoengineering contexts",
            "recent_papers": ["Mid-1 2024 (Sec I)", "End Exam 2022 (Sec III)"],
            "exam_tip": "Focus on the silicate weathering formula ($CaSiO_3 + 2CO_2 + H_2O \\rightarrow Ca^{2+} + 2HCO_3^- + SiO_2$). Exams love contrasting natural 100,000-year geological weathering with human pulverization of basalt to compress reactions into years."
        },
        "eli15_takeaway": "Nature uses rain and volcanic rock to vacuum CO2 out of the air over hundreds of thousands of years. Enhanced rock weathering speeds this up by grinding volcanic basalt rock into powder and spreading it on farm fields, turning CO2 into harmless dissolved ocean minerals while fertilizing soil.",
        "key_facts": [
            "Natural Silicate-Carbonate Geochemical Cycle: Over geological epochs, silicate rock weathering regulates Earth's climate thermostat via the reaction: $CaSiO_3 + 2CO_2 + H_2O \\rightarrow Ca^{2+} + 2HCO_3^- + SiO_2$.",
            "The Surface Area Bottleneck: Natural weathering is extremely slow (100,000+ years) because mountain rocks have very little exposed surface area relative to their immense volume.",
            "Enhanced Weathering Acceleration: Crushing volcanic basalt or olivine into micro-scale particles (<100 micrometres) increases surface area millions of times, speeding up dissolution from millennia into 1–5 years.",
            "Agricultural Co-Benefits: Spreading crushed basalt across croplands releases essential mineral micronutrients (calcium, magnesium, iron, silica), sweetens acidic agricultural soils without fossil-fuel limestone, and runs bicarbonate runoff into the oceans to counteract coastal acidification."
        ],
        "mental_model": "A whole sugar cube versus powdered sugar in hot tea. A big rock takes hundreds of years to weather away. Grind it into dust, and it dissolves almost instantly in rainfall, capturing CO2 with every drop.",
        "checkpoint": {
            "question": "What is the net chemical product when crushed basalt rock weathers with carbonic acid in rainwater?",
            "options": [
                "Toxic sulfur gas and hydrochloric acid",
                "Stable dissolved bicarbonate ions (HCO3-) and bioavailable mineral cations (Ca2+, Mg2+)",
                "Pure elemental methane gas that escapes to the stratosphere",
                "Insoluble chlorofluorocarbon compounds"
            ],
            "correct_index": 1,
            "explanation": "Enhanced rock weathering converts atmospheric CO2 dissolved in rainwater into dissolved bicarbonate ions (HCO3-) and nutrient cations (Ca2+, Mg2+), permanently locking the carbon in ocean alkalinity."
        }
    },
    {
        "card_num": 4,
        "title": "Direct Air Capture (DAC) Architecture, Physics & Sorbents",
        "act": "Act 3: Artificial Trees & The Carbon Economy",
        "slides_covered": [8, 10, 12, 13],
        "slides_label": "Slides 8, 10, 12, 13",
        "exam_rating": {
            "tier": "HIGH (⭐⭐⭐⭐)",
            "stars": 4,
            "badge_class": "badge-high",
            "frequency_count": "Tested in technological capture & contactor mechanics",
            "recent_papers": ["End Exam 2022 (Sec VI, Qc)", "End Exam 2019 (Sec II)"],
            "exam_tip": "Exams test the physical challenge: ambient air has only 420 ppm CO2 (1 molecule in 2,500), requiring immense fan power. Distinguish between Solid Sorbent (Climeworks, low temp 100°C) and Liquid Solvent (Carbon Engineering, high temp 900°C calciner)."
        },
        "eli15_takeaway": "Direct Air Capture (DAC) machines are giant vacuum cleaners with chemical filters. Because carbon dioxide is invisible and rare in air (just 1 part in 2,500), giant fans must blow millions of tonnes of breeze across special sponge filters to grab it.",
        "key_facts": [
            "The Atmospheric Thermodynamic Penalty: Flue gas from a coal plant has ~15% CO2 (150,000 ppm), but ambient open air has only ~0.042% (420 ppm). Capturing diffuse atmospheric CO2 requires approximately 3–4 times more thermodynamic work per tonne.",
            "Solid Sorbent Technology (Low-Temperature DAC): Uses porous cellulose or silica matrices chemically bonded with amine functional groups. Traps CO2 at ambient room temperatures, then releases pure CO2 when heated to 100°C with low-grade geothermal or waste heat (e.g. Climeworks).",
            "Liquid Solvent Technology (High-Temperature DAC): Passes air through a liquid Potassium Hydroxide (KOH) chemical bath forming Potassium Carbonate ($K_2CO_3$), followed by a Calcium Loop with a gas-fired calciner operating at 900°C (e.g. Carbon Engineering).",
            "Scuba-Diving Breakthrough (BIGs): Bis-Iminoguanidines use guanidine crystals inspired by scuba rebreather chemistry to precipitate solid carbonate crystals directly from air, desorbing pure gas at just 60°C using simple solar heat."
        ],
        "mental_model": "Finding a red marble in a bucket of 2,500 white marbles. You need a powerful magnetic glove that ignores white marbles completely and only catches the red ones as millions roll past.",
        "checkpoint": {
            "question": "Why does Direct Air Capture require significantly more energy per tonne of CO2 captured compared to point-source smoke-stack capture?",
            "options": [
                "Ambient air contains zero oxygen, which shuts down chemical filters",
                "Ambient CO2 concentration is extremely dilute (~420 ppm vs ~150,000 ppm in flue gas), requiring massive air volumes and higher thermodynamic separation energy",
                "Point-source smoke-stacks use only gravity to capture carbon",
                "Solid amine filters can only operate under liquid nitrogen temperatures"
            ],
            "correct_index": 1,
            "explanation": "Thermodynamics dictates that separation energy scales with dilution. Flue gas is ~150,000 ppm CO2, whereas ambient air is ~420 ppm (350 times more dilute), requiring massive fan power to process thousands of cubic metres of air per kilogram captured."
        }
    },
    {
        "card_num": 5,
        "title": "Industrial DAC Commercial Pioneers & Deep Geological Storage",
        "act": "Act 3: Artificial Trees & The Carbon Economy",
        "slides_covered": [11, 14, 16],
        "slides_label": "Slides 11, 14, 16",
        "exam_rating": {
            "tier": "HIGH (⭐⭐⭐⭐)",
            "stars": 4,
            "badge_class": "badge-high",
            "frequency_count": "Tested in 2019 and 2022 Endsems",
            "recent_papers": ["End Exam 2022 (Sec VI, Qc - 1M)", "End Exam 2019 (Sec II, Q6 - 2M)"],
            "exam_tip": "Be ready to name the big commercial players: Climeworks (Orca & Mammoth plants in Hellisheiði, Iceland) and Carbon Engineering (Permian Basin). Know the CarbFix process: dissolving CO2 in water and pumping into basalt rock turns it into solid stone in under 2 years."
        },
        "eli15_takeaway": "Commercial DAC facilities are already running. In Iceland, Climeworks captures CO2, fizzes it into water like seltzer, and pumps it a kilometre down into volcanic basalt rock. In 2 years, the bubbly water turns into solid stone forever.",
        "key_facts": [
            "Commercial Flagships: Climeworks 'Orca' (4,000 tCO2/yr) and 'Mammoth' (36,000 tCO2/yr) in Iceland run on 100% renewable zero-emission geothermal electricity and heat.",
            "The CarbFix Basalt Mineralization Mechanism: CO2 gas is dissolved in immense volumes of water (27 tonnes of water per tonne of CO2) under high pressure and injected 800–1,000m into porous basalt bedrock. Reactive divalent cations ($Ca^{2+}, Mg^{2+}, Fe^{2+}$) precipitate stable solid carbonate minerals ($CaCO_3, MgCO_3$) within 24 months, with 0% risk of gas leakage.",
            "Deep Saline Aquifer Storage: Offshore sub-seabed storage (such as the UK's Project Net Zero Teesside in the Endurance Aquifer) pumps supercritical CO2 1,500m below the North Sea into permeable sandstone sealed beneath impermeable thick mudstone caprock.",
            "Energy & Cost Metric: Early commercial DAC cost ~$600–$1,000 per tonne of CO2. Reaching climate impact demands scaling to gigatonnes and bringing costs down toward the $100–$150/tonne threshold."
        ],
        "mental_model": "Making soda and pouring it into stone. If you pump gas into a cave, it can leak out. If you dissolve it in water and pump it into volcanic rock, the rock drinks it and turns it into permanent solid rock.",
        "checkpoint": {
            "question": "How does the CarbFix mineralization method in Iceland eliminate the risk of subterranean CO2 gas leakage?",
            "options": [
                "It burns the CO2 into soot at the surface",
                "It dissolves CO2 in pressurized water and reacts it with basalt cations, turning the carbon into solid carbonate rock within two years",
                "It freezes the gas into permanent glaciers above ground",
                "It vents the gas into the stratosphere via tall chimneys"
            ],
            "correct_index": 1,
            "explanation": "CarbFix dissolves CO2 in water before injection into basalt. The acidic fluid releases calcium, magnesium, and iron from the rock, reacting to form solid carbonate minerals in under two years with zero risk of escape."
        }
    },
    {
        "card_num": 6,
        "title": "Air-to-Luxury: Aether Diamonds from Pollution",
        "act": "Act 3: Artificial Trees & The Carbon Economy",
        "slides_covered": [9, 15],
        "slides_label": "Slides 9, 15 (Standalone)",
        "exam_rating": {
            "tier": "CRITICAL / MUST-KNOW (⭐⭐⭐⭐⭐)",
            "stars": 5,
            "badge_class": "badge-critical",
            "frequency_count": "Tested in 2022 and 2023 End-Semester Exams as a 3-5M question",
            "recent_papers": ["End Exam 2023 (Sec III, Q5 - 3M: 'Explain the process of diamond manufacturing by Aether')", "End Exam 2022 (Sec X, Qb - 5M: 'Diamonds from air pollution')"],
            "exam_tip": "MUST MEMORIZE 5-STEP PROFESSOR ANSWER KEY: (1) Purchase DAC CO2 from Climeworks; (2) Convert CO2 + green H2 into high-purity methane (CH4); (3) Inject CH4 into Chemical Vapor Deposition (CVD) vacuum plasma reactor at extreme temperatures over weeks; (4) Ship rough diamonds to Surat, India for precision cutting/polishing; (5) Offset metrics: 20 tonnes CO2 removed per carat, 50% energy cut, 127 gallons water saved."
        },
        "eli15_takeaway": "Aether creates real, certified luxury diamonds out of thin air. They take captured carbon dioxide from Climeworks, turn it into methane gas, and bake it in a vacuum plasma oven for a month. Each 1-carat diamond removes 20 tonnes of carbon from the sky and cuts out the human and environmental destruction of earth mining.",
        "key_facts": [
            "Step 1 - Atmospheric Capture: Raw CO2 is sourced directly from atmospheric air capture facilities (Climeworks in Europe/Iceland), guaranteeing positive carbon provenance.",
            "Step 2 - Methane Synthesis: Captured CO2 is reacted with green hydrogen produced via solar/wind water electrolysis through the Sabatier methanation reaction ($CO_2 + 4H_2 \\rightarrow CH_4 + 2H_2O$) to produce ultra-pure feedstock methane.",
            "Step 3 - Chemical Vapor Deposition (CVD) Plasma Reactor: Methane gas is injected into near-vacuum CVD reactors, energized with high-frequency microwaves into high-temperature plasma. Carbon atoms break away and deposit layer-upon-layer onto diamond seed plates over 3–4 weeks.",
            "Step 4 - Indian Artisan Value Chain: Rough diamond crystal cubes are shipped to Surat, Gujarat, India—the global diamond capital—where master lapidaries laser-cut and polish them into fine jewelry.",
            "Step 5 - Verified Ecological Metrics: Certified B-Corp; each carat physically removes the equivalent of 20 tonnes of atmospheric carbon (offsetting an average human's annual footprint), consumes 50% less energy than mining, and avoids 127 gallons of water waste and toxic tailings per carat."
        ],
        "mental_model": "Cooking a crystal cake in a plasma microwave. Instead of digging a giant 500-metre crater in the African earth to find a shiny rock, you suck smoke out of the sky, turn it into gas, and grow an identical gem in an oven.",
        "checkpoint": {
            "question": "What is the sequence of physical and chemical operations used by Aether to manufacture diamonds from atmospheric carbon?",
            "options": [
                "Underground coal blasting -> steam heating -> hydraulic fracturing -> mechanical crushing",
                "Climeworks DAC CO2 capture -> Sabatier synthesis to pure CH4 -> Chemical Vapor Deposition (CVD) vacuum plasma reactor -> Surat cutting and polishing",
                "Ocean seawater evaporation -> salt crystallization -> solar sintering -> chemical dyeing",
                "Forest wood combustion -> soot collection -> high-pressure mechanical stamping"
            ],
            "correct_index": 1,
            "explanation": "Aether buys DAC CO2 from Climeworks, synthesizes it with green hydrogen into methane (CH4), feeds it into a high-temperature CVD vacuum plasma reactor to grow diamond crystal lattices over weeks, and ships the gems to Surat, India for cutting and polishing."
        }
    },
    {
        "card_num": 7,
        "title": "Eco-Cements & Green Concrete: Novacem vs Traditional Portland",
        "act": "Act 5: Industrial Cleantech & Carbon-Negative Construction",
        "slides_covered": [23],
        "slides_label": "Slide 23 (Standalone Exam Focus)",
        "exam_rating": {
            "tier": "CRITICAL / MUST-KNOW (⭐⭐⭐⭐⭐)",
            "stars": 5,
            "badge_class": "badge-critical",
            "frequency_count": "Tested in 2018 Mid-2, 2019 Endsem, and 2023 Endsem",
            "recent_papers": ["End Exam 2023 (Sec III, Q7 - 3M: 'Difference between Portland and Novacem cement')", "End Exam 2019 (Sec IV, Q1d - 3M: 'Novacem as ecofriendly cement')", "Mid-2 2018 (Q8b - 1.5M: 'Novacem: MgO + CO2 -> MgCO3')"],
            "exam_tip": "EXACT EXAM QUESTION: Differentiate between Portland and Novacem cement. Portland cement calcines limestone (CaCO3 -> CaO + CO2) at 1450°C emitting 0.9 kg CO2/kg cement. Novacem uses magnesium silicates calcined at 650°C and carbonates ambient CO2 during curing (MgO + CO2 -> MgCO3), becoming net carbon-negative (-100 kg CO2/tonne)."
        },
        "eli15_takeaway": "Normal concrete is one of the dirtiest things on Earth, causing 8% of all global emissions because making it requires roasting limestone at volcanic temperatures. Novacem is a green cement made from magnesium rocks at lower heat that actually drinks carbon dioxide out of the air as it hardens.",
        "key_facts": [
            "Traditional Portland Cement Chemical Burden: Relies on heating limestone ($CaCO_3$) to 1,450°C in giant kilns. Produces dual emissions: fossil fuel combustion heat + inevitable chemical calcination release ($CaCO_3 \\rightarrow CaO + CO_2$). Emits ~0.9 kg CO2 per 1 kg cement produced, generating 8% of total global CO2 emissions.",
            "Novacem Magnesium Silicate Innovation: Developed by Imperial College London. Eliminates limestone completely, substituting magnesium silicates ($Mg_3Si_2O_5(OH)_4$) processed at a significantly lower calcination temperature of only 650°C.",
            "Carbon-Negative Carbonation Reaction: When Novacem cement is mixed with water and cured in structures, atmospheric CO2 actively reacts with magnesium oxide to form hydrated magnesium carbonates: $MgO + CO_2 \\rightarrow MgCO_3$.",
            "Net Carbon Balance Comparison: Traditional Portland cement is net-positive (+800 to +900 kg CO2 emitted per tonne). Novacem is net-negative (absorbs up to 100 kg more CO2 per tonne than emitted over its entire production lifecycle)."
        ],
        "mental_model": "An oven that smokes versus bread that eats smoke. Portland cement is an industrial chimney that belches carbon as it cooks. Novacem is a chemical sponge that inhales carbon from the air as it sets into rock.",
        "checkpoint": {
            "question": "What is the chemical reaction responsible for making Novacem cement carbon-negative during curing?",
            "options": [
                "CaCO3 -> CaO + CO2 at 1450°C",
                "MgO + CO2 -> MgCO3 (ambient carbonation forming solid magnesium carbonates)",
                "2H2 + O2 -> 2H2O",
                "NaCl + H2O -> NaOH + HCl"
            ],
            "correct_index": 1,
            "explanation": "Novacem cures by reacting magnesium oxide with ambient atmospheric CO2: MgO + CO2 -> MgCO3. This carbonation reaction absorbs more CO2 from the air than was produced in low-temperature manufacturing, making it net carbon-negative."
        }
    },
    {
        "card_num": 8,
        "title": "Agricultural Decarbonization: Cattle Methane, Red Seaweed & Insects",
        "act": "Act 4: Fixing the Agricultural Engine",
        "slides_covered": [17, 18, 19],
        "slides_label": "Slides 17, 18, 19",
        "exam_rating": {
            "tier": "HIGH (⭐⭐⭐⭐)",
            "stars": 4,
            "badge_class": "badge-high",
            "frequency_count": "Tested in 2018 Mid-2 and 2022 Endsem",
            "recent_papers": ["End Exam 2022 (Sec III, Q15: 'Methane reduction from livestock can be achieved by adding Seaweed to cattle feed')", "Mid-2 2018 (Q1c: 'Major source of methane emissions')"],
            "exam_tip": "Remember Asparagopsis taxiformis (red seaweed) and bromoform chemical mechanism. 95% of cattle methane comes from burps (enteric fermentation), not flatulence. Zelp halters oxidize methane in real time."
        },
        "eli15_takeaway": "Cows produce immense amounts of methane—a greenhouse gas 28 times more potent than carbon dioxide—from bacteria fermenting grass in their stomachs. Adding a pinch of red ocean seaweed to their feed blocks the methane-making enzyme, cutting burps by up to 80%.",
        "key_facts": [
            "The Enteric Fermentation Problem: Agriculture produces ~24% of global greenhouse emissions. A single beef cow belches ~250–500 litres of methane ($CH_4$) daily via enteric fermentation by methanogenic archaea in the rumen. 95% of this is released via burping, not flatulence.",
            "The Red Seaweed Miracle (*Asparagopsis taxiformis*): Adding just 0.2% to 0.5% dried red seaweed to cattle feed provides concentrated bioavailable bromoform ($CHBr_3$), which directly inhibits the methyl-coenzyme M reductase enzyme used by rumen archaea, slashing burp methane emissions by up to 80–90% without compromising weight gain or milk safety.",
            "Catalytic Burp Halters (Zelp): Wearable bovine headgear that detects exhaled burp plumes using micro-sensors and draws them across an internal catalytic oxidizer, converting methane into water vapor and carbon dioxide before it enters the atmosphere.",
            "Alternative Protein Conversion (Insects vs Cattle): Crickets and black soldier fly larvae deliver equivalent bioavailable complete protein while using 99% less land, 80% less feed, 90% less water, and producing <1% of the greenhouse emissions per kilogram of edible protein compared to industrial cattle."
        ],
        "mental_model": "Putting an enzyme silencer in the stomach. Methanogenic bacteria are factory workers assembling methane molecules. A tiny dose of seaweed is a lock on the factory door that stops them from turning hydrogen into methane gas.",
        "checkpoint": {
            "question": "By what biochemical pathway does feeding Asparagopsis taxiformis red seaweed reduce bovine enteric methane emissions?",
            "options": [
                "It coats the cow's esophagus with impermeable plastic wax",
                "It contains bromoform which chemically blocks the methyl-coenzyme M reductase enzyme in rumen methanogenic archaea",
                "It replaces all rumen bacteria with photosynthetic algae",
                "It converts all digested carbohydrates into atmospheric nitrogen gas"
            ],
            "correct_index": 1,
            "explanation": "Asparagopsis taxiformis contains concentrated bromoform, which reacts with vitamin B12 cofactors to inhibit the methyl-coenzyme M reductase enzyme responsible for the terminal step of methane generation in rumen archaea."
        }
    },
    {
        "card_num": 9,
        "title": "Digital Earth, AI Wildlife Defense & Controlled Environment Agriculture",
        "act": "Act 6: Space, AI Wildlife Defense & Frontier Agritech",
        "slides_covered": [20, 21, 22, 24, 25, 26, 27, 28, 29],
        "slides_label": "Slides 20, 21, 22, 24, 25, 26, 27, 28, 29",
        "exam_rating": {
            "tier": "HIGH (⭐⭐⭐⭐)",
            "stars": 4,
            "badge_class": "badge-high",
            "frequency_count": "Tested in 2022 and 2023 End-Semester Exams",
            "recent_papers": ["End Exam 2023 (Sec I, Q1c: 'What is Wild Me')", "End Exam 2022 (Sec III, Q6: 'Wild Me AI platform')", "End Exam 2022 (Sec III, Q14: 'TRASE platform')"],
            "exam_tip": "Wild Me (open-source computer vision for wildlife biometrics from coat patterns) and TRASE (supply chain mapping of food imports to deforestation sites) are recurring 1-mark fill-in-the-blank and short definition favorites."
        },
        "eli15_takeaway": "We can protect nature using digital tools. Artificial intelligence identifies wild animals from their stripes and spots (Wild Me), satellites track illegal fishing ships (Global Fishing Watch), and vertical indoor farms (AeroFarms) grow fresh greens with 95% less water and zero soil.",
        "key_facts": [
            "Wild Me & Biometric AI: An open-source AI platform that uses deep learning computer vision algorithms (such as HotSpotter and CurvRank) to identify and track individual wild animals (zebras, whale sharks, snow leopards) from unique skin, spot, or fluke patterns, replacing invasive physical tagging.",
            "TRASE Supply Chain Intelligence: A spatial data engine developed by SEI and Global Canopy mapping trade flows and financing from commodity importer nations directly to subnational deforestation hotspots (e.g. Brazilian soy and cattle ranches).",
            "Global Fishing Watch: Leverages machine learning on satellite Automatic Identification System (AIS) vessel tracking beacons to expose illegal, unreported, and unregulated (IUU) commercial trawling inside marine protected areas.",
            "Vertical Aeroponics (AeroFarms): Plants grow vertically on cloth in closed LED-lit towers with zero soil. Roots are periodically misted with precise nutrient solutions, cutting water usage by 95%, slashing fertilizer by 50%, eliminating synthetic pesticides, and generating up to 390 times higher crop yield per square foot.",
            "Agroecological Pest Defense: Trap cropping with marigolds (*Tagetes*) produces alpha-terthienyl, naturally suppressing soil root-knot nematodes and shielding brassica crops without petrochemical synthetic pesticides."
        ],
        "mental_model": "Face ID for leopards, GPS for fish poachers, and multi-story hydroponic pantries. Instead of trashing more wild jungle for farmland, we build indoor vertical farm towers and protect wild animals with smart cameras from orbit.",
        "checkpoint": {
            "question": "What is the core technological capability of the Wild Me conservation platform tested in previous EST examinations?",
            "options": [
                "Genetic cloning of extinct Pleistocene mammoths",
                "Open-source computer vision AI that identifies and tracks individual wild animals biometrically via coat, stripe, or fluke patterns",
                "Automated robotic shooting of invasive predator species",
                "Underwater acoustic sonar that repels sharks from bathing beaches"
            ],
            "correct_index": 1,
            "explanation": "Wild Me is an open-source AI and citizen-science platform that applies computer vision pattern-recognition to identify individual animals from photos of their unique spots, stripes, and fin outlines without invasive collars or tags."
        }
    }
]

# Write to class_11_cards.json
cards_file = "Study_Material/class_11_cards.json"
with open(cards_file, "w", encoding="utf-8") as f:
    json.dump({
        "class_id": 11,
        "title": "Class 11: Climate Change Technology Solutions (9 Topic Cards Rebuilt from 29 Slides)",
        "total_cards": len(class11_cards),
        "total_slides_covered": 29,
        "cards": class11_cards
    }, f, indent=2)

print(f"Saved {len(class11_cards)} topic cards covering 29 slides to {cards_file}")

# Update curriculum_database.json
db_path = "Study_Material/curriculum_database.json"
with open(db_path, "r", encoding="utf-8") as f:
    db = json.load(f)

for c in db.get("classes", []):
    if c.get("class_id") == 11:
        c["topic_cards"] = class11_cards
        c["total_topic_cards"] = len(class11_cards)
        c["title"] = "Class 11: Climate Change Technology Solutions (Exam-Rated Topic Cards)"
        c["summary"] = "High-density exam-focused topic cards covering negative emission technologies, blue carbon, DAC sorbent physics, Aether diamonds, Novacem cement, cattle methane reduction, and digital wildlife AI."
        print("Updated Class 11 in curriculum_database.json with topic_cards")
        break

with open(db_path, "w", encoding="utf-8") as f:
    json.dump(db, f, indent=2, ensure_ascii=False)

print("Saved updated curriculum_database.json")
