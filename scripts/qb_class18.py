# Class 18: Natural Resource Accounting & Geospatial Question Bank
class_18_questions = [
    {
        "id": "EQB-18-01",
        "class_id": 18,
        "class_name": "NRA & Geospatial Technologies",
        "topic": "Remote Sensing (RS) Definition & Principles",
        "category": "Comprehensive Descriptive",
        "exams": [
            {"paper": "End Exam 2019", "section": "Section I, Q1", "marks": "1M"},
            {"paper": "Mid-2 2018", "section": "Q3(b)", "marks": "1M"}
        ],
        "marks": "1M – 2M",
        "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
        "prompt": "Define Remote Sensing. Explain the basic physical principles of electromagnetic radiation (EMR) interaction with the earth's surface and atmosphere.",
        "key_answer_points": """<ul>
          <li><strong>Definition of Remote Sensing:</strong> The science and art of acquiring data and information about physical objects, land surfaces, or environmental phenomena from a distance, <strong>without coming into direct physical contact</strong> with them, primarily using sensors mounted on airborne (drones, aircraft) or spaceborne (satellites) platforms.</li>
          <li><strong>Physical Operating Mechanism (EMR Interaction):</strong>
            <br>• The Sun (or active radar/lidar sensor) illuminates Earth with <strong>Electromagnetic Radiation (EMR)</strong> across diverse wavelengths (Visible: 0.4–0.7 $\\mu$m, Near-Infrared: 0.7–1.1 $\\mu$m, Shortwave Infrared: 1.1–3.0 $\\mu$m, Thermal Infrared: 8–14 $\\mu$m, Microwave: 1 mm–1 m).
            <br>• As EMR strikes physical surface features, energy is partitioned according to the fundamental energy balance equation:
            <div class="formula-box">$$E_{\\text{incident}}(\\lambda) = E_{\\text{reflected}}(\\lambda) + E_{\\text{absorbed}}(\\lambda) + E_{\\text{transmitted}}(\\lambda)$$</div>
            <br>• Every natural material (water, green vegetation, mineral soil, concrete) possesses a unique, wavelength-dependent <strong>Spectral Signature</strong> of reflected and emitted radiation captured by multispectral electro-optical sensors.</li>
          <li><strong>Passive vs Active Sensors:</strong>
            <br>• <em>Passive Sensors:</em> Detect natural reflected sunlight or emitted thermal radiation (e.g. Landsat, Sentinel-2, MODIS).
            <br>• <em>Active Sensors:</em> Emit their own electromagnetic signal and measure the backscattered echo (e.g. Synthetic Aperture Radar / SAR, LiDAR).</li>
        </ul>""",
        "detailed_answer": """<div class="detailed-body">
          <p><strong>The Remote Sensing Workflow:</strong> Source of energy $\rightarrow$ Atmospheric transmission windows $\rightarrow$ Surface interaction $\rightarrow$ Satellite sensor recording $\rightarrow$ Ground telemetry reception and processing $\rightarrow$ Digital image classification and analysis.</p>
          <h4>Atmospheric Windows</h4>
          <p>Earth's atmosphere absorbs specific wavelengths due to water vapor, ozone, and carbon dioxide. Remote sensing instruments are specifically engineered to record in 'atmospheric transmission windows' where solar energy passes through with minimal attenuation.</p>
          <p><em>Slide Reference: Class 18 Slides 4–8 (Remote Sensing Fundamentals).</em></p>
        </div>"""
    },
    {
        "id": "EQB-18-02",
        "class_id": 18,
        "class_name": "NRA & Geospatial Technologies",
        "topic": "Spectral Signatures & Infrared False Color Composite",
        "category": "Comprehensive Descriptive",
        "exams": [
            {"paper": "End Exam 2019", "section": "Section I, Q2", "marks": "2M"}
        ],
        "marks": "2M",
        "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
        "prompt": "How do healthy vegetation and deep water bodies appear in Standard Infrared False Color Composite (FCC) satellite imagery? Explain the underlying biophysical and optical reasons.",
        "key_answer_points": """<ul>
          <li><strong>Standard False Color Composite (FCC) Band Assignment:</strong>
            <br>• <strong>Red Display Channel $\\rightarrow$ Near-Infrared (NIR) Band</strong> (0.76–0.90 $\\mu$m)
            <br>• <strong>Green Display Channel $\\rightarrow$ Red Band</strong> (0.63–0.69 $\\mu$m)
            <br>• <strong>Blue Display Channel $\\rightarrow$ Green Band</strong> (0.52–0.60 $\\mu$m)</li>
          <li><strong>Appearance & Physics of Healthy Green Vegetation:</strong>
            <br>• <strong>Appears: Bright, Brilliant Red / Magenta</strong>.
            <br>• <em>Biophysical Cause:</em> Plant leaves strongly absorb visible Red light via chlorophyll pigments for photosynthesis, but reflect <strong>40% to 60% of incident Near-Infrared (NIR) radiation</strong> due to refractive index mismatches inside the internal spongy mesophyll cell walls (preventing leaves from cooking in the sun). Because the NIR band is assigned to the Red display gun, dense vegetation glows vibrant red.</li>
          <li><strong>Appearance & Physics of Deeper Water Bodies:</strong>
            <br>• <strong>Appears: Dark Black, Jet Navy, or Deep Blue</strong>.
            <br>• <em>Optical Cause:</em> Pure, deep water absorbs virtually <strong>100% of incident Near-Infrared and Shortwave-Infrared radiation</strong> within the top few centimeters of the water column, with near-zero reflectance ($R_{\\text{NIR}} \\approx 0$). With zero signal mapped to the Red gun, deep water displays as deep black.</li>
          <li><strong>Turbid / Shallow Water Contrast:</strong> Shallow or sediment-rich water reflects slightly in the Green and Red visible channels, appearing light cyan or greenish-blue.</li>
        </ul>""",
        "detailed_answer": """<div class="detailed-body">
          <p><strong>Why Use False Color Imagery?</strong> Human eyes cannot perceive near-infrared photons. Standard true-color imagery (RGB as Red, Green, Blue) presents vegetation as dull green and reveals little about plant stress or moisture. By mapping the highly sensitive NIR band to the red visual channel, differences in forest density, crop vigor, and canopy moisture become glaringly obvious.</p>
          <h4>The 'Red Edge' in Plant Biophysics</h4>
          <p>Between 680 nm (chlorophyll red absorption pit) and 730 nm (spongy mesophyll NIR reflection plateau), reflectance jumps abruptly by 500%. This steep gradient—known as the <strong>Red Edge</strong>—is the primary diagnostic indicator of healthy vegetation worldwide. When trees suffer drought or chemical pollution, chlorophyll degrades and internal spongy air cavities collapse, causing the red edge to flatten.</p>
          <p><em>Slide Reference: Class 18 Slides 9–13 (Spectral Signatures & FCC).</em></p>
        </div>"""
    },
    {
        "id": "EQB-18-03",
        "class_id": 18,
        "class_name": "NRA & Geospatial Technologies",
        "topic": "Six Applications of Remote Sensing in Environmental Studies",
        "category": "Comprehensive Descriptive",
        "exams": [
            {"paper": "End Exam 2019", "section": "Section I, Q3", "marks": "3M"},
            {"paper": "Mid-2 2018", "section": "Q10(c)", "marks": "3M"}
        ],
        "marks": "3M",
        "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
        "prompt": "List and detail six distinct applications of remote sensing technology in environmental management and ecological monitoring.",
        "key_answer_points": """<ul>
          <li><strong>1. Forest Canopy Density & Deforestation Monitoring:</strong> Generating periodic Normalized Difference Vegetation Index (NDVI) maps to classify forest cover into Very Dense Forest (>70%), Moderately Dense (40–70%), and Open Forest (10–40%), tracking illegal logging and agricultural encroachment (e.g. Global Forest Watch, Forest Survey of India biannual State of Forest Reports).</li>
          <li><strong>2. Wetland Delineation & Hydrological Dynamics:</strong> Using multispectral water indices (MNDWI) to map wetland extents across seasons, detecting the shrinkage of Ramsar lakes, sediment siltation, and encroachment.</li>
          <li><strong>3. Disaster Management & Flood Inundation Mapping:</strong> Using spaceborne Synthetic Aperture Radar (SAR, like Sentinel-1/RISAT) to penetrate heavy monsoon cloud cover and provide real-time maps of submerged villages and breached embankments during cyclone emergencies.</li>
          <li><strong>4. Urban Heat Island (UHI) & Impervious Surface Mapping:</strong> Utilizing spaceborne Thermal Infrared (TIR) sensors (Landsat TIRS, MODIS) to calculate land surface temperatures (LST) and evaluate microclimate cooling from green corridors and urban tree canopies.</li>
          <li><strong>5. Coral Reef Bleaching & Sea Surface Temperature (SST):</strong> Monitoring regional ocean warming anomalies via thermal radiometers (NOAA Coral Reef Watch); alerting marine park managers when thermal stress degree heating weeks (DHW) threaten coral mortality.</li>
          <li><strong>6. Agricultural Drought Monitoring & Crop Yield Forecasting:</strong> Analyzing temporal soil moisture anomalies (SMAP radar) and Vegetation Condition Index (VCI) to assess drought severity, forecast crop yields, and direct disaster relief before famine occurs.</li>
        </ul>""",
        "detailed_answer": """<div class="detailed-body">
          <p><strong>Synoptic & Repetitive Coverage:</strong> Traditional environmental field sampling is geographically localized and expensive. Earth observation satellites provide synoptic, wall-to-wall spatial coverage with constant revisit frequencies (every 5–16 days), allowing change-detection algorithms to automatically flag illegal mining pits or clearcut patches.</p>
          <p><em>Slide Reference: Class 18 Slides 14–19 (Environmental Applications of RS).</em></p>
        </div>"""
    },
    {
        "id": "EQB-18-04",
        "class_id": 18,
        "class_name": "NRA & Geospatial Technologies",
        "topic": "GIS & Spatial Data Infrastructure in Natural Resource Accounting",
        "category": "Comprehensive Descriptive",
        "exams": [
            {"paper": "General Syllabus & Slide 18 Modules", "section": "Section I", "marks": "4M"}
        ],
        "marks": "4M",
        "importance": "HIGH (⭐⭐⭐⭐)",
        "prompt": "Explain how Geographic Information Systems (GIS) integrate with Natural Resource Accounting (NRA). Differentiate between vector and raster data models, and explain multi-criteria overlay analysis.",
        "key_answer_points": """<ul>
          <li><strong>Integration with NRA:</strong> GIS provides the mandatory <strong>spatial data infrastructure</strong> that underpins System of Environmental-Economic Accounting (SEEA). It converts abstract national accounting numbers into georeferenced physical asset maps—tracking exact spatial locations where forests are expanding, aquifers are declining, or soil erosion is accelerating.</li>
          <li><strong>Vector vs Raster Spatial Data Models:</strong>
            <br>• <strong>Raster Data Model:</strong> Space is partitioned into a regular continuous grid of equal-sized square pixels/cells, where each cell stores a single value (e.g., satellite imagery, elevation DEMs, temperature maps). Best for continuously varying environmental phenomena.
            <br>• <strong>Vector Data Model:</strong> Real-world spatial features are stored as discrete coordinate geometries using <em>Points</em> (water wells, pollution discharge pipes), <em>Lines</em> (rivers, fault lines, roads), and <em>Polygons</em> (forest reserves, watershed boundaries, cadastral property parcels). Best for discrete, bounded human and ecological administrative units.</li>
          <li><strong>Multi-Criteria Overlay Analysis:</strong> A spatial modeling technique where multiple thematic raster/vector map layers (slope steepness, rainfall, soil permeability, distance from rivers, wildlife corridors) are standardized, given mathematical weights, and overlaid using Boolean or weighted linear combination to identify optimal eco-sensitive zoning (e.g. siting protected reserves or identifying groundwater recharge zones).</li>
        </ul>""",
        "detailed_answer": """<div class="detailed-body">
          <p><strong>From Spreadsheets to Spatial Accounting:</strong> Standard economics tracks numbers in flat spreadsheets. However, natural capital is spatially explicit: losing 100 hectares of forest in an arid upstream watershed has a radically different ecological impact than losing 100 hectares in a flat commercial monoculture plantation. GIS enables spatially explicit Natural Resource Accounting.</p>
          <h4>Multi-Criteria Decision Analysis (MCDA) in Environmental Zoning</h4>
          <div class="formula-box">$$\\text{Suitability Index } S = \\sum_{i=1}^n w_i \\cdot X_i \\times \\prod c_j$$</div>
          <p>Where $w_i$ is the weight of environmental criterion $i$, $X_i$ is the standardized score, and $c_j$ represents absolute spatial constraints (e.g. strict zero-building buffer zones within 500m of national parks).</p>
          <p><em>Slide Reference: Class 18 Slides 20–26 (GIS & Spatial NRA).</em></p>
        </div>"""
    },
    {
        "id": "EQB-18-05",
        "class_id": 18,
        "class_name": "NRA & Geospatial Technologies",
        "topic": "Normalized Difference Vegetation Index (NDVI)",
        "category": "Comprehensive Descriptive",
        "exams": [
            {"paper": "General Syllabus & Slide 18 Modules", "section": "Section I", "marks": "3M"}
        ],
        "marks": "3M",
        "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
        "prompt": "Define the Normalized Difference Vegetation Index (NDVI). State its mathematical formula, explain the physical meaning of values from -1 to +1, and discuss its role in measuring forest canopy degradation.",
        "key_answer_points": """<ul>
          <li><strong>Definition of NDVI:</strong> A standardized, universally utilized radiometric index calculated from satellite spectral bands that quantifies the photosynthetic greenness, biomass density, and structural vigor of vegetation canopy.</li>
          <li><strong>Mathematical Formula:</strong>
            <div class="formula-box">$$\\text{NDVI} = \\frac{\\text{NIR} - \\text{Red}}{\\text{NIR} + \\text{Red}}$$</div>
            Where $\text{NIR}$ is reflectance in the Near-Infrared channel (0.76–0.90 $\\mu$m) and $\text{Red}$ is reflectance in the visible Red channel (0.63–0.69 $\\mu$m).</li>
          <li><strong>Physical Meaning of Numerical Value Range (-1.0 to +1.0):</strong>
            <br>• <strong>Negative Values (-1.0 to 0.0):</strong> Water bodies, snow, ice, and clouds (because water absorbs NIR completely while reflecting visible light, yielding a negative numerator).
            <br>• <strong>Low Positive Values (0.1 to 0.2):</strong> Bare barren rock, desert sand, concrete, urban asphalt.
            <br>• <strong>Moderate Positive Values (0.2 to 0.5):</strong> Sparse scrub, dry rangelands, senescent crops, grasslands.
            <br>• <strong>High Positive Values (0.6 to 0.9+):</strong> Dense, healthy, multi-layered temperate and tropical moist rainforests at peak photosynthetic vigor.</li>
          <li><strong>Role in Monitoring Forest Degradation:</strong> Enables automated multi-temporal satellite change-detection. When illegal selective logging or forest fires thin the canopy without clearcutting, NIR reflectance drops and exposed red soil reflectance rises, triggering an immediate drop in pixel NDVI that alerts forest rangers.</li>
        </ul>""",
        "detailed_answer": """<div class="detailed-body">
          <p><strong>Normalization Physics:</strong> Raw satellite reflectance values vary wildly based on sun illumination angle, cloud shadows, and atmospheric haze. By dividing the difference by the sum ($\frac{\text{NIR} - \text{Red}}{\text{NIR} + \text{Red}}$), topographic shadowing and solar variations are canceled out, normalizing the output into a stable, dimensionless ratio between -1 and +1.</p>
          <p><em>Slide Reference: Class 18 Slides 27–31 (NDVI & Canopy Density).</em></p>
        </div>"""
    }
]
