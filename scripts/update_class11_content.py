import json
import os

def update_class11():
    db_path = os.path.join("Study_Material", "curriculum_database.json")
    with open(db_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # 29 Detailed Slidewise Modules with Narrative Continuity and Zero Slop
    slides_data = [
        {
            "slide_num": 1,
            "title": "Mission Briefing: The Net-Zero Dilemma",
            "act": "Act 1: The Negative Emissions Imperative & Nature's Carbon Sponges",
            "continuity_bridge": "We know emissions are driving global temperatures past safe thresholds. Class 11 shifts from analyzing the disaster to engineering the technological countermeasures.",
            "eli15_takeaway": "Stopping new emissions is no longer enough to avoid climate catastrophe; we must actively extract historical carbon already floating in our sky.",
            "key_facts": [
                "Course topic: Climate change technology solutions presented by Dr. Rama Chandra Prasad.",
                "Explores technological wedges across carbon removal, clean transport, agriculture, and computational monitoring.",
                "Sets up the fundamental split between biological capture, geochemical engineering, industrial direct air capture, and agricultural redesign."
            ],
            "mental_model": "Imagine a bathtub overflowing with hot water. Turning off the tap stops adding water, but the bathroom floor is still ruined unless you open the drain and pull the water out.",
            "checkpoint": {
                "question": "What is the core premise of Class 11 regarding climate technology solutions?",
                "options": [
                    "Reaching climate stability requires active negative emissions technologies alongside aggressive emissions reductions",
                    "Climate change has already solved itself without human intervention",
                    "Technology solutions are strictly limited to planting ornamental garden flowers",
                    "All industrial factories must immediately dismantle their electrical grids"
                ],
                "correct_index": 0,
                "explanation": "Stopping emissions halts future damage, but net-zero goals require active carbon removal technologies to extract existing atmospheric CO2."
            }
        },
        {
            "slide_num": 2,
            "title": "Negative Emission Technologies (NETs) & The Paris Target",
            "act": "Act 1: The Negative Emissions Imperative & Nature's Carbon Sponges",
            "continuity_bridge": "Now that we know we need active carbon removal, let's look at the legal target set by world leaders and the simplest tool we have: trees.",
            "eli15_takeaway": "The Paris Agreement aims to cap warming at 1.5°C; tree planting absorbs about 3.7 tons of carbon per hectare each year, but land competition limits its scale.",
            "key_facts": [
                "COP21 Paris Agreement target: Limit average global temperature rise to 1.5°C above pre-industrial levels.",
                "Negative Emissions Technologies (NETs) remove atmospheric CO2 to offset ongoing hard-to-abate releases.",
                "Afforestation & Reforestation: Sequester CO2 at roughly 3.7 tonnes per hectare per year.",
                "Economic cost: $20–100 per tonne of CO2 removed.",
                "Major bottlenecks: Competition with agricultural food land, freshwater availability, forest fires, and permanence risks."
            ],
            "mental_model": "Planting trees is like installing natural solar-powered carbon vacuums. They work reliably, but you quickly run out of room in the house to park them.",
            "checkpoint": {
                "question": "What is the approximate CO2 sequestration rate of afforestation and reforestation noted in the lecture?",
                "options": [
                    "3.7 tonnes per hectare per year",
                    "500 tonnes per hectare per year",
                    "0.01 tonnes per hectare per year",
                    "10,000 tonnes per hectare per year"
                ],
                "correct_index": 0,
                "explanation": "Afforestation captures roughly 3.7 tonnes of CO2 per hectare annually at a price of $20 to $100 per tonne, constrained by land availability."
            }
        },
        {
            "slide_num": 3,
            "title": "Biochar: Baking Plant Waste into Permanent Soil Gold",
            "act": "Act 1: The Negative Emissions Imperative & Nature's Carbon Sponges",
            "continuity_bridge": "Living trees eventually die and rot, venting their carbon back into the air. What if we could permanently lock that biomass carbon before it decomposes?",
            "eli15_takeaway": "Baking crop stalks in an oxygen-free furnace turns plant carbon into biochar—a porous black charcoal that locks carbon in soil for centuries while helping crops grow.",
            "key_facts": [
                "Sequestration potential: Up to 4.8 billion tonnes (4.8 Gt) of CO2 per year globally.",
                "Production process: Pyrolysis—heating renewable organic biomass at high temperatures in an oxygen-limited environment.",
                "Avoided emissions: Prevents open-field crop residue burning and rotting, which generate uncontrolled methane and black carbon.",
                "Soil co-benefits: Porous biochar structure retains soil moisture, binds nutrients, and increases agricultural yield."
            ],
            "mental_model": "Burning wood in an open campfire turns it to smoke in minutes. Baking it in a sealed pressure cooker freezes the carbon into solid charcoal pencils that last 500 years.",
            "checkpoint": {
                "question": "Why does biochar remain stable in soil for centuries compared to uncharred organic compost?",
                "options": [
                    "Pyrolysis rearranges carbon into recalcitrant aromatic structures that soil microbes cannot readily break down",
                    "Biochar turns into radioactive uranium that scares away earthworms",
                    "Biochar evaporates into the clouds within 48 hours",
                    "Biochar turns directly into liquid diesel fuel when buried"
                ],
                "correct_index": 0,
                "explanation": "Pyrolysis converts volatile plant carbon into stable aromatic carbon rings that resist microbial digestion, locking carbon in agricultural soils."
            }
        },
        {
            "slide_num": 4,
            "title": "Blue Carbon: Coastal Ocean Super-Sinks",
            "act": "Act 1: The Negative Emissions Imperative & Nature's Carbon Sponges",
            "continuity_bridge": "We explored land trees and farm biochar; now we move to where land meets water—coastal ecosystems that bury carbon dozens of times faster than inland forests.",
            "eli15_takeaway": "Mangroves, salt marshes, and seagrass meadows bury carbon in underwater mud without oxygen; destroying them releases up to 19% of global deforestation emissions.",
            "key_facts": [
                "Blue carbon definition: Organic carbon captured by coastal, marine, and estuarine ecosystems.",
                "Key habitats: Mangrove forests, tidal salt marshes, and seagrass meadows.",
                "Emissions impact: Destroying and draining coastal wetlands releases an estimated 3% to 19% of global deforestation emissions.",
                "Mechanism: Waterlogged sediment lacks dissolved oxygen, stopping microbes from decomposing buried root biomass."
            ],
            "mental_model": "Dropping a phone into a backyard puddle ruins the electronics, but dropping dead leaves into salty, oxygen-depleted marine mud preserves them like a deep-sea freezer.",
            "checkpoint": {
                "question": "What is 'Blue Carbon' in climate science?",
                "options": [
                    "Carbon sequestered and stored in coastal and marine habitats like mangroves, tidal marshes, and seagrasses",
                    "Carbon atoms dyed blue by industrial factory scrubbers",
                    "Carbon soot released by ocean-crossing cargo ships",
                    "Artificial diamond crystals grown in marine laboratories"
                ],
                "correct_index": 0,
                "explanation": "Blue carbon refers to biological carbon fixed and stored in the sediments of coastal marine ecosystems like mangroves and tidal salt marshes."
            }
        },
        {
            "slide_num": 5,
            "title": "Building with Structural Biomass: Timber Skyscrapers",
            "act": "Act 1: The Negative Emissions Imperative & Nature's Carbon Sponges",
            "continuity_bridge": "If coastal wetlands and soil can store carbon, why can't our urban buildings do the same instead of pouring emission-heavy concrete and steel?",
            "eli15_takeaway": "Replacing polluting concrete with engineered cross-laminated timber, bamboo, hemp insulation, and hemp-lime plaster turns city skyscrapers into carbon vaults.",
            "key_facts": [
                "Structural elements: Mass timber and fast-growing bamboo replace energy-intensive reinforced concrete and steel beams.",
                "Natural insulation: Hemp fibers and natural sheep wool replace petroleum-derived synthetic polystyrene foam.",
                "Wall assemblies: Hemp-lime (hempcrete) absorbs ambient CO2 over decades as it cures into lightweight solid walling.",
                "Double benefit: Avoids emissions from cement kilns while physically locking biological carbon inside buildings for 100+ years."
            ],
            "mental_model": "Every ton of steel manufactured belches carbon into the sky. Every beam of engineered timber is a tree that sucked carbon out of the sky and is now holding up your bedroom ceiling.",
            "checkpoint": {
                "question": "How does building with mass timber and hempcrete provide a 'double climate benefit'?",
                "options": [
                    "It physically locks biological carbon inside the building frame while displacing carbon-intensive cement and steel production",
                    "It makes buildings invisible to military radar systems",
                    "It causes houses to float into the upper atmosphere to cool off",
                    "It generates free electricity directly from rainwater"
                ],
                "correct_index": 0,
                "explanation": "Using structural biomass stores the carbon captured by trees while cutting the massive emissions created by firing limestone kilns for concrete."
            }
        },
        {
            "slide_num": 6,
            "title": "Earth-Scale Chemistry: Cloud & Ocean Alkali Dosing",
            "act": "Act 2: Earth-Scale Chemical Interventions",
            "continuity_bridge": "Biological systems like forests and wooden buildings have physical limits. To scale removals, scientists are turning to large-scale chemical adjustments of the clouds and oceans.",
            "eli15_takeaway": "Spraying alkaline chemicals into clouds or adding crushed limestone to the ocean neutralizes acid and converts dissolved carbon dioxide into harmless bicarbonate.",
            "key_facts": [
                "Atmospheric spray proposal: Spraying 56 million tonnes of Potassium Hydroxide (KOH) into clouds across 0.4% of Earth's surface (roughly the land area of Greenland).",
                "Ocean liming: Adding 2.5 billion to 8 billion tonnes of crushed limestone per year directly to surface ocean currents.",
                "Chemical effect: Counteracts ocean acidification and forces dissolved CO2 into stable bicarbonate ions ($HCO_3^-$).",
                "Logistical challenge: Massive mining, grinding, and marine distribution footprint."
            ],
            "mental_model": "Chewing an antacid tablet when your stomach is churning with acid. Adding alkaline mineral powder to acidic oceans neutralizes the burn and locks the acid into dissolved salt.",
            "checkpoint": {
                "question": "What is the primary scientific purpose of adding alkali (like crushed limestone) to oceans?",
                "options": [
                    "To neutralize ocean acidification and chemically convert dissolved CO2 into stable bicarbonate ions",
                    "To dye the seawater bright green so satellites can navigate",
                    "To freeze the surface of the ocean into solid ice sheets",
                    "To exterminate deep-sea fish populations"
                ],
                "correct_index": 0,
                "explanation": "Alkaline substances raise ocean pH, buffering against acidification and shifting carbonate chemistry so seawater absorbs and holds more carbon as dissolved bicarbonate."
            }
        },
        {
            "slide_num": 7,
            "title": "Enhanced Rock Weathering: Fast-Forwarding Geology",
            "act": "Act 2: Earth-Scale Chemical Interventions",
            "continuity_bridge": "Spraying chemicals from planes is controversial and expensive. But nature already dissolves rocks to absorb carbon over millions of years—what if we speed that up on farm fields?",
            "eli15_takeaway": "Natural rock weathering soaks up 3% of global emissions; grinding volcanic silicate basalt into fine dust and spreading it on croplands can trap 3.7 billion tonnes of carbon every year.",
            "key_facts": [
                "Natural baseline: Natural silicate rock erosion naturally locks away about 3% of all global fossil fuel emissions over geological eras.",
                "Enhanced Weathering (EW): Crushing silicate rocks (like basalt or olivine) to micro-particles drastically increases reactive surface area.",
                "Global capacity: EW could sequester up to 3.7 billion tonnes (3.7 Gt) of CO2 equivalent per year globally.",
                "Co-benefits: Releases vital minerals (calcium, magnesium, phosphorus) into depleted agricultural soils and runoff helps de-acidify coastal rivers."
            ],
            "mental_model": "A giant sugar cube in a cup of tea takes ten minutes to dissolve. Grind that same cube into fine powdered baker's sugar, and it dissolves in three seconds flat.",
            "checkpoint": {
                "question": "How does Enhanced Weathering (EW) accelerate natural rock carbon absorption?",
                "options": [
                    "Crushing silicate rocks into fine powder massively increases surface area, speeding up chemical carbon absorption from centuries to months",
                    "Setting rocks on fire with kerosene",
                    "Launching boulders into orbit around the sun",
                    "Soaking rocks in battery acid inside swimming pools"
                ],
                "correct_index": 0,
                "explanation": "Natural weathering is rate-limited by surface exposure. Grinding basalt increases contact area by thousands of times, accelerating carbon fixation."
            }
        },
        {
            "slide_num": 8,
            "title": "Direct Air Capture (DAC): Industrial Vacuum Cleaners",
            "act": "Act 3: Artificial Trees: Direct Air Capture & The Carbon Economy",
            "continuity_bridge": "Rocks and wetlands absorb carbon at nature's pace. For concentrated, high-throughput extraction, engineers built industrial Direct Air Capture machines.",
            "eli15_takeaway": "Direct Air Capture uses giant industrial fans and chemical filters to suck carbon dioxide straight out of outdoor air, then sends it deep underground for permanent storage.",
            "key_facts": [
                "Core system: Giant motorized fan arrays pull ambient outdoor air through porous chemical contactors.",
                "Operating pathways: Standalone extraction, deep geologic mineral storage, or commercial Enhanced Oil Recovery (EOR).",
                "Physical footprint: Occupies thousands of times less land area than equivalent afforestation plots.",
                "Key challenge: Ambient air is only 0.04% CO2 (420 ppm), meaning a DAC plant must process millions of cubic meters of air to capture a single ton."
            ],
            "mental_model": "A giant sieve in a muddy river. You scoop through Olympic swimming pools of water just to filter out a single tablespoon of gold dust.",
            "checkpoint": {
                "question": "What makes Direct Air Capture (DAC) thermodynamically challenging compared to flue-gas capture?",
                "options": [
                    "Ambient air has an extremely dilute CO2 concentration (~0.04%), requiring immense volumes of air to be moved through filters",
                    "Direct Air Capture only works inside dark caves",
                    "Outdoor air contains no carbon dioxide at all",
                    "Fans cannot turn in normal outdoor atmospheric pressure"
                ],
                "correct_index": 0,
                "explanation": "Because ambient air is 99.96% non-CO2, moving and filtering enough air to collect a single ton of carbon requires significant energy."
            }
        },
        {
            "slide_num": 9,
            "title": "Air-to-Fuels: Circular Aviation from Thin Air",
            "act": "Act 3: Artificial Trees: Direct Air Capture & The Carbon Economy",
            "continuity_bridge": "Once you capture pure CO2 from the air, you don't just have to bury it—you can combine it with water and clean electricity to replace fossil jet fuel.",
            "eli15_takeaway": "Carbon Engineering uses captured air carbon, split water, and solar power to synthesize clean drop-in gasoline, diesel, and jet fuel with zero fossil crude.",
            "key_facts": [
                "Process pioneered by Carbon Engineering (CE): Air + Water + Renewable Electricity = Clean Synthetic Hydrocarbons.",
                "Products: Drop-in synthetic gasoline, diesel, and Jet-A aviation fuel compatible with existing aircraft engines.",
                "Net carbon logic: When the plane burns the fuel, it releases only the carbon that was sucked out of the air earlier, creating a closed circular loop.",
                "Energy requirement: Requires abundant, low-cost renewable or nuclear power to run high-temperature Fischer-Tropsch synthesis."
            ],
            "mental_model": "Borrowing a book from the public library, reading it on the bus, and returning it to the exact same shelf. No new books are printed or destroyed.",
            "checkpoint": {
                "question": "Why is synthetic fuel made from Direct Air Capture considered carbon-neutral when burned in a jet engine?",
                "options": [
                    "The CO2 released during flight is the exact same carbon previously captured out of the atmosphere, adding zero net carbon to the sky",
                    "The fuel emits pure oxygen instead of exhaust",
                    "Jet engines destroy carbon atoms completely",
                    "Synthetic fuel freezes the atmosphere into solid dry ice"
                ],
                "correct_index": 0,
                "explanation": "Because the raw carbon feedstock came from the air rather than an underground fossil reservoir, burning it recycles existing atmospheric carbon."
            }
        },
        {
            "slide_num": 10,
            "title": "Inside the Machine: Solid Sorbents & Chemical Contactors",
            "act": "Act 3: Artificial Trees: Direct Air Capture & The Carbon Economy",
            "continuity_bridge": "How does a DAC machine chemically grab a carbon molecule floating past a fan blade? Let's inspect the chemical contactor loop.",
            "eli15_takeaway": "Air passes through chemical sponge filters treated with basic amine compounds; the carbon sticks to the filter, and a flash of mild heat releases it as pure gas.",
            "key_facts": [
                "Two main chemical systems: Liquid solvent systems (potassium hydroxide / calcium carbonate loop) and solid porous sorbent filters (amine-functionalized resins).",
                "Regeneration cycle: Heating the saturated solid filter to ~100°C releases 99.9% pure CO2 gas and resets the chemical filter for the next cycle.",
                "Collector modularity: Arranged in stackable shipping container-sized modules that scale horizontally.",
                "Parasitic heat: Designing low-temperature desorption systems allows facilities to run on industrial waste heat."
            ],
            "mental_model": "A magnetic lint roller for pet hair. You roll it over a sweater to collect all the cat fur, tap a button to drop the fur into the trash, and roll again.",
            "checkpoint": {
                "question": "How do solid-sorbent Direct Air Capture systems release the captured CO2 from their chemical filters?",
                "options": [
                    "They apply mild heat (~100°C) to break the weak chemical bond, driving off pure CO2 gas and resetting the filter",
                    "They submerge the machines in liquid nitrogen",
                    "They smash the filters with hydraulic jackhammers",
                    "They shoot the filters into the sun"
                ],
                "correct_index": 0,
                "explanation": "Solid sorbents bind CO2 at ambient temperatures and release it when gently heated to roughly 100°C, resetting the filter for thousands of cycles."
            }
        },
        {
            "slide_num": 11,
            "title": "Where to Bury the Carbon: Sub-Seabed & Basalt Vaults",
            "act": "Act 3: Artificial Trees: Direct Air Capture & The Carbon Economy",
            "continuity_bridge": "Once captured, pure CO2 gas must go somewhere it can never escape. Where on Earth can you safely store billions of tons of gas for millions of years?",
            "eli15_takeaway": "Engineers pump liquid carbon dioxide kilometers beneath the earth into porous sandstone or volcanic basalt rock, where it permanently turns into solid stone.",
            "key_facts": [
                "Deep Saline Aquifers: Permeable sandstone layers kilometers underground sealed by impermeable caprock shale.",
                "Basalt Mineralization (CarbFix method): Dissolving CO2 in water and pumping it into basalt volcanic rock, where calcium and magnesium react to form solid limestone within 2 years.",
                "Sub-Seabed Storage: Offshore storage reservoirs beneath depleted marine oil and gas fields (e.g. North Sea).",
                "Permanence: Geochemical mineralization eliminates risk of gas leaks because the carbon becomes literal rock."
            ],
            "mental_model": "Pumping fizzy soda water deep into hot volcanic rocks. The minerals in the rock react with the fizz, turning it into solid calcium chalk that can never leak.",
            "checkpoint": {
                "question": "Why is in-situ basalt mineralization (like the CarbFix process) considered safer than simple gas cavity storage?",
                "options": [
                    "Dissolved CO2 chemically reacts with basalt minerals to permanently solidify into stable stone (limestone) within two years",
                    "Basalt rocks are magnetic and pull carbon from space",
                    "Basalt completely destroys the carbon atoms",
                    "Basalt is legally exempt from environmental regulations"
                ],
                "correct_index": 0,
                "explanation": "Mineralization turns carbon into solid carbonate rock. Once solidified into stone, it cannot migrate, leak, or escape back into the air."
            }
        },
        {
            "slide_num": 12,
            "title": "Scaling to Gigatonnes a Year: The Engineering Chasm",
            "act": "Act 3: Artificial Trees: Direct Air Capture & The Carbon Economy",
            "continuity_bridge": "We know how to capture carbon and we know where to bury it. Now comes the hard truth: we must scale from thousands of tons to billions of tons per year.",
            "eli15_takeaway": "Today's carbon capture plants remove a few thousand tons per year; reaching climate targets requires scaling this industry by a factor of one million into a gigaton-scale giant.",
            "key_facts": [
                "Current scale: Global operational DAC capacity is roughly 8,000 tonnes of CO2 per year across 18 pilot facilities.",
                "Required scale: Climate stabilization requires removing 5 to 10 billion tonnes (5–10 Gigatonnes) per year by 2050.",
                "Scale multiplier: The carbon management industry must grow by roughly 1,000,000x over 25 years.",
                "Infrastructure demands: Requires dedicated clean electricity grids, pipelines, compressors, and specialized chemical supply chains."
            ],
            "mental_model": "Building the world's first single wooden canoe versus operating the entire modern global container shipping fleet. The gap between today's pilots and required scale is immense.",
            "checkpoint": {
                "question": "By what factor must global carbon removal scale from today's pilot plants (~8,000 tonnes/yr) to meet climate stabilization targets (~5-10 Gt/yr)?",
                "options": [
                    "Roughly one million times (1,000,000x)",
                    "Two times (2x)",
                    "Ten times (10x)",
                    "It does not need to scale at all"
                ],
                "correct_index": 0,
                "explanation": "Moving from 8,000 tonnes to 8 billion tonnes represents an expansion of six orders of magnitude—one million-fold growth."
            }
        },
        {
            "slide_num": 13,
            "title": "Scuba-Gear Scrubbers: The BIG-Bicarbonate Breakthrough",
            "act": "Act 3: Artificial Trees: Direct Air Capture & The Carbon Economy",
            "continuity_bridge": "To jump that million-fold scaling gap, scientists are reinventing the basic chemistry using principles borrowed from scuba diver rebreathers.",
            "eli15_takeaway": "Using bis-iminoguanidine (BIG) compounds, scientists built scrubbers that grab carbon like scuba-diving gear, releasing the gas under gentle heat with half the energy.",
            "key_facts": [
                "Analogy: Operates like closed-circuit scuba rebreathers that scrub exhaled CO2 from breathing air.",
                "Chemistry: Bis-iminoguanidine (BIG) ligands bind carbon dioxide to precipitate insoluble solid bicarbonate salts.",
                "Desorption: Gentle heating releases pure CO2 into collection vessels while water vapor condenses in an ice-cooled U-tube.",
                "Advantage: Drastically slashes the high energy penalty of boiling traditional liquid amine solutions."
            ],
            "mental_model": "A scuba diver swimming underwater for hours without bubbles. A small canister of chemical crystals quietly scrubs their exhaled breath clean, recycling the air over and over.",
            "checkpoint": {
                "question": "What is the primary operational advantage of BIG-bicarbonate solid-state carbon scrubbing over traditional liquid solvents?",
                "options": [
                    "It releases captured CO2 at much lower regeneration temperatures, slashing the massive energy penalty of boiling liquid solutions",
                    "It produces drinkable orange soda during the reaction",
                    "It requires no chemical compounds whatsoever",
                    "It only functions inside deep volcanic craters"
                ],
                "correct_index": 0,
                "explanation": "Solid-state BIG scrubbers release carbon with mild heat, avoiding the massive energetic penalty of boiling millions of liters of water in liquid solvent systems."
            }
        },
        {
            "slide_num": 14,
            "title": "The Commercial Pioneers: Climeworks, Carbon Engineering & 18 Plants",
            "act": "Act 3: Artificial Trees: Direct Air Capture & The Carbon Economy",
            "continuity_bridge": "Who is actually operating these machines right now in the real world? Let's look at the operational commercial landscape today.",
            "eli15_takeaway": "The world's leading DAC companies operate 18 pilot plants capturing under 8,000 tons of CO2 a year—half buried underground, half sold for fizzy drinks and fuels.",
            "key_facts": [
                "Leading commercial players: Climeworks (Switzerland), Carbon Engineering (Canada), and Global Thermostat (USA).",
                "Operating footprint: 18 active plants worldwide ranging from 1 tonne/year to 4,000 tonnes/year (Climeworks Orca/Mammoth in Iceland).",
                "Total capture: Just under 8,000 tonnes of CO2 per year total across all plants.",
                "End fate: About 50% is sequestered permanently underground; the other 50% is sold for commercial uses (sparkling water, greenhouses, synthetic fuels).",
                "Context: 8,000 tonnes equals the annual exhaust emissions of roughly 870 gasoline cars."
            ],
            "mental_model": "Early aviation in 1903: The Wright brothers' first flight lasted 12 seconds and carried one person. Today's DAC plants are that 12-second flight—tiny, but proving the physics work.",
            "checkpoint": {
                "question": "How much total CO2 was captured annually by the world's 18 leading commercial DAC plants when the lecture was recorded?",
                "options": [
                    "Just under 8,000 tonnes per year (equivalent to the emissions of ~870 cars)",
                    "500 million tonnes per year",
                    "Zero tonnes",
                    "10 billion tonnes per year"
                ],
                "correct_index": 0,
                "explanation": "The combined capacity of the 18 active commercial pilot plants totaled just under 8,000 tonnes annually, roughly equal to the emissions of 870 cars."
            }
        },
        {
            "slide_num": 15,
            "title": "Air-to-Luxury Case Study: Aether Diamonds from Pollution",
            "act": "Act 3: Artificial Trees: Direct Air Capture & The Carbon Economy",
            "continuity_bridge": "If burying carbon underground costs money without immediate revenue, how can companies generate early profits? Enter luxury jewelry made from air pollution.",
            "eli15_takeaway": "Aether buys carbon captured from ambient air by Climeworks, turns it into methane, and grows certified vegan diamonds in solar-powered vacuum reactors; 1 carat removes 20 tons of carbon.",
            "key_facts": [
                "Feedstock: Atmospheric CO2 captured directly from outdoor air by Climeworks in Europe.",
                "Synthesis: CO2 is chemically reduced into high-purity methane ($CH_4$).",
                "Growth reactor: Chemical Vapor Deposition (CVD) heats gasses to extreme temperatures in near-vacuum to crystallize rough diamond material over several weeks.",
                "Global craftsmanship: Raw diamonds are shipped to Surat, India, for precision laser cutting and facet polishing, then sold in New York City.",
                "Impact: Powered by solar and nuclear energy; each 1-carat diamond removes the equivalent of 20 metric tons of carbon from the atmosphere."
            ],
            "mental_model": "Spinning straw into gold: You take invisible smoke from the sky, heat it in a clean microwave reactor, cut it in Surat, and put a sparkling engagement ring on someone's finger.",
            "checkpoint": {
                "question": "Where are Aether's air-captured rough diamonds cut and polished before being sold in New York luxury stores?",
                "options": [
                    "Surat, India",
                    "Antarctica",
                    "A coal mine in Australia",
                    "An underwater submarine in the Pacific"
                ],
                "correct_index": 0,
                "explanation": "Rough CVD diamond material grown from captured atmospheric methane is sent to Surat, India—the diamond cutting and polishing capital of the world."
            }
        },
        {
            "slide_num": 16,
            "title": "Industrial-Scale Burial: Project Net Zero Teesside (NZT)",
            "act": "Act 3: Artificial Trees: Direct Air Capture & The Carbon Economy",
            "continuity_bridge": "Growing luxury diamonds proves high-value circularity, but solving climate change requires massive heavy-industry decarbonization. Let's look at a real industrial hub.",
            "eli15_takeaway": "The Net Zero Teesside project gathers smokestack carbon from chemical factories in northeast England and pipes it kilometers under the North Sea seabed for zero emissions by 2030.",
            "key_facts": [
                "Location: Teesside, North East England.",
                "Goal: Decarbonize a dense cluster of carbon-intensive chemical, fertilizer, and power industries to net-zero by as early as 2030.",
                "Transport: Heavy-duty pipelines collect captured CO2 from multiple manufacturing sites across the industrial corridor.",
                "Storage: Injected into saline aquifers and depleted gas fields several kilometers beneath the offshore North Sea floor.",
                "Model: Shared multi-user carbon transport and storage infrastructure shared by multiple private companies."
            ],
            "mental_model": "A municipal sewer system for industrial carbon. Instead of every house having its own septic tank, all factories plug into a single shared underground pipeline.",
            "checkpoint": {
                "question": "Where does the Net Zero Teesside (NZT) project store captured industrial carbon emissions?",
                "options": [
                    "In deep offshore geological formations several kilometers beneath the North Sea",
                    "In plastic garbage bags piled in city parks",
                    "Ventilated into school playgrounds",
                    "Pumped into local residential drinking water reservoirs"
                ],
                "correct_index": 0,
                "explanation": "NZT transports captured industrial emissions via offshore pipeline networks to seal them kilometers below the North Sea seabed."
            }
        },
        {
            "slide_num": 17,
            "title": "The Food Engine: Why Beef Dominates Agricultural Emissions",
            "act": "Act 4: Fixing the Agricultural Engine: Cows, Insects & Vertical Towers",
            "continuity_bridge": "Heavy industry and power plants are half the puzzle. But the global food system produces 14.5% of all human greenhouse gases—and one animal dominates the damage.",
            "eli15_takeaway": "Livestock generates 7.1 billion tonnes of emissions each year (14.5% of humanity's total); producing a single kilogram of beef belches 60 kg of greenhouse gas—twice as much as lamb.",
            "key_facts": [
                "Global footprint: Meat and dairy production creates 7.1 gigatons of GHG annually (~14.5% of total man-made emissions).",
                "Beef disparity: Generating 1 kg of beef produces 60 kg of GHG emissions—more than double the next highest meat (lamb).",
                "Deforestation driver: Clearing tropical forests for cattle ranching and soy animal feed destroys critical terrestrial carbon sinks.",
                "Monitoring tool: The TRASE platform (Stockholm Environment Institute & Global Canopy) maps supply chains linking commodity deforestation directly to global buyers."
            ],
            "mental_model": "Driving a massive diesel semi-truck across the country just to deliver a single pizza. Beef is the most resource-inefficient machine in the human food chain.",
            "checkpoint": {
                "question": "According to the lecture, how many kilograms of greenhouse gas emissions are generated per kilogram of beef produced?",
                "options": [
                    "60 kilograms of GHG emissions per kg of beef",
                    "1 kilogram of GHG emissions",
                    "0.05 kilograms of GHG emissions",
                    "10,000 kilograms of GHG emissions"
                ],
                "correct_index": 0,
                "explanation": "Beef generates roughly 60 kg of GHG per kg of meat—more than twice as high as lamb and vastly higher than poultry, pork, or plant proteins."
            }
        },
        {
            "slide_num": 18,
            "title": "Hacking the Cow: Red Seaweed Feed & Catalytic Burp Halters",
            "act": "Act 4: Fixing the Agricultural Engine: Cows, Insects & Vertical Towers",
            "continuity_bridge": "Since billions of people still eat beef, how can technology stop cows from burping methane while they chew grass?",
            "eli15_takeaway": "Sprinkling a pinch of tropical red seaweed into cow feed slashes burp methane by 80%, while British engineers designed wearable cattle halters that burn methane on the fly.",
            "key_facts": [
                "Red Seaweed (*Asparagopsis taxiformis*): A tropical seaweed containing bromoform; adding a tiny pinch (under 1%) to cattle feed cuts enteric methane emissions by up to 80%.",
                "Scaling bottleneck: Supplying feed for 1.5 billion cattle worldwide requires massive offshore seaweed aquaculture farms.",
                "Wearable Catalytic Halters (Zelp, UK): A smart harness worn over a cow's nostrils that captures exhaled burp methane and catalytically oxidizes it into harmless water and CO2.",
                "Target: Attacks methane at the source before it escapes into the open atmosphere."
            ],
            "mental_model": "Putting a catalytic converter on a cow's face, or giving them a herbal mint that stops their stomach from producing gas bubbles.",
            "checkpoint": {
                "question": "How much can adding tropical red seaweed (Asparagopsis) to cattle feed reduce a cow's methane emissions?",
                "options": [
                    "By up to 80%",
                    "By 0%",
                    "By exactly 2%",
                    "It increases methane by 500%"
                ],
                "correct_index": 0,
                "explanation": "Bioactive compounds in red seaweed disrupt methanogenic archaea in the cow's rumen, reducing enteric methane emissions by up to 80%."
            }
        },
        {
            "slide_num": 19,
            "title": "Alternative Protein: Why Grasshoppers Outperform Cattle",
            "act": "Act 4: Fixing the Agricultural Engine: Cows, Insects & Vertical Towers",
            "continuity_bridge": "If fixing cow biology is difficult, what if we swap the animal entirely for something that needs almost no land, no water, and produces zero methane?",
            "eli15_takeaway": "Grasshopper and cricket protein burgers provide the same complete nutrition as beef while using 95% less land, tiny amounts of water, and emitting almost zero methane.",
            "key_facts": [
                "Resource efficiency: Insects convert feed into edible protein roughly 12 times more efficiently than cattle.",
                "Zero methane: Grasshoppers, crickets, and mealworms do not have ruminant digestive fermentation systems.",
                "Vertical rearing: Billions of insects can be farmed in stacked indoor trays inside a single warehouse without deforestation.",
                "Processing: Ground into neutral-tasting protein powder for burger patties, pasta, and protein bars."
            ],
            "mental_model": "A laptop vs a 1950s vacuum-tube computer. Both calculate math, but the laptop fits in your backpack and uses a fraction of the electricity.",
            "checkpoint": {
                "question": "What primary environmental advantage does insect farming have over traditional cattle ranching?",
                "options": [
                    "Insects require vastly less land and water, emit virtually no enteric methane, and convert feed to protein far more efficiently",
                    "Insects can be trained to drive tractors",
                    "Insects lay eggs made of pure gold",
                    "Insects breathe underwater without oxygen"
                ],
                "correct_index": 0,
                "explanation": "Insects are cold-blooded and lack ruminant stomachs, converting food into high-grade edible protein with a fraction of cattle's land, water, and methane footprint."
            }
        },
        {
            "slide_num": 20,
            "title": "Refreezing the Poles: Marine Cloud Brightening & Flettner Ships",
            "act": "Act 6: Space, AI Wildlife Defense & The XPRIZE Frontier",
            "continuity_bridge": "Even with clean farming and DAC, melting polar ice caps threaten runaway tipping points. Can geoengineering buy time by physically reflecting sunlight away from the Arctic?",
            "eli15_takeaway": "Unmanned wind-powered ships spray sea-salt mist into marine clouds to make them whiter and more reflective, bouncing sunlight back to space to protect polar ice.",
            "key_facts": [
                "Concept: Marine Cloud Brightening (MCB) proposed by John Latham and Stephen Salter.",
                "Mechanism: Wind-powered Flettner rotor ships spray microscopically atomized seawater into low marine stratocumulus clouds.",
                "Physics: Sea-salt crystals act as cloud condensation nuclei (CCN), creating billions of smaller water droplets that reflect far more sunlight (Twomey effect).",
                "Observation proof: Satellite images of 'ship tracks' show clouds brightening directly along commercial ocean shipping lanes.",
                "Triple dilemma: Scientific feasibility (can we do it?), ethical responsibility (should we do it?), and international governance (who decides the planet's thermostat?)."
            ],
            "mental_model": "Painting your house roof with ultra-reflective white paint on a scorching summer day. The white surface bounces sunlight away, keeping the attic cool without air conditioning.",
            "checkpoint": {
                "question": "What is the physical principle behind Marine Cloud Brightening for climate repair?",
                "options": [
                    "Spraying tiny sea-salt particles creates smaller, denser cloud droplets that reflect significantly more incoming solar radiation back into space",
                    "Spraying salt into the sea causes the water to boil instantly",
                    "Covering the Arctic ocean with giant black plastic sheets",
                    "Setting fire to offshore oil platforms to create smoke blankets"
                ],
                "correct_index": 0,
                "explanation": "Salt particles act as cloud condensation nuclei. Smaller, more numerous droplets dramatically increase cloud albedo, reflecting solar heat."
            }
        },
        {
            "slide_num": 21,
            "title": "Decarbonizing Mobility: Commute Elimination via Remote Work",
            "act": "Act 5: Clean Propulsion, Urban Heat & Decarbonized Work",
            "continuity_bridge": "Geoengineering addresses the atmosphere from above. But what about the cars driving on city streets below? What if the greenest ride is the ride you never take?",
            "eli15_takeaway": "Remote work eliminates daily vehicular commuting, cutting urban traffic congestion, fuel combustion, and office heating emissions with zero new hardware.",
            "key_facts": [
                "Transport wedge: Passenger vehicle transport accounts for a major slice of urban oil consumption and smog.",
                "Avoided energy: Working from home eliminates the physical energy burned transporting a 1,500 kg metal automobile to carry one 75 kg human to a desk.",
                "Urban co-benefits: Reduces highway gridlock, lowers tire-wear particulate pollution ($PM_{2.5}$), and avoids office building HVAC energy peaks.",
                "Trade-off: Must ensure residential home heating/cooling does not cancel out the transport savings."
            ],
            "mental_model": "Attending a meeting over a high-definition video call burns a few watts of fiber-optic electricity instead of exploding two gallons of gasoline in an engine.",
            "checkpoint": {
                "question": "How does remote work function as a climate technology solution?",
                "options": [
                    "By eliminating the substantial energy and fossil fuel burned during daily vehicular commuting",
                    "By replacing computers with stone tablets",
                    "By forcing employees to walk five miles every morning",
                    "By making highways illegal to build"
                ],
                "correct_index": 0,
                "explanation": "Eliminating daily vehicle trips removes the fuel consumption and tailpipe emissions required to physically move commuters back and forth."
            }
        },
        {
            "slide_num": 22,
            "title": "Sustainable IT: High-Efficiency Data Centers & Virtualization",
            "act": "Act 5: Clean Propulsion, Urban Heat & Decarbonized Work",
            "continuity_bridge": "As everyone works remotely over the internet, digital computation demand surges. That brings us to the carbon footprint of the cloud servers powering that internet.",
            "eli15_takeaway": "Consolidating software on virtual cloud servers and using direct liquid cooling cuts data center energy use so digital communication stays dramatically cleaner than physical travel.",
            "key_facts": [
                "Infrastructure shift: Moving computation from inefficient on-premise server closets to hyper-efficient centralized cloud facilities.",
                "Energy-efficient datacentres: Modern hyperscale facilities use intelligent load balancing and clean renewable energy.",
                "Server Virtualization: Consolidates dozens of underworked server boxes onto single high-utilization hardware blades.",
                "Cooling innovation: Shifting from massive air-chillers to free-air economizers, geothermal heat sinks, and direct-to-chip liquid cooling.",
                "Energy metrics: Drives Power Usage Effectiveness (PUE) down from legacy ~2.0 toward the ideal 1.1 mark."
            ],
            "mental_model": "Carpooling in a hybrid bus with 40 people instead of 40 separate people driving 40 half-empty SUVs to the exact same office.",
            "checkpoint": {
                "question": "Why is cloud virtualization more energy-efficient than traditional on-premise company server rooms?",
                "options": [
                    "It packs workloads onto fewer physical servers running at peak efficiency, avoiding the massive idle electricity waste of empty machines",
                    "Virtual servers do not require any electricity to run",
                    "It moves computers to the moon where cooling is free",
                    "It slows down computing speeds to zero"
                ],
                "correct_index": 0,
                "explanation": "Idle servers still consume over half their peak power. Virtualization consolidates tasks onto fewer physical machines running at optimal load."
            }
        },
        {
            "slide_num": 23,
            "title": "Clean Transport & Clean Power Innovations",
            "act": "Act 5: Clean Propulsion, Urban Heat & Decarbonized Work",
            "continuity_bridge": "For the physical goods that cannot be virtualized—like global cargo ships and aircraft—we need breakthrough zero-emission propulsion and creative urban cooling.",
            "eli15_takeaway": "Hydrogen cargo ships, electric airplanes, floating solar plants, tidal energy platforms, and urban tree corridors are cleaning the heaviest transport and power sectors.",
            "key_facts": [
                "Maritime shipping: Generates 2.5% of global CO2; developing green hydrogen and ammonia fuel-cell vessels to eliminate bunker fuel.",
                "Aviation: Responsible for ~2% of global emissions; developing battery-electric and hydrogen short-haul commercial aircraft.",
                "Floating Solar (South Korea): A 41 Megawatt floating solar farm on reservoir water saves valuable land and water cools the panels, boosting solar efficiency.",
                "Tidal Platforms (Canada): Harnessing predictable ocean tidal currents for continuous baseload power.",
                "Medellín Tree Corridors (Colombia): Planting 350,000+ trees across interconnected transit corridors cooled the city by 3°C, slashing air-conditioning demand."
            ],
            "mental_model": "Putting a shaded canopy of trees over a scorching parking lot. The shade naturally cools the cars, so nobody needs to blast the vehicle AC on full blast.",
            "checkpoint": {
                "question": "What notable cooling effect did Medellín, Colombia achieve by planting 350,000 trees across connected urban transit corridors?",
                "options": [
                    "It lowered citywide ambient urban temperatures by 3°C",
                    "It made it snow in the middle of summer",
                    "It caused all city rivers to dry up",
                    "It raised temperatures by 10°C"
                ],
                "correct_index": 0,
                "explanation": "Medellín's green corridors cooled the city by 3°C through shade and evapotranspiration, mitigating the urban heat island effect."
            }
        },
        {
            "slide_num": 24,
            "title": "Digital Earth: AI Wildlife Defense, Blockchain Tuna & GFW Drones",
            "act": "Act 6: Space, AI Wildlife Defense & The XPRIZE Frontier",
            "continuity_bridge": "Environmental laws are meaningless without enforcement. How do we catch illegal loggers in deep jungles and poachers in open oceans? With digital satellites and AI.",
            "eli15_takeaway": "Drones, satellite radar, blockchain commodity tracking, and AI image models like DolphinGemma protect wild tigers, stop illegal tuna fishing, and catch forest poachers.",
            "key_facts": [
                "Blockchain Commodity Tracking: Verifies legal supply chains, stopping pirate tuna vessels that disable GPS transponders.",
                "Global Forest Watch (WRI GFW): Combines daily satellite imagery, crowdsourcing, and autonomous drones to detect illegal logging in real-time.",
                "Thermal Anti-Poaching Cameras: Deployed across Kenya's national park savannas to spot night-time poachers crossing borders.",
                "AI Wildlife Recognition: Wild Me platform uses computer vision and LLM models (DolphinGemma) to track individual tigers, zebras, and marine mammals by unique coat patterns.",
                "Battle of technologies: Pitting high-tech digital monitoring tools against illegal wildlife traffickers."
            ],
            "mental_model": "A digital fingerprint scanner for nature. An AI recognizes an individual tiger's stripe pattern from a drone snapshot just like an airport passport scanner reads your face.",
            "checkpoint": {
                "question": "How does Global Forest Watch (GFW) detect illegal logging deep inside tropical rainforests?",
                "options": [
                    "By combining high-resolution satellite remote sensing, autonomous drone patrols, and crowdsourced alert networks",
                    "By sending physical paper letters to every tree in the forest",
                    "By installing landline telephone poles next to every river",
                    "By cutting down all the trees to inspect them in laboratories"
                ],
                "correct_index": 0,
                "explanation": "GFW monitors global forest loss in near real-time by fusing satellite radar, optical imagery, drone tracking, and ground alert verification."
            }
        },
        {
            "slide_num": 25,
            "title": "Controlled Environment Agriculture: Vertical Farming Foundations",
            "act": "Act 4: Fixing the Agricultural Engine: Cows, Insects & Vertical Towers",
            "continuity_bridge": "We explored how digital satellites monitor outdoor forests. Now we bring farming completely indoors into controlled, stacked, climate-proof towers.",
            "eli15_takeaway": "Vertical farming grows crops in vertically stacked indoor layers with computer-controlled temperature, LED lighting, and gas levels, producing huge yields in cramped city spaces.",
            "key_facts": [
                "Definition: Modern agricultural technology using Controlled Environment Agriculture (CEA) to grow crops indoors without outdoor soil or sunlight.",
                "Primary purpose: Drastically increase food yields per square meter of footprint in dense, urban, or cramped spaces.",
                "Climate insulation: Totally shielded from outdoor droughts, floods, hailstorms, and seasonal weather swings.",
                "Atmospheric optimization: Artificially controls indoor air temperature, relative humidity, LED light spectrum, and elevated CO2 levels to accelerate plant growth."
            ],
            "mental_model": "A high-rise apartment building for lettuce. Instead of spreading 10,000 plants across 10 acres of dirt, you stack them 30 shelves high inside a renovated city warehouse.",
            "checkpoint": {
                "question": "What is the primary objective of Controlled Environment Agriculture (CEA) and vertical farming?",
                "options": [
                    "Maximizing crop yields in compact indoor footprints by artificially controlling light, temperature, and nutrients year-round",
                    "Growing crops exclusively in outer space on the International Space Station",
                    "Replacing food crops with synthetic plastic replicas",
                    "Testing how plants survive without any water or carbon dioxide"
                ],
                "correct_index": 0,
                "explanation": "CEA stacks crops vertically indoors with optimized artificial lighting and climate control, producing high-density food independent of outdoor weather."
            }
        },
        {
            "slide_num": 26,
            "title": "The Four Essential Pillars of Vertical Farming",
            "act": "Act 4: Fixing the Agricultural Engine: Cows, Insects & Vertical Towers",
            "continuity_bridge": "What hardware and technology makes a vertical farm actually work without dying? Let's break down the four essential engineering systems.",
            "eli15_takeaway": "Vertical farms rely on four key pillars: vertical tower racks, tuned LED light recipes, soilless root systems (hydroponics/aeroponics), and closed-loop 95% water recycling.",
            "key_facts": [
                "1. Physical Arrangement: Crops are grown in tall modular tower structures that maximize cubic volume rather than flat floor area.",
                "2. Customized Lighting: Precision LED fixtures deliver specific red and blue wavelengths tailored to maximize photosynthetic absorption efficiency.",
                "3. Soilless Growth Mediums: Roots grow in nutrient water (Hydroponics), fine mist (Aeroponics), or fish-waste symbiosis (Aquaponics) using coconut coir or moss.",
                "4. Sustainability Metric: Closed-loop water recovery condenses evaporated plant moisture, slashing water consumption by up to 95%."
            ],
            "mental_model": "Four legs of a sturdy dining table. Remove the light recipe (LEDs), the towers fall; remove the water loop (aeroponics), the plants dry up.",
            "checkpoint": {
                "question": "Which soilless cultivation technique suspends plant roots in mid-air and sprays them with a micro-fine nutrient mist?",
                "options": [
                    "Aeroponics",
                    "Open-pit strip mining",
                    "Flood irrigation",
                    "Slash-and-burn farming"
                ],
                "correct_index": 0,
                "explanation": "Aeroponics suspends plant roots in enclosed chambers and sprays them with fine nutrient mist, maximizing oxygen delivery while saving 95% of water."
            }
        },
        {
            "slide_num": 27,
            "title": "Industrial Vertical Aeroponics: AeroFarms & The 95% Water Slash",
            "act": "Act 4: Fixing the Agricultural Engine: Cows, Insects & Vertical Towers",
            "continuity_bridge": "Does vertical farming work at commercial scale, or is it just an academic concept? Let's examine AeroFarms, the global industrial benchmark.",
            "eli15_takeaway": "AeroFarms grows leafy greens on reusable cloth made from recycled plastic bottles, misting roots with zero soil and 95% less water across commercial hubs worldwide.",
            "key_facts": [
                "Operational benchmark: AeroFarms operates massive commercial indoor aeroponic facilities globally.",
                "Technology: Seeds are sown on reusable cloth fabric spun from recycled post-consumer plastic bottles; roots dangle below in dark chambers.",
                "Resource efficiency: Aeroponic misting cuts freshwater consumption by 95% compared to conventional field agriculture.",
                "Zero pesticides: Completely sealed indoor environment eliminates synthetic pesticides and herbicides.",
                "Global footprint: Commercial facilities deployed across the United States, Europe, Singapore, South Korea, and the Middle East."
            ],
            "mental_model": "A hospital incubator for baby greens. Every drop of moisture is measured, misted, captured, and recycled, with zero dirt and zero chemicals.",
            "checkpoint": {
                "question": "How does AeroFarms achieve a 95% reduction in agricultural water consumption?",
                "options": [
                    "By misting roots with a precise closed-loop aeroponic spray system and recycling all evaporated plant humidity",
                    "By breeding mutant desert cactus plants that never consume water",
                    "By importing iceberg water from the Arctic on airplanes",
                    "By replacing water with liquid petroleum oil"
                ],
                "correct_index": 0,
                "explanation": "Closed-loop aeroponic misting delivers water directly to root hairs without soil runoff, condensing and recycling evaporated moisture."
            }
        },
        {
            "slide_num": 28,
            "title": "Agroecological Pest Defense: Marigold & Brassica Trap Cropping",
            "act": "Act 4: Fixing the Agricultural Engine: Cows, Insects & Vertical Towers",
            "continuity_bridge": "For crops that must still grow outdoors in soil, warming temperatures are causing pest swarms. Instead of spraying toxic neurotoxin chemicals, how can we use nature against itself?",
            "eli15_takeaway": "Farmers plant marigolds and mustard crops around their main fields; the companion plants lure bugs into a decoy trap or poison them naturally, saving the harvest without pesticides.",
            "key_facts": [
                "Climate trigger: Warmer temperatures and higher humidity expand insect ranges, multiplying destructive pest outbreaks.",
                "Marigold weapon: Marigold roots release alpha-terthienyl, which kills parasitic root-knot nematodes; their flowers emit volatile aromas that repel aphids and whiteflies.",
                "Trap Cropping Mechanism: Planting an attractive sacrificial plant border that lures pests away from the high-value commercial crop.",
                "Real-world proof: Italian farmers plant *Brassicaceae* borders to decoy flea beetles away from sugarbeets; Chinese farmers plant maize borders around cotton to trap whiteflies.",
                "Ecosystem outcome: Eliminates toxic synthetic pesticides while protecting pollinating wild bees."
            ],
            "mental_model": "A nightclub security team setting up velvet ropes and a decoy snack table outside the club entrance. The loud crowd swarms the free snack table and never touches the main lounge inside.",
            "checkpoint": {
                "question": "How do marigolds biologically protect agricultural fields when used in trap cropping and companion planting?",
                "options": [
                    "Their roots release compounds that suppress parasitic root-knot nematodes and their flowers emit natural chemicals that deter aphids and whiteflies",
                    "They physically swat pests with mechanical wooden clubs",
                    "They freeze the surrounding field with cold air blasts",
                    "They emit ultrasound radio frequencies that shatter insect shells"
                ],
                "correct_index": 0,
                "explanation": "Marigold root exudates kill root-knot nematodes, while volatile organic compounds in their foliage repel aphids and whiteflies, acting as a biological shield."
            }
        },
        {
            "slide_num": 29,
            "title": "The Moonshot Scaling Prize: The $100M Elon Musk XPRIZE",
            "act": "Act 6: Space, AI Wildlife Defense & The XPRIZE Frontier",
            "continuity_bridge": "We have traveled from biochar and ocean liming to Direct Air Capture, seaweed cows, and vertical towers. How do we turn these promising ideas into gigaton-scale reality? With massive prize incentives.",
            "eli15_takeaway": "The $100 Million XPRIZE for Carbon Removal, funded by Elon Musk, challenges global teams to extract 1,000 tons of carbon per year and prove a viable roadmap to 1 billion tons.",
            "key_facts": [
                "Competition: XPRIZE Carbon Removal, launched in 2021 with $100 million in prize funding from Elon Musk and the Musk Foundation.",
                "Operational requirement: Competitors must demonstrate a working solution that actively removes at least 1,000 tonnes of net CO2 per year.",
                "Scalability test: Teams must present a rigorously audited engineering roadmap proving how their solution can scale to 1 Gigaton (1 billion tonnes) per year by 2050.",
                "Technological neutrality: Open to all pathways—air capture, ocean carbon removal, enhanced rock weathering, biochar, and biomass burial.",
                "The ultimate goal: Catalyzing a self-sustaining gigaton-scale carbon removal industry to secure planetary climate stability."
            ],
            "mental_model": "The 1927 Orteig Prize that challenged Charles Lindbergh to fly non-stop from New York to Paris. A single prize transformed aviation from a daredevil hobby into a worldwide commercial industry.",
            "checkpoint": {
                "question": "What is the primary challenge posed by the $100M XPRIZE for Carbon Removal funded by Elon Musk?",
                "options": [
                    "Demonstrating an operational system that removes at least 1,000 tonnes of CO2 per year with an audited pathway to scale to 1 Gigaton per year",
                    "Building a passenger rocket that can travel to Mars in 24 hours",
                    "Creating a social media app with one billion active users",
                    "Drilling the deepest oil well in the Arctic ocean"
                ],
                "correct_index": 0,
                "explanation": "The XPRIZE demands working proof of at least 1,000 tonnes/year of carbon removal paired with a credible engineering pathway to gigaton scale."
            }
        }
    ]

    # Find and update Class 11 in database
    for c in data["classes"]:
        if c["class_id"] == 11:
            c["slides"] = slides_data
            c["title"] = "Class 11: Climate Change Technology Solutions (Complete 29-Slide Slidewise Deck)"
            c["summary"] = "A comprehensive 29-slide narrative journey from negative emission biological sponges and ocean liming to Direct Air Capture, Aether diamonds, cow seaweed, insect protein, vertical farms, and the $100M XPRIZE."
            break

    with open(db_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Successfully updated Class 11 with {len(slides_data)} detailed slidewise modules in {db_path}!")

if __name__ == "__main__":
    update_class11()
