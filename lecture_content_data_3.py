# Detailed pedagogical and simulator content for Lectures 09-12

LECTURE_DETAILS_3 = {
    "09": {
        "intuition": {
            "title": "Carbon Sequestration & Terrestrial Sinks",
            "subtitle": "Biological Pumping, Soil Humification, Biochar, and Geological Mineralization",
            "why": "Reaching global and national net-zero targets requires both emissions abatement and active carbon removal. Terrestrial ecosystems currently absorb approximately 30% of anthropogenic $CO_2$ emissions. Maximizing biological sinks (afforestation, soil organic carbon enhancement, biochar addition) and engineered geological carbon capture and storage (CCS) provides the technical toolkit for net-negative emissions.",
            "pillars": [
                {"title": "Biological Terrestrial Sinks", "desc": "Photosynthetic assimilation: $6CO_2 + 6H_2O + h\\nu \\to C_6H_{12}O_6 + 6O_2$. Carbon is allocated to above-ground woody biomass, fine roots, and exudates into the rhizosphere.", "badge": "Biosphere"},
                {"title": "Soil Organic Carbon (SOC)", "desc": "Soils hold $>1500\\,\\text{Gt C}$, more than the atmosphere and vegetation combined. Humification converts labile organic matter into recalcitrant organo-mineral complexes with decadal-to-century permanence.", "badge": "Soil"},
                {"title": "Geological CCS & Mineralization", "desc": "Capturing $CO_2$ from flue gases, compressing into supercritical fluid ($P > 73.9\\,\\text{bar}, T > 31.1^\\circ\\text{C}$), and injecting into deep saline formations or basalt rocks where in-situ mineral carbonation locks it permanently as solid calcite ($CaCO_3$).", "badge": "Geology"}
            ]
        },
        "theory": {
            "title": "Thermodynamics of Mineral Carbonation & Geological Trapping",
            "content": """
            <p class="mb-3">In geological storage, four progressive trapping mechanisms ensure containment security over time:</p>
            <ol class="list-decimal pl-5 space-y-2 mb-4 text-emerald-200/90 text-sm">
              <li><strong>Structural & Stratigraphic Trapping:</strong> Physical capping beneath an impermeable caprock shale or clay layer (immediate security).</li>
              <li><strong>Residual Trapping:</strong> Capillary forces trap disconnected microscopic droplets of supercritical $CO_2$ in pore throats (decades).</li>
              <li><strong>Solubility Trapping:</strong> Supercritical $CO_2$ dissolves into formation brine ($CO_2 + H_2O \\leftrightarrow H_2CO_3$), increasing brine density and causing it to sink downward, eliminating buoyancy risk (centuries).</li>
              <li><strong>Mineral Trapping (Permanent):</strong> Dissolved carbonic acid reacts with divalent metal cations in basalt / ultramafic formations ($Ca^{2+}, Mg^{2+}, Fe^{2+}$) to precipitate solid carbonate minerals (e.g. the Carbfix process in Iceland):
                <br/>$$\\text{Basalt: } (Ca, Mg)SiO_3 + CO_2 \\longrightarrow (Ca, Mg)CO_3 \\downarrow + SiO_2$$
              </li>
            </ol>
            <p class="text-sm">Biochar produced via slow pyrolysis ($450-600^\\circ\\text{C}$) of biomass converts labile cellulose and lignin into condensed aromatic carbon rings with a mean residence time exceeding 500–1000 years.</p>
            """
        },
        "math": {
            "title": "Sequestration Flux & Permanence Mathematics",
            "formula": "C_{\\text{permanence}}(t) = C_0 \\cdot e^{-k_{\\text{decomp}} t}, \\quad \\Delta C_{\\text{geo}} = \\int_0^T \\dot{m}_{CO_2}(t)\\,dt",
            "notes": "Where $k_{\\text{decomp}}$ is the microbial decomposition rate constant. Labile soil carbon has half-life $t_{1/2} \\sim 1-5\\,\\text{years}$; biochar has $t_{1/2} > 500\\,\\text{years}$; mineralized calcite has permanence $> 100,000\\,\\text{years}$.",
            "table_headers": ["Sequestration Method", "Capture Cost ($/t $CO_2$)", "Global Potential (Gt $CO_2$/yr)", "Permanence / Residence Time"],
            "table_rows": [
                ["Afforestation & Reforestation", "$10 - $50", "1.5 – 3.5 Gt", "Decades to centuries (vulnerable to wildfires & pests)"],
                ["Soil Carbon Enhancement (SOC)", "$20 - $80", "1.0 – 2.0 Gt", "Decades (sensitive to tillage and soil temperature)"],
                ["Biochar Soil Amendment", "$50 - $150", "0.5 – 1.8 Gt", "Centuries to millennia (highly recalcitrant)"],
                ["Geological CCS (Saline Aquifers)", "$60 - $120", "2.0 – 5.0 Gt", "Thousands of years (>99% retained over 1000 yr)"],
                ["In-situ Basalt Mineralization", "$100 - $200", "Enormous capacity (>1000 Gt)", "Permanent (>100,000 yr, thermodynamically stable rock)"]
            ]
        },
        "simulator": "sim_09",
        "flashcards": [
            {"q": "What are the critical temperature and pressure conditions for supercritical $CO_2$?", "a": "Critical temperature $T_c = 31.1^\\circ\\text{C}$ and critical pressure $P_c = 73.9\\,\\text{bar}$ ($7.39\\,\\text{MPa}$). Under these reservoir conditions, $CO_2$ has gas-like diffusivity and liquid-like density."},
            {"q": "What is the mineral carbonation reaction between olivine and carbon dioxide?", "a": "$Mg_2SiO_4 + 2CO_2 \\longrightarrow 2MgCO_3 + SiO_2 + \\text{Heat}$. This exothermic reaction permanently binds $CO_2$ into magnesite stone."},
            {"q": "Why does dissolved $CO_2$ in brine enhance geological storage safety over time?", "a": "Because $CO_2$-saturated formation brine is approximately 1% denser than pristine brine. It naturally sinks toward the bottom of the geological reservoir rather than rising toward the surface."}
        ],
        "traps": [
            "⚠️ <strong>Trap:</strong> Assuming tree planting alone can permanently solve fossil fuel emissions. Biological terrestrial sinks can saturate, and stored forest carbon can be released back to the atmosphere via wildfires, drought, or logging.",
            "⚠️ <strong>Exam Tip:</strong> Be sure to distinguish between Point-Source CCS (capturing from high-concentration industrial smokestacks) and Direct Air Capture (capturing from ambient 420 ppm air)."
        ],
        "quiz": [
            {
                "question": "Which trapping mechanism provides the earliest physical containment immediately after injecting supercritical $CO_2$ into a deep aquifer?",
                "options": [
                    "Mineral precipitation into limestone",
                    "Structural and stratigraphic trapping beneath an impermeable caprock",
                    "Dissolution into groundwater",
                    "Adsorption onto clay minerals"
                ],
                "correct": 1,
                "explanation": "Structural trapping beneath low-permeability caprock (shale/mudstone) is the immediate primary barrier preventing buoyant upward migration."
            },
            {
                "question": "How does biochar application enhance soil agricultural resilience in addition to sequestering carbon?",
                "options": [
                    "It sterilizes the soil of all bacteria",
                    "Its high specific surface area and porosity increase soil Cation Exchange Capacity (CEC) and water retention",
                    "It turns the soil permanently acidic",
                    "It replaces the need for solar radiation"
                ],
                "correct": 1,
                "explanation": "The highly porous, functionalized aromatic structure of biochar boosts nutrient retention (CEC), enhances moisture capacity, and provides a microbial habitat."
            }
        ]
    },

    "10": {
        "intuition": {
            "title": "Clean Development Mechanism (CDM) & Ocean Sequestration",
            "subtitle": "Kyoto Flexible Instruments, Additionality Rubrics, and Oceanic Carbon Injection",
            "why": "The Clean Development Mechanism (Article 12 of the Kyoto Protocol) pioneered international market-based carbon finance, enabling Annex I developed nations to invest in emission-reduction projects in developing nations in exchange for Certified Emission Reductions (CERs). Concurrently, the ocean—Earth's largest active carbon pool—has been investigated for ocean iron fertilization and direct liquid $CO_2$ injection, raising complex ecological questions regarding ocean acidification and marine food web collapse.",
            "pillars": [
                {"title": "CDM & Certified Emission Reductions (CERs)", "desc": "1 CER = 1 metric ton of $CO_2$ equivalent reduced. Projects must prove strict 'Additionality': emissions with the project are lower than what would have occurred in the baseline scenario without carbon revenue.", "badge": "Carbon Finance"},
                {"title": "Ocean Carbon Pumps", "desc": "1. Solubility pump (cooling surface water absorbs $CO_2$ and sinks at poles). 2. Biological pump (phytoplankton photosynthesis and sinking particulate organic carbon POC / marine snow).", "badge": "Ocean Pumps"},
                {"title": "Deep Ocean Injection & Acidification", "desc": "Injecting liquid $CO_2$ at depths $>3000\\,\\text{m}$ (where liquid $CO_2$ is denser than seawater and forms clathrate hydrate lakes). Risks: significant localized pH drops, dissolution of calcareous plankton, and benthic toxicity.", "badge": "Ocean Engineering"}
            ]
        },
        "theory": {
            "title": "Carbon Chemistry & Ocean Acidification Reactions",
            "content": """
            <p class="mb-3">When gaseous or liquid $CO_2$ dissolves in seawater, it establishes a series of chemical equilibria:</p>
            <div class="p-3 my-2 bg-[#06110d] border border-emerald-900/60 rounded text-center font-mono text-emerald-300">
              $$CO_2\\text{(aq)} + H_2O \\rightleftharpoons H_2CO_3 \\rightleftharpoons H^+ + HCO_3^- \\rightleftharpoons 2H^+ + CO_3^{2-}$$
            </div>
            <p class="text-sm">The release of free hydrogen ions ($H^+$) consumes carbonate ions ($CO_3^{2-}$):</p>
            <div class="p-3 my-2 bg-[#06110d] border border-emerald-900/60 rounded text-center font-mono text-emerald-300">
              $$H^+ + CO_3^{2-} \\rightleftharpoons HCO_3^-$$
            </div>
            <p class="text-sm">This drives down the <strong>carbonate saturation state</strong> ($\\Omega$):</p>
            <div class="p-3 my-2 bg-[#06110d] border border-emerald-900/60 rounded text-center font-mono text-emerald-300">
              $$\\Omega = \\frac{[Ca^{2+}][CO_3^{2-}]}{K'_{sp}}$$
            </div>
            <p class="text-sm">When $\\Omega < 1.0$, water becomes undersaturated and corrosive to calcium carbonate shells of corals, pteropods, and coccolithophores.</p>
            """
        },
        "math": {
            "title": "CDM Baseline & Carbon Credit Formulas",
            "formula": "CERs = \\sum_t \\left( BE_t - PE_t - LE_t \\right), \\quad \\text{Additionality: } PE_t < BE_t",
            "notes": "Where $BE_t$ is baseline emissions, $PE_t$ is project emissions, and $LE_t$ is leakage emissions occurring outside the project boundary.",
            "table_headers": ["Mechanism / Concept", "Governing Protocol / Science", "Core Requirement", "Key Environmental Concern"],
            "table_rows": [
                ["Clean Development Mechanism (CDM)", "Kyoto Protocol Article 12", "Additionality proof & third-party DOE validation", "Gaming of baseline scenarios and non-permanent forestry credits"],
                ["Ocean Iron Fertilization", "Martin's Hypothesis (HNLC ocean zones)", "Stimulate diatom blooms via micro-nutrient Fe", "Toxic anoxia in deep water, $N_2O$ production, unverified carbon export"],
                ["Deep Ocean Liquid $CO_2$ Injection", "High-pressure physics ($>3000\\,\\text{m}$ depth)", "$CO_2$ hydrate lake formation (density $> 1028\\,\\text{kg/m}^3$)", "Extreme localized pH drop (pH < 6.5), mortality of benthic fauna"],
                ["Alkalinity Enhancement", "Accelerated olivine / lime weathering", "Shift bicarbonate equilibrium to lock carbon", "High energy mining footprint and potential trace heavy metal release ($Ni, Cr$)"]
            ]
        },
        "simulator": "sim_10",
        "flashcards": [
            {"q": "What is the Additionality Principle in CDM projects?", "a": "The requirement that a project's greenhouse gas reductions must be additional to any that would occur in the absence of the certified CDM project activity (i.e., not business-as-usual)."},
            {"q": "What are High-Nutrient, Low-Chlorophyll (HNLC) ocean regions?", "a": "Ocean areas (such as the Southern Ocean and subarctic Pacific) with abundant nitrate and phosphate but low phytoplankton productivity due to the lack of the limiting trace micronutrient Iron ($Fe$)."},
            {"q": "Why does liquid $CO_2$ sink only below ~3,000 meters in the ocean?", "a": "Because liquid $CO_2$ is more compressible than seawater. Above ~3,000 m it is buoyant and rises; below ~3,000 m (pressure $> 30\\,\\text{MPa}$), its density exceeds that of seawater, allowing it to sink."}
        ],
        "traps": [
            "⚠️ <strong>Trap:</strong> Confusing CDM with Joint Implementation (JI). CDM involves developed Annex I nations investing in <em>non-Annex I developing nations</em>. Joint Implementation involves developed nations investing in <em>other Annex I nations</em> (typically economies in transition).",
            "⚠️ <strong>Exam Tip:</strong> Be ready to write out the carbonate equilibrium equations showing that adding $CO_2$ decreases free carbonate ion $[CO_3^{2-}]$ concentration, harming calcifying marine organisms."
        ],
        "quiz": [
            {
                "question": "What is the numerical equivalence of one Certified Emission Reduction (CER) unit under the Kyoto Protocol?",
                "options": [
                    "1 metric ton of $CO_2$ equivalent reduced or sequestered",
                    "1,000 metric tons of pure methane",
                    "1 kilogram of sulfur hexafluoride",
                    "1 megawatt-hour of solar electricity"
                ],
                "correct": 0,
                "explanation": "By definition, 1 CER corresponds to exactly one metric ton of $CO_2$ equivalent ($1\\,\\text{t } CO_2e$) avoided or removed."
            },
            {
                "question": "What is the primary ecological risk associated with large-scale ocean iron fertilization?",
                "options": [
                    "Immediate freezing of the ocean surface",
                    "Deep-water oxygen depletion (hypoxia) during organic matter decay and potential release of powerful $N_2O$ gas",
                    "Massive loss of oceanic salinity",
                    "Accelerated solar ultraviolet penetration"
                ],
                "correct": 1,
                "explanation": "As massive stimulated blooms sink, heterotrophic bacteria consume dissolved oxygen to decompose the biomass, producing anoxic dead zones and generating nitrous oxide ($N_2O$, GWP=273)."
            }
        ]
    },

    "11": {
        "intuition": {
            "title": "Climate Change Technology Solutions & Clean Tech Innovations",
            "subtitle": "Direct Air Capture, Geoengineering, Green Hydrogen, and Circular Economy",
            "why": "Halting climate change requires an unprecedented deployment of scalable clean technologies. These encompass active carbon dioxide removal (Direct Air Capture and mineralization), zero-emission energy carriers (green hydrogen electrolysis), electrochemical grid storage, and potentially contentious solar radiation management (SRM). Evaluating the thermodynamic limits, energy penalties, and lifecycle footprints of these clean technologies is a core engineering imperative.",
            "pillars": [
                {"title": "Direct Air Capture (DAC)", "desc": "Removing $CO_2$ from ambient air ($0.042\\%$ concentration). Two dominant architectures: Solid sorbents (amine-functionalized filters regenerated at 100°C) and Liquid solvents (KOH and Calcium looping regenerated at 900°C).", "badge": "DAC"},
                {"title": "Green Hydrogen Ecosystem", "desc": "Electrolysis of water using 100% renewable electricity ($2H_2O \\to 2H_2 + O_2$). Replaces fossil coal and gas in hard-to-abate sectors like steelmaking, ammonia synthesis, and heavy transport.", "badge": "Hydrogen"},
                {"title": "Solar Radiation Management (SRM)", "desc": "Deliberate modification of Earth's shortwave radiation balance (e.g. Stratospheric Aerosol Injection of $SO_2$ particles to mimic volcanic cooling, or Marine Cloud Brightening via sea-salt aerosols).", "badge": "Geoengineering"}
            ]
        },
        "theory": {
            "title": "Thermodynamics of Direct Air Capture & Minimum Separation Work",
            "content": """
            <p class="mb-3">From the Second Law of Thermodynamics, the minimum reversible work ($W_{\\min}$) required to separate a gas from a mixture at ambient temperature $T_0$ is given by:</p>
            <div class="p-3 my-2 bg-[#06110d] border border-emerald-900/60 rounded text-center font-mono text-emerald-300">
              $$W_{\\min} = -R T_0 \\left[ \\ln y_{CO_2} + \\frac{1 - y_{CO_2}}{y_{CO_2}} \\ln(1 - y_{CO_2}) \\right]$$
            </div>
            <p class="text-sm">Because ambient $CO_2$ concentration is dilute ($y_{CO_2} \\approx 420\\,\\text{ppm} = 0.00042$), $W_{\\min} \\approx 20\\,\\text{kJ/mol } CO_2$ ($455\\,\\text{kJ/kg } CO_2 = 126\\,\\text{kWh/tonne } CO_2$).</p>
            <p class="text-sm mt-3">In real-world DAC systems, thermodynamic irreversibilities, fan pressure drops, and thermal regeneration heat require <strong>$1500 - 2500\\,\\text{kWh}$ of thermal energy</strong> plus <strong>$300 - 500\\,\\text{kWh}$ of electricity</strong> per tonne of $CO_2$ captured. Consequently, DAC must be powered strictly by zero-carbon surplus renewable or waste thermal energy to avoid net-positive emissions.</p>
            """
        },
        "math": {
            "title": "Clean Tech Metrics & Energy Efficiencies",
            "formula": "\\eta_{\\text{electrolyzer}} = \\frac{\\text{HHV of } H_2}{\\text{Electricity Input}} \\approx 65\\% - 80\\%, \\quad \\text{HHV} = 141.8\\,\\text{MJ/kg } H_2",
            "notes": "Where HHV is the Higher Heating Value of hydrogen. A modern PEM electrolyzer requires $\\sim 50 - 55\\,\\text{kWh}$ of renewable electricity to generate $1\\,\\text{kg}$ of green hydrogen.",
            "table_headers": ["Technology", "TRL (Technology Readiness Level)", "Levelized Cost", "Primary Engineering Bottleneck"],
            "table_rows": [
                ["Direct Air Capture (Solid Sorbent)", "TRL 7 – 8 (Climeworks Orca/Mammoth)", "$400 - $600 / t $CO_2$", "Huge thermal desorption energy and sorbent degradation"],
                ["Green Hydrogen (PEM Electrolysis)", "TRL 8 – 9", "$4 - $6 / kg $H_2$ (targeting $1-2)", "Iridium and Platinum catalyst scarcity, electricity tariffs"],
                ["Stratospheric Aerosol Injection (SRM)", "TRL 3 – 4", "Low economic cost (~$10-20B/yr)", "Ozone depletion, monsoon rainfall termination shock, moral hazard"],
                ["Carbon Capture & Utilization (CCU)", "TRL 6 – 8", "Varies by end product", "High thermodynamic reduction energy needed to turn $CO_2$ into hydrocarbons"]
            ]
        },
        "simulator": "sim_11",
        "flashcards": [
            {"q": "What is the 'Termination Shock' risk of Solar Radiation Management (SRM)?", "a": "If stratospheric aerosol injection is suddenly halted (due to war, geopolitical conflict, or technical failure), the accumulated greenhouse gases would trigger rapid, catastrophic catch-up warming at unprecedented rates."},
            {"q": "What distinguishes Green, Grey, and Blue Hydrogen?", "a": "Grey: Produced from methane via Steam Methane Reforming (SMR) with fossil emissions ($CO_2$ vented). Blue: SMR with Carbon Capture and Storage. Green: Electrolysis of water using 100% renewable electricity with zero emissions."},
            {"q": "Why does Direct Air Capture require substantially more energy than flue gas capture?", "a": "Flue gas contains 12-15% $CO_2$ (coal) or 4-8% (gas), whereas ambient air contains only 0.042% $CO_2$ (~300 times more dilute). The thermodynamic minimum separation work scales logarithmically with dilution."}
        ],
        "traps": [
            "⚠️ <strong>Trap:</strong> Confusing Carbon Capture and Storage (CCS) with Direct Air Capture (DAC). CCS captures $CO_2$ from concentrated industrial emissions before it enters the atmosphere; DAC removes $CO_2$ that is already dispersed in ambient air.",
            "⚠️ <strong>Exam Tip:</strong> Be sure to emphasize that Solar Radiation Management (SRM) does NOT solve ocean acidification, because it only masks planetary temperature without reducing atmospheric $CO_2$ concentrations."
        ],
        "quiz": [
            {
                "question": "Which geoengineering technique cools the planet without addressing the root chemical cause of Ocean Acidification?",
                "options": [
                    "Direct Air Capture with mineral storage",
                    "Stratospheric Aerosol Injection (SAI) of sulfur dioxide",
                    "Afforestation and reforestation",
                    "Enhanced silicate rock weathering"
                ],
                "correct": 1,
                "explanation": "Stratospheric Aerosol Injection reflects sunlight to lower temperatures, but leaves atmospheric $CO_2$ levels unabated, allowing ocean acidification to proceed unchecked."
            },
            {
                "question": "What is the primary thermodynamic reason why Direct Air Capture requires such enormous airflow volumes?",
                "options": [
                    "Ambient air is 99.96% non-$CO_2$ gases ($N_2, O_2, Ar$), requiring millions of cubic meters of air to capture a single ton of $CO_2$",
                    "$CO_2$ is heavier than air and only settles on the ground",
                    "Oxygen reacts explosively with sorbents",
                    "Air must be heated to 2000°C before contact"
                ],
                "correct": 0,
                "explanation": "At 420 ppm, 1 ton of $CO_2$ is distributed across roughly 1.8 to 2.0 million cubic meters of air, requiring massive fans and contactor areas."
            }
        ]
    },

    "12": {
        "intuition": {
            "title": "Environmental Impact Assessment (EIA): Framework & Protocols",
            "subtitle": "Screening, Scoping, Leopold Matrices, Public Hearings, and Environmental Clearance",
            "why": "Environmental Impact Assessment (EIA) is the formal statutory planning tool used to identify, predict, and evaluate the environmental consequences of proposed developmental projects prior to major decision-making. In India, EIA is legally mandated under the Environment (Protection) Act, 1986 and governed by the EIA Notification 2006. Mastering the 8-stage EIA lifecycle and quantitative matrices is mandatory for environmental engineering professionals.",
            "pillars": [
                {"title": "The 8-Stage EIA Lifecycle", "desc": "1. Screening. 2. Scoping (TOR). 3. Baseline Data Collection. 4. Impact Prediction. 5. Mitigation & EMP. 6. Public Hearing. 7. Appraisal (EAC/SEAC). 8. Post-Project Compliance Monitoring.", "badge": "Lifecycle"},
                {"title": "Categorization (Category A vs B)", "desc": "Category A projects (national scale, river valley, nuclear, large thermal plants) evaluated at central MoEFCC level. Category B projects evaluated at state level (SEIAA) and subdivided into B1 (mandatory EIA) and B2 (EIA exempt).", "badge": "Jurisdiction"},
                {"title": "The Leopold Interaction Matrix", "desc": "A two-dimensional matrix crossing 100 developmental project actions along the horizontal axis with 88 environmental characteristics along the vertical axis. Each cell receives a score for Magnitude ($1-10$) and Importance ($1-10$).", "badge": "Methodology"}
            ]
        },
        "theory": {
            "title": "Leopold Matrix & Batelle Environmental Evaluation System",
            "content": """
            <p class="mb-3">The <strong>Leopold Matrix</strong> (1971) uses a double-score format in each interaction cell:</p>
            <div class="p-3 my-2 bg-[#06110d] border border-emerald-900/60 rounded text-center font-mono text-emerald-300">
              $$\\text{Cell Score} = \\frac{\\text{Magnitude } (M)}{\\text{Importance } (I)} \\quad (M \\in [-10, +10], \\; I \\in [1, 10])$$
            </div>
            <p class="text-sm"><strong>Magnitude ($M$)</strong> represents the physical scale, degree, or extensiveness of the impact (positive for beneficial, negative for adverse). <strong>Importance ($I$)</strong> represents the social, ecological, and policy significance of that impact.</p>
            <p class="text-sm mt-3">The <strong>Batelle Environmental Evaluation System (BEES)</strong> provides a hierarchical quantitative metric across 78 environmental parameters. Each parameter $i$ is assigned a Parameter Importance Unit ($PIU_i$, where $\\sum PIU_i = 1000$). The Environmental Impact ($EI$) is computed as:</p>
            <div class="p-3 my-2 bg-[#06110d] border border-emerald-900/60 rounded text-center font-mono text-emerald-300">
              $$EI = \\sum_{i=1}^{78} PIU_i \\times \\left( EQ_{i, \\text{with}} - EQ_{i, \\text{without}} \\right)$$
            </div>
            <p class="text-sm">Where $EQ_i \\in [0, 1]$ is the Environmental Quality index derived from value functions.</p>
            """
        },
        "math": {
            "title": "Environmental Management Plan (EMP) Architecture",
            "formula": "EI = \\sum_{i=1}^n PIU_i \\cdot \\Delta EQ_i, \\quad \\sum_{i=1}^{78} PIU_i = 1000",
            "notes": "An Environmental Management Plan (EMP) must specify for every identified negative impact: mitigation measures, monitoring parameter, frequency of sampling, institutional responsibility, and capital/recurring cost allocation.",
            "table_headers": ["EIA Stage", "Key Activities Involved", "Responsible Entity", "Statutory Outcome"],
            "table_rows": [
                ["1. Screening", "Determine whether project requires EIA based on investment and threshold criteria", "SEIAA / MoEFCC", "Classification into Category A, B1, or B2"],
                ["2. Scoping", "Determine spatial and temporal boundaries and formulate Terms of Reference (TOR)", "Expert Appraisal Committee (EAC)", "Approved Terms of Reference (TOR)"],
                ["3. Baseline Study", "Collect 1 full season (non-monsoon) air, water, soil, noise, biodiversity data", "Accredited EIA Consultant (NABET)", "Baseline Environmental Status Report"],
                ["4. Public Consultation", "Notice published in national & local language newspapers; public hearing", "State Pollution Control Board (SPCB)", "Recorded Public Hearing Proceedings & Video"],
                ["5. Appraisal", "Detailed scrutiny of final EIA and public concerns by expert committee", "EAC / SEAC", "Grant or Rejection of Environmental Clearance (EC)"]
            ]
        },
        "simulator": "sim_12",
        "flashcards": [
            {"q": "What is the primary difference between Category A and Category B projects under the Indian EIA Notification 2006?", "a": "Category A projects require mandatory EIA and clearance at the Central Government level (MoEFCC). Category B projects are appraised at the State level (SEIAA); Category B1 requires EIA, while Category B2 is exempt from EIA."},
            {"q": "What two numbers are assigned to each interacting cell in a Leopold Matrix?", "a": "Magnitude (from 1 to 10, often with +/- sign, measuring the physical scale of impact) and Importance (from 1 to 10, measuring the ecological or social weight)."},
            {"q": "How long must baseline environmental data be collected for a standard EIA in India?", "a": "One full season (three months), excluding the monsoon season (which dilutes pollutants and skews ecological baselines)."}
        ],
        "traps": [
            "⚠️ <strong>Trap:</strong> Confusing Scoping with Screening. Screening asks: <em>'Does this project need an EIA?'</em> Scoping asks: <em>'What specific environmental topics and boundaries must the EIA investigate?'</em>",
            "⚠️ <strong>Exam Tip:</strong> Remember that Public Consultation consists of two components: 1. A public hearing at the site for locally affected persons. 2. Obtaining written responses from other concerned stakeholders."
        ],
        "quiz": [
            {
                "question": "Which of the following projects is strictly categorized as a Category 'A' project requiring Central MoEFCC appraisal in India?",
                "options": [
                    "Nuclear power projects and associated fuel processing facilities",
                    "Small building construction projects < 20,000 sq. meters",
                    "Isolated brick kilns",
                    "Minor mineral mining in areas < 5 hectares"
                ],
                "correct": 0,
                "explanation": "Nuclear power projects, large ports, major river valley projects, and petroleum refineries are strictly Category A projects requiring central Expert Appraisal Committee scrutiny."
            },
            {
                "question": "In the Batelle Environmental Evaluation System (BEES), what is the total sum of Parameter Importance Units (PIU) across all 78 parameters?",
                "options": [
                    "100 units",
                    "500 units",
                    "1,000 units",
                    "10,000 units"
                ],
                "correct": 2,
                "explanation": "The Batelle system apportions a total fixed budget of 1,000 Parameter Importance Units among the 78 environmental indicators."
            }
        ]
    }
}
print("Lecture details 9-12 loaded.")
