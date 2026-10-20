# Detailed pedagogical and simulator content for each of the 12 EST lectures

LECTURE_DETAILS = {
    "01": {
        "intuition": {
            "title": "Planetary Vision 2070: Navigating the Anthropocene",
            "subtitle": "The Grand Transition from Resource Depletion to Earth System Equilibrium",
            "why": "Human industrial activity has become the dominant geological force altering Earth's biogeochemical cycles (the Anthropocene). To avoid catastrophic destabilization of Earth's climate and biosphere, India and the global community have formalized aggressive decarbonization roadmaps (India Net-Zero by 2070, Global by 2050). Understanding the planetary scale and the thermodynamic limits of growth is the starting foundation of Environmental Science & Technology.",
            "pillars": [
                {"title": "The IPAT Identity", "desc": "Environmental Impact $I = P \\times A \\times T$ (Population $\\times$ Affluence $\\times$ Technology). Decarbonization requires radical improvements in the Technology factor $T$ to decouple economic welfare from resource exhaustion.", "badge": "Core Theory"},
                {"title": "Planetary Boundaries", "desc": "Rockström et al. identified 9 planetary boundaries (Climate, Biosphere integrity, Biogeochemical flows, Land system change, Freshwater, Novel entities). Exceeding these thresholds triggers non-linear planetary regime shifts.", "badge": "Thresholds"},
                {"title": "Decarbonization Pillars", "desc": "1. Renewable electrification of power and transport. 2. Deep industrial decarbonization (green hydrogen, cement/steel CCUS). 3. Enhanced terrestrial and coastal carbon sinks.", "badge": "Roadmap"}
            ]
        },
        "theory": {
            "title": "Thermodynamics of Growth & Decarbonization Milestones",
            "content": """
            <p class="mb-3">At the 26th UN Climate Change Conference of the Parties (COP26) in Glasgow, Prime Minister Narendra Modi unveiled India's <strong>Panchamrit</strong> (Five Nectar Elements) commitment:</p>
            <ul class="list-disc pl-5 space-y-1 mb-4 text-emerald-200/90 text-sm">
              <li>Reach 500 GW non-fossil energy capacity by 2030.</li>
              <li>Meet 50% of energy requirements from renewable energy by 2030.</li>
              <li>Reduce projected total carbon emissions by 1 billion tonnes by 2030.</li>
              <li>Reduce carbon intensity of GDP by 45% over 2005 levels by 2030.</li>
              <li>Achieve the net-zero emissions target by <strong>2070</strong>.</li>
            </ul>
            <p>The mathematical decarbonization path is governed by the IPAT identity and carbon budgeting. Cumulative global $CO_2$ emissions between 1850 and 2019 reached $\\sim 2390\\,\\text{Gt } CO_2$. To retain a 50% probability of limiting warming to $1.5^\\circ\\text{C}$, the remaining carbon budget is under $500\\,\\text{Gt } CO_2$.</p>
            """
        },
        "math": {
            "title": "Mathematical Formulations & Emission Budgets",
            "formula": "I = P \\cdot A \\cdot T \\quad\\Longleftrightarrow\\quad CO_2 = \\text{Pop} \\times \\frac{\\text{GDP}}{\\text{Pop}} \\times \\frac{\\text{Energy}}{\\text{GDP}} \\times \\frac{CO_2}{\\text{Energy}}",
            "notes": "Known as the Kaya Identity in carbon economics: Carbon Intensity of Energy $\\left(\\frac{CO_2}{\\text{Energy}}\\right)$ must approach zero via clean tech, while Energy Intensity of GDP $\\left(\\frac{\\text{Energy}}{\\text{GDP}}\\right)$ decreases through thermodynamic efficiency.",
            "table_headers": ["Decarbonization Metric", "Baseline (2020)", "Target 2030", "Net-Zero Target (2070)"],
            "table_rows": [
                ["Renewable Capacity", "85 GW", "500 GW", "> 1,800 GW"],
                ["Emission Intensity of GDP", "Reference (100%)", "-45% vs 2005", "-95% (Hard-to-abate residual)"],
                ["Forest Carbon Sink", "2.5-3.0 Gt $CO_2e$", "+2.5-3.0 Gt $CO_2e$", "Permanently Maintained"],
                ["Green Hydrogen", "~ 0 MT", "5 MT/yr", "> 25 MT/yr"]
            ]
        },
        "simulator": "sim_01",
        "flashcards": [
            {"q": "What is the Kaya Identity?", "a": "A mathematical decomposition: $CO_2 = P \\times (\\text{GDP}/P) \\times (\\text{Energy}/\\text{GDP}) \\times (CO_2/\\text{Energy})$. It formalizes the four drivers of anthropogenic carbon emissions."},
            {"q": "What is the year of India's Net-Zero commitment declared at COP26?", "a": "Year 2070 (part of the Panchamrit pledge)."},
            {"q": "What are the Planetary Boundaries defined by Rockström et al.?", "a": "A set of 9 quantitative planetary safe-operating boundaries (including Climate Change, Biosphere Integrity, Nitrogen/Phosphorus flows, and Ocean Acidification) that delineate the Holocene-like stability zone."}
        ],
        "traps": [
            "⚠️ <strong>Trap:</strong> Confusing 'Net-Zero' with 'Absolute Zero Emissions'. Net-Zero permits residual emissions in hard-to-abate sectors (steel, cement, aviation) as long as they are balanced 1:1 by active carbon removal.",
            "⚠️ <strong>Trap:</strong> Assuming increasing population $P$ is the sole driver of environmental degradation. In the IPAT equation, per-capita affluence $A$ and carbon intensity $T$ frequently outweigh population growth in total footprint.",
            "⚠️ <strong>Exam Tip:</strong> Be ready to state all 5 Panchamrit targets from COP26, including the 500 GW renewable target and 2070 net-zero year."
        ],
        "quiz": [
            {
                "question": "Which of the following is NOT one of the five 'Panchamrit' commitments made by India at COP26?",
                "options": [
                    "Reach 500 GW non-fossil energy capacity by 2030",
                    "Complete phase-out of all coal thermal power plants by 2035",
                    "Reduce carbon intensity of GDP by 45% by 2030",
                    "Achieve net-zero carbon emissions by 2070"
                ],
                "correct": 1,
                "explanation": "India did not commit to completely shutting down all coal plants by 2035. Instead, the focus is on scaling renewables to 500 GW, reducing emission intensity, and achieving Net-Zero by 2070."
            },
            {
                "question": "In the Kaya Identity $CO_2 = P \\times (GDP/P) \\times (Energy/GDP) \\times (CO_2/Energy)$, what does the term $(Energy/GDP)$ represent?",
                "options": [
                    "Carbon intensity of energy",
                    "Energy intensity of the economy (energy efficiency)",
                    "Per capita energy consumption",
                    "Total primary energy supply"
                ],
                "correct": 1,
                "explanation": "Energy/GDP measures the energy intensity of economic output; lowering this term signifies higher macroeconomic energy efficiency."
            }
        ]
    },

    "02": {
        "intuition": {
            "title": "Earth Spheres & Global Thermodynamics",
            "subtitle": "Coupled Dynamic Systems, Solar Flux, and the Natural Greenhouse Blanket",
            "why": "The Earth is an open thermodynamic system with respect to energy (receiving solar radiation and radiating infrared heat) but closed with respect to matter. The interaction between the Atmosphere, Hydrosphere, Lithosphere, and Biosphere maintains the planetary surface in a stable, life-supporting thermal equilibrium. Understanding this radiation balance is essential for analyzing anthropogenic perturbations.",
            "pillars": [
                {"title": "Vertical Atmospheric Structure", "desc": "Troposphere (temperature decreases with altitude at standard environmental lapse rate $\\Gamma = 6.5^\\circ\\text{C/km}$), Stratosphere (inversion due to $O_3$ UV absorption), Mesosphere, and Thermosphere.", "badge": "Atmosphere"},
                {"title": "Planetary Radiation Budget", "desc": "Solar constant $S_0 = 1361\\,\\text{W/m}^2$. Effective incident flux is $S_0/4 = 340\\,\\text{W/m}^2$. Earth's albedo $\\alpha \\approx 0.30$ reflects $\\sim 100\\,\\text{W/m}^2$. The remaining $240\\,\\text{W/m}^2$ heats the surface and atmosphere.", "badge": "Radiation"},
                {"title": "Thermodynamic Greenhouse Effect", "desc": "Without atmosphere, Stefan-Boltzmann law dictates blackbody temperature $T_e = 255\\,\\text{K}$ ($-18^\\circ\\text{C}$). Greenhouse gases absorb outgoing infrared and re-radiate back down, raising surface temperature to a hospitable $T_s = 288\\,\\text{K}$ ($+15^\\circ\\text{C}$).", "badge": "Equilibrium"}
            ]
        },
        "theory": {
            "title": "Stefan-Boltzmann Equilibrium & Radiative Transfer",
            "content": """
            <p class="mb-3">The planetary energy equilibrium is governed by the conservation of radiant flux. The absorbed solar power must balance outgoing longwave radiation (OLR):</p>
            <div class="p-3 my-2 bg-[#06110d] border border-emerald-900/60 rounded text-center font-mono text-emerald-300">
              $$\\frac{S_0}{4}(1 - \\alpha) = \\sigma T_e^4$$
            </div>
            <p class="text-sm">Solving for effective emitting temperature $T_e$:</p>
            <div class="p-3 my-2 bg-[#06110d] border border-emerald-900/60 rounded text-center font-mono text-emerald-300">
              $$T_e = \\left[ \\frac{S_0 (1 - \\alpha)}{4\\sigma} \\right]^{1/4} = \\left[ \\frac{1361 \\times 0.70}{4 \\times 5.67 \\times 10^{-8}} \\right]^{1/4} \\approx 254.9\\,\\text{K} \\; (-18.2^\\circ\\text{C})$$
            </div>
            <p class="text-sm mt-3">In a single-layer isothermal atmospheric model with emissivity $\\epsilon$, the surface temperature is elevated to:</p>
            <div class="p-3 my-2 bg-[#06110d] border border-emerald-900/60 rounded text-center font-mono text-emerald-300">
              $$T_s = \\left( \\frac{2}{2 - \\epsilon} \\right)^{1/4} T_e$$
            </div>
            <p class="text-sm">For $\\epsilon \\approx 0.77$, $T_s \\approx 288\\,\\text{K}$ ($+15^\\circ\\text{C}$). The natural greenhouse effect accounts for $+33^\\circ\\text{C}$ of planetary warming.</p>
            """
        },
        "math": {
            "title": "Governing Thermodynamic Parameters",
            "formula": "T_s = \\left( \\frac{1}{1 - \\epsilon/2} \\right)^{1/4} \\cdot \\left[ \\frac{S_0(1-\\alpha)}{4\\sigma} \\right]^{1/4}",
            "notes": "Where $\\sigma = 5.670374 \\times 10^{-8}\\,\\text{W/m}^2\\text{K}^4$ is the Stefan-Boltzmann constant, $\\alpha$ is planetary albedo ($0.30$), and $\\epsilon$ is effective infrared emissivity of greenhouse gases.",
            "table_headers": ["Sphere", "Primary Constituents", "Scale / Characteristic Mass", "Key Environmental Role"],
            "table_rows": [
                ["Atmosphere", "$N_2 (78.08\\%), O_2 (20.95\\%), Ar (0.93\\%), CO_2 (0.042\\%)$", "$5.15 \\times 10^{18}\\,\\text{kg}$", "Radiation shield, thermal regulation, weather"],
                ["Hydrosphere", "Oceans ($97.5\\%$), Glaciers ($1.75\\%$), Groundwater ($0.75\\%$)", "$1.4 \\times 10^{21}\\,\\text{kg}$", "Huge thermal inertia ($C_p \\approx 4184\\,\\text{J/kg K}$), ocean conveyor"],
                ["Lithosphere", "Crust & Upper Mantle ($SiO_2, Al_2O_3, Fe, Ca$)", "$2.4 \\times 10^{22}\\,\\text{kg}$", "Nutrient reservoir, plate tectonics, geochemical carbon sink"],
                ["Biosphere", "Living organic matter (carbon mass $\\sim 550\\,\\text{Gt C}$)", "Global living biomass", "Biogeochemical flux catalyst, photosynthesis/respiration"]
            ]
        },
        "simulator": "sim_02",
        "flashcards": [
            {"q": "Why does temperature increase with altitude in the Stratosphere?", "a": "Due to the absorption of solar ultraviolet radiation by the ozone ($O_3$) layer via the Chapman mechanism ($O_2 + h\\nu \\to 2O$, $O + O_2 + M \\to O_3 + M$)."},
            {"q": "What is Earth's average planetary albedo?", "a": "Approximately $\\alpha = 0.30$ (30% of incoming solar radiation is reflected back to space by clouds, aerosols, and bright surfaces like ice)."},
            {"q": "What would Earth's surface temperature be without any natural greenhouse gases?", "a": "Approximately $255\\,\\text{K}$ ($-18^\\circ\\text{C}$), rendering Earth an entirely frozen ice ball."}
        ],
        "traps": [
            "⚠️ <strong>Trap:</strong> Confusing solar constant $S_0$ with average incident flux. Solar constant is measured perpendicular to beam ($1361\\,\\text{W/m}^2$), but Earth's surface area ($4\\pi R^2$) is 4 times its cross-sectional area ($\\pi R^2$), making average incident flux $S_0 / 4 \\approx 340\\,\\text{W/m}^2$.",
            "⚠️ <strong>Trap:</strong> Misidentifying the atmospheric window. The atmospheric window is in the thermal infrared spectrum ($8 - 12\\,\\mu\\text{m}$), where clear atmosphere absorbs little radiation, allowing heat to escape directly to space."
        ],
        "quiz": [
            {
                "question": "What is the primary physical reason for the negative environmental lapse rate (cooling with height) in the Troposphere?",
                "options": [
                    "Decreasing gravitational attraction on gas molecules",
                    "The Troposphere is heated primarily from below by the planetary surface and cools via adiabatic expansion as air rises",
                    "Ozone depletion occurring at the tropopause",
                    "Solar radiation only interacts with the mesosphere"
                ],
                "correct": 1,
                "explanation": "Solar shortwave radiation passes through the atmosphere and heats the ground; the ground then heats the troposphere from below via conduction, convection, and latent heat."
            },
            {
                "question": "If Earth's planetary albedo $\\alpha$ increased from 0.30 to 0.35 due to cloud seeding, what would happen to the effective emitting temperature $T_e$?",
                "options": [
                    "It would increase because more energy is absorbed",
                    "It would decrease because less solar energy is absorbed into the Earth system",
                    "It would remain strictly unchanged at 255 K",
                    "It would cause immediate stratospheric heating"
                ],
                "correct": 1,
                "explanation": "Higher albedo means less solar energy is absorbed ($1-\\alpha$ decreases), reducing total outgoing emission required for equilibrium and lowering $T_e$."
            }
        ]
    },

    "03": {
        "intuition": {
            "title": "Environmental Issues, Anthropogenic Pressures & Pollution",
            "subtitle": "Chemical Kinetics of Smog, Particulate Dynamics, and Aquatic Eutrophication",
            "why": "Modern industrial and urban activities discharge massive quantities of reactive chemicals into the air, water, and soil. Primary pollutants transform through atmospheric photochemistry into toxic secondary pollutants (e.g. tropospheric ozone and PAN), while aquatic waste loads collapse dissolved oxygen in rivers via microbiological oxygen demand. Mastering pollution mechanics enables targeted engineering interventions.",
            "pillars": [
                {"title": "Photochemical Smog Dynamics", "desc": "Formed by the reaction of volatile organic compounds (VOCs) and nitrogen oxides ($NO_x$) driven by solar ultraviolet photons ($h\\nu$), producing peroxyacetyl nitrate (PAN), ground-level ozone ($O_3$), and aldehydes.", "badge": "Air Pollution"},
                {"title": "Aerodynamic Particulate Mechanics", "desc": "$PM_{10}$ ($<10\\,\\mu\\text{m}$) deposits in upper respiratory airways, while $PM_{2.5}$ ($<2.5\\,\\mu\\text{m}$) penetrates deep into lung alveoli and the bloodstream, carrying polycyclic aromatic hydrocarbons (PAHs) and heavy metals.", "badge": "Particulates"},
                {"title": "DO Sag & Eutrophication", "desc": "Discharge of sewage and agricultural runoff (phosphates & nitrates) triggers algal blooms. Bacterial decomposition consumes dissolved oxygen (DO), creating hypoxic 'dead zones' modeled by the Streeter-Phelps equation.", "badge": "Water Quality"}
            ]
        },
        "theory": {
            "title": "Streeter-Phelps Dissolved Oxygen Sag Formulation",
            "content": """
            <p class="mb-3">When organic effluent with Biochemical Oxygen Demand ($L_0$) enters a river, oxygen deficit $D(t) = C_s - C(t)$ is governed by simultaneous deoxygenation (rate $k_1$) and atmospheric reaeration (rate $k_2$):</p>
            <div class="p-3 my-2 bg-[#06110d] border border-emerald-900/60 rounded text-center font-mono text-emerald-300">
              $$D(t) = \\frac{k_1 L_0}{k_2 - k_1} \\left( e^{-k_1 t} - e^{-k_2 t} \\right) + D_0 e^{-k_2 t}$$
            </div>
            <p class="text-sm">The critical point in downstream distance/time $t_c$ where dissolved oxygen reaches its absolute minimum (maximum deficit $D_c$) occurs when rate of deoxygenation exactly equals reaeration:</p>
            <div class="p-3 my-2 bg-[#06110d] border border-emerald-900/60 rounded text-center font-mono text-emerald-300">
              $$t_c = \\frac{1}{k_2 - k_1} \\ln \\left[ \\frac{k_2}{k_1} \\left( 1 - D_0 \\frac{k_2 - k_1}{k_1 L_0} \\right) \\right]$$
            </div>
            """
        },
        "math": {
            "title": "Key Environmental Pollution Formulas",
            "formula": "\\text{AQI Sub-index } I = \\frac{I_{hi} - I_{lo}}{BP_{hi} - BP_{lo}} (C_p - BP_{lo}) + I_{lo}",
            "notes": "Where $C_p$ is pollutant concentration, $BP_{hi}, BP_{lo}$ are breakpoint concentrations from regulatory standards (CPCB / EPA), and $I_{hi}, I_{lo}$ are corresponding AQI breakpoints.",
            "table_headers": ["Pollutant", "Origin / Source", "Threshold Standard (24h)", "Environmental / Health Impact"],
            "table_rows": [
                ["$PM_{2.5}$", "Combustion, vehicle exhaust, biomass burning", "$60\\,\\mu\\text{g/m}^3$ (CPCB) / $15$ (WHO)", "Cardiovascular diseases, lung carcinoma, reduced visibility"],
                ["$NO_x$ ($NO + NO_2$)", "High-temperature internal combustion engines", "$80\\,\\mu\\text{g/m}^3$ (CPCB)", "Acid rain precursor, photochemical smog catalyst, lung inflammation"],
                ["$SO_2$", "Coal-fired thermal plants, metal smelting", "$80\\,\\mu\\text{g/m}^3$ (CPCB)", "Sulfuric acid aerosols, building corrosion, respiratory bronchoconstriction"],
                ["Tropospheric $O_3$", "Secondary: $VOCs + NO_x + \\text{UV}$", "$100\\,\\mu\\text{g/m}^3$ (8h)", "Potent cellular oxidant, crop yield reduction, asthma exacerbation"]
            ]
        },
        "simulator": "sim_03",
        "flashcards": [
            {"q": "What is the difference between BOD and COD?", "a": "BOD (Biochemical Oxygen Demand) measures oxygen consumed by aerobic microorganisms decomposing biodegradable organics over 5 days at $20^\\circ\\text{C}$. COD (Chemical Oxygen Demand) measures total chemically oxidizable matter using a strong chemical oxidant ($K_2Cr_2O_7$ in acid). COD is always $\\ge$ BOD."},
            {"q": "What chemical conditions are required for Photochemical Smog formation?", "a": "1. High emissions of $NO_x$ and VOCs. 2. Strong sunlight (UV radiation). 3. Warm temperatures and stagnant air (thermal inversion)."},
            {"q": "What is cultural eutrophication?", "a": "Accelerated nutrient enrichment of water bodies (primarily phosphorus and nitrogen from fertilizers/sewage) leading to dense algal blooms, water deoxygenation, and aquatic ecosystem collapse."}
        ],
        "traps": [
            "⚠️ <strong>Trap:</strong> Assuming Ozone ($O_3$) is emitted directly from car tailpipes. Ground-level ozone is purely a secondary pollutant generated via sunlight-induced reactions between $NO_2$ and hydrocarbons.",
            "⚠️ <strong>Exam Trap:</strong> In the Streeter-Phelps oxygen sag curve, the minimum dissolved oxygen concentration is NOT at the point of discharge ($t=0$). It occurs downstream at the critical time $t_c$ where the rate of deoxygenation equals the rate of reaeration."
        ],
        "quiz": [
            {
                "question": "Which ratio of COD to BOD indicates a wastewater that is easily amenable to biological treatment?",
                "options": [
                    "COD / BOD > 10.0",
                    "COD / BOD < 2.0",
                    "COD / BOD = 0",
                    "BOD is always greater than COD"
                ],
                "correct": 1,
                "explanation": "A COD/BOD ratio below 2.0 indicates that a large fraction of the organic matter is readily biodegradable by microorganisms."
            },
            {
                "question": "In classical photochemical smog, what is the initial reaction that triggers the radical cascade?",
                "options": [
                    "$NO_2 + h\\nu (\\lambda < 420\\text{ nm}) \\to NO + O(^3P)$",
                    "$SO_2 + O_2 \\to SO_3$",
                    "$CO_2 + H_2O \\to H_2CO_3$",
                    "$CH_4 + O_2 \\to CO_2 + 2H_2O$"
                ],
                "correct": 0,
                "explanation": "Photolysis of nitrogen dioxide ($NO_2$) by near-UV sunlight yields nitric oxide and an atomic oxygen radical, which immediately combines with $O_2$ to form ozone."
            }
        ]
    },

    "04": {
        "intuition": {
            "title": "Remote Sensing & GIS in Environmental Technology",
            "subtitle": "Electromagnetic Spectral Signatures, Earth Observation Satellites, and Spatial Analysis",
            "why": "Ground-based environmental sampling is spatially sparse and logistically expensive. Remote Sensing (RS) and Geographic Information Systems (GIS) provide synoptic, multi-temporal, and multi-spectral observation of the Earth's surface. From tracking deforestation in the Western Ghats to mapping Urban Heat Islands (UHI) and water turbidity, satellite remote sensing is the primary quantitative monitoring tool of modern environmental engineering.",
            "pillars": [
                {"title": "Spectral Reflectance Curves", "desc": "Healthy vegetation displays a distinctive 'Red Edge': strong absorption in Blue & Red (chlorophyll pigments) and high reflectance in Near-Infrared (spongy mesophyll cellular scattering). Water absorbs strongly in NIR, while dry soil shows monotonic reflectance increase.", "badge": "Physics"},
                {"title": "Sensor Resolutions", "desc": "1. Spatial (pixel size, e.g. Sentinel-2: 10m, Landsat-8: 30m). 2. Spectral (band width & count). 3. Radiometric (bit depth, 12-bit / 16-bit). 4. Temporal (revisit cycle, Sentinel-2: 5 days).", "badge": "Sensors"},
                {"title": "Vegetation & Water Indices", "desc": "Normalized Difference Vegetation Index ($NDVI = \\frac{NIR - Red}{NIR + Red}$) normalizes illumination variations and correlates directly with photosynthetic biomass and leaf area index (LAI).", "badge": "Analytics"}
            ]
        },
        "theory": {
            "title": "Electromagnetic Radiation & Spectral Signature Mathematics",
            "content": """
            <p class="mb-3">Planck's law and Wien's Displacement Law govern electromagnetic emissions from environmental surfaces:</p>
            <div class="p-3 my-2 bg-[#06110d] border border-emerald-900/60 rounded text-center font-mono text-emerald-300">
              $$\\lambda_{\\max} = \\frac{b}{T} \\quad (b = 2897.8\\,\\mu\\text{m}\\cdot\\text{K})$$
            </div>
            <p class="text-sm">For the Sun ($T \\approx 5800\\,\\text{K}$), $\\lambda_{\\max} \\approx 0.5\\,\\mu\\text{m}$ (visible green-blue). For Earth ($T \\approx 288\\,\\text{K}$), $\\lambda_{\\max} \\approx 9.7\\,\\mu\\text{m}$ (thermal infrared).</p>
            <p class="text-sm mt-3">The False Color Composite (FCC) standard places Near-Infrared (NIR) into the Red display channel, Red into Green, and Green into Blue. Healthy dense vegetation consequently appears <strong>bright crimson red</strong> in standard FCC imagery.</p>
            """
        },
        "math": {
            "title": "Key Remote Sensing Indices",
            "formula": "NDVI = \\frac{\\rho_{\\text{NIR}} - \\rho_{\\text{Red}}}{\\rho_{\\text{NIR}} + \\rho_{\\text{Red}}}, \\quad NDWI = \\frac{\\rho_{\\text{Green}} - \\rho_{\\text{NIR}}}{\\rho_{\\text{Green}} + \\rho_{\\text{NIR}}}",
            "notes": "NDVI ranges from $-1.0$ to $+1.0$. Water bodies yield negative values ($-0.5$ to $0$), bare soil yields $0.1$ to $0.2$, and dense healthy forest canopies reach $0.7$ to $0.9$.",
            "table_headers": ["Band Name", "Wavelength ($\\mu m$)", "Primary Environmental Application", "Sensor Mapping (Landsat 8 / Sentinel-2)"],
            "table_rows": [
                ["Blue", "0.45 – 0.51", "Coastal water depth, bathymetry, smoke/haze mapping", "Band 2 (L8) / Band 2 (S2)"],
                ["Green", "0.53 – 0.59", "Vegetation vigor assessment, peak reflectance", "Band 3 (L8) / Band 3 (S2)"],
                ["Red", "0.64 – 0.67", "Chlorophyll absorption, plant stress detection", "Band 4 (L8) / Band 4 (S2)"],
                ["Near-Infrared (NIR)", "0.85 – 0.88", "Biomass volume, leaf canopy structure, water boundary demarcation", "Band 5 (L8) / Band 8 (S2)"],
                ["Shortwave IR (SWIR)", "1.57 – 1.65", "Soil moisture content, vegetation water stress, fire burn scars", "Band 6 (L8) / Band 11 (S2)"]
            ]
        },
        "simulator": "sim_04",
        "flashcards": [
            {"q": "Why does healthy vegetation appear bright red in a Standard False Color Composite (FCC)?", "a": "Because in standard FCC, the sensor's Near-Infrared (NIR) band is assigned to the monitor's Red display channel. Healthy leaves reflect 40-50% of NIR radiation due to spongy mesophyll scattering, producing intense red coloration."},
            {"q": "What is the physical significance of the 'Red Edge' in vegetation spectroscopy?", "a": "The sharp transition between strong chlorophyll absorption in the red band (~0.67 $\\mu$m) and intense cellular scattering in the NIR (~0.70-0.75 $\\mu$m). Its steepness correlates with leaf chlorophyll content and plant health."},
            {"q": "What is the formula for Normalized Difference Water Index (NDWI)?", "a": "$NDWI = \\frac{\\text{Green} - \\text{NIR}}{\\text{Green} + \\text{NIR}}$. It enhances open water bodies while suppressing soil and vegetation features."}
        ],
        "traps": [
            "⚠️ <strong>Trap:</strong> Confusing Spatial Resolution with Temporal Resolution. High spatial resolution (e.g. 0.5m WorldView) often comes with poor temporal revisit (weeks), whereas MODIS offers daily revisit at coarse 250m-1km spatial resolution.",
            "⚠️ <strong>Exam Trap:</strong> Thinking water has high NDVI. Water absorbs almost 100% of NIR radiation, making $\\rho_{\\text{NIR}} \\approx 0$, which results in a distinctly negative NDVI."
        ],
        "quiz": [
            {
                "question": "A pixel in a satellite image has a Red reflectance $\\rho_{\\text{Red}} = 0.05$ and a Near-Infrared reflectance $\\rho_{\\text{NIR}} = 0.45$. What is its NDVI, and what land cover does it represent?",
                "options": [
                    "NDVI = 0.80, representing dense healthy vegetation canopy",
                    "NDVI = 0.50, representing dry sandy soil",
                    "NDVI = -0.80, representing an ocean body",
                    "NDVI = 0.00, representing cloud shadow"
                ],
                "correct": 0,
                "explanation": "$NDVI = (0.45 - 0.05) / (0.45 + 0.05) = 0.40 / 0.50 = 0.80$. Values above 0.7 signify dense, active photosynthesizing vegetation."
            },
            {
                "question": "Which atmospheric window is exploited by satellite thermal sensors to measure Sea Surface Temperature (SST) and Land Surface Temperature (LST)?",
                "options": [
                    "0.4 to 0.7 $\\mu$m (Visible)",
                    "8.0 to 12.0 $\\mu$m (Thermal Infrared)",
                    "1.4 to 1.9 $\\mu$m (Water vapor absorption band)",
                    "0.1 to 0.3 $\\mu$m (Ultraviolet)"
                ],
                "correct": 1,
                "explanation": "The 8-12 $\\mu$m thermal infrared atmospheric window coincides with Earth's peak thermal emission and experiences minimal atmospheric attenuation."
            }
        ]
    }
}
print("Lecture details 1-4 loaded.")
