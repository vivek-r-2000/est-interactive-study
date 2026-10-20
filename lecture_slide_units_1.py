# Slide Learning Units for Lectures 01 - 04
# Contains structured slide groups, exact slide mappings, and deep pedagogical notes

UNITS_LEC_01 = [
    {
        "unit_id": "u01_1",
        "title": "Course Scope & The 'Earth Without People' Thought Experiment",
        "slide_range": "Slides 01–03",
        "slides_idx": [1, 2, 3],
        "takeaway": "Establishes Environmental Science as an interdisciplinary technology domain combining spatial informatics, ecological modeling, and systems thinking.",
        "synthesis": """
        <div class="space-y-3">
          <p><strong>1. Interdisciplinary Foundations:</strong> Dr. P. Rama Chandra Prasad introduces Environmental Science at IIIT Hyderabad not as passive nature study, but as a rigorous technological discipline. The course curriculum unites three foundational pillars: (a) Fundamental Earth system dynamics and biogeochemical equilibrium, (b) Critical anthropogenic pressures and industrial externalities, and (c) Information Technology (IT) solutions including spatial informatics, remote sensing, and machine learning.</p>
          <p><strong>2. The 'Earth Without People' Thought Experiment (Slide 3):</strong> Students are challenged to envision Earth devoid of human civilization. This thought experiment isolates the baseline carrying capacity and regenerative velocity of natural biogeochemical cycles (carbon, nitrogen, water) from anthropogenic disturbances. When human pressures are removed, ecological succession rapidly reclaims built environments, and atmospheric trace gases settle to pre-industrial equilibrium ($~280\\,\\text{ppm } CO_2$).</p>
        </div>
        """,
        "math_formula": "I = P \\cdot A \\cdot T \\quad\\text{(Baseline Anthropogenic Forcing)}",
        "exam_checkpoint": "Distinguish between pure ecological science and environmental technology. Be prepared to explain how spatial informatics and data analytics decouple economic activity from environmental degradation."
    },
    {
        "unit_id": "u01_2",
        "title": "The 10 Landmark Global Environmental Campaigns",
        "slide_range": "Slides 04–13",
        "slides_idx": [4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
        "takeaway": "Analyzes how global NGOs use visual rhetoric and cognitive framing to communicate complex ecological crises to society.",
        "synthesis": """
        <div class="space-y-3">
          <p><strong>Visual Rhetoric in Environmental Action:</strong> Slides 4 through 13 showcase 10 of the most impactful public environmental advertising campaigns in modern history. These campaigns demonstrate how non-governmental organizations translate abstract ecological data into immediate cognitive resonance:</p>
          <ul class="list-disc pl-5 space-y-1.5 text-slate-300">
            <li><strong>UNICEF Clean Drinking Water Campaign (Slide 4):</strong> Highlights global disparities in access to potable water; millions of children lack potable groundwater free of pathogenic contamination.</li>
            <li><strong>IFAW Save the Elephant (Slide 5):</strong> Addresses ivory poaching, keystone species loss, and trophic cascade destabilization in African savannahs.</li>
            <li><strong>Greenpeace 'The Greatest Wonder of the Sea' (Slide 6):</strong> Depicts coral bleaching on the Great Barrier Reef driven by ocean warming and acidification ($\Delta pH \approx -0.1$ since 1850).</li>
            <li><strong>Ecoeduca & Friends of the Earth Climate Campaigns (Slides 7, 11):</strong> Uses visual metaphors of melting icecaps and sea-level inundation to convey the non-linearity of climate impacts.</li>
            <li><strong>WWF 'Preserve Your World', 'Rubbish' & 'Stop Climate Change' (Slides 8, 12, 13):</strong> Confronts municipal solid waste accumulation, plastic persistence in marine food chains, and irreversible biome shifts.</li>
          </ul>
        </div>
        """,
        "math_formula": "\\Delta pH = -\\log_{10}\\left(\\frac{[H^+]_{present}}{[H^+]_{pre-ind}}\\right) \\approx -0.1 \\implies 30\\% \\text{ increase in } [H^+]",
        "exam_checkpoint": "Professors frequently test the concept of 'Framing in Environmental Communication'. Understand why visual metaphors like coral bleaching and melting icecaps serve as proxy indicators of broader planetary boundary transgressions."
    },
    {
        "unit_id": "u01_3",
        "title": "Environmental Media, Public Perception & Advertising Dynamics",
        "slide_range": "Slides 14–30",
        "slides_idx": [14, 15, 18, 22, 26, 30],
        "takeaway": "Examines the role of mass media, eco-labeling, and corporate greenwashing in shaping public environmental consciousness.",
        "synthesis": """
        <div class="space-y-3">
          <p><strong>1. Societal Environmental Awareness:</strong> Slides 14 through 30 review international visual media campaigns and public service announcements. The pedagogical focus is on how societal perception shifts from passive acceptance of pollution as an inevitable consequence of economic growth to active demand for regulatory oversight and circular economy standards.</p>
          <p><strong>2. Cognitive Dissonance & Greenwashing:</strong> Media campaigns often expose the contradiction between corporate advertising and actual ecological supply chain impacts. True environmental accounting requires cradle-to-grave Life Cycle Assessment (LCA) rather than superficial marketing claims.</p>
        </div>
        """,
        "math_formula": "\\text{Total Ecological Footprint} = \\sum_{i} \\frac{\\text{Consumption}_i}{\\text{Yield}_i} \\times \\text{Equivalence Factor}_i",
        "exam_checkpoint": "Be able to evaluate an environmental campaign: does it promote genuine structural sustainability (policy reform, decarbonization) or merely individualized consumer tokenism?"
    },
    {
        "unit_id": "u01_4",
        "title": "Policy Frameworks, Environmental AI & Evaluation Scheme",
        "slide_range": "Slides 31–33",
        "slides_idx": [31, 32, 33],
        "takeaway": "Maps government policies, spatial changes over time, and the integration of deep learning and ensemble models into environmental monitoring.",
        "synthesis": """
        <div class="space-y-3">
          <p><strong>1. Policy & Landscape History (Slide 31):</strong> Government schemes and statutory interventions directly alter landscape architecture. Using historical geospatial data, researchers trace multi-decadal land use and land cover (LULC) changes to assess whether environmental laws actually protect sensitive biomes.</p>
          <p><strong>2. Artificial Intelligence in Environmental Science:</strong> Slide 31 explicitly highlights project directions linking AI and Environmental Science at IIIT-H:
            <ul class="list-disc pl-5 mt-1 space-y-1 text-emerald-200">
              <li><strong>Ensemble Learning (Random Forests, Gradient Boosting):</strong> Modeling forest biomass, groundwater potential, and species distribution.</li>
              <li><strong>Deep Learning (CNNs, Vision Transformers):</strong> Automated high-resolution satellite imagery segmentation for deforestation and urban heat islands.</li>
            </ul>
          </p>
          <p><strong>3. Course Evaluation Scheme (Slide 33):</strong> Continuous assessment combining 20% Assignments, hands-on environmental computing projects, and rigorous exams.</p>
        </div>
        """,
        "math_formula": "\\hat{y}_{ensemble} = \\frac{1}{M} \\sum_{m=1}^{M} f_m(x_{\\text{spatial}})",
        "exam_checkpoint": "Know the specific AI techniques highlighted by the instructor (Ensemble learning, Deep learning) and their specific applications in landscape spatial analytics."
    },
    {
        "unit_id": "u01_5",
        "title": "Dr. A.P.J. Abdul Kalam's 'Letter Written in the Year 2070'",
        "slide_range": "Slides 34–54",
        "slides_idx": [34, 35, 36, 39, 40, 41, 42, 45, 48, 52, 54],
        "takeaway": "A haunting narrative case study of complete planetary overshoot, irreversible water depletion, and severe societal collapse.",
        "synthesis": """
        <div class="space-y-3">
          <p><strong>1. The Narrative Premise (Slides 34–38):</strong> A 50-year-old narrator in the year 2070 describes living in an ecologically devastated world. Though only 50, physical appearance resembles someone of 85 due to acute cellular dehydration, severe kidney pathology, and unshielded UV radiation. The narrator recalls childhood (circa early 2000s) when water was abundant, showers lasted 30 minutes, and warning signs were ignored.</p>
          <p><strong>2. Economic & Societal Breakdown (Slides 39–44):</strong>
            <ul class="list-disc pl-5 mt-1 space-y-1 text-slate-300">
              <li><strong>Desalination Economy:</strong> Heavy industry has collapsed; desalination plants are the primary employer, paying workers partially in potable water rations.</li>
              <li><strong>Resource Wars:</strong> Armed assaults on city streets for a single jerrycan of water are routine; 80% of human food is synthetic.</li>
              <li><strong>Severe Rationing:</strong> Daily water allowance is restricted to half a glass per adult (down from the recommended 8 glasses).</li>
              <li><strong>Mutagenic Impacts:</strong> Stratospheric ozone collapse causes widespread skin cancers and severe spermatozoan morphological alterations.</li>
            </ul>
          </p>
          <p><strong>3. Air Taxation & Irreversible Tipping Points (Slides 45–54):</strong> The state charges citizens for oxygen breathing rations ($137\\,\\text{m}^3\\text{/day/adult}$). Remaining green river basins are guarded by military forces. Rain, when it occurs, is highly corrosive acid rain. The letter concludes with profound intergenerational guilt: earlier generations exhausted the Holocene stability window without taking action.</p>
        </div>
        """,
        "math_formula": "\\text{Oxygen Consumption: } V_{O_2} = 137\\,\\text{m}^3/\\text{day/adult} \\quad | \\quad \\text{Ration: } \\frac{1}{2} \\text{ glass } H_2O/\\text{day}",
        "exam_checkpoint": "Prof. Prasad uses this letter to emphasize 'Intergenerational Equity' and 'Irreversibility'. Pay close attention to the specific numbers cited ($137\\,\\text{m}^3$ air/day, half a glass water, year 2070 net-zero connection)."
    }
]

UNITS_LEC_02 = [
    {
        "unit_id": "u02_1",
        "title": "Earth Spheres, Tragedy of the Commons & The IPAT Identity",
        "slide_range": "Slides 01–14",
        "slides_idx": [1, 4, 5, 6, 8, 11, 12, 14],
        "takeaway": "Defines the 4 interconnected Earth spheres, Garrett Hardin's classic commons dilemma, and the IPAT environmental impact equation.",
        "synthesis": """
        <div class="space-y-3">
          <p><strong>1. The Four Spheres (Slide 5):</strong> Earth operates as an integrated system of four continuously exchanging spheres: Atmosphere (gas envelope), Hydrosphere (liquid and frozen water), Lithosphere (crust and upper mantle), and Biosphere (living organisms). Disturbances in one sphere cascade into the others through feedback loops.</p>
          <p><strong>2. Garrett Hardin's Tragedy of the Commons (1968, Slide 6):</strong> In an open-access, unregulated common-pool resource (pasture, fisheries, atmosphere), each rational user receives $+1$ utility for adding an animal or emitting a unit of pollutant, while bearing only a fraction $-1/N$ of the collective depletion cost. This inevitably drives the commons to ruin unless regulated through institutional governance or private property rights.</p>
          <p><strong>3. The IPAT Formulation (Slide 11):</strong> Environmental degradation is formalized by Paul Ehrlich and John Holdren: $I = P \\times A \\times T$. Developing countries experience high population growth ($P$), whereas developed nations drive degradation through extreme per-capita consumption ($A$).</p>
          <p><strong>4. The Easter Island Paradigm (Slide 12):</strong> Colonized ~300 AD with dense palm forests. Unrestrained deforestation for agriculture and moai transport triggered severe soil erosion, agricultural collapse, clan warfare, and population crash—a classic microcosm of planetary ecological suicide.</p>
        </div>
        """,
        "math_formula": "I = P \\cdot A \\cdot T \\quad\\text{where } I = \\text{Impact}, P = \\text{Population}, A = \\text{Affluence } (\\frac{\\text{GDP}}{\\text{Pop}}), T = \\text{Technology } (\\frac{\\text{Impact}}{\\text{GDP}})",
        "exam_checkpoint": "Hardin's Tragedy of the Commons is a core exam question. Remember Hardin's conclusion: 'Freedom in a commons brings ruin to all'. Be ready to solve numericals using the IPAT identity."
    },
    {
        "unit_id": "u02_2",
        "title": "Baltic Cyanobacteria Blooms, Sacred Groves & Kolleru Lake Degradation",
        "slide_range": "Slides 15–29",
        "slides_idx": [15, 17, 18, 22, 26, 27, 28],
        "takeaway": "Explores harmful algal blooms, indigenous forest conservation, gene banks, and multi-decadal wetland destruction.",
        "synthesis": """
        <div class="space-y-3">
          <p><strong>1. Baltic Sea Cyanobacteria Blooms (Slide 17):</strong> Massive surface accumulations of toxic cyanobacteria (*Nodularia spumigena*) in the Baltic Sea detected via enhanced true-color MODIS satellite imagery. Nutrient over-enrichment (nitrogen and phosphorus agricultural runoff) triggers Harmful Algal Blooms (HABs), producing hepatotoxins and creating extensive benthic anoxia (dead zones).</p>
          <p><strong>2. Sacred Groves as Genetic Refugia (Slide 22):</strong> In India, traditional community-protected forest patches (Sacred Groves) conserve rare, endemic, and near-extinct dry evergreen vegetation. These represent centuries of informal community-based biodiversity preservation.</p>
          <p><strong>3. ICRISAT Genebank (Slide 26):</strong> The International Crops Research Institute for the Semi-Arid Tropics (Hyderabad) houses over 128,000 germplasm accessions, preserving genetic crop biodiversity against climate vulnerability.</p>
          <p><strong>4. Kolleru Lake Wetland Shrinkage (Slide 28):</strong> A major Ramsar wetland in Andhra Pradesh. Survey of India toposheets of 1955 recorded 231.22 $km^2$ of open water. Rampant illegal aquaculture encroachments, fertilizer runoff, and water hyacinth weed infestation severely degraded this vital bird sanctuary and flood-retention basin.</p>
        </div>
        """,
        "math_formula": "\\text{Trophic State Index (TSI)} = 10 \\left(6 - \\frac{\\ln(\\text{Secchi Disk Depth})}{\\ln 2}\\right) > 60 \\implies \\text{Eutrophic/Hypereutrophic}",
        "exam_checkpoint": "Kolleru Lake and Baltic Sea blooms are classic case studies tested in midterms. Note the exact 1955 Kolleru baseline ($231.22\\,\\text{km}^2$) and the mechanism of cyanobacterial hepatotoxin production."
    },
    {
        "unit_id": "u02_3",
        "title": "Ecological Footprint, Biocapacity & Earth Overshoot Day",
        "slide_range": "Slides 30–39",
        "slides_idx": [30, 31, 32, 33, 35, 37, 39],
        "takeaway": "Quantifies the global ecological deficit: humanity's demand on nature exceeds Earth's annual regenerative biocapacity by over 70%.",
        "synthesis": """
        <div class="space-y-3">
          <p><strong>1. Ecological Footprint Accounting (Slide 30):</strong> Developed by Mathis Wackernagel and William Rees, the Ecological Footprint measures the biologically productive land and water area (in global hectares, gha) required to produce the resources an individual or population consumes and to assimilate their generated wastes.</p>
          <p><strong>2. Biocapacity Deficit (Slide 32–33):</strong> Biocapacity is the capacity of ecosystems to regenerate biological resources. When a nation's footprint exceeds its local biocapacity, it runs an ecological deficit, liquidating local natural capital or importing biocapacity from abroad.</p>
          <p><strong>3. Earth Overshoot Day (Slides 35–37):</strong> The calendar date on which humanity's resource consumption exceeds what Earth can regenerate in that entire year:
            <ul class="list-disc pl-5 mt-1 space-y-1 text-slate-300">
              <li>2018: August 1</li>
              <li>2020: August 22 (temporarily delayed due to COVID-19 pandemic lockdowns)</li>
              <li>2022: July 28</li>
              <li>2024: August 1</li>
            </ul>
          </p>
          <p><strong>4. Nepal Biocapacity Asymmetry (Slide 39):</strong> Countries in the low-income, biocapacity-deficit quadrant (e.g. Nepal producing only 78% of its domestic food consumption biocapacity) face acute food insecurity and economic vulnerability under climate shocks.</p>
        </div>
        """,
        "math_formula": "\\text{Earth Overshoot Day} = \\frac{\\text{World Biocapacity}}{\\text{World Ecological Footprint}} \\times 365 \\quad \\left(\\approx \\frac{1}{1.7} \\times 365 \\approx 214\\text{ days} \\implies \\text{Early August}\\right)",
        "exam_checkpoint": "Memorize the formula for Earth Overshoot Day. Notice the 2020 COVID anomaly where the date shifted back by 3 weeks, illustrating how industrial slowdown immediately alters planetary throughput."
    },
    {
        "unit_id": "u02_4",
        "title": "Waste Colonialism & Kondapalli Forest Ecology",
        "slide_range": "Slides 40–47",
        "slides_idx": [40, 41, 43, 46],
        "takeaway": "Examines global municipal solid waste flows, toxic dumping in developing nations, and local forest biodiversity surveys.",
        "synthesis": """
        <div class="space-y-3">
          <p><strong>1. Global Waste Throughput (Slide 40):</strong> In the United States alone, 160 million tons of municipal solid waste are discarded annually, including 50 million tons of paper, 67 billion cans and bottles, 25 billion styrofoam cups, and 2 billion disposable razors. This linear 'take-make-waste' model overwhelms terrestrial landfill capacities.</p>
          <p><strong>2. Waste Colonialism (Slide 41):</strong> The export of hazardous, electronic, and plastic waste from affluent Global North nations to low-income countries under the guise of 'recycling'. Recipient nations lack high-temperature incinerators or hazardous effluent treatment plants, resulting in heavy metal leaching (lead, cadmium, mercury) into local aquifers.</p>
          <p><strong>3. Kondapalli Dry Evergreen Forest (Slide 43):</strong> Research study on the floristic structure, species composition, and tree diversity of the dry evergreen reserve forest of Kondapalli in the Eastern Ghats (Andhra Pradesh), highlighting severe fragmentation pressures from mining and agricultural encroachment.</p>
        </div>
        """,
        "math_formula": "\\text{Shannon Diversity Index: } H' = -\\sum_{i=1}^{S} p_i \\ln p_i \\quad | \\quad \\text{Equitability: } J = \\frac{H'}{\\ln S}",
        "exam_checkpoint": "Define 'Waste Colonialism' with examples of e-waste shipments (Basel Convention violations) and the distinction between formal recycling and cross-border environmental injustice."
    },
    {
        "unit_id": "u02_5",
        "title": "Human Development Index (HDI) & Conservation Philosophies",
        "slide_range": "Slides 48–57",
        "slides_idx": [48, 49, 50, 54, 55, 56, 57],
        "takeaway": "Details the mathematical computation of HDI, inequality adjustment (IHDI), indigenous land conservation, and environmental ethics.",
        "synthesis": """
        <div class="space-y-3">
          <p><strong>1. HDI Mathematical Formulation (Slides 48–50):</strong> The United Nations Development Programme (UNDP) HDI is the geometric mean of three normalized dimension indices:
            <ul class="list-disc pl-5 mt-1 space-y-1 text-slate-300">
              <li>$I_{\\text{Health}} = \\frac{\\text{LE} - 20}{85 - 20}$ (Life Expectancy at birth)</li>
              <li>$I_{\\text{Education}} = \\frac{1}{2}\\left(\\frac{\\text{MYS}}{15} + \\frac{\\text{EYS}}{18}\\right)$ (Mean & Expected Years of Schooling)</li>
              <li>$I_{\\text{Income}} = \\frac{\\ln(\\text{GNIpc}) - \\ln(100)}{\\ln(75000) - \\ln(100)}$ (Gross National Income per capita)</li>
            </ul>
            $HDI = \\sqrt[3]{I_{\\text{Health}} \\cdot I_{\\text{Education}} \\cdot I_{\\text{Income}}}$. The Inequality-adjusted HDI (IHDI, Slide 54) accounts for inequality across citizens; if IHDI < HDI, deep domestic inequality exists.
          </p>
          <p><strong>2. Indigenous Peoples as Biodiversity Guardians (Slides 55–56):</strong> 500 million indigenous people comprise $<5\%$ of the world's population, yet their customary territories contain $80\%$ of global terrestrial biodiversity and intersect with the majority of intact forest landscapes.</p>
          <p><strong>3. Conservation Ideologies (Slide 57):</strong>
            <ul class="list-disc pl-5 mt-1 space-y-1 text-emerald-200">
              <li><strong>Pragmatic Utilitarian Conservation (Gifford Pinchot):</strong> Resources should be managed for 'the greatest good for the greatest number for the longest time'.</li>
              <li><strong>Biocentric Preservation (John Muir):</strong> Nature has an inherent moral right to exist undisturbed regardless of human utility.</li>
              <li><strong>Global Environmental Citizenship:</strong> Recognizing Earth as a fragile closed life-support system requiring planetary stewardship.</li>
            </ul>
          </p>
        </div>
        """,
        "math_formula": "HDI = \\left(I_{\\text{Health}} \\cdot I_{\\text{Education}} \\cdot I_{\\text{Income}}\\right)^{\\frac{1}{3}}",
        "exam_checkpoint": "You must be able to calculate HDI using the geometric mean formula. Know the difference between Pinchot's utilitarian conservation and Muir's biocentric preservation."
    }
]

UNITS_LEC_03 = [
    {
        "unit_id": "u03_1",
        "title": "Aquatic Crises: Eutrophication, Ocean Dead Zones & Deepwater Horizon",
        "slide_range": "Slides 01–09",
        "slides_idx": [1, 3, 4, 6, 8, 9],
        "takeaway": "Investigates freshwater and marine collapse: agricultural nitrogen cascades, the Aral Sea desiccation, and the 2010 Gulf of Mexico explosion.",
        "synthesis": """
        <div class="space-y-3">
          <p><strong>1. Eutrophication & The Ocean Dead Zone Cascade (Slides 3–4):</strong> Agricultural fertilizers (synthetic nitrates and phosphates) applied in the Mississippi River basin wash downstream into the Gulf of Mexico. This nutrient influx stimulates massive algal blooms. When algae die, heterotrophic bacteria consume dissolved oxygen ($DO$) during decomposition, causing hypoxia ($DO < 2\\,\\text{mg/L}$) and creating extensive dead zones where fish and benthic organisms suffocate.</p>
          <p><strong>2. The Aral Sea Ecological Catastrophe (Slide 8):</strong> Formerly the world's 4th largest inland lake ($68,000\\,\\text{km}^2$). Soviet diversion of the Amu Darya and Syr Darya rivers for cotton monoculture drained 90% of its volume, leaving behind a toxic, salt-encrusted desert (the Aralkum Desert) that generates toxic pesticide dust storms.</p>
          <p><strong>3. Deepwater Horizon Blowout (Slide 9):</strong> On April 20, 2010, the BP offshore drilling rig exploded in the Gulf of Mexico, killing 11 workers and discharging ~4.9 million barrels (780,000 $m^3$) of crude oil over 87 days, contaminating 2,100 km of Gulf shoreline.</p>
        </div>
        """,
        "math_formula": "\\text{Hypoxia Threshold: } [DO] < 2.0\\,\\text{mg/L} \\quad (\\text{Healthy Waters: } 6.5 - 9.0\\,\\text{mg/L})",
        "exam_checkpoint": "Trace the step-by-step biochemical cascade of cultural eutrophication: Nutrient Loading $\\to$ Algal Bloom $\\to$ Light Blockage $\\to$ Microbial Respiration $\\to$ Severe Anoxia $\\to$ Fish Kills."
    },
    {
        "unit_id": "u03_2",
        "title": "Niger Delta Oil Devastation, Thermal Pollution & Acid Rain",
        "slide_range": "Slides 10–16",
        "slides_idx": [10, 11, 13, 15, 16],
        "takeaway": "Analyzes chronic petrochemical devastation, cooling water thermal shocks in China, and regional acid precipitation.",
        "synthesis": """
        <div class="space-y-3">
          <p><strong>1. Niger Delta Chronic Oil Spills (Slide 10):</strong> Decades of pipeline ruptures and sabotaged wells by multinational oil operations have coated mangrove creeks in oil, annihilating local fisheries, destroying snail populations, and contaminating drinking water with high benzene concentrations.</p>
          <p><strong>2. Thermal Pollution in Chaohu Lake, China (Slide 11):</strong> Once-through cooling systems in coal-fired power plants discharge effluent water $10^\\circ\\text{C}$ to $15^\\circ\\text{C}$ above ambient river temperature. Henry's Law dictates that gas solubility decreases as temperature rises, reducing dissolved oxygen while accelerating metabolic oxygen demand in aquatic organisms.</p>
          <p><strong>3. Acid Deposition & Nuclear Fallout (Slides 15–16):</strong> Sulfur dioxide ($SO_2$) and nitrogen oxides ($NO_x$) from thermal plants undergo gas-to-particle photochemical oxidation forming sulfuric acid ($H_2SO_4$) and nitric acid ($HNO_3$), depressing precipitation pH below 4.5. Slide 15 also notes the 2011 Fukushima Daiichi triple meltdown releasing radioactive cesium-137 into the Pacific.</p>
        </div>
        """,
        "math_formula": "SO_2 + \\text{OH}^\\bullet \\to HOSO_2^\\bullet \\xrightarrow{O_2, H_2O} H_2SO_4 + HO_2^\\bullet \\quad | \\quad \\text{Henry's Law: } C = k_H(T) \\cdot P",
        "exam_checkpoint": "Explain the inverse relationship between water temperature and dissolved oxygen solubility using Henry's Law, and how thermal shock creates lethal zones near industrial discharge flumes."
    },
    {
        "unit_id": "u03_3",
        "title": "Desertification, The Kubuqi Greening Model & Shifting Cultivation",
        "slide_range": "Slides 17–23",
        "slides_idx": [17, 18, 19, 20, 22, 23],
        "takeaway": "Evaluates land degradation, China's Kubuqi desert restoration model, and shifting cultivation (Jhum) geospatial dynamics.",
        "synthesis": """
        <div class="space-y-3">
          <p><strong>1. Desertification Dynamics (Slide 17):</strong> Land degradation in arid, semi-arid, and sub-humid areas resulting from human overgrazing, unsustainable irrigation (salinization), and climate swings. Productive topsoil is stripped away by wind and water erosion.</p>
          <p><strong>2. The Kubuqi Greening Model (Slide 18):</strong> Located in Inner Mongolia, China. The Kubuqi ecological restoration model restored over 6,000 $km^2$ of desert through private-public partnerships: planting drought-tolerant licorice (*Glycyrrhiza uralensis*) which enriches soil nitrogen, combining it with massive solar PV arrays that provide shading and reduce surface wind erosion.</p>
          <p><strong>3. Shifting Cultivation (Jhum) in Northeast India (Slides 20, 22):</strong> Traditional slash-and-burn farming in the Barak Basin. Historically sustainable with 15–20 year fallow cycles allowing secondary forest regeneration; under population pressure, cycles have contracted to 3–5 years, resulting in severe soil erosion and forest degradation.</p>
        </div>
        """,
        "math_formula": "\\text{Universal Soil Loss Equation (USLE): } A = R \\cdot K \\cdot LS \\cdot C \\cdot P",
        "exam_checkpoint": "Why is the Kubuqi Model celebrated globally? Be prepared to cite the symbiotic integration of licorice leguminous nitrogen fixation with utility-scale solar PV panels."
    },
    {
        "unit_id": "u03_4",
        "title": "Soil Pollution, Biomagnification & Antarctic Ozone Hole",
        "slide_range": "Slides 24–34",
        "slides_idx": [24, 25, 26, 27, 28, 30, 31, 34],
        "takeaway": "Examines landfill leachate contamination, pesticide biomagnification up food chains, and stratospheric ozone depletion.",
        "synthesis": """
        <div class="space-y-3">
          <p><strong>1. Soil Contamination & Waste Management (Slides 24–26):</strong> Unlined municipal and industrial landfills generate toxic leachate—a complex liquid cocktail of organic acids, dissolved heavy metals (arsenic, mercury), and chlorinated solvents that percolates through soil horizons into unconfined groundwater tables.</p>
          <p><strong>2. Bioaccumulation vs. Biomagnification (Slide 30):</strong>
            <ul class="list-disc pl-5 mt-1 space-y-1 text-slate-300">
              <li><strong>Bioaccumulation:</strong> The net buildup of a persistent, fat-soluble chemical (e.g. DDT, PCBs) in a single organism's adipose tissues over its lifespan because intake rate exceeds metabolic breakdown/excretion rate.</li>
              <li><strong>Biomagnification:</strong> The progressive increase in contaminant concentration at each successive trophic level of a food pyramid. Apex predators (e.g. raptors, dolphins) exhibit concentrations millions of times higher than ambient water levels.</li>
            </ul>
          </p>
          <p><strong>3. Antarctic Ozone Hole (Slide 34):</strong> Catalytic destruction of stratospheric ozone ($O_3$) by chlorine free radicals ($Cl^\\bullet$) released from anthropogenic chlorofluorocarbons (CFCs). Polar stratospheric clouds (PSCs) provide ice crystal surfaces for heterogeneous reactions during polar winter, releasing active chlorine that decimates ozone during spring sunrise.</p>
        </div>
        """,
        "math_formula": "Cl^\\bullet + O_3 \\to ClO^\\bullet + O_2 \\quad ; \\quad ClO^\\bullet + O^\\bullet \\to Cl^\\bullet + O_2 \\quad (\\text{One } Cl^\\bullet \\text{ destroys } 10^5\\, O_3)",
        "exam_checkpoint": "Never confuse Bioaccumulation (within one organism over time) with Biomagnification (across trophic levels up a food chain). Know the catalytic ozone depletion cycle."
    }
]

UNITS_LEC_04 = [
    {
        "unit_id": "u04_1",
        "title": "Remote Sensing Principles, EMS Bands & Satellite Sensors",
        "slide_range": "Slides 01–05",
        "slides_idx": [1, 2, 3, 4, 5],
        "takeaway": "Details the physical foundations of remote sensing, electromagnetic spectrum partitioning, and satellite sensor systems.",
        "synthesis": """
        <div class="space-y-3">
          <p><strong>1. Physics of Remote Sensing (Slides 1–3):</strong> Remote sensing is the acquisition of physical data about Earth's surface without making direct physical contact, by measuring reflected solar radiance and emitted terrestrial thermal radiation across specific bands of the Electromagnetic Spectrum (EMS).</p>
          <p><strong>2. EMS Partitioning & Atmospheric Windows:</strong>
            <ul class="list-disc pl-5 mt-1 space-y-1 text-slate-300">
              <li><strong>Visible (0.4–0.7 $\\mu m$):</strong> Blue (0.45–0.51 $\\mu m$), Green (0.53–0.59 $\\mu m$), Red (0.64–0.67 $\\mu m$). Healthy chlorophyll absorbs Blue and Red strongly for photosynthesis while reflecting Green.</li>
              <li><strong>Near-Infrared (NIR, 0.7–1.3 $\\mu m$):</strong> Uniquely sensitive to plant leaf internal mesophyll cell structure; healthy vegetation displays intense high reflectance (the 'NIR plateau').</li>
              <li><strong>Shortwave-Infrared (SWIR, 1.3–2.5 $\\mu m$):</strong> Strongly absorbed by plant leaf water content and soil moisture; critical for drought stress detection.</li>
              <li><strong>Thermal-Infrared (TIR, 8–14 $\\mu m$):</strong> Measures blackbody thermal emission for Land Surface Temperature (LST).</li>
            </ul>
          </p>
          <p><strong>3. Satellite Sensors (Slide 5):</strong> Landsat series (MSS, TM, ETM+, OLI), ISRO IRS/LISS sensors, and ESA Sentinel-2 multispectral instruments providing spatial, spectral, temporal, and radiometric resolutions.</p>
        </div>
        """,
        "math_formula": "NDVI = \\frac{NIR - \\text{Red}}{NIR + \\text{Red}} \\quad | \\quad \\text{Wien's Displacement Law: } \\lambda_{max} = \\frac{2898}{T}\\,\\mu m\\cdot K",
        "exam_checkpoint": "Why do healthy plants have high NIR and low Red reflectance? Be prepared to sketch the classic vegetation spectral reflectance curve and write the NDVI formula."
    },
    {
        "unit_id": "u04_2",
        "title": "Mangrove Mapping, 1976–1999 Change Detection & Katchal Island",
        "slide_range": "Slides 06–11",
        "slides_idx": [6, 7, 8, 9, 10, 11],
        "takeaway": "Demonstrates multi-decadal change detection in coastal ecosystems and catastrophic 2004 tsunami impacts.",
        "synthesis": """
        <div class="space-y-3">
          <p><strong>1. Mangrove Forest Type Mapping (Slide 6):</strong> Mangroves represent critical coastal buffer zones with unique spectral signatures. Remote sensing discriminates dense mangrove stands from mudflats and inland forests using False Color Composites (FCC: NIR in red channel).</p>
          <p><strong>2. Multi-Decadal Change Detection (Slide 7):</strong> Comparative analysis between Landsat MSS (1976, 80m resolution) and IRS LISS III (1999, 23.5m resolution) in a sensitive coastal study region revealed an overall forest loss of 12.5% (5.0% interior forest fragmentation, 7.5% coastal mangrove clearing), with a corresponding rise in degraded scrub and agricultural land.</p>
          <p><strong>3. Katchal Island Post-Tsunami Remote Sensing (Slide 9):</strong> The December 26, 2004 Indian Ocean Tsunami devastated Katchal Island in the Nicobar archipelago. Multi-temporal satellite imagery tracked co-seismic land subsidence, tidal wave scouring of entire coastal forests, and altered coastline geomorphology.</p>
        </div>
        """,
        "math_formula": "\\Delta \\text{Area} = \\text{Area}_{t_2} - \\text{Area}_{t_1} \\quad | \\quad \\text{Overall Accuracy} = \\frac{\\sum \\text{Correct Pixels}}{\\text{Total Pixels}} \\times 100\\%",
        "exam_checkpoint": "Know the sensors compared in the instructor's case study: 1976 Landsat MSS (80m) vs 1999 IRS LISS III (23.5m), and the exact 12.5% forest loss statistic."
    },
    {
        "unit_id": "u04_3",
        "title": "Kollam Coastal Water Quality, Nilambur AHP Landslide Mapping & GHMC LST",
        "slide_range": "Slides 12–14",
        "slides_idx": [12, 13, 14],
        "takeaway": "Applied geospatial informatics: marine water turbidity modeling, multi-criteria landslide risk zonation, and urban heat islands.",
        "synthesis": """
        <div class="space-y-3">
          <p><strong>1. Coastal Water Quality Dynamics in Kollam, Kerala (Slide 12):</strong> High-resolution Sentinel-2 multispectral imagery mapped Total Suspended Solids (TSS), turbidity, and chlorophyll-a concentrations in the Arabian Sea off the coast of Kollam, tracking industrial effluent plumes and monsoonal sediment discharge.</p>
          <p><strong>2. Analytical Hierarchy Process (AHP) for Landslides in Nilambur (Slide 13):</strong> In Nilambur Taluk, Kerala (Western Ghats), catastrophic monsoon debris flows occur on steep slopes. AHP multi-criteria decision evaluation weighs diverse spatial thematic layers: slope angle, elevation, lithology, soil depth, distance to fault lines, and LULC. Pairwise comparison matrices yield a Landslide Susceptibility Index (LSI) with a validated Consistency Ratio ($CR < 0.10$).</p>
          <p><strong>3. Urban Heat Islands & Green Space Mitigation in Hyderabad (Slide 14):</strong> Study within Greater Hyderabad Municipal Corporation (GHMC) using Landsat-8 TIRS. Quantified how urban parks, water bodies, and tree canopy cool Land Surface Temperature (LST) by $2^\\circ\\text{C}$ to $5^\\circ\\text{C}$ relative to dense asphalt and concrete built-up areas via evapotranspirative cooling.</p>
        </div>
        """,
        "math_formula": "LSI = \\sum_{i=1}^{n} w_i \\cdot r_i \\quad | \\quad CR = \\frac{CI}{RI} < 0.10 \\quad | \\quad LST = \\frac{T_B}{1 + (\\lambda T_B / \\rho) \\ln \\varepsilon}",
        "exam_checkpoint": "AHP Landslide Susceptibility Mapping is a favorite exam topic. Be prepared to explain pairwise comparison matrices, the role of Consistency Ratio ($CR < 0.1$), and how urban green spaces mitigate LST."
    },
    {
        "unit_id": "u04_4",
        "title": "Idukki Forest Carbon, Mining in Manuguru, MaxEnt Aphids & Kondapalli",
        "slide_range": "Slides 15–18",
        "slides_idx": [15, 16, 17, 18],
        "takeaway": "Advanced ecological modeling: allometric biomass estimation, opencast coal mining impacts, MaxEnt niche modeling, and patch fragmentation.",
        "synthesis": """
        <div class="space-y-3">
          <p><strong>1. Forest Dynamics & Carbon in Idukki, Kerala (Slide 15):</strong> Combined multi-sensor satellite imagery with field biometric plots in Idukki District. Applied allometric regression equations to convert canopy height and Crown Closure into Aboveground Biomass (AGB) and carbon stocks ($tC/ha$), modeling carbon sequestration losses under agricultural encroachment.</p>
          <p><strong>2. Manuguru Coal Belt Mining Pressure, Telangana (Slide 16):</strong> Multi-decadal remote sensing of the Singareni Collieries opencast coal belt in Manuguru. Quantified large-scale deforestation, topsoil stripping, overburden dump growth, and calculated the net loss in total ecosystem service valuation (ESV).</p>
          <p><strong>3. MaxEnt Ecological Niche Modeling of Pea Aphid (Slide 17):</strong> Maximum Entropy (MaxEnt) machine learning algorithm used bioclimatic variables (WorldClim temperature and precipitation surfaces) to predict the geographic range shift of the agricultural pest Pea Aphid (*Acyrthosiphon pisum*) under IPCC future warming scenarios.</p>
          <p><strong>4. Kondapalli Reserve Forest Patch Fragmentation (Slide 18):</strong> Landscape metrics (Mean Patch Size, Perimeter-Area Ratio, Euclidean Nearest-Neighbor Distance) quantified remnant patch isolation and edge effects in Andhra Pradesh.</p>
        </div>
        """,
        "math_formula": "AGB = a \\cdot (DBH)^b \\cdot H^c \\quad | \\quad P(x) = \\frac{1}{Z} \\exp\\left(\\sum_{i} \\lambda_i f_i(x)\\right) \\quad \\text{(MaxEnt Probability)}",
        "exam_checkpoint": "Understand how MaxEnt uses presence-only occurrence records with environmental raster layers to model species distribution shifts under climate change."
    }
]
