# Slide Learning Units for Lectures 09 - 12

UNITS_LEC_09 = [
    {
        "unit_id": "u09_1",
        "title": "Glacial Retreat, Atmospheric CO2 & Global Carbon Budget Partitioning",
        "slide_range": "Slides 01–08",
        "slides_idx": [1, 2, 5, 7, 8],
        "takeaway": "Quantifies empirical cryosphere retreat (Muir Glacier) and the global partitioning of anthropogenic carbon emissions.",
        "synthesis": """
        <div class="space-y-3">
          <p><strong>1. Empirical Cryosphere Evidence (Slide 2):</strong> Paired historical photography of Alaska's Muir Glacier shows catastrophic retreat: in August 1941, the glacier filled the entire bay with ice >100 meters thick; by August 2004, the glacier had retreated over 12 kilometers out of the field of view, replaced by ocean water and recolonizing temperate vegetation.</p>
          <p><strong>2. Atmospheric Carbon Acceleration (Slide 5):</strong> Continuous measurements at Mauna Loa show atmospheric $CO_2$ surging from pre-industrial levels of ~280 ppm to over 419 ppm today, rising at an unprecedented rate of >2.5 ppm/year.</p>
          <p><strong>3. The Global Carbon Budget Partitioning (Slides 7–8):</strong> Anthropogenic emissions from fossil fuels and land-use change (~40 Gt $CO_2$/yr) are partitioned among three major Earth system sinks:
            <ul class="list-disc pl-5 mt-1 space-y-1 text-slate-300">
              <li><strong>Atmosphere:</strong> Absorbs approximately 40% of emissions, driving ongoing global radiative forcing.</li>
              <li><strong>Oceanic Sink:</strong> Absorbs ~30% via chemical dissolution and the solubility pump, mitigating atmospheric warming at the cost of ocean acidification.</li>
              <li><strong>Terrestrial Biosphere Sink:</strong> Absorbs ~30% through forest growth and vegetation carbon fertilization.</li>
            </ul>
          </p>
        </div>
        """,
        "math_formula": "\\Delta C_{\\text{atm}} = E_{\\text{fossil}} + E_{\\text{LUC}} - S_{\\text{ocean}} - S_{\\text{land}} \\quad (40\\% \\text{ atm}, 30\\% \\text{ ocean}, 30\\% \\text{ land})",
        "exam_checkpoint": "State the exact global carbon emission partitioning: ~40% remains in the atmosphere, ~30% goes to oceans, and ~30% is taken up by terrestrial vegetation."
    },
    {
        "unit_id": "u09_2",
        "title": "Forest Carbon Stocks, Gross Deforestation & Landsat Grid Monitoring",
        "slide_range": "Slides 09–15",
        "slides_idx": [9, 10, 11, 12, 13, 14, 15],
        "takeaway": "Formulates forest biomass carbon conversion, global forest extent (4.06B ha), and satellite carbon stock tracking.",
        "synthesis": """
        <div class="space-y-3">
          <p><strong>1. Forest Biomass Allometry (Slide 9):</strong> A living forest is an active carbon stock. In dry wood biomass, carbon content is remarkably constant: <strong>1 kilogram of dry wood contains $\\approx 0.5$ kilograms of elemental carbon</strong> (the 50% carbon fraction rule). To convert dry biomass to $CO_2$ equivalents, multiply by the stoichiometric ratio $\\frac{44}{12} \\approx 3.67$.</p>
          <p><strong>2. Global Forest Coverage & Emissions (Slides 10–14):</strong>
            <ul class="list-disc pl-5 mt-1 space-y-1 text-slate-300">
              <li>Forests cover 4.06 billion hectares (31% of Earth's total land area).</li>
              <li>Total forest carbon storage stands at 662 billion tonnes of carbon (equivalent to ~2.4 trillion tonnes of $CO_2$).</li>
              <li>Net forest loss between 2010 and 2020 averaged 4.7 million hectares/year, with gross tropical deforestation reaching ~10 million hectares/year.</li>
              <li>Tropical deforestation releases 5.6 billion tonnes of $CO_2$ annually, while undisturbed forest regeneration sequestered 14.4 billion tonnes of $CO_2$/yr.</li>
            </ul>
          </p>
          <p><strong>3. High-Resolution Landsat 1° Grid Cell Carbon Monitoring (Slide 15):</strong> Combining Landsat Analysis Ready Data (ARD) with spaceborne LiDAR (GEDI) enables automated tracking of mean canopy height (meters), net forest area change, and degradation across global $1^\\circ \\times 1^\\circ$ spatial grids.</p>
        </div>
        """,
        "math_formula": "C_{\\text{stock}} = \\text{Biomass} \\times 0.50 \\quad | \\quad CO_2e = C_{\\text{stock}} \\times \\frac{44}{12} = C_{\\text{stock}} \\times 3.667",
        "exam_checkpoint": "Memorize the dry wood-to-carbon ratio (0.50) and the stoichiometric conversion factor to $CO_2$ (3.67). Know the global forest area: 4.06 billion hectares."
    },
    {
        "unit_id": "u09_3",
        "title": "Soil Organic Carbon & Agroforestry Practices",
        "slide_range": "Slides 16–25",
        "slides_idx": [16, 18, 19, 20, 21, 22, 23, 24, 25],
        "takeaway": "Analyzes the massive soil carbon reservoir and agricultural sequestration techniques: windbreaks, riparian buffers, and silvopasture.",
        "synthesis": """
        <div class="space-y-3">
          <p><strong>1. Soil Organic Carbon (SOC) Reservoir (Slide 18):</strong> The Harmonized World Soil Database (HWSD) reveals that topsoil (0–1 meter depth) stores approximately 1,500 to 2,000 gigatons of carbon—more than double the entire carbon content of the atmosphere. Agricultural tilling aerates soil, accelerating microbial decomposition of humus and venting huge pulses of $CO_2$.</p>
          <p><strong>2. Agroforestry Sequestration Systems (Slides 21–25):</strong>
            <ul class="list-disc pl-5 mt-1 space-y-1 text-slate-300">
              <li><strong>Windbreaks (Slide 22):</strong> Linear rows of trees and shrubs protecting crops from wind erosion while accumulating woody biomass carbon.</li>
              <li><strong>Riparian Forest Buffers (Slide 23):</strong> Multi-canopy vegetated strips along streams that intercept agrochemical nitrogen runoff while building root biomass.</li>
              <li><strong>Silvopasture (Slide 24):</strong> The intentional integration of trees, forage, and grazing livestock on the same land parcel; sequesters up to 5–10 times more carbon per hectare than open pasture.</li>
              <li><strong>Short-Rotation Eucalyptus Plantations (Slide 25):</strong> Fast-growing species with high photosynthetic carbon capture velocity under intensive rotation cycles.</li>
            </ul>
          </p>
        </div>
        """,
        "math_formula": "\\text{SOC Stock } (tC/ha) = \\text{SOC}\\% \\times \\text{Bulk Density } (g/cm^3) \\times \\text{Depth } (cm) \\times (1 - \\text{Gravel}\\%/100)",
        "exam_checkpoint": "Why does soil store more carbon than the atmosphere and living vegetation combined? Be prepared to define the four major agroforestry practices: windbreaks, riparian buffers, silvopasture, and alley cropping."
    },
    {
        "unit_id": "u09_4",
        "title": "Forest Productivity vs. Age, India's Afforestation & Infapro / Plan Vivo",
        "slide_range": "Slides 26–34",
        "slides_idx": [26, 27, 29, 30, 31, 32, 33],
        "takeaway": "Examines forest growth maturation curves, India's 65.45 Mha potential, and international carbon projects in Malaysia and Mexico.",
        "synthesis": """
        <div class="space-y-3">
          <p><strong>1. Forest Productivity vs. Age Curve (Slide 29):</strong> A young, growing forest acts as a vigorous net carbon sink, sequestering 5–11 tons of $CO_2$/ha/year. Sequestration rate peaks between 25 and 75 years of age depending on forest type. At biological maturity (climax forest), gross primary productivity ($GPP$) is balanced by autotrophic and heterotrophic respiration ($NPP \\approx 0$), reaching a steady-state carbon pool rather than a net accumulator.</p>
          <p><strong>2. India's Carbon Sequestration Potential (Slides 27, 30):</strong> Total forest biomass in Indian forests was estimated at 8,357.9 Mt (1986). India possesses 65.45 million hectares (Mha) of land categories available for afforestation, with degraded open forests comprising 25% of this land base.</p>
          <p><strong>3. Landmark International Forestry Carbon Projects (Slides 31–33):</strong>
            <ul class="list-disc pl-5 mt-1 space-y-1 text-slate-300">
              <li><strong>Infapro Project, Sabah, Malaysia (Slide 31):</strong> 25,000 hectares of logged lowland dipterocarp rainforest rehabilitated via enrichment planting of native species, funded by the Dutch FACE Foundation (Forests Absorbing Carbon dioxide Emissions).</li>
              <li><strong>Plan Vivo, Chiapas, Mexico (Slides 32–33):</strong> A community-led forest carbon initiative in southern Mexico where local indigenous farmer cooperatives were paid directly for reforestation and agroforestry ($15 million investment).</li>
            </ul>
          </p>
        </div>
        """,
        "math_formula": "NEP = GPP - R_{\\text{autotrophic}} - R_{\\text{heterotrophic}} \\quad (NEP \\to 0 \\text{ as forest reaches climax maturity})",
        "exam_checkpoint": "Why do mature climax forests cease to be strong net carbon sinks? (NEP approaches zero because total ecosystem respiration balances photosynthesis). Know the net available afforestation land in India: 65.45 Mha."
    }
]

UNITS_LEC_10 = [
    {
        "unit_id": "u10_1",
        "title": "UNFCCC, Kyoto Protocol Framework & Certified Emission Reductions (CERs)",
        "slide_range": "Slides 01–13",
        "slides_idx": [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 13],
        "takeaway": "Details the international climate regulatory architecture: Kyoto Protocol, the six covered greenhouse gases, and the mechanics of CER carbon credits.",
        "synthesis": """
        <div class="space-y-3">
          <p><strong>1. UNFCCC Foundations & CBDR Principle (Slides 3–4):</strong> Adopted at the 1992 Rio Earth Summit. The cornerstone principle is <strong>Common But Differentiated Responsibilities (CBDR)</strong>: recognizes that developed nations (Annex I) produced the vast majority of historical cumulative emissions and must take the lead in mitigation, while developing nations (non-Annex I) have overriding priorities of poverty eradication and economic development.</p>
          <p><strong>2. Kyoto Protocol (1997 / Ratified 2005, Slides 6–8):</strong> Established legally binding emission reduction targets for Annex I nations (-5.2% below 1990 levels during 2008–2012). It created three market-based flexible mechanisms: Clean Development Mechanism (CDM), Joint Implementation (JI), and International Emissions Trading (IET).</p>
          <p><strong>3. The Six Greenhouse Gases Covered (Slide 11):</strong>
            Carbon Dioxide ($CO_2$, GWP=1), Methane ($CH_4$, GWP=28), Nitrous Oxide ($N_2O$, GWP=265), Hydrofluorocarbons (HFCs), Perfluorocarbons (PFCs), and Sulfur Hexafluoride ($SF_6$, GWP=23,500).</p>
          <p><strong>4. Concept of Certified Emission Reductions (CERs, Slides 9–10):</strong> $1\\,\\text{CER} = 1\\,\\text{metric tonne of } CO_2\\text{-equivalent}$ avoided or sequestered. An Annex I country invests in a green project in a non-Annex I nation, earning CERs to offset its domestic compliance cap at lower marginal cost.</p>
        </div>
        """,
        "math_formula": "1\\,\\text{CER} = 1\\,\\text{tCO}_2\\text{e} = \\sum_{i} m_i \\cdot GWP_i \\quad | \\quad \\text{Kyoto Target: } -5.2\\% \\text{ below 1990 levels}",
        "exam_checkpoint": "State the definition of 1 CER (1 metric tonne of CO2 equivalent). Name all six greenhouse gases covered under Annex A of the Kyoto Protocol and their relative GWPs."
    },
    {
        "unit_id": "u10_2",
        "title": "CDM Additionality Rules, Renewable Energy & Powerguda Village Case",
        "slide_range": "Slides 14–26",
        "slides_idx": [14, 15, 16, 17, 18, 20, 21, 23, 24],
        "takeaway": "Formulates the strict 'Additionality' test, agricultural mitigation, and India's pioneering rural carbon trade in Powerguda.",
        "synthesis": """
        <div class="space-y-3">
          <p><strong>1. The Additionality Principle (Slide 16):</strong> The cardinal rule of the CDM: a project is 'additional' if and only if anthropogenic emissions are reduced below those that would have occurred in the absence of the certified project activity (the baseline scenario). The project must overcome financial, technological, or institutional barriers that would otherwise prevent its execution without carbon finance.</p>
          <p><strong>2. Eligible Project Categories (Slides 17–22):</strong> Renewable energy (solar, wind, small hydro, tidal), industrial fuel switching, industrial fugitive methane capture from landfills, and agricultural soil management (e.g. replacing urea with ammonium sulfate: 1 ton of urea emits ~0.73 tons of $CO_2$ during hydrolysis).</p>
          <p><strong>3. Powerguda Village Landmark Case Study (July 2004, Slide 23):</strong> Powerguda, a remote tribal village in Adilabad District, Andhra Pradesh, became the <strong>first village in India to sell carbon credits directly to the World Bank</strong>. Villagers planted 4,500 Pongamia pinnata (karanja) trees on degraded land, extracting non-edible oil to produce biodiesel that displaced diesel fuel in municipal generators, earning $645 in verified carbon finance.</p>
          <p><strong>4. Transition to Paris Agreement Article 6 (Slide 24):</strong> In 2015, the Paris Agreement replaced Kyoto's top-down targets with nationally determined contributions (NDCs). Article 6 formalizes new bilateral and multilateral carbon market mechanisms (ITMOs - Internationally Transferred Mitigation Outcomes).</p>
        </div>
        """,
        "math_formula": "\\text{Emission Reductions: } ER_y = BE_y - PE_y - LE_y \\quad (\\text{Baseline} - \\text{Project} - \\text{Leakage})",
        "exam_checkpoint": "Define 'Additionality' in CDM with mathematical clarity. Memorize the Powerguda Village case study: location (Adilabad, AP), date (2004), and feedstock (Pongamia biodiesel)."
    },
    {
        "unit_id": "u10_3",
        "title": "Azolla Sequestration, Geological Storage & The Ocean Iron Hypothesis",
        "slide_range": "Slides 27–34",
        "slides_idx": [27, 28, 29, 30, 31, 32, 34],
        "takeaway": "Investigates biological Azolla hyper-accumulation, Illinois Basin geological CCS, and John Martin's ocean iron hypothesis.",
        "synthesis": """
        <div class="space-y-3">
          <p><strong>1. Biological Sequestration via Azolla (Slide 28):</strong> Floating water fern *Azolla filiculoides* displays exceptional carbon capture: sequesters 32.54 metric tonnes $CO_2$/ha/year after only 18 days of growth with 10% initial cover, due to its symbiotic cyanobacterium *Anabaena azollae* fixing atmospheric nitrogen at high rates.</p>
          <p><strong>2. Geological Sequestration & The Illinois Basin Project (Slides 29–30):</strong> Injecting supercritical $CO_2$ ($T > 31.1^\\circ\\text{C}, P > 73.9\\,\\text{bar}$, exhibiting liquid-like density and gas-like viscosity) into deep saline formations at depths $>800$ meters beneath impermeable caprock shales. The Illinois Basin - Decatur Project (IBDP, 2007–2021) safely injected over 1 million metric tons of anthropogenic $CO_2$ into the Mount Simon Sandstone.</p>
          <p><strong>3. John Martin's Ocean Iron Hypothesis (1988, Slides 31–32):</strong> Oceanographer John Martin observed High-Nutrient, Low-Chlorophyll (HNLC) ocean regions (Southern Ocean, sub-Arctic Pacific) where abundant nitrate and phosphate remain unutilized by phytoplankton due to micronutrient iron limitation. Martin famously stated: <em>'Give me half a tanker of iron, and I will give you an ice age.'</em> Adding ferrous iron salts ($FeSO_4$) stimulates massive diatom blooms that draw down atmospheric $CO_2$.</p>
        </div>
        """,
        "math_formula": "CO_2 \\text{ Supercritical State: } T_c = 31.1^\\circ\\text{C}, \\quad P_c = 7.39\\,\\text{MPa} \\implies \\rho \\approx 600 - 800\\,\\text{kg/m}^3",
        "exam_checkpoint": "State the critical temperature and pressure for supercritical CO2 ($31.1^\\circ\\text{C}, 73.9\\,\\text{bar}$). Know John Martin's Iron Hypothesis and what 'HNLC' stands for (High-Nutrient, Low-Chlorophyll)."
    },
    {
        "unit_id": "u10_4",
        "title": "Ocean Fertilization Verification Hazards, Toxic Diatoms & Deep Anoxia",
        "slide_range": "Slides 35–44",
        "slides_idx": [35, 38, 39, 40, 41, 42, 44],
        "takeaway": "Details the ecological risks of large-scale geoengineering: Domoic acid toxicity, paralytic shellfish poisoning, and unverified carbon offsets.",
        "synthesis": """
        <div class="space-y-3">
          <p><strong>1. Ocean Fertilization Verification Crisis (Slide 38):</strong> International scientific consensus holds that commercial carbon credits for ocean fertilization cannot be reliably verified. To evaluate net carbon drawdown, the project boundary must encompass the entire global ocean; lateral advection transports sequestered biomass, and zooplankton respiration returns >90% of captured carbon back to the atmosphere as dissolved inorganic carbon before it sinks past the 1,000m lysocline.</p>
          <p><strong>2. Toxic Phytoplankton Proliferation (Slides 39–41):</strong> In situ iron addition experiments (such as the 2007 Sulu Sea urea experiment) often stimulate undesirable species rather than beneficial large diatoms:
            <ul class="list-disc pl-5 mt-1 space-y-1 text-slate-300">
              <li><strong>Dinoflagellate Blooms:</strong> Produce saxitoxins responsible for fatal Paralytic Shellfish Poisoning (PSP).</li>
              <li><strong>Pseudo-nitzschia Diatoms:</strong> Produce neurotoxin domoic acid, which causes Amnesic Shellfish Poisoning (ASP), bioaccumulating up marine food webs to cause mortality in sea lions, whales, and humans.</li>
            </ul>
          </p>
          <p><strong>3. Deep Ocean Anoxia & Nutrient Robbing (Slide 42):</strong> Sinking biomass decomposition consumes dissolved oxygen in intermediate water layers, expanding mid-water Oxygen Minimum Zones (OMZs) and triggering production of potent greenhouse gases ($N_2O, CH_4$).</p>
        </div>
        """,
        "math_formula": "\\text{Redfield-Brzezinski Stoichiometry: } 106\\text{C} : 16\\text{N} : 1\\text{P} : 0.001\\text{Fe} \\quad | \\quad \\text{Export Efficiency } \\eta < 5\\%",
        "exam_checkpoint": "Why is commercial ocean fertilization banned under the London Convention? Cite the verification problem, toxic Pseudo-nitzschia domoic acid production, and deep-water deoxygenation."
    },
    {
        "unit_id": "u10_5",
        "title": "Ocean Acidification, Coal-Bed Methane Displacement & Novacem Cement",
        "slide_range": "Slides 45–54",
        "slides_idx": [45, 46, 48, 49, 50, 51, 52],
        "takeaway": "Examines marine carbonate chemistry shifts, the 72x GWP hazard of methane leakage from ECBM, and magnesium-silicate carbon-negative cement.",
        "synthesis": """
        <div class="space-y-3">
          <p><strong>1. Ocean Acidification Carbonate Chemistry (Slides 45–46):</strong> Dissolved $CO_2$ reacts with seawater to form carbonic acid: $CO_2 + H_2O \\leftrightarrow H_2CO_3 \\leftrightarrow H^+ + HCO_3^-$. The surplus hydrogen ions react with carbonate ions: $H^+ + CO_3^{2-} \\leftrightarrow HCO_3^-$. This depletes available carbonate ions ($CO_3^{2-}$), depressing the calcium carbonate saturation state ($\\Omega < 1$) and causing the shells of pteropods, corals, and shellfish to dissolve.</p>
          <p><strong>2. Enhanced Coal-Bed Methane (ECBM) Leakage Risk (Slides 48–49):</strong> Injecting $CO_2$ into unmineable coal seams displaces adsorbed methane ($CH_4$) because coal affinity for $CO_2$ is ~twice that of $CH_4$. However, methane has a Global Warming Potential 72 times that of $CO_2$ over a 20-year horizon ($GWP_{20} = 72$). If even a tiny fraction ($>1.5\%$) of displaced methane escapes through fractured caprock, the net climate benefit is completely wiped out.</p>
          <p><strong>3. Novacem Carbon-Negative Cement (Slide 51):</strong> Traditional Portland cement manufacturing produces ~5% of global anthropogenic $CO_2$ emissions (calcination of limestone: $CaCO_3 \\to CaO + CO_2$). Novacem, developed at Imperial College London, uses magnesium silicates ($Mg_3Si_2O_5(OH)_4$) that require lower kiln temperatures and actively absorb atmospheric $CO_2$ during curing, resulting in a net carbon-negative cement absorbing ~0.5 tonnes $CO_2$ per tonne produced.</p>
        </div>
        """,
        "math_formula": "\\Omega = \\frac{[Ca^{2+}][CO_3^{2-}]}{K'_{sp}} < 1 \\implies \\text{Shell Dissolution} \\quad | \\quad GWP_{20}(CH_4) = 72 \\times CO_2",
        "exam_checkpoint": "Explain why ocean acidification reduces carbonate ion ($CO_3^{2-}$) concentration rather than increasing it. Remember the 20-year GWP of methane (72x) in the context of coal-bed methane injection."
    }
]

UNITS_LEC_11 = [
    {
        "unit_id": "u11_1",
        "title": "Negative Emission Technologies, Biochar Pyrolysis & Enhanced Weathering",
        "slide_range": "Slides 01–07",
        "slides_idx": [1, 2, 3, 4, 5, 6, 7],
        "takeaway": "Formulates negative emission pathways required to limit global warming to 1.5°C under the Paris Agreement.",
        "synthesis": """
        <div class="space-y-3">
          <p><strong>1. Negative Emission Technologies (NETs) Overview (Slide 2):</strong> IPCC climate models indicate that emissions reductions alone are insufficient to meet the Paris Agreement $1.5^\\circ\\text{C}$ threshold; humanity must actively remove 100–1,000 Gt $CO_2$ from the atmosphere over the 21st century.</p>
          <p><strong>2. Biochar Pyrolysis (Slide 3):</strong> Thermal decomposition of biomass in the absence of oxygen ($400^\\circ\\text{C}$ to $700^\\circ\\text{C}$) converts labile organic carbon into highly stable, recalcitrant polycyclic aromatic carbon (biochar) with a soil mean residence time exceeding 1,000 years. Potential to sequester up to 4.8 billion tonnes of $CO_2$/year while enhancing soil moisture retention and cation exchange capacity.</p>
          <p><strong>3. Blue Carbon Restoration & Biomass Building (Slides 4–5):</strong> Coastal wetland restoration (mangroves, salt marshes, seagrasses) sequesters carbon up to 40 times faster per unit area than terrestrial forests. Engineered mass timber and cross-laminated bamboo in architecture lock carbon permanently into urban infrastructure.</p>
          <p><strong>4. Enhanced Rock Weathering & Ocean Liming (Slides 6–7):</strong> Natural silicate rock weathering absorbs ~3% of fossil emissions over geological epochs. Enhanced weathering pulverizes olivine or basalt into micro-particles ($<50\\,\\mu m$) spread across agricultural soils, reacting with rainwater to convert dissolved $CO_2$ into stable aqueous bicarbonate ($HCO_3^-$). Slide 6 also notes ocean treatment with potassium hydroxide (KOH) or 2.5 billion tonnes of limestone.</p>
        </div>
        """,
        "math_formula": "Mg_2SiO_4 \\text{ (Olivine)} + 4CO_2 + 4H_2O \\to 2Mg^{2+} + 4HCO_3^- + H_4SiO_4 \\quad (\\text{Enhanced Weathering Reaction})",
        "exam_checkpoint": "State the chemical reaction for Enhanced Silicate Weathering using olivine. Know the annual sequestration potential of biochar (up to 4.8 Gt CO2/year)."
    },
    {
        "unit_id": "u11_2",
        "title": "Direct Air Capture (DAC), Air-to-Fuels & Net Zero Teesside",
        "slide_range": "Slides 08–16",
        "slides_idx": [8, 9, 11, 13, 14, 15, 16],
        "takeaway": "Examines industrial carbon removal engineering: solid-sorbent and liquid-solvent DAC plants, synthetic hydrocarbon fuels, and subsea North Sea storage.",
        "synthesis": """
        <div class="space-y-3">
          <p><strong>1. Direct Air Capture Engineering (Slides 8, 13–14):</strong> DAC chemically extracts $CO_2$ directly from ambient air where concentration is dilute (~420 ppm or 0.042%). Two primary architectures dominate:</p>
            <ul class="list-disc pl-5 mt-1 space-y-1 text-slate-300">
              <li><strong>Solid Sorbent Systems (Climeworks Orca/Mammoth):</strong> Ambient air passes over amine-functionalized chemical filter matrices; mild thermal desorption ($100^\\circ\\text{C}$) releases concentrated $CO_2$.</li>
              <li><strong>Liquid Solvent Systems (Carbon Engineering):</strong> Uses potassium hydroxide (KOH) contactors reacting to form $K_2CO_3$, precipitated with calcium to form $CaCO_3$, then calcined at $900^\\circ\\text{C}$ in an oxy-fired kiln.</li>
            </ul>
          <p><strong>2. Air-to-Fuels & Air-Captured Diamonds (Slides 9, 15):</strong> Combining captured $CO_2$ with green hydrogen ($H_2$ produced via water electrolysis powered by renewables) through Fischer-Tropsch synthesis yields drop-in synthetic aviation fuels (SAF), diesel, and kerosene. Slide 15 highlights Aether Diamonds, which synthesizes certified vegan diamonds using $CO_2$ extracted directly from the atmosphere by Climeworks.</p>
          <p><strong>3. Net Zero Teesside Project (NZT, UK, Slide 16):</strong> A flagship industrial decarbonization cluster capturing up to 10 million tonnes of $CO_2$/year from industrial emitters, compressed into supercritical fluid, transported via pipeline, and sequestered permanently in saline aquifers deep beneath the North Sea.</p>
        </div>
        """,
        "math_formula": "CO_2 + 3H_2 \\xrightarrow{\\text{Catalyst, } \\Delta} -(\\text{CH}_2)-_n + 2H_2O \\quad \\text{(Fischer-Tropsch Synthetic Fuel)}",
        "exam_checkpoint": "Explain why DAC requires significantly higher thermodynamic energy than flue-gas scrubbing (ambient air is ~0.04% CO2 vs. coal flue gas at ~12-15% CO2, requiring higher minimum work of separation)."
    },
    {
        "unit_id": "u11_3",
        "title": "Cattle Methane Abatement, Insect Protein & Marine Cloud Brightening",
        "slide_range": "Slides 17–22",
        "slides_idx": [17, 18, 19, 20, 21, 22],
        "takeaway": "Analyzes enteric fermentation mitigation via seaweed, alternate insect proteins, marine cloud brightening, and low-PUE green datacenters.",
        "synthesis": """
        <div class="space-y-3">
          <p><strong>1. Livestock Decarbonization (Slides 17–18):</strong> Ruminant livestock produce 7.1 gigatons of GHG annually (~14.5% of total anthropogenic emissions), with beef cattle responsible for the vast majority via enteric fermentation. Feeding cattle tiny supplements (0.2–0.5% of feed) of red marine macroalgae (*Asparagopsis taxiformis*) inhibits the enzymatic pathway of methanogenic archaea in the rumen, reducing enteric methane emissions by up to 80% without affecting animal productivity.</p>
          <p><strong>2. Entomophagy & Alternative Protein (Slide 19):</strong> Replacing cattle feed and human meat consumption with farmed insects (e.g. grasshopper and black soldier fly larvae meal). Insect farming requires 90% less land, 80% less water, and produces a tiny fraction of GHG emissions per gram of protein compared to industrial beef.</p>
          <p><strong>3. Marine Cloud Brightening for Climate Repair (Slide 20):</strong> Geoengineering proposal to deploy autonomous ocean vessels that spray microscopic sub-micron sea-salt aerosol droplets into marine stratocumulus cloud decks over the oceans. The sea-salt crystals act as cloud condensation nuclei, brightening clouds and reflecting sunlight to refreeze polar ice.</p>
          <p><strong>4. Sustainable IT & Green Datacenters (Slide 22):</strong> Cloud platforms and machine learning infrastructure consume massive electrical power. Transitioning datacenters to liquid immersion cooling, locating them in cold climates, and optimizing Power Usage Effectiveness ($PUE = \\frac{\\text{Total Energy}}{\\text{IT Equipment Energy}} \\to 1.0$) drastically reduces computational carbon footprints.</p>
        </div>
        """,
        "math_formula": "PUE = \\frac{\\text{Total Facility Energy}}{\\text{IT Equipment Energy}} \\quad (\\text{Ideal: } PUE = 1.0; \\quad \\text{Average: } 1.5 - 1.8)",
        "exam_checkpoint": "Name the marine red algae (*Asparagopsis taxiformis*) used to suppress bovine enteric methane. Define Power Usage Effectiveness (PUE) in green datacenter design."
    },
    {
        "unit_id": "u11_4",
        "title": "Hydrogen Maritime Ships, Blockchain Tracking & Vertical Aeroponics",
        "slide_range": "Slides 23–29",
        "slides_idx": [23, 24, 25, 26, 27, 28, 29],
        "takeaway": "Evaluates zero-emission hydrogen transport, blockchain supply chain verification, vertical farming, and the XPRIZE Carbon Removal challenge.",
        "synthesis": """
        <div class="space-y-3">
          <p><strong>1. Hydrogen Propulsion & Floating Solar (Slide 23):</strong> Replacing heavy bunker fuel oil in maritime cargo shipping with green liquid hydrogen fuel cells. Floating Photovoltaic (FPV) arrays installed on water reservoirs reduce land competition while water cooling improves solar cell semiconductor efficiency by 5–15%.</p>
          <p><strong>2. Blockchain for Commodity Provenance (Slide 24):</strong> Integrating satellite remote sensing and GPS transponders with immutable distributed ledgers (blockchain) to verify that commodities (tuna catches, timber, palm oil) originate strictly from legal, non-deforested concessions, eradicating illegal supply chain laundering.</p>
          <p><strong>3. Vertical Urban Farming (Slides 25–27):</strong> Controlled Environment Agriculture (CEA) utilizing vertical tower modular structures. Combines LED targeted photosynthetically active radiation (PAR) spectra with soil-free cultivation:
            <ul class="list-disc pl-5 mt-1 space-y-1 text-slate-300">
              <li><strong>Hydroponics:</strong> Roots submerged in mineral-enriched circulating water.</li>
              <li><strong>Aeroponics:</strong> Roots suspended in air and misted with nutrient solution; saves 95% water and 90% land compared to conventional open-field agriculture.</li>
            </ul>
          </p>
          <p><strong>4. XPRIZE Carbon Removal (Slide 29):</strong> The $100 million XPRIZE funded by Elon Musk, challenging global innovators to demonstrate working carbon dioxide removal solutions with verifiable gigatonne-per-year scaling potential by 2050.</p>
        </div>
        """,
        "math_formula": "\\text{Water Efficiency Gain: } \\Delta W = \\frac{W_{\\text{field}} - W_{\\text{aeroponics}}}{W_{\\text{field}}} \\times 100\\% \\approx 95\\%",
        "exam_checkpoint": "Contrast Hydroponics vs. Aeroponics in vertical farming. Explain how blockchain paired with satellite remote sensing enforces zero-deforestation commodity verification."
    }
]

UNITS_LEC_12 = [
    {
        "unit_id": "u12_1",
        "title": "EIA Foundations, Baseline Environmental Dynamics & Activity Mapping",
        "slide_range": "Slides 01–07",
        "slides_idx": [1, 3, 4, 5, 6, 7],
        "takeaway": "Defines Environmental Impact Assessment (EIA), characterization of dynamic baseline environments, and the decomposition of activities into specific actions.",
        "synthesis": """
        <div class="space-y-3">
          <p><strong>1. Definition & Core Purpose of EIA (Slides 1, 7):</strong> Environmental Impact Assessment (EIA) is a systematic formal planning process used to identify, predict, evaluate, and mitigate the biophysical, social, and economic effects of proposed development projects <em>prior</em> to major decisions and commitments being made.</p>
          <p><strong>2. The Baseline Environment is Dynamic (Slides 3–4):</strong> A fundamental EIA error is treating the baseline situation as a static 'snapshot' in time. The baseline environment exhibits natural cyclical variations (seasonal monsoons, tidal cycles, annual temperature swings) and long-term evolutionary trends. The EIA must project the future state of the environment <em>without</em> the project versus <em>with</em> the project.</p>
          <p><strong>3. Activity Breakdown (Slide 6):</strong> An 'activity' is not analyzed in aggregate. It must be decomposed into discrete physical actions across all project phases (Pre-construction, Construction, Operation, Decommissioning): surveying, land clearing, grading, blasting, culvert construction, soil compaction, and hazardous effluent disposal.</p>
          <p><strong>4. Impact Attributes (Slide 5):</strong> Impacts are categorized across multiple dimensions: Direct (primary cause-effect, e.g. habitat destruction from road building) vs. Indirect (secondary/tertiary, e.g. subsequent illegal logging enabled by road access), Short-term vs. Long-term, Reversible vs. Irreversible, and Cumulative impacts.</p>
        </div>
        """,
        "math_formula": "\\text{Net Impact} = \\text{Future State with Project} - \\text{Future Projected Baseline without Project}",
        "exam_checkpoint": "Explain why the baseline environment in an EIA cannot be treated as a static snapshot. Distinguish with concrete examples between Direct and Indirect environmental impacts."
    },
    {
        "unit_id": "u12_2",
        "title": "Phase 1 EIA Protocols: Screening, Scoping & Preliminary Assessment",
        "slide_range": "Slides 08–16",
        "slides_idx": [8, 9, 11, 13, 14, 15, 16],
        "takeaway": "Examines project screening criteria, scoping terms of reference (ToR), and preliminary environmental assessment (PEA) thresholds.",
        "synthesis": """
        <div class="space-y-3">
          <p><strong>1. Screening (Slides 8, 11):</strong> The initial phase that determines whether a proposed project requires an EIA and at what level of detail. Projects are sorted into statutory categories:
            <ul class="list-disc pl-5 mt-1 space-y-1 text-slate-300">
              <li><strong>Category A:</strong> Projects with significant, irreversible, transboundary, or unprecedented adverse environmental impacts (e.g. nuclear power, large dams, chemical refineries); full EIA mandatory.</li>
              <li><strong>Category B:</strong> Projects with site-specific, largely reversible impacts; requires an Initial Environmental Examination (IEE) / Preliminary Assessment. May be escalated to Category A if sensitive receptors exist.</li>
              <li><strong>Category C:</strong> Projects with negligible environmental footprint; exempt from formal assessment.</li>
            </ul>
          </p>
          <p><strong>2. Scoping & Terms of Reference (ToR):</strong> Scoping defines the spatial boundaries, temporal horizons, key environmental issues, and methodologies to be investigated, ensuring the study focuses strictly on critical impacts.</p>
          <p><strong>3. Preliminary Environmental Assessment (PEA, Slides 13–15):</strong> A rapid, preliminary study conducted when impacts are uncertain. It identifies, predicts, and judges potential impacts against regulatory standards. Only if significant uncertainties or unmitigated impacts persist does the project advance to a Full EIA Study (Slide 16).</p>
        </div>
        """,
        "math_formula": "\\text{Screening Decision: } \\text{Project Type} + \\text{Scale/Investment} + \\text{Site Sensitivity} \\implies \\text{Cat A / B1 / B2 / C}",
        "exam_checkpoint": "Differentiate clearly between 'Screening' (determining if an EIA is required) and 'Scoping' (defining the spatial, temporal, and methodological boundaries of the study)."
    },
    {
        "unit_id": "u12_3",
        "title": "Phase 2 Full EIA Study, Stakeholder Participation & Mitigation",
        "slide_range": "Slides 17–22",
        "slides_idx": [17, 18, 19, 20, 21, 22],
        "takeaway": "Details the multi-disciplinary full EIA execution, public hearing protocols, the mitigation hierarchy, and the Environmental Management Plan (EMP).",
        "synthesis": """
        <div class="space-y-3">
          <p><strong>1. Full EIA Study Components (Slides 17–19):</strong> Involves baseline environmental monitoring (air quality sampling, seasonal water quality, terrestrial floristic/faunistic surveys, socio-economic baseline), mathematical dispersion modeling, and multi-criteria evaluation of project alternatives (including the 'No-Action' baseline alternative).</p>
          <p><strong>2. Stakeholder Involvement (Slide 20):</strong> Genuine EIA requires transparent participation of three key groups:
            <ul class="list-disc pl-5 mt-1 space-y-1 text-slate-300">
              <li><strong>Project Proponent:</strong> Commissions and funds the EIA study.</li>
              <li><strong>Regulatory Agencies:</strong> Review, issue Terms of Reference, and grant/deny Environmental Clearance.</li>
              <li><strong>Affected Public & Civil Society:</strong> Mandatory Public Hearings ensure local indigenous and resident concerns regarding displacement and pollution are addressed.</li>
            </ul>
          </p>
          <p><strong>3. Timing & The Mitigation Hierarchy (Slide 21):</strong> EIA must be undertaken early enough in the feasibility stage to fundamentally influence project engineering design and site selection. Follows the strict <strong>Mitigation Hierarchy</strong>: Avoid $\\to$ Minimize $\\to$ Rehabilitate $\\to$ Compensate/Offset. Formulates an enforceable Environmental Management Plan (EMP).</p>
        </div>
        """,
        "math_formula": "\\text{Leopold Matrix Impact Score: } S = \\sum_{i=1}^{m} \\sum_{j=1}^{n} M_{ij} \\times I_{ij} \\quad (M \\in [-10, 10], \\, I \\in [1, 10])",
        "exam_checkpoint": "Name the four levels of the Mitigation Hierarchy in exact order: 1. Avoid, 2. Minimize, 3. Rehabilitate, 4. Offset. Explain the role of the Environmental Management Plan (EMP)."
    },
    {
        "unit_id": "u12_4",
        "title": "Indian EIA Notification (1994, 2006), Schedule-1 & Buffer Siting Rules",
        "slide_range": "Slides 23–32",
        "slides_idx": [23, 24, 25, 26, 27, 28, 29, 30, 31],
        "takeaway": "Analyzes Indian statutory frameworks under the Environmental Protection Act 1986, Schedule-1 clearance lists, and strict buffer siting zones.",
        "synthesis": """
        <div class="space-y-3">
          <p><strong>1. Statutory Evolution in India (Slides 23–25):</strong> Promulgated by the Ministry of Environment, Forest and Climate Change (MoEFCC) under the landmark Environment (Protection) Act, 1986. The first formal EIA Notification in 1994 made environmental clearance mandatory for 29 project categories, subsequently overhauled by the EIA Notification 2006 which decentralized clearances into Category A (Central MoEFCC appraisal) and Category B (State Environment Impact Assessment Authority - SEIAA).</p>
          <p><strong>2. Schedule-1 Mandatory Clearance List (Slides 26–28):</strong> Specific project categories requiring mandatory Environmental Clearance from the Central Government:
            <ul class="list-disc pl-5 mt-1 space-y-1 text-slate-300">
              <li>Nuclear power plants and nuclear fuel complexes.</li>
              <li>Thermal power plants (>500 MW central, lower thresholds for coal).</li>
              <li>Mining projects (major minerals with lease area $>50$ hectares).</li>
              <li>Synthetic rubber, asbestos and asbestos-based manufacturing, chemical refineries, and pesticide manufacturing.</li>
            </ul>
          </p>
          <p><strong>3. Strict Environmental Siting Rules (Slides 29–30):</strong> Statutory spatial prohibitions:
            <ul class="list-disc pl-5 mt-1 space-y-1 text-slate-300">
              <li>Absolute prohibition on setting up polluting red-category industries within municipal limits.</li>
              <li>Mandatory 25 km buffer zone from ecologically sensitive areas (National Parks, Sanctuaries).</li>
              <li>Allowed in <strong>7 km to 25 km zone</strong> around wetlands and coastal ecosystems only with stringent effluent treatment conditions.</li>
            </ul>
          </p>
        </div>
        """,
        "math_formula": "\\text{Clearance Path: } \\begin{cases} \\text{Category A} \\implies \\text{EAC (MoEFCC Central)} \\\\ \\text{Category B1} \\implies \\text{SEAC / SEIAA (State Level)} \\\\ \\text{Category B2} \\implies \\text{No Full EIA (State Level)} \\end{cases}",
        "exam_checkpoint": "Know the parent act for EIA in India (Environment Protection Act, 1986). List 3 Schedule-1 project categories and cite the exact siting buffer rule (7 km to 25 km zone around wetlands with special clearances)."
    }
]
