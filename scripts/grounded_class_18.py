"""
Class 18: Natural Resource Accounting & Geospatial Technology
Grounded Question Bank Module
Strictly audited against official lecture slides (Class-18-NRA-Geospatial.pdf, 25 slides).
Zero external hallucinations. Comprehensive, unclipped detailed answers with full case study calculations.
"""

def get_class18_grounded_questions():
    return [
        {
            "id": "EQB-18-01",
            "class_id": 18,
            "class_name": "Natural Resource Accounting & Geospatial Technology",
            "topic": "Remote Sensing Definition & Principles in Natural Resource Accounting",
            "category": "Short Answer & Definitions",
            "exams": [
                {"paper": "End Exam 2019", "section": "Section I, Q1", "marks": "1M"}
            ],
            "marks": "1M",
            "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
            "prompt": "Define Remote sensing.",
            "key_answer_points": "<ul>\n"
                                 "<li><strong>Definition:</strong> Remote Sensing is the science and art of acquiring data and information about physical objects, land surfaces, water bodies, or environmental phenomena from a distance—<strong>without making direct physical contact</strong> with them—primarily by recording reflected or emitted electromagnetic radiation (EMR) using sensors mounted on aircraft or satellite platforms.</li>\n"
                                 "<li><strong>Physical Workflow:</strong> Solar radiation / EMR source $\\rightarrow$ Atmospheric transmission $\\rightarrow$ Surface interaction (absorption, reflection, transmission) $\\rightarrow$ Spaceborne sensor detection across multispectral bands $\\rightarrow$ Telemetry data downlink $\\rightarrow$ Digital image processing and thematic mapping.</li>\n"
                                 "<li><strong>Role in Natural Resource Accounting (NRA):</strong> Provides a continuous, scalable, and verifiable method to quantify the physical depletion and degradation of natural capital stocks (forests, water bodies, wetlands) over time, overcoming the severe cost, time, and accessibility bottlenecks of conventional field surveys.</li>\n"
                                 "</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n"
                               "<p><strong>What is Remote Sensing?</strong></p>\n"
                               "<p>Remote sensing is the science, technology, and art of obtaining dependable information about the Earth's surface, atmosphere, and aquatic resources without coming into direct physical contact with the object of study. This is achieved by detecting, recording, and analyzing electromagnetic radiation (EMR) that is either reflected (in visible, near-infrared, and shortwave-infrared bands) or emitted (in thermal infrared bands) from Earth surface features.</p>\n"
                               "<h4>Physical Mechanism and the Remote Sensing Workflow</h4>\n"
                               "<p>The acquisition of satellite Earth observation data relies on an unbroken chain of physical interactions:</p>\n"
                               "<ol>\n"
                               "<li><strong>Energy Source:</strong> The primary passive source is the Sun, illuminating the Earth with electromagnetic radiation across multiple wavelengths—ranging from visible light (0.4–0.7 $\\mu\\text{m}$) to Near-Infrared (NIR: 0.7–1.1 $\\mu\\text{m}$), Shortwave-Infrared (SWIR: 1.1–3.0 $\\mu\\text{m}$), and Thermal Infrared (TIR: 8–14 $\\mu\\text{m}$). Active sensors (like radar/SAR) emit their own microwave pulses.</li>\n"
                               "<li><strong>Atmospheric Transmission:</strong> Radiation passes through the atmosphere twice (downwelling to Earth and upwelling to the sensor), selectively transmitting through specific 'atmospheric transmission windows' while being partially scattered by aerosols and absorbed by water vapor, ozone, and carbon dioxide.</li>\n"
                               "<li><strong>Surface Interaction:</strong> When incident radiation strikes an Earth surface feature (tree canopy, soil, or lake), energy is conserved according to the fundamental balance:\n"
                               "<div class=\"formula-box\">$$E_{\\text{incident}}(\\lambda) = E_{\\text{reflected}}(\\lambda) + E_{\\text{absorbed}}(\\lambda) + E_{\\text{transmitted}}(\\lambda)$$</div>\n"
                               "Every natural material exhibits a distinct, wavelength-dependent pattern of reflectance and absorption (its unique 'spectral signature').</li>\n"
                               "<li><strong>Sensor Recording & Telemetry:</strong> Spaceborne electro-optical sensors (such as Landsat, Sentinel, or MODIS) divide incoming EMR into narrow spectral channels (bands), convert photon energy into digital numbers (DNs), and beam the data to ground receiving stations.</li>\n"
                               "<li><strong>Processing & Thematic Classification:</strong> Digital image processing converts raw data into surface reflectance, vegetation indices (e.g., NDVI), and classified land use/land cover (LULC) maps.</li>\n"
                               "</ol>\n"
                               "<h4>Why Remote Sensing is Indispensable for Natural Resource Accounting (NRA)</h4>\n"
                               "<p>Natural Resource Accounting (NRA) is defined as the systematic process of estimating the value of natural resource depletion and environmental degradation resulting from economic activities (UNESCWA, SEEA). Conventional ground surveys suffer from critical limitations:</p>\n"
                               "<ul>\n"
                               "<li><strong>High cost & time-consuming:</strong> Measuring thousands of square kilometers of forest or remote wetlands on foot requires massive labor, prolonged field campaigns, and exorbitant budgets.</li>\n"
                               "<li><strong>Limited spatial coverage:</strong> Field teams can only sample discrete points or linear transects, missing widespread landscape fragmentation and regional ecological dynamics.</li>\n"
                               "<li><strong>Data inconsistency:</strong> Manual surveys introduce surveyor bias, varying field methodologies, and subjective qualitative estimates.</li>\n"
                               "<li><strong>Slow update cycles:</strong> Traditional census and forest inventories often take 5 to 10 years between updates, making timely policy interventions and real-time environmental auditing impossible.</li>\n"
                               "<li><strong>Accessibility challenges:</strong> Dense tropical forests, steep Himalayan terrains, and fragile wetland interiors (such as Ashtamudi or Vembanad) are physically hazardous or inaccessible to human field auditors.</li>\n"
                               "</ul>\n"
                               "<p>Geospatial remote sensing directly eliminates these limitations by offering <strong>cost-effective, scalable, frequent, objective, and verifiable</strong> observations. Satellite sensors provide synoptic, wall-to-wall spatial coverage with regular temporal revisit cycles (5 to 16 days), creating an immutable, repeatable baseline to measure natural capital stocks and flows across decades.</p>\n"
                               "<p><em>Slide Reference: Class 18, Slides 1, 4, 7–9.</em></p>\n"
                               "</div>"
        },
        {
            "id": "EQB-18-02",
            "class_id": 18,
            "class_name": "Natural Resource Accounting & Geospatial Technology",
            "topic": "Vegetation & Water in Infrared FCC Satellite Imagery",
            "category": "Short Answer & Definitions",
            "exams": [
                {"paper": "End Exam 2019", "section": "Section I, Q2", "marks": "2M"}
            ],
            "marks": "2M",
            "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
            "prompt": "How vegetation and deeper water bodies appear in infrared composite satellite data?",
            "key_answer_points": "<ul>\n"
                                 "<li><strong>Standard False Color Composite (FCC) Channel Mapping:</strong>\n"
                                 "<br>• Red Display Channel $\\leftarrow$ <strong>Near-Infrared (NIR) Band</strong> ($\approx 0.76\\text{--}0.90\\ \\mu\\text{m}$)\n"
                                 "<br>• Green Display Channel $\\leftarrow$ <strong>Visible Red Band</strong> ($\approx 0.63\\text{--}0.69\\ \\mu\\text{m}$)\n"
                                 "<br>• Blue Display Channel $\\leftarrow$ <strong>Visible Green Band</strong> ($\approx 0.52\\text{--}0.60\\ \\mu\\text{m}$)</li>\n"
                                 "<li><strong>Appearance of Healthy Green Vegetation:</strong>\n"
                                 "<br>• <strong>Appears:</strong> <strong>Vibrant Bright Red / Crimson / Magenta</strong>.\n"
                                 "<br>• <strong>Biophysical Reason:</strong> Photosynthetic pigments (chlorophyll $a$ and $b$) strongly absorb visible red and blue photons, but plant leaves reflect <strong>40% to 60% of incident Near-Infrared (NIR)</strong> radiation due to multiple scattering within internal spongy mesophyll cell walls (preventing fatal solar overheating). Because high NIR reflectance is mapped to the Red visual channel, dense, healthy foliage glows bright red.</li>\n"
                                 "<li><strong>Appearance of Deeper Clear Water Bodies:</strong>\n"
                                 "<br>• <strong>Appears:</strong> <strong>Jet Black to Very Dark Navy Blue</strong>.\n"
                                 "<br>• <strong>Optical Reason:</strong> Pure, deep water strongly absorbs nearly 100% of incident Near-Infrared and Shortwave-Infrared radiation within the first few centimeters of the water column ($R_{\\text{NIR}} \\approx 0$). Since near-zero energy is recorded in the NIR channel (which drives the Red display gun) and minimal visible light is reflected, deep clear water displays as pitch black.</li>\n"
                                 "<li><strong>Contrast with Turbid Water & Built-Up Surfaces:</strong> Shallow or sediment-laden water reflects scattered green/red light, appearing cyan or light blue; urban concrete and barren soil reflect evenly across visible bands, displaying as grey, cyan, or white.</li>\n"
                                 "</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n"
                               "<p><strong>Understanding Standard False Color Composite (FCC) Satellite Imagery</strong></p>\n"
                               "<p>The human eye is biologically restricted to visible light (wavelengths between 0.4 and 0.7 $\\mu\\text{m}$). However, the most critical diagnostic information regarding ecological health, vegetation vigor, and aquatic boundaries occurs in the invisible Near-Infrared (NIR: 0.7–1.1 $\\mu\\text{m}$) spectrum. To make this invisible information visually interpretable, satellite image processors construct a <strong>Standard False Color Composite (FCC)</strong> (also known as Color-Infrared or CIR composite) by shifting bands into primary display channels:</p>\n"
                               "<ul>\n"
                               "<li><strong>Red Screen Gun $\\leftarrow$ Near-Infrared (NIR) band</strong></li>\n"
                               "<li><strong>Green Screen Gun $\\leftarrow$ Visible Red band</strong></li>\n"
                               "<li><strong>Blue Screen Gun $\\leftarrow$ Visible Green band</strong></li>\n"
                               "</ul>\n"
                               "<h4>1. Appearance and Biophysical Mechanics of Healthy Vegetation</h4>\n"
                               "<p>In standard FCC imagery, healthy green vegetation displays as <strong>striking, brilliant red or vivid magenta</strong>.</p>\n"
                               "<ul>\n"
                               "<li><strong>Chlorophyll Absorption in the Visible Spectrum:</strong> In the visible red channel (around 0.66 $\\mu\\text{m}$), plant leaf chloroplasts contain chlorophyll pigments that absorb over 85–90% of incident light to drive the light reactions of photosynthesis.</li>\n"
                               "<li><strong>Spongy Mesophyll Scattering in the NIR Spectrum:</strong> In the near-infrared spectrum (0.76–0.90 $\\mu\\text{m}$), photon energy is too low to drive photosynthesis, yet high enough to heat up and kill leaf tissue if absorbed. Evolution has equipped leaves with an internal spongy mesophyll layer composed of loosely packed, irregularly shaped cells interleaved with air-filled voids. The sharp refractive index difference between hydration-filled cell walls ($n \\approx 1.4$) and internal air cavities ($n \\approx 1.0$) causes intense internal refraction and diffuse backscattering. Healthy leaves reflect between <strong>40% and 60%</strong> of incident NIR radiation.</li>\n"
                               "<li><strong>The 'Red Edge':</strong> At the boundary between 680 nm (chlorophyll red absorption trough) and 730 nm (mesophyll NIR reflection plateau), leaf reflectance jumps abruptly by 400% to 500%. Because this enormous NIR reflectance is piped directly into the monitor's Red color gun, areas with dense canopy cover (such as the Kondapalli Reserve Forest or Kerala wetland mangroves) glow bright red.</li>\n"
                               "</ul>\n"
                               "<h4>2. Appearance and Optical Mechanics of Deeper Water Bodies</h4>\n"
                               "<p>In sharp contrast to vegetation, deep, clear water bodies (such as pristine sections of Ashtamudi Wetland, Sasthamkotta Lake, or coastal lagoons) appear <strong>jet black, dark navy, or deep indigo</strong>.</p>\n"
                               "<ul>\n"
                               "<li><strong>Total NIR Absorption:</strong> Liquid water possesses intense molecular vibrational absorption bands in the infrared. As wavelength increases beyond 0.7 $\\mu\\text{m}$, water's absorption coefficient increases by orders of magnitude. Within the top 5 to 10 centimeters of water, incoming near-infrared radiation is virtually 100% absorbed and converted into thermal energy.</li>\n"
                               "<li><strong>Zero NIR Signal:</strong> As a result, the water surface reflects almost zero NIR photons back up to the spaceborne detector ($R_{\\text{NIR}} \\approx 0$).</li>\n"
                               "<li><strong>Display Result:</strong> Because the Red channel receives a digital value near zero ($0$), and clean deep water reflects very little visible red or green light, the resulting screen pixels register as near-zero across all three color guns, yielding pure black or deep navy.</li>\n"
                               "</ul>\n"
                               "<h4>3. Diagnostic Contrast and NRA Utility</h4>\n"
                               "<p>This stark optical dichotomy—where vegetation reflects maximally in NIR while water absorbs completely—makes the standard FCC composite the single most effective tool in Natural Resource Accounting. It allows instantaneous, automated spatial delineation of:</p>\n"
                               "<ul>\n"
                               "<li><strong>Shoreline and Wetland Boundaries:</strong> Crisp demarcation of land-water interfaces (e.g. tracking the 94.4 km² loss of water bodies in Vembanad-Kol, Slide 21).</li>\n"
                               "<li><strong>Canopy Stress vs. Moisture:</strong> Thinned or dying forests reflect less NIR and more visible red, shifting from vibrant red to muted brownish-pink or grey, allowing early identification of forest depletion.</li>\n"
                               "<li><strong>Sediment & Shallow Waters:</strong> Turbid, silt-laden water reflects scattered green and red light, appearing light cyan or milky blue, instantly flagging wetland sedimentation.</li>\n"
                               "</ul>\n"
                               "<p><em>Slide Reference: Class 18, Slides 8, 9, 11, 12, 18.</em></p>\n"
                               "</div>"
        },
        {
            "id": "EQB-18-03",
            "class_id": 18,
            "class_name": "Natural Resource Accounting & Geospatial Technology",
            "topic": "Six Applications of Remote Sensing in Environmental Management & NRA",
            "category": "Descriptive & Case Study",
            "exams": [
                {"paper": "End Exam 2019", "section": "Section I, Q3", "marks": "3M"}
            ],
            "marks": "3M",
            "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
            "prompt": "List any Six applications of remote sensing technology in environmental studies.",
            "key_answer_points": "<ul>\n"
                                 "<li><strong>1. Forest Cover Change Detection & Deforestation Auditing:</strong> Multi-temporal satellite imagery quantifies canopy thinning, clearcutting, and afforestation over decades (e.g. Kondapalli Reserve Forest losing 9.74 km² of forest cover from 1990 to 2015).</li>\n"
                                 "<li><strong>2. Wetland Extent & Water Body Dynamics:</strong> Delineating seasonal open water boundaries and measuring wetland shrinkage and encroachment in Ramsar sites (e.g. Vembanad-Kol water body loss of 94.4 km² and Ashtamudi/Sasthamkotta lake decline).</li>\n"
                                 "<li><strong>3. Land Use / Land Cover (LULC) Classification:</strong> Mapping transitions from natural capital (forests, agriculture) to manufactured capital (urban built-up area), providing the spatial foundation for System of Environmental-Economic Accounting (SEEA).</li>\n"
                                 "<li><strong>4. Biomass Carbon Stock & Flow Estimation:</strong> Combining forest area loss with mean biomass density (30 tC/ha) to calculate lost carbon storage (e.g. 29,220 tC / 107,140 tCO2 loss in Kondapalli valued up to \\$2.14M).</li>\n"
                                 "<li><strong>5. Coastal Zone & Agricultural Land Monitoring:</strong> Tracking shoreline erosion, mangrove loss, and agricultural conversion (e.g. 40% reduction in traditional Pokkali rice cultivation in Vembanad-Kol).</li>\n"
                                 "<li><strong>6. Disaster Impact & Water Regulation Assessment:</strong> Mapping flood inundation zones, estimating diminished water storage capacity, and calculating externalized economic damages from urban runoff and destroyed wetland buffers.</li>\n"
                                 "</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n"
                               "<p><strong>Remote Sensing Applications in Environmental Management and Natural Resource Accounting</strong></p>\n"
                               "<p>Remote sensing (RS) provides the core spatial data infrastructure required to operationalize the United Nations System of Environmental-Economic Accounting (SEEA) framework. By linking physical land surface changes to ecosystem services and economic valuation, RS enables objective auditing of natural capital. Six critical applications include:</p>\n"
                               "<h4>1. Forest Cover Change Detection and Deforestation Auditing</h4>\n"
                               "<p>Multi-temporal satellite imagery allows environmental authorities to track forest canopy changes over multi-decadal timelines. High-resolution multispectral sensors capture changes in canopy density, separating intact primary forest from degraded scrub and clearcuts.</p>\n"
                               "<p><em>Slide Case Study (Kondapalli Reserve Forest, AP):</em> Satellite imagery tracked forest cover from 1990 (115.74 km², representing 41.63% of the study area) to 2015 (106.00 km², or 37.53%), detecting an exact net forest loss of <strong>9.74 km²</strong> (a depletion rate of ~0.39 km²/year).</p>\n"
                               "<h4>2. Wetland Extent and Water Body Dynamics Monitoring</h4>\n"
                               "<p>Wetlands provide vital regulating ecosystem services, including flood retention, groundwater recharge, and water purification. Remote sensing tracks surface water shrinkage, siltation, and encroachment in protected Ramsar sites.</p>\n"
                               "<p><em>Slide Case Study (Kerala Ramsar Sites):</em> Satellite monitoring between 1988 and 2023 revealed a massive contraction in water bodies across Vembanad-Kol from <strong>442.1 km² to 347.7 km²</strong>—a net loss of <strong>94.4 km² (9,440 ha)</strong> of open water, while Ashtamudi and Sasthamkotta lost <strong>2.2 km² (220 ha)</strong> of open water.</p>\n"
                               "<h4>3. Land Use / Land Cover (LULC) Classification and Urban Sprawl Mapping</h4>\n"
                               "<p>LULC maps serve as the direct spatial representation of natural capital stocks. Supervised digital classification identifies the rapid conversion of natural biomes into built-up infrastructure:</p>\n"
                               "<p><em>Conversion of Natural to Manufactured Capital:</em> In Kondapalli, built-up area expanded from 3.10 km² (1.11%) in 1990 to 62.26 km² (22.07%) in 2017—a 20-fold explosion. Similarly, in Ashtamudi and Sasthamkotta, built-up surfaces surged from 15.6 km² to 167.8 km² (a 10-fold increase), externalizing severe ecological costs onto surrounding wetlands.</p>\n"
                               "<h4>4. Biomass Carbon Stock and Flow Accounting</h4>\n"
                               "<p>By integrating satellite-derived forest extent changes with ground-calibrated biomass density coefficients, remote sensing quantifies physical carbon sequestration flows and translates them into monetary accounts:</p>\n"
                               "<p><em>Slide Valuation Framework:</em> In Kondapalli, losing 974 ha of forest with an assumed mean biomass density of 30 tC/ha resulted in a physical stock loss of <strong>29,220 tC</strong>, corresponding to <strong>107,140 tCO₂</strong> emitted. Under SEEA carbon accounts, this natural capital depletion was monetized at \\$535,700 (at \\$5/tCO₂), \\$1,071,400 (at \\$10/tCO₂), and \\$2,142,800 (at \\$20/tCO₂).</p>\n"
                               "<h4>5. Coastal Zone Protection and Traditional Agro-Ecosystem Monitoring</h4>\n"
                               "<p>Spaceborne sensors monitor the health of fragile coastal ecotones and traditional sustainable agricultural systems:</p>\n"
                               "<p><em>Slide Case Study (Pokkali Rice Fields):</em> In Vembanad-Kol, remote sensing tracked a <strong>40% collapse</strong> in unique saline-tolerant Pokkali rice fields—shrinking from 97.1 km² in 1988 to 57.7 km² in 2023 (a loss of 3,940 ha). This direct use loss crippled local farming livelihoods and destroyed traditional fish-paddy agro-ecosystems.</p>\n"
                               "<h4>6. Disaster Impact Assessment and Ecosystem Service Valuation</h4>\n"
                               "<p>Satellite imagery enables spatial modeling of flood regulation, water storage, and coastal storm buffering services. When wetlands and forests are converted to impervious concrete, water retention drops, driving up disaster recovery expenditures:</p>\n"
                               "<p><em>Slide Economic Synthesis:</em> Satellite accounting in Kerala demonstrated that shrinking wetlands and vegetation resulted in annual lost ecosystem services of <strong>₹201.5 crores/year</strong> in Vembanad-Kol and <strong>₹68.9 crores/year</strong> in Ashtamudi & Sasthamkotta, totaling <strong>₹270.36 crores/year</strong> in combined lost fisheries, agriculture, flood regulation, tourism, and biodiversity benefits.</p>\n"
                               "<p><em>Slide Reference: Class 18, Slides 6–10, 11–12, 15–25.</em></p>\n"
                               "</div>"
        },
        {
            "id": "EQB-18-04",
            "class_id": 18,
            "class_name": "Natural Resource Accounting & Geospatial Technology",
            "topic": "Spectral Signatures in Natural Resource Accounting & Optical Physics",
            "category": "Short Answer & Definitions",
            "exams": [
                {"paper": "End Exam 2019", "section": "Section I", "marks": "2M"}
            ],
            "marks": "2M",
            "importance": "HIGH (⭐⭐⭐⭐)",
            "prompt": "What are spectral signatures, and why is the near-infrared band critical for vegetation monitoring?",
            "key_answer_points": "<ul>\n"
                                 "<li><strong>Definition of Spectral Signature:</strong> The unique, wavelength-dependent pattern of electromagnetic radiation reflectance, absorption, and transmission displayed by a specific Earth surface material across the spectrum, functioning as an optical 'fingerprint'.</li>\n"
                                 "<li><strong>Physical Law of Conservation:</strong> Incident electromagnetic energy at wavelength $\\lambda$ is partitioned as:\n"
                                 "<div class=\"formula-box\">$$E_{\\text{incident}}(\\lambda) = E_{\\text{reflected}}(\\lambda) + E_{\\text{absorbed}}(\\lambda) + E_{\\text{transmitted}}(\\lambda)$$</div></li>\n"
                                 "<li><strong>Why the Near-Infrared (NIR) Band (0.7–1.1 $\\mu\\text{m}$) is Critical:</strong>\n"
                                 "<br>• <em>Chlorophyll vs. Mesophyll Separation:</em> In the visible band, chlorophyll absorbs red light ($\sim 660\\text{ nm}$) for photosynthesis. In the NIR band, light penetrates the cuticle and encounters the internal <strong>spongy mesophyll layer</strong>, where multiple refractions between hydrated cell walls and intercellular air spaces scatter and reflect <strong>40% to 60%</strong> of NIR radiation.\n"
                                 "<br>• <em>Early Stress Diagnostic Indicator:</em> When plants undergo drought stress, insect infestation, or chemical pollution, their internal spongy mesophyll cells collapse and intercellular air cavities fill with water or shrink long before chlorophyll breaks down. As a result, <strong>NIR reflectance drops sharply days or weeks before any visible yellowing (chlorosis)</strong> can be seen by human eyes or visible RGB cameras.</li>\n"
                                 "<li><strong>Indispensability in NRA:</strong> Enables satellite sensors to detect subtle forest canopy degradation, selective logging, and biomass loss that cannot be seen in visible bands, providing verifiable evidence of natural capital depreciation.</li>\n"
                                 "</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n"
                               "<p><strong>Understanding Spectral Signatures in Earth Observation</strong></p>\n"
                               "<p>A <strong>spectral signature</strong> is the characteristic profile of electromagnetic reflectance and absorption that an Earth surface material displays across various wavelengths of the spectrum. Just as human beings possess unique biometric fingerprints, every natural and man-made surface feature—green vegetation, clear lake water, turbid sediment-laden rivers, dry bare soil, and asphalt roads—interacts with electromagnetic radiation (EMR) in a distinct, mathematically repeatable way governed by physical and chemical laws.</p>\n"
                               "<h4>The Physical Energy Conservation Principle</h4>\n"
                               "<p>When solar radiation of wavelength $\\lambda$ strikes an environmental target, the total incident energy must be conserved:</p>\n"
                               "<div class=\"formula-box\">$$E_{\\text{incident}}(\\lambda) = E_{\\text{reflected}}(\\lambda) + E_{\\text{absorbed}}(\\lambda) + E_{\\text{transmitted}}(\\lambda)$$</div>\n"
                               "<p>Dividing both sides by $E_{\\text{incident}}(\\lambda)$ yields:</p>\n"
                               "<div class=\"formula-box\">$$\\rho(\\lambda) + \\alpha(\\lambda) + \\tau(\\lambda) = 1$$</div>\n"
                               "<p>Where $\\rho(\\lambda)$ is spectral reflectance, $\\alpha(\\lambda)$ is spectral absorptance, and $\\tau(\\lambda)$ is spectral transmittance. Multispectral satellite sensors measure the reflected component $\\rho(\\lambda)$ to classify land cover and assess resource condition.</p>\n"
                               "<h4>Comparative Spectral Profiles of Major Earth Features</h4>\n"
                               "<ol>\n"
                               "<li><strong>Healthy Green Vegetation:</strong> Shows a distinct 'trough-peak-trough-plateau' profile. Blue (~0.45 $\\mu\\text{m}$) and Red (~0.66 $\\mu\\text{m}$) visible wavelengths are heavily absorbed by chlorophyll $a$ and $b$ for photosynthesis (absorptance > 85%). A slight green reflectance peak occurs at ~0.55 $\\mu\\text{m}$ (why plants look green to humans). Then, between 0.68 $\\mu\\text{m}$ and 0.73 $\\mu\\text{m}$, reflectance increases dramatically across the <strong>Red Edge</strong> into the Near-Infrared (NIR) plateau (0.76–1.1 $\\mu\\text{m}$), where reflectance reaches 40–60%.</li>\n"
                               "<li><strong>Clear Deep Water:</strong> High transmittance and absorption across visible blue-green, but nearly 100% absorption in the NIR and SWIR bands ($\\rho_{\\text{NIR}} \\approx 0$).</li>\n"
                               "<li><strong>Bare Mineral Soil:</strong> Exhibits a monotonic, steadily rising reflectance curve from visible to shortwave infrared, without the sharp chlorophyll absorption dips or the dramatic NIR jump seen in vegetation.</li>\n"
                               "</ol>\n"
                               "<h4>Why the Near-Infrared (NIR) Band is Critical for Vegetation Monitoring</h4>\n"
                               "<p>The Near-Infrared band is the single most important spectral band for environmental monitoring and Natural Resource Accounting for three key reasons:</p>\n"
                               "<ul>\n"
                               "<li><strong>1. Leaf Internal Anatomy (Spongy Mesophyll Scattering):</strong> Visible light interaction is dictated by biochemical leaf pigments (chlorophyll, carotenoids), whereas NIR interaction is governed purely by leaf internal physical structure. When NIR radiation enters a healthy leaf, it encounters the spongy mesophyll—a porous tissue of irregular parenchymal cells surrounded by air cavities. The abrupt change in refractive index between the hydrated cell walls ($n \\approx 1.42$) and air spaces ($n \\approx 1.0$) causes intense internal scattering, bouncing roughly half the radiation back out of the canopy.</li>\n"
                               "<li><strong>2. Pre-Visual Early Warning of Plant Stress:</strong> When a forest or crop experiences water deficit, heat stress, root rot, or pest attacks, the internal cell turgor pressure drops and the spongy mesophyll architecture collapses. Consequently, the multi-surface scattering mechanism fails, and <strong>NIR reflectance drops steeply</strong>. Crucially, this collapse in NIR reflectance occurs <strong>several days to weeks before chlorophyll degrades</strong>. To a human observer or standard visible camera, the forest still looks lush green, but a satellite NIR sensor immediately flags the physiological collapse.</li>\n"
                               "<li><strong>3. Quantitative Biomass and Canopy Density Estimation:</strong> In a sparse or degraded forest, satellite sensors capture a mixed signal of leaves and bare ground. As canopy layers stack up (higher Leaf Area Index, LAI), NIR radiation undergoes multiple scattering across multiple canopy layers, causing total NIR reflectance to rise in proportion to standing green biomass. This makes NIR the fundamental building block for vegetation indices like NDVI and biomass accounting under SEEA.</li>\n"
                               "</ul>\n"
                               "<p><em>Slide Reference: Class 18, Slides 8, 9, 12, 16.</em></p>\n"
                               "</div>"
        },
        {
            "id": "EQB-18-05",
            "class_id": 18,
            "class_name": "Natural Resource Accounting & Geospatial Technology",
            "topic": "Normalized Difference Vegetation Index (NDVI) & Quantitative Case Studies in NRA",
            "category": "Short Answer & Definitions",
            "exams": [
                {"paper": "End Exam 2019", "section": "Section I", "marks": "2M"}
            ],
            "marks": "2M",
            "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
            "prompt": "What is NDVI (Normalized Difference Vegetation Index) and how is it used in natural resource accounting?",
            "key_answer_points": "<ul>\n"
                                 "<li><strong>Mathematical Formula:</strong>\n"
                                 "<div class=\"formula-box\">$$\\text{NDVI} = \\frac{\\text{NIR} - \\text{Red}}{\\text{NIR} + \\text{Red}}$$</div>\n"
                                 "Where $\\text{NIR}$ is spectral reflectance in the Near-Infrared channel ($\sim 0.76\\text{--}0.90\\ \\mu\\text{m}$) and $\\text{Red}$ is reflectance in the visible Red channel ($\sim 0.63\\text{--}0.69\\ \\mu\\text{m}$).</li>\n"
                                 "<li><strong>Numerical Value Range & Ecological Interpretation:</strong>\n"
                                 "<br>• Values strictly range from <strong>$-1.0$ to $+1.0$</strong>.\n"
                                 "<br>• <strong>Negative Values ($-1.0$ to $0.0$):</strong> Water bodies, snow, ice, clouds (water absorbs NIR while reflecting slight visible light, making the numerator negative).\n"
                                 "<br>• <strong>Near Zero to Low Positive ($0.0$ to $0.2$):</strong> Bare rock, sand, concrete urban infrastructure, barren soil.\n"
                                 "<br>• <strong>Moderate Positive ($0.2$ to $0.5$):</strong> Sparse grassland, scrublands, dry senescent crops.\n"
                                 "<br>• <strong>High Positive ($0.6$ to $0.9+$):</strong> Dense, healthy, multi-layered temperate and tropical moist rainforests.</li>\n"
                                 "<li><strong>Why Normalization Matters:</strong> Dividing the difference $(\\text{NIR} - \\text{Red})$ by their sum $(\\text{NIR} + \\text{Red})$ cancels out variations caused by solar illumination angles, hill topography, shadow effects, and atmospheric haze.</li>\n"
                                 "<li><strong>Application in Natural Resource Accounting (NRA):</strong>\n"
                                 "<br>• Serves as the quantitative spatial metric for <strong>SEEA physical ecosystem extent and condition accounts</strong>.\n"
                                 "<br>• Quantifies annual depletion of natural capital stocks (forest canopy loss, wetland shrinkage) and converts physical flows into monetary balance sheets.\n"
                                 "<br>• Grounded in the two official slide case studies:\n"
                                 "<br>&nbsp;&nbsp;1. <em>Kondapalli Reserve Forest (AP):</em> 9.74 km² net forest loss (1990–2015), representing 29,220 tC / 107,140 tCO2 loss valued up to \\$2,142,800.\n"
                                 "<br>&nbsp;&nbsp;2. <em>Kerala Ramsar Wetlands (Ashtamudi, Sasthamkotta, Vembanad-Kol):</em> Over 100 km² water body reduction, 20–40% vegetation decline, and combined ecosystem service loss of ₹270.36 crores/year.</li>\n"
                                 "</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n"
                               "<p><strong>Definition and Mathematical Foundation of NDVI</strong></p>\n"
                               "<p>The <strong>Normalized Difference Vegetation Index (NDVI)</strong> is a standardized radiometric index computed from satellite multispectral bands that quantifies the photosynthetic vigor, canopy greenness, and standing biomass density of Earth surface vegetation. It leverages the sharp contrast between chlorophyll absorption in the visible Red band and internal mesophyll scattering in the Near-Infrared (NIR) band:</p>\n"
                               "<div class=\"formula-box\">$$\\text{NDVI} = \\frac{\\text{NIR} - \\text{Red}}{\\text{NIR} + \\text{Red}}$$</div>\n"
                               "<h4>Physical Principle and Normalization Mechanics</h4>\n"
                               "<ul>\n"
                               "<li><strong>Why Subtract $(\\text{NIR} - \\text{Red})$?</strong> Healthy green leaves absorb Red photons (low reflectance, $\\approx 0.05$) and strongly reflect NIR photons (high reflectance, $\\approx 0.50$). This produces a large positive numerator $(\\text{NIR} - \\text{Red} > 0)$. Non-vegetated surfaces like water have $R_{\\text{NIR}} \\approx 0$ and $R_{\\text{Red}} > 0$, yielding a negative numerator.</li>\n"
                               "<li><strong>Why Divide by $(\\text{NIR} + \\text{Red})$?</strong> Dividing by the sum normalizes the index into a dimensionless ratio bounded between $-1.0$ and $+1.0$. This mathematical normalization cancels out extraneous environmental noise—such as varying solar zenith angles, differential topographic shading on mountain slopes, and uniform atmospheric haze.</li>\n"
                               "</ul>\n"
                               "<h4>NDVI Numerical Scale and Land Cover Classification</h4>\n"
                               "<table class=\"exam-table\">\n"
                               "<thead><tr><th>NDVI Value Range</th><th>Land Cover / Surface Type</th><th>Spectral Behavior</th></tr></thead>\n"
                               "<tbody>\n"
                               "<tr><td>$-1.0$ to $0.0$</td><td>Deep Water bodies, Snow, Clouds</td><td>$\\text{NIR} \\approx 0$, visible reflectance higher $\\rightarrow$ negative ratio</td></tr>\n"
                               "<tr><td>$0.0$ to $0.2$</td><td>Bare Rock, Sand, Built-up Concrete, Barren Soil</td><td>Nearly equal reflectance in Red and NIR $\\rightarrow$ ratio near zero</td></tr>\n"
                               "<tr><td>$0.2$ to $0.5$</td><td>Shrublands, Grasslands, Sparse / Stressed Crops</td><td>Moderate NIR scattering, moderate red absorption</td></tr>\n"
                               "<tr><td>$0.6$ to $0.9+$</td><td>Dense Tropical Forest, Closed-Canopy Woodlands</td><td>Maximum mesophyll scattering (NIR) + peak chlorophyll absorption (Red)</td></tr>\n"
                               "</tbody>\n"
                               "</table>\n"
                               "<h4>Operational Role of NDVI in Natural Resource Accounting (NRA)</h4>\n"
                               "<p>Natural Resource Accounting under the United Nations System of Environmental-Economic Accounting (SEEA) requires measuring:</p>\n"
                               "<ol>\n"
                               "<li><strong>Ecosystem Extent Accounts:</strong> Physical area of different ecosystem types over time.</li>\n"
                               "<li><strong>Ecosystem Condition Accounts:</strong> The biophysical quality, canopy density, and ecological health of those ecosystems.</li>\n"
                               "<li><strong>Ecosystem Services and Valuation:</strong> Translating physical depletion into monetary depreciation.</li>\n"
                               "</ol>\n"
                               "<p>NDVI provides the continuous, objective spatial baseline to establish opening stocks, track additions/reductions (flows), and record closing stocks of natural capital. This is illustrated by the two comprehensive case studies presented in the lecture slides:</p>\n"
                               "<h4>Case Study 1: Kondapalli Reserve Forest (Andhra Pradesh) — Stocks and Flows Accounting</h4>\n"
                               "<p>The Kondapalli Reserve Forest study demonstrates how multi-temporal satellite LULC and vegetation indices establish environmental accounting balance sheets:</p>\n"
                               "<ul>\n"
                               "<li><strong>Physical Extent Stocks & Flows (1990–2015/2017):</strong>\n"
                               "<br>• <em>Forest Capital Stock:</em> Shrank from <strong>115.74 km² (41.63%)</strong> in 1990 down to <strong>106.00 km² (37.53%)</strong> in 2015.\n"
                               "<br>• <em>Net Forest Depletion Flow:</em> A negative physical flow of <strong>$-9.74\\text{ km²}$ (974 hectares)</strong>, averaging an annual loss of $\\sim 0.39\\text{ km²}/\\text{year}$.\n"
                               "<br>• <em>Manufactured Capital Stock:</em> Built-up impervious area expanded from <strong>3.10 km² (1.11%)</strong> in 1990 to <strong>62.26 km² (22.07%)</strong> in 2017—a positive flow of $+59.16\\text{ km²}$ of manufactured infrastructure, driving severe habitat fragmentation.</li>\n"
                               "<li><strong>Worked Example: Biomass Carbon Valuation:</strong>\n"
                               "Using the SEEA accounting framework, physical forest depletion is monetized via carbon stock accounting:\n"
                               "<ol>\n"
                               "<li><em>Physical Forest Loss:</em> $9.74\\text{ km²} = 974\\text{ ha}$.</li>\n"
                               "<li><em>Mean Biomass Carbon Density:</em> $30\\text{ tC/ha}$.</li>\n"
                               "<li><em>Total Carbon Stock Loss:</em>\n"
                               "<div class=\"formula-box\">$$\\text{Total C Loss} = 974\\text{ ha} \\times 30\\text{ tC/ha} = 29,220\\text{ tC}$$</div></li>\n"
                               "<li><em>Equivalent Carbon Dioxide ($\\text{CO}_2$):</em> Using the stoichiometric molecular ratio of $\\text{CO}_2$ to Carbon ($44/12 \\approx 3.67$):\n"
                               "<div class=\"formula-box\">$$\\text{Emissions} = 29,220\\text{ tC} \\times 3.67 = 107,140\\text{ tCO}_2$$</div></li>\n"
                               "<li><em>Monetary Valuation Across Carbon Pricing Scenarios:</em>\n"
                               "<br>• At US\\$5 / $\\text{tCO}_2$: $107,140 \\times \\$5 = \\text{US}\\$535,700$\n"
                               "<br>• At US\\$10 / $\\text{tCO}_2$: $107,140 \\times \\$10 = \\text{US}\\$1,071,400$\n"
                               "<br>• At US\\$20 / $\\text{tCO}_2$: $107,140 \\times \\$20 = \\text{US}\\$2,142,800$</li>\n"
                               "</ol></li>\n"
                               "</ul>\n"
                               "<h4>Case Study 2: Kerala Ramsar Wetland Ecosystems — Economic Valuation of Ecosystem Services</h4>\n"
                               "<p>The second slide case study applies geospatial accounting to three critical Ramsar wetland systems in Kerala: <strong>Ashtamudi Wetland</strong> (61.4 km²), <strong>Sasthamkotta Lake</strong> (3.75 km², Kerala's largest freshwater drinking lake), and <strong>Vembanad-Kol Wetland</strong> (2,033 km², largest tropical brackish wetland in India, supporting sub-sea-level agriculture).</p>\n"
                               "<ul>\n"
                               "<li><strong>Physical Area Dynamics (1988–2022/2023):</strong>\n"
                               "<br>• <em>Ashtamudi & Sasthamkotta (1988–2022):</em> Water bodies declined from 67.9 km² to 65.7 km² (loss of 220 ha); natural vegetation suffered a sharp decline from 220.7 km² to 139.8 km² (loss of 8,090 ha); agriculture/fallow dropped from 84.8 km² to 15.7 km² (loss of 6,910 ha); built-up area surged from 15.6 km² to 167.8 km² (more than a 10-fold increase).\n"
                               "<br>• <em>Vembanad-Kol (1988–2023):</em> Open water bodies contracted from 442.1 km² to 347.7 km² (<strong>net loss of 94.4 km² or 9,440 ha</strong>); vegetation fell from 767.3 km² to 650.3 km² (loss of 11,700 ha); traditional saline-tolerant Pokkali rice fields collapsed from 97.1 km² to 57.7 km² (loss of 3,940 ha or 40%); built-up land expanded from 80.8 km² to 340.6 km² (over 4-fold increase).</li>\n"
                               "<li><strong>Economic Valuation Methodology (Benefit-Transfer Using Mid-Point Values):</strong>\n"
                               "<br>• <em>Fisheries Provisioning:</em> ₹115,000 / ha / year (Vembanad estuarine fisheries); ₹80,000 / ha / year (Ashtamudi & Sasthamkotta clam/freshwater fisheries).\n"
                               "<br>• <em>Agricultural Provisioning:</em> ₹50,000 / ha / year (Pokkali rice fields); ₹37,500 / ha / year (Paddy / fallow agriculture).\n"
                               "<br>• <em>Regulating Services (Flood regulation, water purification, carbon storage):</em> ₹42,500 / ha / year (mid-point of ₹25,000–60,000 range).\n"
                               "<br>• <em>Recreation & Tourism:</em> ₹15,000 / ha / year (mid-point of ₹12,000–18,000 range from backwater tourism studies).\n"
                               "<br>• <em>Biodiversity & Non-Use Values:</em> ₹8,000 / ha / year (mid-point of ₹6,000–10,000 Willingness-To-Pay range).</li>\n"
                               "<li><strong>Mid-Case Annual Economic Losses Calculated in the Slides:</strong>\n"
                               "<br>• <strong>Vembanad-Kol Annual Loss:</strong>\n"
                               "<br>&nbsp;&nbsp;- Fisheries ($9,440\\text{ ha} \\times ₹115,000$): ₹1,085,600,000\n"
                               "<br>&nbsp;&nbsp;- Agriculture ($3,940\\text{ ha} \\times ₹50,000$): ₹197,000,000\n"
                               "<br>&nbsp;&nbsp;- Regulating Services ($11,700\\text{ ha} \\times ₹42,500$): ₹497,250,000\n"
                               "<br>&nbsp;&nbsp;- Recreation / Tourism ($9,440\\text{ ha} \\times ₹15,000$): ₹141,600,000\n"
                               "<br>&nbsp;&nbsp;- Biodiversity / Non-use ($11,700\\text{ ha} \\times ₹8,000$): ₹93,600,000\n"
                               "<br>&nbsp;&nbsp;<em>Total Vembanad-Kol Annual Loss:</em> <strong>₹2,015,050,000 per year (~₹201.5 crores/year)</strong>.\n"
                               "<br>• <strong>Ashtamudi & Sasthamkotta Annual Loss:</strong>\n"
                               "<br>&nbsp;&nbsp;- Fisheries ($220\\text{ ha} \\times ₹80,000$): ₹17,600,000\n"
                               "<br>&nbsp;&nbsp;- Agriculture ($6,910\\text{ ha} \\times ₹37,500$): ₹259,125,000\n"
                               "<br>&nbsp;&nbsp;- Regulating Services ($8,090\\text{ ha} \\times ₹42,500$): ₹343,825,000\n"
                               "<br>&nbsp;&nbsp;- Recreation / Tourism ($220\\text{ ha} \\times ₹15,000$): ₹3,300,000\n"
                               "<br>&nbsp;&nbsp;- Biodiversity / Non-use ($8,090\\text{ ha} \\times ₹8,000$): ₹64,720,000\n"
                               "<br>&nbsp;&nbsp;<em>Total Ashtamudi & Sasthamkotta Annual Loss:</em> <strong>₹688,570,000 per year (~₹68.9 crores/year)</strong>.\n"
                               "<br>• <strong>Combined Kerala Ramsar Sites Total Economic Loss:</strong>\n"
                               "<div class=\"formula-box\">$$\\text{Combined Loss} \\approx ₹2,015,050,000 + ₹688,570,000 = ₹2,703,620,000\\text{ per year (~₹270.36 crores/year)}$$</div></li>\n"
                               "</ul>\n"
                               "<p><em>Slide Reference: Class 18, Slides 7, 8, 9, 11, 12, 15–25.</em></p>\n"
                               "</div>"
        }
    ]

# Alias for backwards compatibility
def get_class18_questions():
    return get_class18_grounded_questions()

if __name__ == "__main__":
    qs = get_class18_grounded_questions()
    print(f"Loaded {len(qs)} grounded Class 18 questions successfully.")
    for q in qs:
        print(f" - {q['id']}: {q['topic']} ({len(q['detailed_answer'])} chars in detailed answer)")
