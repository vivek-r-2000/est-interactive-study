import json

exam_questions_map = {
    1: [
        {
            "paper": "EST Mid-1 2022",
            "section": "Section I, Q3",
            "marks": "2 Marks",
            "question": "Explain why reducing future emissions alone cannot achieve net-zero targets and why negative emissions technologies (NETs) are required under the Paris Agreement 1.5°C goal.",
            "answer_guideline": "<ul><li><strong>Residual Hard-to-Abate Emissions:</strong> Certain vital industrial and transport sectors (heavy aviation, long-haul shipping, blast-furnace steelmaking, cement, and enteric agricultural methane) cannot technically or economically reach absolute zero emissions by 2050.</li><li><strong>Carbon Budget & Historical Load:</strong> To prevent exceeding the 1.5°C threshold under COP21, residual positive emissions must be actively counterbalanced by Negative Emissions Technologies (NETs) that pull historical CO2 directly from ambient air into durable geologic or biospheric sinks.</li></ul>"
        },
        {
            "paper": "EVS Quiz-3 2020",
            "section": "Q1(b)",
            "marks": "1 Mark",
            "question": "Compare mature forests with growing forests in terms of gross primary productivity and net addition to standing biomass.",
            "answer_guideline": "<ul><li><strong>Mature Climax Forests:</strong> In mature equilibrium forests, gross primary productivity (GPP) is fully consumed by plant respiration and organic decomposition, resulting in <em>zero net addition</em> to standing biomass.</li><li><strong>Young Growing Forests:</strong> Actively growing forests store net carbon at a rate of ~3.7 tonnes CO2/ha/year, but face severe trade-offs: land competition, permanence risks (wildfires, beetle infestations), and snowy albedo warming.</li></ul>"
        },
        {
            "paper": "EVS End Exam 2019",
            "section": "Section II, Q6",
            "marks": "2 Marks",
            "question": "What is biochar and why does it represent a more permanent carbon sink than surface organic matter?",
            "answer_guideline": "<ul><li><strong>Production:</strong> Biochar is produced by pyrolyzing agricultural biomass at 400–700°C in an oxygen-limited environment, avoiding rapid aerobic rotting or open-field burning.</li><li><strong>Permanence:</strong> Transforms labile cellulosic carbon into recalcitrant aromatic carbon rings that soil microorganisms cannot enzymatically break down, locking carbon in soil for centuries while improving soil moisture and nutrient retention.</li></ul>"
        }
    ],
    2: [
        {
            "paper": "EVS End Exam 2023",
            "section": "Section I, Q1(g)",
            "marks": "1 Mark",
            "question": "What is Blue carbon?",
            "answer_guideline": "<p><strong>Definition:</strong> Blue carbon refers to the carbon captured and sequestered by coastal marine ecosystems, predominantly mangroves, tidal salt marshes, and seagrass meadows, stored primarily in waterlogged, anoxic sediments.</p>"
        },
        {
            "paper": "EVS End Exam 2022",
            "section": "Section V, Q(e)",
            "marks": "2 Marks",
            "question": "State the advantages of blue carbon habitat restoration (mention at least 3 distinct ecosystem points).",
            "answer_guideline": "<ol><li><strong>Exceptional Burial Velocity:</strong> Mangrove and salt marsh sediments accumulate and bury carbon 10 to 40 times faster per hectare than terrestrial tropical rainforests due to permanently anoxic (oxygen-depleted) saline mud that prevents microbial decay.</li><li><strong>Multi-Hazard Storm Surges:</strong> Mangrove root complexes attenuate up to 66% of incoming wave energy within 100 meters, shielding coastal human communities from cyclones and tsunamis.</li><li><strong>Biodiversity & Fisheries Nursery:</strong> Coastal wetland roots provide critical nursery and feeding grounds for ~75% of commercial tropical fish and crustacean species.</li></ol>"
        },
        {
            "paper": "EVS End Exam 2018",
            "section": "Part IV, Q3",
            "marks": "4 Marks",
            "question": "What kind of ecosystem services are provided by mangrove habitats, and what is the consequence of their degradation?",
            "answer_guideline": "<ul><li><strong>Ecosystem Services:</strong> Carbon storage in deep peat sediment, shoreline stabilization, heavy-metal sediment filtration, wave dampening, and fishery breeding grounds.</li><li><strong>Degradation Consequences:</strong> Draining and clearing coastal wetlands exposes millennia of trapped organic sediment to air, generating an estimated <strong>3% to 19% of all global deforestation emissions</strong> despite covering less than 0.5% of the seabed.</li></ul>"
        }
    ],
    3: [
        {
            "paper": "EST Mid-1 2022",
            "section": "Section I, Q3(c)",
            "marks": "2 Marks",
            "question": "How does substituting traditional building materials with engineered biomass (like CLT timber and hempcrete) affect a city's embodied carbon?",
            "answer_guideline": "<ul><li><strong>Embodied Carbon Inversion:</strong> Conventional steel smelting and Portland cement calcination account for ~11% of global emissions. Replacing them with Cross-Laminated Timber (CLT) turns buildings into carbon sinks, locking ~1 tonne of atmospheric CO2 in every cubic meter of timber.</li><li><strong>Low-Carbon Envelope:</strong> Using hemp-lime (hempcrete) and sheep's wool insulation provides fire-resistant, breathable thermal insulation with virtually zero manufacturing emissions compared to polystyrene foams.</li></ul>"
        },
        {
            "paper": "EVS Quiz-3 2020",
            "section": "Q2",
            "marks": "1 Mark",
            "question": "Name two natural agricultural materials that can replace petroleum-based insulation in eco-friendly architecture.",
            "answer_guideline": "<p><strong>Answer:</strong> Agricultural industrial hemp fibers (or hemp-lime) and sheep's wool.</p>"
        }
    ],
    4: [
        {
            "paper": "EST Mid-1 2024",
            "section": "Section I, Q2",
            "marks": "2 Marks",
            "question": "Explain the mechanism of Enhanced Rock Weathering (EW) and its dual impact on atmospheric carbon and ocean chemistry.",
            "answer_guideline": "<ul><li><strong>Mechanism:</strong> Pulverizing reactive volcanic silicate rocks (basalt or olivine) multiplies their reactive surface area by millions, accelerating natural weathering kinetics: $\\text{CaSiO}_3 + 2\\text{CO}_2 + \\text{H}_2\\text{O} \\rightarrow \\text{Ca}^{2+} + 2\\text{HCO}_3^- + \\text{SiO}_2$.</li><li><strong>Dual Impact:</strong> (1) Sequesters up to 3.7 billion tonnes of CO2eq per year globally; (2) Washes soluble bicarbonate ions ($\\text{HCO}_3^-$) into rivers and oceans, neutralizing carbonic acid and directly counteracting ocean acidification.</li></ul>"
        },
        {
            "paper": "EST Quiz-1 2023",
            "section": "Q3",
            "marks": "1 Mark",
            "question": "What chemical compound is proposed to be sprayed into clouds to offset global emissions, and over what surface area?",
            "answer_guideline": "<p><strong>Answer:</strong> Dispersing <strong>56 million tonnes of potassium hydroxide (KOH)</strong> into clouds across 0.4% of Earth's surface (an area equivalent to the Greenland ice sheet).</p>"
        }
    ],
    5: [
        {
            "paper": "EVS End Exam 2023",
            "section": "Section III, Q2(b)",
            "marks": "3 Marks",
            "question": "Explain the chemical steps involved in high-temperature liquid Direct Air Capture systems (Carbon Engineering closed loop).",
            "answer_guideline": "<ol><li><strong>Air Contactor:</strong> Ambient air passes through a potassium hydroxide spray: $2\\text{KOH} + \\text{CO}_2 \\rightarrow \\text{K}_2\\text{CO}_3 + \\text{H}_2\\text{O}$.</li><li><strong>Pellet Reactor:</strong> Potassium carbonate reacts with calcium hydroxide to precipitate solid calcium carbonate pellets: $\\text{K}_2\\text{CO}_3 + \\text{Ca(OH)}_2 \\rightarrow 2\\text{KOH} + \\text{CaCO}_3\\downarrow$.</li><li><strong>Oxy-fired Calciner:</strong> Pellets are heated to ~900°C: $\\text{CaCO}_3 \\xrightarrow{\\Delta} \\text{CaO} + \\text{CO}_2\\uparrow$ to release pure CO2 gas.</li><li><strong>Slaker:</strong> Calcium oxide is rehydrated with water: $\\text{CaO} + \\text{H}_2\\text{O} \\rightarrow \\text{Ca(OH)}_2$ to close and regenerate the loop.</li></ol>"
        },
        {
            "paper": "EST Mid-1 2024",
            "section": "Section II, Q4",
            "marks": "2 Marks",
            "question": "What are Bis-iminoguanidines (BIGs) in carbon capture, and what is their primary thermodynamic advantage over traditional calciners?",
            "answer_guideline": "<ul><li><strong>Definition:</strong> BIGs are crystalline guanidine compounds developed by Oak Ridge National Laboratory that scrub CO2 from air streams like scuba rebreathers by selectively crystallizing bicarbonate solids.</li><li><strong>Thermodynamic Advantage:</strong> BIGs release pure CO2 under mild heating at only <strong>~120°C</strong> (with water vapor condensed in ice tubes), avoiding the extreme 900°C calcination kilns and slashing regeneration thermal energy penalties by over 60%.</li></ul>"
        },
        {
            "paper": "EVS Quiz-4 2020",
            "section": "Q2",
            "marks": "1 Mark",
            "question": "What is the difference between DAC Standalone Geologic Storage and DAC Air-to-Fuels plants?",
            "answer_guideline": "<p><strong>Answer:</strong> Standalone Geologic Storage injects captured CO2 permanently into deep basalt or saline rock for true negative emissions. Air-to-Fuels plants combine captured CO2 with electrolytic green hydrogen and renewable electricity to produce drop-in synthetic hydrocarbons (gasoline, diesel, Jet-A) for circular, zero-fossil transportation.</p>"
        }
    ],
    6: [
        {
            "paper": "EVS End Exam 2022",
            "section": "Section VI, Q(c)",
            "marks": "1 Mark",
            "question": "Give names of leading commercial Direct Air Capture companies and their current operational capacity.",
            "answer_guideline": "<p><strong>Answer:</strong> Climeworks (Switzerland), Carbon Engineering (Canada), and Global Thermostat (USA). Together they operate 18 commercial plants with capacities from 1 to 4,000 tCO2/yr (totaling just under 8,000 tCO2/yr worldwide).</p>"
        },
        {
            "paper": "EST End Exam 2024",
            "section": "Section I, Q1(c)",
            "marks": "2 Marks",
            "question": "How does deep basalt mineralization (CarbFix) differ from offshore saline aquifer storage (Net Zero Teesside)?",
            "answer_guideline": "<ul><li><strong>CarbFix (Iceland):</strong> CO2 is dissolved in water and injected into basaltic formations; within 2 years, natural geochemical reactions convert >95% of the carbon into solid carbonate rock, eliminating leakage risks permanently.</li><li><strong>Net Zero Teesside (NZT, UK):</strong> Captures up to 10M tCO2/yr from industrial clusters and pumps supercritical CO2 via offshore pipelines into porous saline sandstone aquifers (Endurance reservoir) beneath impermeable North Sea caprock.</li></ul>"
        }
    ],
    7: [
        {
            "paper": "EVS End Exam 2023",
            "section": "Section III, Q5",
            "marks": "3 Marks",
            "question": "Explain the process of diamond manufacturing by Aether (only the process).",
            "answer_guideline": "<ol><li><strong>Sourcing:</strong> Atmospheric CO2 is purchased directly from Climeworks' commercial DAC collectors in Europe and shipped to the US.</li><li><strong>Methanation:</strong> CO2 is catalytically converted into ultra-high-purity methane ($CH_4$) via the Sabatier reduction process: $\\text{CO}_2 + 4\\text{H}_2 \\rightarrow \\text{CH}_4 + 2\\text{H}_2\\text{O}$.</li><li><strong>CVD Plasma Deposition:</strong> Pure $CH_4$ is injected into Chemical Vapor Deposition (CVD) diamond reactors heated to extreme temperatures under near-vacuum conditions, growing rough diamond crystal lattice layer by layer over several weeks.</li><li><strong>100% Clean Energy:</strong> Entire manufacturing synthesis is powered by zero-carbon solar and nuclear power.</li><li><strong>Surat Cutting:</strong> Rough diamonds are shipped to Surat, Gujarat, India for precision gem cutting and facet polishing, then returned to NYC for jewelry sales.</li></ol>"
        },
        {
            "paper": "EVS End Exam 2022",
            "section": "Section X, Q(b)",
            "marks": "5 Marks",
            "question": "Give a detailed account on Diamonds from air pollution: include sourcing, intermediate chemical reactions, plasma synthesis, polishing hub, and environmental savings per carat.",
            "answer_guideline": "<ul><li><strong>Sourcing & Chemistry:</strong> Procures DAC CO2 from Climeworks $\\rightarrow$ catalytic conversion to $CH_4$ $\\rightarrow$ Chemical Vapor Deposition (CVD) vacuum plasma synthesis powered 100% by solar and nuclear energy.</li><li><strong>Polishing Hub:</strong> Surat, India cuts and polishes the rough gems.</li><li><strong>Environmental Impact:</strong> Each 1-carat Aether diamond sequesters the equivalent of <strong>20 tonnes of atmospheric CO2</strong> (offsetting ~1.5 years of human emissions), avoids <strong>127 gallons of water</strong> wasted per mined carat, and uses half the energy of open-pit mining.</li></ul>"
        }
    ],
    8: [
        {
            "paper": "EVS End Exam 2022",
            "section": "Section III, Q15",
            "marks": "1 Mark",
            "question": "Fill in the blank: Methane reduction from livestock can be achieved by adding ________ to cattle feed.",
            "answer_guideline": "<p><strong>Answer:</strong> <em>Asparagopsis taxiformis</em> (tropical red seaweed).</p>"
        },
        {
            "paper": "EVS Mid-2 2018",
            "section": "Section I, Q1(c)",
            "marks": "0.5 Mark",
            "question": "What is the single largest agricultural source of global anthropogenic methane emissions?",
            "answer_guideline": "<p><strong>Answer:</strong> Enteric fermentation in cattle and livestock (meat and dairy produce 7.1 Gt GHG/yr, representing 14.5% of total man-made global emissions).</p>"
        },
        {
            "paper": "EVS End Exam 2022",
            "section": "Section IV, Q3",
            "marks": "3 Marks",
            "question": "Describe two technological solutions to mitigate bovine enteric methane emissions: one biochemical dietary intervention and one wearable mechanical device.",
            "answer_guideline": "<ul><li><strong>Dietary Supplement:</strong> Adding 0.2–0.5% red seaweed (<em>Asparagopsis taxiformis</em>) to feed reduces enteric methane by up to <strong>80%</strong> by inhibiting the bromoform enzyme pathway in rumen methanogenic archaea.</li><li><strong>Wearable Halter (Zelp, UK):</strong> A smart halter worn around the snout detects exhaled methane burps and routes them through a micro-catalytic converter that oxidizes $CH_4$ into water vapor and trace $CO_2$: $\\text{CH}_4 + 2\\text{O}_2 \\rightarrow \\text{CO}_2 + 2\\text{H}_2\\text{O}$.</li></ul>"
        }
    ],
    9: [
        {
            "paper": "EST Mid-1 2024",
            "section": "Section I, Q4",
            "marks": "2 Marks",
            "question": "What is Marine Cloud Brightening (MCB), and what observational evidence validates its physical mechanism?",
            "answer_guideline": "<ul><li><strong>Mechanism:</strong> Autonomous, wind-powered Flettner rotor ships spray microscopic sea-salt aerosol droplets into marine boundary layer clouds. Salt crystals act as cloud condensation nuclei (CCN), creating smaller and more numerous cloud droplets that dramatically increase cloud albedo (Twomey effect) and reflect solar radiation.</li><li><strong>Empirical Evidence:</strong> NASA satellite imagery revealing bright, persistent reflective 'ship tracks' formed in low marine stratocumulus clouds along cargo vessel shipping lanes.</li></ul>"
        },
        {
            "paper": "EVS End Exam 2022",
            "section": "Section IV, Q4(b)",
            "marks": "2 Marks",
            "question": "What are the three fundamental questions (scientific, ethical, and governance) that must be addressed before deploying geoengineering solar radiation management?",
            "answer_guideline": "<ol><li><strong>The Science Question:</strong> Can we do it without triggering disastrous monsoonal disruptions or precipitation collapses?</li><li><strong>The Ethics Question:</strong> Should humanity artificially manipulate the planetary climate thermostat?</li><li><strong>The Policy Question:</strong> How would global nations govern, regulate, and avoid unilateral or rogue deployment?</li></ol>"
        }
    ],
    10: [
        {
            "paper": "EVS End Exam 2023",
            "section": "Section III, Q3(b)",
            "marks": "3 Marks",
            "question": "Explain how floating solar photovoltaic (FPV) systems differ in operational efficiency and land-use benefits from conventional terrestrial solar farms, citing the South Korea installation.",
            "answer_guideline": "<ul><li><strong>Land Preservation:</strong> Installed on reservoir water surfaces (e.g., South Korea 41 MW Hapcheon Dam plant), eliminating deforestation and agricultural land-use conflicts.</li><li><strong>Water Conservation:</strong> Shading reservoir waters reduces evaporative water loss and suppresses toxic cyanobacterial algal blooms.</li><li><strong>Efficiency Bonus:</strong> The thermodynamic cooling effect of the water body lowers photovoltaic cell operating temperatures, mitigating thermal efficiency loss and delivering a <strong>5% to 10% increase in power generation</strong>.</li></ul>"
        },
        {
            "paper": "EVS Mid-2 2018",
            "section": "Q2",
            "marks": "2 Marks",
            "question": "Describe the urban microclimate cooling achieved by the Medellín green corridor tree planting initiative in Colombia.",
            "answer_guideline": "<p><strong>Answer:</strong> Medellín planted over 350,000 trees across 30 interconnected green corridors, transforming concrete urban heat islands into shaded vegetative corridors that successfully lowered citywide ambient microclimate temperatures by up to <strong>3°C (3.5°F)</strong>.</p>"
        },
        {
            "paper": "EVS End Exam 2019",
            "section": "Q4",
            "marks": "2 Marks",
            "question": "What percentage of global CO2 emissions originates from maritime cargo shipping and commercial aviation, and what clean fuels replace fossil bunker oil and jet fuel?",
            "answer_guideline": "<p><strong>Answer:</strong> Maritime cargo shipping generates <strong>2.5% of global CO2</strong> (transitioning to green hydrogen fuel cells and liquid ammonia propulsion). Commercial aviation accounts for <strong>2% of global CO2</strong> (transitioning to battery-electric regional flights and Sustainable Aviation Fuels / SAF).</p>"
        }
    ],
    11: [
        {
            "paper": "EVS End Exam 2023",
            "section": "Section I, Q1(c)",
            "marks": "1 Mark",
            "question": "What is Wild Me?",
            "answer_guideline": "<p><strong>Answer:</strong> Wild Me is an open-source AI platform that uses computer vision algorithms (such as Wildbook and DolphinGemma) to identify and track individual wild animals based on their unique natural skin, coat, stripe, and spot patterns, enabling non-invasive conservation censuses without harmful physical tagging.</p>"
        },
        {
            "paper": "EVS End Exam 2022",
            "section": "Section III, Q6",
            "marks": "1 Mark",
            "question": "Fill in the blank: ________ is an open-source AI technology/platform to identify and track wildlife.",
            "answer_guideline": "<p><strong>Answer:</strong> Wild Me.</p>"
        },
        {
            "paper": "EVS End Exam 2022",
            "section": "Section III, Q14",
            "marks": "1 Mark",
            "question": "Fill in the blank: ________ platform maps the links between food importing countries and the places where the food is produced to track deforestation.",
            "answer_guideline": "<p><strong>Answer:</strong> TRASE (Transparency for Sustainable Economies).</p>"
        },
        {
            "paper": "EVS End Exam 2019",
            "section": "Section III, Q3",
            "marks": "2 Marks",
            "question": "How do blockchain and remote sensing combat illegal fishing and timber deforestation in environmental surveillance?",
            "answer_guideline": "<ul><li><strong>Blockchain:</strong> Provides tamper-proof digital ledgers coupled with GPS transponders to trace seafood supply chains from catch to market, halting illegal tuna fishing and commodity fraud.</li><li><strong>Remote Sensing:</strong> High-resolution optical/radar satellites combined with autonomous drones (Global Forest Watch) monitor tropical canopies in real time to detect illegal roads and palm oil expansion before clearcutting occurs.</li></ul>"
        }
    ],
    12: [
        {
            "paper": "EVS End Exam 2023",
            "section": "Section III, Q5(a)",
            "marks": "3 Marks",
            "question": "List the four essential aspects of vertical farming and describe AeroFarms' patented aeroponic technology.",
            "answer_guideline": "<ol><li><strong>Four Essential Aspects:</strong> (1) Tower-like vertical modular structure; (2) Tuned LED spectrum lighting (photosynthetic red/blue wavelengths); (3) Soilless growth media (hydroponics/aeroponics/aquaponics); (4) Closed-loop recirculating water systems saving 95% water.</li><li><strong>AeroFarms System:</strong> Plant roots are suspended in air and misted with nutrient water; seeds are germinated on reusable cloth fleece woven from recycled plastic bottles; grown indoors with zero soil and zero pesticides.</li></ol>"
        },
        {
            "paper": "EST Mid-1 2024",
            "section": "Section II, Q5",
            "marks": "2 Marks",
            "question": "Why does vertical farming reduce plant water consumption by 95% compared to open-field farming?",
            "answer_guideline": "<p><strong>Answer:</strong> Traditional field irrigation suffers heavy losses to deep soil drainage, runoff, and uncontained solar evaporation. Vertical farms operate in closed indoor loops that capture all plant transpiration via industrial dehumidifiers and recirculate the distilled water directly back into precision root-misting loops, reducing water consumption by 95%.</p>"
        }
    ],
    13: [
        {
            "paper": "EST Mid-1 2024",
            "section": "Section I, Q1",
            "marks": "2 Marks",
            "question": "What is trap cropping? Explain how marigolds act as a trap crop to protect primary crops.",
            "answer_guideline": "<ul><li><strong>Definition:</strong> Planting sacrificial companion plants in perimeter borders or intercropped rows to attract, intercept, or repel insect pests without synthetic chemical pesticides.</li><li><strong>Marigolds (Tagetes):</strong> Root systems exude alpha-terthienyl nematicides that kill root-knot nematodes upon penetration, while blossoms release volatile aromatic compounds that confuse and repel foliar pests like aphids and whiteflies.</li></ul>"
        },
        {
            "paper": "EVS End Exam 2022",
            "section": "Section IV, Q2",
            "marks": "2 Marks",
            "question": "Cite two international examples of trap cropping combinations and their targeted agricultural pests.",
            "answer_guideline": "<ol><li><strong>Italy:</strong> Planting <em>Brassicaceae</em> border strips around sugar beet fields to intercept flea beetles.</li><li><strong>China:</strong> Interplanting maize border strips around cotton fields to divert whiteflies and bollworms.</li></ol>"
        }
    ],
    14: [
        {
            "paper": "EVS End Exam 2023",
            "section": "Section III, Q7",
            "marks": "3 Marks",
            "question": "Difference between Portland and Novacem cement.",
            "answer_guideline": "<ol><li><strong>Raw Material & Temperature:</strong> Portland cement requires calcining limestone ($\\text{CaCO}_3$) at $1,450^\\circ\\text{C}$ in fossil-fueled rotary kilns, emitting 0.8–1.0 t CO2/t cement. Novacem uses magnesium silicates ($\\text{MgSiO}_3$) processed at only $650^\\circ\\text{C}$, cutting thermal fuel emissions in half.</li><li><strong>Chemical Reaction:</strong> Portland: $\\text{CaCO}_3 \\xrightarrow{1450^\\circ\\text{C}} \\text{CaO} + \\text{CO}_2\\uparrow$. Novacem: $\\text{MgSiO}_3 \\xrightarrow{650^\\circ\\text{C}} \\text{MgO} + \\text{SiO}_2$.</li><li><strong>Curing & Carbon Balance:</strong> Portland cures by hydration. Novacem cures by carbonation: $\\text{MgO} + \\text{CO}_2 + \\text{H}_2\\text{O} \\rightarrow \\text{MgCO}_3\\cdot 3\\text{H}_2\\text{O}$, absorbing up to 100 kg CO2 net per tonne, making it carbon-negative.</li></ol>"
        },
        {
            "paper": "EVS End Exam 2019",
            "section": "Section IV, Q1(d)",
            "marks": "3 Marks",
            "question": "Novacem as ecofriendly cement.",
            "answer_guideline": "<p><strong>Answer:</strong> Novacem is an eco-friendly magnesium silicate cement manufactured at 650°C. During curing, it actively absorbs atmospheric CO2 to form magnesium carbonates, achieving a net carbon-negative footprint of -100 kg CO2 per tonne.</p>"
        },
        {
            "paper": "EVS Mid-2 2018",
            "section": "Q8(b)",
            "marks": "1.5 Marks",
            "question": "Answer in three sentences: brief account on Novacem (MgO + CO2 -> MgCO3).",
            "answer_guideline": "<p><strong>Answer:</strong> (1) Novacem is a carbon-negative cement manufactured from magnesium silicates at 650°C instead of limestone at 1,450°C. (2) During hardening, it absorbs atmospheric carbon dioxide via the reaction $\\text{MgO} + \\text{CO}_2 \\rightarrow \\text{MgCO}_3$. (3) It sequesters up to 100 kg more CO2 per tonne than emitted during production.</p>"
        }
    ]
}

# 1. Update Study_Material/class_11_cards.json
with open("Study_Material/class_11_cards.json", "r", encoding="utf-8") as f:
    cards = json.load(f)

for card in cards:
    cnum = card["card_num"]
    if cnum in exam_questions_map:
        card["exam_questions"] = exam_questions_map[cnum]
        print(f"Attached {len(exam_questions_map[cnum])} exam questions to Card {cnum}")

with open("Study_Material/class_11_cards.json", "w", encoding="utf-8") as f:
    json.dump(cards, f, indent=2)

# 2. Update Study_Material/curriculum_database.json
with open("Study_Material/curriculum_database.json", "r", encoding="utf-8") as f:
    db = json.load(f)

for c in db["classes"]:
    if c["class_id"] == 11:
        c["topic_cards"] = cards
        print("Updated Class 11 topic_cards in curriculum_database.json")
        break

with open("Study_Material/curriculum_database.json", "w", encoding="utf-8") as f:
    json.dump(db, f, indent=2)

print("Successfully attached all past exam questions with model answers!")
