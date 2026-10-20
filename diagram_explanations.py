# Deep pedagogical explanations for extracted slide diagrams across all 12 lectures

DIAGRAM_EXPLANATIONS = {
    "01": [
        {
            "image": "assets/diagrams/lec_01/diagram_01.jpeg",
            "title": "Decarbonization Imperative & Planetary Footprint Paradigm",
            "source": "Class-1 Overview.pdf, Slide 5",
            "what_it_shows": "This diagram contrasts human industrial resource extraction against planetary biocapacity boundaries, demonstrating how modern consumption exceeds Earth's ecological regeneration rate.",
            "scientific_mechanism": "Illustrates the IPAT paradigm ($I = P \\cdot A \\cdot T$). As global population ($P$) and affluence ($A$) expanded post-Industrial Revolution, resource extraction grew exponentially. Achieving environmental stability requires decoupling economic growth from environmental degradation through clean technology ($T$).",
            "quantitative_math": "Governed by the ecological overshoot equation: $\\text{Overshoot} = \\frac{\\text{Ecological Footprint} - \\text{Biocapacity}}{\\text{Biocapacity}} \\times 100\\%$. Global human demand currently operates at $\\sim 1.75$ Earth equivalents.",
            "exam_trap": "⚠️ <strong>Exam Trap:</strong> Do not confuse 'Biocapacity' with 'Total Land Area'. Biocapacity measures only biologically productive areas (cropland, grazing land, fishing grounds) capable of generating resources and absorbing waste."
        },
        {
            "image": "assets/diagrams/lec_01/diagram_02.jpeg",
            "title": "Ecological Fragility & Biodiversity Cascade",
            "source": "Class-1 Overview.pdf, Slide 7",
            "what_it_shows": "Depicts keystone species loss and trophic collapse resulting from habitat fragmentation and climate stress.",
            "scientific_mechanism": "Keystone species maintain the structural integrity of an ecological community. When apex or keystone organisms are removed, subordinate species proliferate uncontrolled or secondary extinctions cascade down trophic levels.",
            "quantitative_math": "Follows the species-area power relationship: $S = c A^z$, where $S$ is species richness, $A$ is habitat area, and $z \\approx 0.25 - 0.35$. A 90% reduction in habitat area leads to a roughly 50% loss of sustainable species capacity.",
            "exam_trap": "⚠️ <strong>Exam Trap:</strong> Remember that extinction debt refers to the future ecological extinction of species due to events that have already occurred."
        }
    ],

    "02": [
        {
            "image": "assets/diagrams/lec_02/diagram_01.jpeg",
            "title": "Natural Capital Depgradation & Material Flux Cycle",
            "source": "Class-2-Comprehend our Environment-Part-1.pdf, Slide 8",
            "what_it_shows": "Illustrates the linear 'Take-Make-Dispose' anthropogenic throughput versus the closed-loop circular material cycles of natural ecosystems.",
            "scientific_mechanism": "Human systems convert natural capital (lithospheric minerals, fossil carbon, biotic resources) into short-lived consumer goods and ultimate waste. In contrast, natural biogeochemical systems exhibit zero waste: every organism's metabolic byproduct is another organism's thermodynamic input.",
            "quantitative_math": "First and Second Laws of Thermodynamics: Total mass is conserved ($\\sum m_{\\text{in}} = \\sum m_{\\text{out}}$), but entropy increases ($\\Delta S_{\\text{universe}} > 0$). Dissipated low-grade heat and dispersed pollutants require work to reconcentrate.",
            "exam_trap": "⚠️ <strong>Exam Trap:</strong> Confusing 'Natural Capital' with 'Renewable Resources'. Natural capital includes non-renewable resources (fossil reserves, mineral ores) and ecosystem services (pollination, flood control) alongside renewable biomass."
        },
        {
            "image": "assets/diagrams/lec_02/diagram_02.jpeg",
            "title": "Domestic Material Footprint vs Economic Development",
            "source": "Class-2-Comprehend our Environment-Part-3.pdf, Slide 10",
            "what_it_shows": "Plots per-capita domestic material consumption across global income brackets, demonstrating resource decoupling challenges.",
            "scientific_mechanism": "Evaluates the Environmental Kuznets Curve (EKC) hypothesis. While some local air pollutants ($SO_2, PM$) decrease at higher per-capita income levels due to environmental regulations, aggregate carbon emissions and raw material footprints continue rising with GDP unless structural decoupling is enforced.",
            "quantitative_math": "Resource Intensity Index: $RI = \\frac{\\text{Domestic Material Consumption (DMC)}}{\\text{GDP}}$. Relative decoupling occurs when $RI$ decreases, but absolute decoupling requires total $DMC$ to decline while GDP grows.",
            "exam_trap": "⚠️ <strong>Exam Trap:</strong> Developing economies frequently appear to have lower domestic environmental impact because heavy manufacturing is outsourced; always evaluate consumption-based footprint (trade-adjusted) rather than territorial emissions alone."
        }
    ],

    "03": [
        {
            "image": "assets/diagrams/lec_03/diagram_01.jpeg",
            "title": "Kubuqi Model: Ecosystem Restoration & Desert Greening",
            "source": "Class-3 Enviromental issues-Part-2.pdf, Slide 3",
            "what_it_shows": "A schematic of multi-tiered ecological engineered barriers: solar photovoltaic arrays on sand dunes, drought-tolerant legume plantings (licorice/salix), and livestock integration.",
            "scientific_mechanism": "Solar PV panels provide shade, reducing soil evapotranspiration and surface temperatures. Condensate dripping from panel washing irrigates nitrogen-fixing leguminous herbs below, whose roots secrete organic glues that stabilize mobile sand particles and generate fertile topsoil.",
            "quantitative_math": "Soil water retention increases exponentially with organic matter: $\\theta_s = \\theta_0 (1 + \\gamma \\cdot \\text{SOC})$, while surface albedo shifts from high-reflectance sand ($\\alpha \\approx 0.40$) to dark productive vegetation ($\\alpha \\approx 0.18$), altering local boundary-layer microclimates.",
            "exam_trap": "⚠️ <strong>Exam Trap:</strong> Desertification is NOT simply the physical expansion of existing deserts; it is the degradation of fertile dryland ecosystems into non-productive soil driven by overgrazing, deforestation, and poor agricultural irrigation."
        },
        {
            "image": "assets/diagrams/lec_03/diagram_02.jpeg",
            "title": "Atmospheric Thermal Inversion & Smog Entrapment",
            "source": "Class-3 Enviromental issues-Part-1.pdf, Slide 5",
            "what_it_shows": "Shows the vertical atmospheric temperature profile during a radiation inversion layer, trapping particulate matter ($PM_{2.5}$) and $NO_x$ close to the urban floor.",
            "scientific_mechanism": "Under normal conditions, air temperature decreases with altitude (environmental lapse rate $\\Gamma \\approx -6.5^\\circ\\text{C/km}$), allowing warm, buoyant emissions to disperse upward. During calm, clear winter nights, rapid radiative cooling of the ground creates a cold layer beneath warmer air aloft (temperature inversion). Vertical mixing ceases, producing hazardous pollution episodes.",
            "quantitative_math": "Governed by the atmospheric stability parameter: $S = \\frac{dT}{dz} - \\Gamma_d$. When $\\frac{dT}{dz} > \\Gamma_d$ (where $\\Gamma_d = -9.8^\\circ\\text{C/km}$ is the dry adiabatic lapse rate), the atmosphere is stable, vertical eddy diffusivity $K_z \\to 0$, and pollutants accumulate.",
            "exam_trap": "⚠️ <strong>Exam Trap:</strong> Do not assume sunlight is needed for radiation inversions. Radiation inversions occur at <em>night</em> due to terrestrial infrared cooling to clear skies."
        }
    ],

    "04": [
        {
            "image": "assets/diagrams/lec_04/diagram_01.jpeg",
            "title": "Remote Sensing Electromagnetic Interaction & Sensor Geometry",
            "source": "Class-4-RS-EVS-upload.pdf, Slide 2",
            "what_it_shows": "A comprehensive diagram tracing solar radiant energy path: transmission through atmospheric windows, surface reflection/absorption, and detection by satellite sensors.",
            "scientific_mechanism": "Solar radiation travels through the atmosphere where it encounters Rayleigh scattering (by air molecules, proportional to $\\lambda^{-4}$), Mie scattering (by aerosols), and selective gaseous absorption ($O_3, CO_2, H_2O$). Only radiation passing through atmospheric windows reaches the ground and reflects back to the satellite detector.",
            "quantitative_math": "Radiance received at sensor: $L_{\\text{sensor}} = \\frac{1}{\\pi} \\rho \\tau_v (E_0 \\tau_s \\cos \\theta_s + E_{\\text{down}}) + L_p$, where $\\rho$ is surface reflectance, $\\tau$ is atmospheric transmittance, and $L_p$ is atmospheric path radiance.",
            "exam_trap": "⚠️ <strong>Exam Trap:</strong> Forgetting that Rayleigh scattering dominates the blue spectrum (giving sky its blue color and causing haze in satellite blue bands), while NIR radiation penetrates haze far more effectively."
        },
        {
            "image": "assets/diagrams/lec_04/diagram_02.jpeg",
            "title": "Spectral Reflectance Curves for Pure Environmental Endmembers",
            "source": "Class-4-RS-EVS-upload.pdf, Slide 6",
            "what_it_shows": "Curves comparing the percentage reflectance across visible, near-infrared (NIR), and shortwave infrared (SWIR) wavelengths for healthy vegetation, bare dry soil, and clear water.",
            "scientific_mechanism": "1. <strong>Vegetation:</strong> Low visible reflectance due to chlorophyll a/b absorption, sharp rise at 0.7 $\\mu$m (the Red Edge) to ~50% NIR reflectance from cellular scattering, and water absorption dips at 1.4 and 1.9 $\\mu$m. 2. <strong>Water:</strong> High absorption in NIR (reflectance near zero). 3. <strong>Soil:</strong> Smooth monotonic increase from visible into SWIR.",
            "quantitative_math": "The basis of NDVI: $NDVI = \\frac{\\rho_{\\text{NIR}} - \\rho_{\\text{Red}}}{\\rho_{\\text{NIR}} + \\rho_{\\text{Red}}}$. Because vegetation maximizes the difference between high NIR and low Red, NDVI is maximized (+0.7 to +0.9).",
            "exam_trap": "⚠️ <strong>Exam Trap:</strong> Turbid or sediment-laden water reflects visible light (green/red) much more than clear water, but still drops to nearly zero in the NIR spectrum."
        }
    ],

    "05": [
        {
            "image": "assets/diagrams/lec_05/diagram_02.jpeg",
            "title": "Global Distillation & Persistent Organic Pollutant (POP) Migration",
            "source": "Class-5 -Environmental Events.pdf, Slide 8",
            "what_it_shows": "The 'Grasshopper Effect' illustrating how volatile persistent toxic chemicals evaporate in warm tropical latitudes and condense in cold polar regions.",
            "scientific_mechanism": "Semivolatile organic pollutants (such as DDT, PCBs, and dioxins) undergo repeated cycles of volatilization during warm seasons and atmospheric transport via prevailing winds, followed by condensation and deposition during cold seasons. Because polar regions are perpetual cold condensation sinks, POPs concentrate in Arctic ice and fat-rich marine mammals.",
            "quantitative_math": "Governed by temperature-dependent vapor pressure (Clausius-Clapeyron relation): $\\ln\\left(\\frac{P_2}{P_1}\\right) = -\\frac{\\Delta H_{\\text{vap}}}{R} \\left( \\frac{1}{T_2} - \\frac{1}{T_1} \\right)$. Lower temperatures drive partitioning from gas phase into condensed environmental matrices.",
            "exam_trap": "⚠️ <strong>Exam Trap:</strong> Thinking polar regions are clean because there are no local factories. The Arctic Paradox demonstrates that the highest concentrations of lipophilic bioaccumulative toxics occur in Arctic Inuit populations and polar bears."
        },
        {
            "image": "assets/diagrams/lec_05/diagram_03.jpeg",
            "title": "Biomagnification Trophic Cascade in Aquatic Ecosystems",
            "source": "Class-5 -Environmental Events.pdf, Slide 14",
            "what_it_shows": "A multi-level food web showing concentration amplification of methylmercury from water (parts per trillion) to apex predators and humans (parts per million).",
            "scientific_mechanism": "Methylmercury ($[CH_3Hg]^+$) is lipid-soluble and binds covalently to sulfhydryl ($-SH$) groups in muscle protein. Organisms absorb it much faster than they can metabolize or excrete it (half-life in humans is ~70 days). Each successive trophic level consumes multiple prey organisms, compounding toxic concentration.",
            "quantitative_math": "Trophic Magnification Factor: $TMF = 10^{\\beta}$, where $\\beta$ is the slope of the regression $\\log(C) = \\alpha + \\beta \\times TL$ ($TL$ = trophic level). For methylmercury, $TMF$ typically exceeds 3.5 to 5.0 per trophic transfer.",
            "exam_trap": "⚠️ <strong>Exam Trap:</strong> Confusing elemental inorganic mercury ($Hg^0$) with methylmercury. Metallic mercury swallowed passes through digestive systems largely unabsorbed; microbial methylation in anoxic sediment is what creates the lethal neurotoxin."
        }
    ],

    "06": [
        {
            "image": "assets/diagrams/lec_06/diagram_01.png",
            "title": "Interactive Earth System Spheres & Geochemical Couplings",
            "source": "Class-6 Earth components-part-1.pdf, Slide 8",
            "what_it_shows": "A systems flow diagram detailing mass and energy feedback loops linking the Atmosphere, Hydrosphere, Cryosphere, Lithosphere, and Biosphere.",
            "scientific_mechanism": "Demonstrates that environmental science cannot analyze components in isolation. For instance, volcanic eruptions in the Lithosphere emit $SO_2$ into the Atmosphere, altering cloud albedo, cooling the Hydrosphere, and perturbing primary productivity in the Biosphere.",
            "quantitative_math": "Mass balance for any geochemical reservoir $i$: $\\frac{dM_i}{dt} = \\sum F_{\\text{in}} - \\sum F_{\\text{out}}$. At steady state, residence time is $\\tau_i = \\frac{M_i}{\\sum F_{\\text{out}}}$.",
            "exam_trap": "⚠️ <strong>Exam Trap:</strong> Do not overlook that residence time is reservoir-dependent: water in the atmosphere has a residence time of ~9 days, but in deep oceans it exceeds 3,000 years."
        },
        {
            "image": "assets/diagrams/lec_06/diagram_02.jpeg",
            "title": "The Global Nitrogen Cycle & Anthropogenic Haber-Bosch Forcing",
            "source": "Class-6 Earth components-Part-2.pdf, Slide 28",
            "what_it_shows": "The complete biogeochemical pathway of Nitrogen, detailing biological fixation, Haber-Bosch synthesis, nitrification, plant uptake, and anaerobic denitrification.",
            "scientific_mechanism": "Industrial Haber-Bosch synthesis ($N_2 + 3H_2 \\to 2NH_3$) currently fixes $\\sim 150\\,\\text{Tg N/yr}$, rivaling all natural terrestrial fixation combined. Excess fertilizer drains into rivers, creating eutrophication, while soil nitrification/denitrification leaks nitrous oxide ($N_2O$, a potent greenhouse gas).",
            "quantitative_math": "Stoichiometric Nitrification: $NH_4^+ + 2O_2 \\longrightarrow NO_3^- + 2H^+ + H_2O$. Notice that 2 moles of $H^+$ are released per mole of ammonium oxidized, explaining why heavy ammonium fertilizer usage severely acidifies agricultural soils.",
            "exam_trap": "⚠️ <strong>Exam Trap:</strong> Nitrification is an <strong>acidifying aerobic</strong> oxidation process, whereas Denitrification is an <strong>alkalizing anaerobic</strong> reduction process requiring organic carbon."
        }
    ],

    "07": [
        {
            "image": "assets/diagrams/lec_07/diagram_01.jpeg",
            "title": "Components of the Climate System & Radiative Feedback Loops",
            "source": "Class-7 Climate Change impacts.pdf, Slide 4",
            "what_it_shows": "A schematic of radiative fluxes, sensible and latent heat exchange, and coupled cloud and ocean thermal feedback loops.",
            "scientific_mechanism": "Incoming shortwave solar flux ($340\\,\\text{W/m}^2$) is partitioned between surface absorption ($161\\,\\text{W/m}^2$), atmospheric absorption ($78\\,\\text{W/m}^2$), and reflection ($100\\,\\text{W/m}^2$). The heated surface returns energy via latent heat of evaporation ($84\\,\\text{W/m}^2$), thermals ($20\\,\\text{W/m}^2$), and longwave thermal infrared.",
            "quantitative_math": "Global surface energy budget equation: $R_n = H + LE + G$, where $R_n$ is net radiant energy, $H$ is sensible heat flux, $LE$ is latent heat flux, and $G$ is ground conduction heat flux.",
            "exam_trap": "⚠️ <strong>Exam Trap:</strong> Latent heat flux ($LE$) is the largest single non-radiative mechanism transferring heat from Earth's surface to the troposphere, driving global precipitation."
        },
        {
            "image": "assets/diagrams/lec_07/diagram_02.jpeg",
            "title": "Radiative Forcing Bar Chart by Anthropogenic Driver",
            "source": "Class-7 Climate Change impacts.pdf, Slide 11",
            "what_it_shows": "IPCC breakdown of radiative forcing contributions from greenhouse gases ($CO_2, CH_4, N_2O$, halocarbons) contrasted against cooling aerosol effects.",
            "scientific_mechanism": "$CO_2$ provides the largest positive forcing ($+2.16\\,\\text{W/m}^2$), followed by methane ($+0.54\\,\\text{W/m}^2$). In contrast, sulfur dioxide and organic carbon aerosols reflect sunlight directly and brighten clouds (indirect aerosol effect), exerting a masking cooling forcing of $\\sim -1.1\\,\\text{W/m}^2$.",
            "quantitative_math": "Total Net Anthropogenic Radiative Forcing: $\\Delta F_{\\text{total}} = \\sum \\Delta F_{\\text{GHG}} + \\Delta F_{\\text{aerosol}} \\approx +2.72\\,\\text{W/m}^2$ (relative to 1750).",
            "exam_trap": "⚠️ <strong>Exam Trap:</strong> As coal power plants install flue gas desulfurization (scrubbers) to eliminate acid rain ($SO_2$), the negative aerosol cooling mask is unpeeled, accelerating greenhouse warming."
        }
    ],

    "08": [
        {
            "image": "assets/diagrams/lec_08/diagram_01.jpeg",
            "title": "Global Map of Planetary Climate Tipping Elements",
            "source": "Class-8 Unexpected climate changes.pdf, Slide 6",
            "what_it_shows": "A world map identifying the 9 core continental tipping subsystems: AMOC, Greenland Ice Sheet, West Antarctic Ice Sheet, Amazon Rainforest, Boreal Permafrost, Coral Reefs, and Indian Monsoon.",
            "scientific_mechanism": "Tipping elements are planetary subsystems that can be pushed past a critical threshold into a qualitatively different operational state. These elements are interconnected through 'teleconnections': Greenland melting freshens the North Atlantic, slowing down AMOC, which shifts tropical rainfall belts southward, desiccating the Amazon basin and destabilizing the Indian Monsoon.",
            "quantitative_math": "Coupled non-linear dynamical systems exhibiting tipping cascades: $\\frac{dx_i}{dt} = f_i(x_i) + \\sum_{j \\neq i} c_{ij} x_j$, where $c_{ij}$ is the coupling coefficient between tipping element $i$ and $j$.",
            "exam_trap": "⚠️ <strong>Exam Trap:</strong> Tipping elements do NOT act as independent risks. One tipping event significantly lowers the temperature threshold for adjacent tipping elements, creating cascade vulnerability."
        },
        {
            "image": "assets/diagrams/lec_08/diagram_03.jpeg",
            "title": "Marine Ice Sheet Instability (MISI) & Ice Shelf Grounding Collapse",
            "source": "Class-8 Unexpected climate changes.pdf, Slide 14",
            "what_it_shows": "Cross-section of the West Antarctic Ice Sheet showing retrograde (inward-sloping) bedrock topography and warm circumpolar deep water intrusion.",
            "scientific_mechanism": "Because the bedrock slopes downwards towards the continental interior, as the grounding line retreats into deeper water, the ice thickness at the marine boundary increases. Ice flux across the grounding line scales with the fourth power of ice thickness ($Q \\propto h^4$), triggering uncontrollable, runaway ice sheet discharge regardless of atmospheric warming.",
            "quantitative_math": "Weertman's ice grounding flux law: $q_g = \\rho_i h_g u_g \\propto h_g^{m}$ ($m \\approx 4 - 5$). An inward-sloping bed ($dh/dx < 0$) guarantees positive feedback instability.",
            "exam_trap": "⚠️ <strong>Exam Trap:</strong> Floating ice shelves provide back-stress (buttressing) that holds back the grounded continental ice sheet. Calving of floating shelves removes this back-stress, accelerating inland glaciers."
        }
    ],

    "09": [
        {
            "image": "assets/diagrams/lec_09/diagram_01.jpeg",
            "title": "Glacial Recession & Terrestrial Cryosphere Mass Loss",
            "source": "Class-9- Carbon sequestration.pdf, Slide 4",
            "what_it_shows": "Historical photographic and topographic comparative transect of Muir Glacier showing dramatic multi-kilometer retreat between 1941 and modern times.",
            "scientific_mechanism": "Visualizes the physical reality of cryospheric shrinkage. Glaciers act as natural freshwater storage towers; recession alters seasonal river discharge hydrographs from summer melt-dominated flows to flash winter floods followed by severe summer water shortages.",
            "quantitative_math": "Glacier Mass Balance: $B_n = \\int (A - M)\\,dt$, where $A$ is accumulation (snowfall) and $M$ is ablation (melting and sublimation). Negative mass balance shifts the Equilibrium Line Altitude (ELA) upslope.",
            "exam_trap": "⚠️ <strong>Exam Trap:</strong> Glacial retreat initially causes a temporary <em>increase</em> in downstream river discharge ('peak water') before experiencing permanent, irreversible flow collapse."
        },
        {
            "image": "assets/diagrams/lec_09/diagram_02.jpeg",
            "title": "Terrestrial Forest Carbon Stock & Flux Dynamics",
            "source": "Class-9- Carbon sequestration.pdf, Slide 15",
            "what_it_shows": "A global 1° × 1° spatial modeling grid evaluating above-ground biomass, root carbon, and soil organic carbon flux across diverse forest biomes.",
            "scientific_mechanism": "Quantifies Net Ecosystem Productivity ($NEP = GPP - R_a - R_h$), where $GPP$ is gross primary productivity, $R_a$ is autotrophic plant respiration, and $R_h$ is heterotrophic microbial soil respiration. In mature climax forests, $NEP \\to 0$ (carbon saturation), whereas young, actively growing secondary forests exhibit high net sequestration rates.",
            "quantitative_math": "Carbon residence time in woody biomass: $\\tau = \\frac{B_{\\text{woody}}}{NPP}$. For tropical rainforests, $\\tau \\approx 30 - 50\\,\\text{years}$; for boreal conifer forests, $\\tau \\approx 80 - 120\\,\\text{years}$.",
            "exam_trap": "⚠️ <strong>Exam Trap:</strong> Planting trees in high-latitude snow-covered tundra (afforestation) can actually cause planetary <em>warming</em> by replacing high-albedo bright snow with dark tree canopies, outweighing the carbon sequestration benefit."
        }
    ],

    "10": [
        {
            "image": "assets/diagrams/lec_10/diagram_02.jpeg",
            "title": "Clean Development Mechanism (CDM) Architectural Flowchart",
            "source": "Class-10- CDM.pdf, Slide 13",
            "what_it_shows": "A complete operational flowchart showing financial and credit flows between Annex I developed investor countries and non-Annex I developing host nations under the Kyoto Protocol.",
            "scientific_mechanism": "Developed nations provide capital investment and clean technology to build emission-reduction projects in developing nations. The quantified emission reductions are verified by independent Designated Operational Entities (DOEs) and issued by the UN as Certified Emission Reductions (CERs).",
            "quantitative_math": "CER Generation Formula: $CER = BE - PE - LE$, where $BE$ is baseline emissions under business-as-usual, $PE$ is actual measured project emissions, and $LE$ is leakage occurring outside the project boundary.",
            "exam_trap": "⚠️ <strong>Exam Trap:</strong> To qualify, a project must demonstrate 'Financial Additionality'—meaning it would have been financially unviable without the anticipated revenue from carbon credit sales."
        },
        {
            "image": "assets/diagrams/lec_10/diagram_03.jpeg",
            "title": "Ocean Carbon Pumps & Deep-Sea CO₂ Injection Thermodynamics",
            "source": "Class-10b-Ocean Sequestration.pdf, Slide 8",
            "what_it_shows": "A depth profile of the ocean showing atmospheric $CO_2$ dissolution, the biological pump (marine snow), and phase behavior of injected liquid $CO_2$.",
            "scientific_mechanism": "Liquid $CO_2$ is highly compressible compared to seawater. At depths less than ~3000 m, liquid $CO_2$ is less dense than surrounding water and floats upwards. Below 3000 m (pressures >300 atmospheres), liquid $CO_2$ becomes denser than seawater ($>1028\\,\\text{kg/m}^3$) and sinks to the seafloor, forming negative-buoyancy hydrate lakes.",
            "quantitative_math": "Density crossover depth: $\\rho_{CO_2}(T, P) = \\rho_{\\text{seawater}}(T, P, S)$. Injected $CO_2$ dissolves into bottom water, forming carbonic acid: $CO_2 + H_2O \\rightleftharpoons H^+ + HCO_3^-$, causing severe localized benthic acidification (pH drop of 0.5 to 1.5 units).",
            "exam_trap": "⚠️ <strong>Exam Trap:</strong> Deep ocean injection does not isolate carbon permanently forever; ocean thermohaline overturning will return deep water to the surface in approximately 500 to 1,000 years."
        }
    ],

    "11": [
        {
            "image": "assets/diagrams/lec_11/diagram_01.jpeg",
            "title": "Biochar Pyrolysis & Recalcitrant Carbon Chemistry",
            "source": "Class-11-Climate Change-Technology Solutions.pdf, Slide 5",
            "what_it_shows": "A molecular and process schematic illustrating the thermochemical conversion of labile plant biomass into polycyclic aromatic biochar under oxygen-free pyrolysis.",
            "scientific_mechanism": "Raw plant biomass decomposes in soil within 2–5 years, releasing $CO_2$ back to the atmosphere. Pyrolysis at 500–600°C removes hydrogen and oxygen, condensing aliphatic carbon chains into fused aromatic benzene-ring clusters that soil microbes cannot readily enzymatically cleave.",
            "quantitative_math": "Carbon stability index: $O:C$ molar ratio. Fresh biomass has $O:C \\approx 0.6 - 0.8$. Quality biochar achieved via pyrolysis has $O:C < 0.20$, guaranteeing a soil half-life $>1000\\,\\text{years}$.",
            "exam_trap": "⚠️ <strong>Exam Trap:</strong> Slow pyrolysis yields ~35% biochar, 30% bio-oil, and 35% syngas. Fast pyrolysis (seconds) maximizes liquid bio-oil, NOT solid biochar."
        },
        {
            "image": "assets/diagrams/lec_11/diagram_02.jpeg",
            "title": "Blue Carbon Coastal Ecosystem Sequestration",
            "source": "Class-11-Climate Change-Technology Solutions.pdf, Slide 8",
            "what_it_shows": "Cross-section of coastal mangrove, tidal salt marsh, and seagrass meadow ecosystems detailing sediment carbon accumulation.",
            "scientific_mechanism": "Coastal wetlands sequester carbon at rates up to 10 times higher per hectare than terrestrial tropical forests. Their soils are perpetually waterlogged and anoxic, preventing microbial oxidation and allowing organic sediment to accumulate continuously over millennia without saturating.",
            "quantitative_math": "Carbon burial rate: $C_{\\text{burial}} = \\rho_{\\text{bulk}} \\times \\text{SAR} \\times \\%C_{\\text{org}}$, where $\\rho_{\\text{bulk}}$ is soil bulk density, $\\text{SAR}$ is sediment accretion rate ($2 - 10\\,\\text{mm/yr}$), and $\\%C_{\\text{org}}$ is organic carbon percentage.",
            "exam_trap": "⚠️ <strong>Exam Trap:</strong> Draining coastal mangroves for shrimp farming or real estate exposes centuries of anoxic carbon to air, causing massive immediate $CO_2$ pulse releases."
        }
    ],

    "12": [
        {
            "image": "assets/diagrams/lec_12/diagram_03.jpeg",
            "title": "Environmental Baseline & Impact Prediction Trajectory",
            "source": "Class-12 EIA.pdf, Slide 10",
            "what_it_shows": "A temporal trend chart comparing the future environmental quality trajectory 'Without Project' (baseline trend) versus 'With Project' (adverse degradation) versus 'With EMP Mitigation'.",
            "scientific_mechanism": "Demonstrates the core philosophy of EIA: an environmental impact is NOT measured by comparing environmental quality after the project against the initial state ($T_0$). It must be measured against what the environment <em>would have been</em> at time $T$ in the absence of the project.",
            "quantitative_math": "True Environmental Impact: $\\Delta EI(t) = EQ_{\\text{with project}}(t) - EQ_{\\text{without project}}(t)$. Mitigation efficiency: $\\eta_{\\text{EMP}} = \\frac{EQ_{\\text{mitigated}} - EQ_{\\text{unmitigated}}}{EQ_{\\text{baseline}} - EQ_{\\text{unmitigated}}} \\times 100\\%$.",
            "exam_trap": "⚠️ <strong>Exam Trap:</strong> Evaluating impact purely as post-project status minus pre-project status. If the baseline environment was already deteriorating independently (e.g. existing urban groundwater depletion), failing to model the 'Without Project' baseline skews the assessment."
        },
        {
            "image": "assets/diagrams/lec_12/diagram_01.png",
            "title": "EIA Statutory Clearance Flowchart & Review Matrix",
            "source": "Class-12 EIA.pdf, Slide 2",
            "what_it_shows": "The complete statutory workflow under India's EIA Notification 2006, from Application (Form 1) through Screening, Scoping, Draft EIA, Public Consultation, Final EIA, and Expert Appraisal Committee (EAC) clearance.",
            "scientific_mechanism": "Provides institutional governance checkpoints ensuring public transparency and engineering accountability. The State Pollution Control Board (SPCB) facilitates the public hearing and submits the verbatim video and proceedings to MoEFCC within 45 days.",
            "quantitative_math": "Statutory timeline: Scoping (TOR issued within 60 days), Public Hearing (45 days), Final Appraisal by EAC (60 days), Total regulatory turnaround target: 105 to 180 days.",
            "exam_trap": "⚠️ <strong>Exam Trap:</strong> Category B2 projects are exempt from EIA studies, but they are NOT exempt from obtaining Environmental Clearance (EC) from the SEIAA based on Form 1 and EMP."
        }
    ]
}
print("Diagram explanations loaded.")
