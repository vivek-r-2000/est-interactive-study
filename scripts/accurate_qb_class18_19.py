import json

def get_class18_questions():
    return [
        {
            "id": "EQB-18-01",
            "class_id": 18,
            "class_name": "Natural Resource Accounting & Geospatial Technology",
            "topic": "Remote Sensing Definition",
            "category": "Short Answer & Definitions",
            "exams": [
                {"paper": "End Exam 2019", "section": "Section I, Q1", "marks": "1M"}
            ],
            "marks": "1M",
            "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
            "prompt": "Define Remote sensing.",
            "key_answer_points": "<ul>\n<li><strong>Definition:</strong> The science and art of acquiring information about the Earth's surface, atmosphere, and oceans from a distance—typically using satellite or aircraft sensors measuring reflected or emitted electromagnetic radiation—without making physical contact with the object.</li>\n<li><strong>Core Workflow:</strong> Energy Source (Sun/Radar) $\\rightarrow$ Transmission through atmosphere $\\rightarrow$ Interaction with target Earth surface $\\rightarrow$ Sensor recording $\\rightarrow$ Transmission & Digital Image Processing.</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>Earth Observation:</strong> Enables continuous, non-invasive monitoring of global natural resources across spatial and temporal scales.</p>\n<p><em>Slide Reference: Class 18 Slide 4.</em></p>\n</div>"
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
            "key_answer_points": "<ul>\n<li><strong>Healthy Green Vegetation:</strong> Appears as <strong>Vibrant Red / Bright Pink</strong> in standard False Color Composites (FCC: NIR band mapped to Red channel, Red band mapped to Green, Green band mapped to Blue).\n<br>• <em>Reason:</em> Spongy mesophyll leaf cells reflect strongly in the Near-Infrared (NIR) spectrum (40–50% reflectance) while absorbing visible red light for photosynthesis.</li>\n<li><strong>Deeper Clear Water Bodies:</strong> Appear as <strong>Deep Blue to Jet Black</strong>.\n<br>• <em>Reason:</em> Water absorbs almost 100% of incoming Near-Infrared and Shortwave-Infrared radiation; deep, clear water reflects virtually zero NIR back to satellite sensors.</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>Why False Color?:</strong> The human eye cannot perceive infrared light. Mapping near-infrared reflectance to the visible red color channel makes healthy plant biomass stand out vividly against non-living backgrounds.</p>\n<p><em>Slide Reference: Class 18 Slides 8–10.</em></p>\n</div>"
        },
        {
            "id": "EQB-18-03",
            "class_id": 18,
            "class_name": "Natural Resource Accounting & Geospatial Technology",
            "topic": "Six Applications of Remote Sensing in Environmental Studies",
            "category": "Descriptive & Case Study",
            "exams": [
                {"paper": "End Exam 2019", "section": "Section I, Q3", "marks": "3M"}
            ],
            "marks": "3M",
            "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
            "prompt": "List any Six applications of remote sensing technology in environmental studies.",
            "key_answer_points": "<ul>\n<li><strong>1. Forest Cover & Deforestation Monitoring:</strong> Tracking canopy density loss, illegal logging, and measuring afforestation rates over time.</li>\n<li><strong>2. Natural Disaster Management:</strong> Mapping real-time flood extents, earthquake damage zones, cyclone tracks, and active forest wildfire perimeters (using thermal infrared sensors).</li>\n<li><strong>3. Agricultural Crop Health & Yield Prediction:</strong> Calculating NDVI vegetation health, drought stress, and soil moisture patterns.</li>\n<li><strong>4. Water Resource Assessment:</strong> Delineating reservoir shrinkage, glacial lake outburst flood (GLOF) risks, and coastal sediment plumes.</li>\n<li><strong>5. Urban Heat Island & Land Use Mapping (LULC):</strong> Detecting urban sprawl, wetland encroachment, and concrete heat retention.</li>\n<li><strong>6. Coastal & Coral Reef Health:</strong> Mapping mangrove extent, coastal erosion, and thermal coral bleaching anomalies.</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>Planetary Scale:</strong> Satellite sensors provide synoptic, repetitive coverage of remote terrains (like the Himalayas or Amazon basin) that are impossible to survey manually on foot.</p>\n<p><em>Slide Reference: Class 18 Slides 12–16.</em></p>\n</div>"
        },
        {
            "id": "EQB-18-04",
            "class_id": 18,
            "class_name": "Natural Resource Accounting & Geospatial Technology",
            "topic": "Spectral Signatures in Natural Resource Accounting",
            "category": "Short Answer & Definitions",
            "exams": [
                {"paper": "End Exam 2019", "section": "Section I", "marks": "2M"}
            ],
            "marks": "2M",
            "importance": "HIGH (⭐⭐⭐⭐)",
            "prompt": "What are spectral signatures, and why is the near-infrared band critical for vegetation monitoring?",
            "key_answer_points": "<ul>\n<li><strong>Spectral Signature:</strong> The specific pattern of electromagnetic reflectance and absorption displayed by a material across different wavelengths of the spectrum, serving as a unique 'optical fingerprint'.</li>\n<li><strong>Why the Near-Infrared (NIR) Band is Critical:</strong> Chlorophyll pigments in green leaves absorb blue and red light for photosynthesis. However, leaf spongy mesophyll cells strongly bounce back Near-Infrared wavelengths (0.7–1.1 $\\mu$m) to avoid overheating. When a plant suffers water stress or disease, its cellular mesophyll collapses, causing NIR reflectance to drop dramatically before any visual yellowing is visible to the human eye.</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>Early Stress Detection:</strong> Near-infrared sensors detect crop drought and pest attacks days before damage becomes visible to human farmers.</p>\n<p><em>Slide Reference: Class 18 Slides 7–9.</em></p>\n</div>"
        },
        {
            "id": "EQB-18-05",
            "class_id": 18,
            "class_name": "Natural Resource Accounting & Geospatial Technology",
            "topic": "Normalized Difference Vegetation Index (NDVI)",
            "category": "Short Answer & Definitions",
            "exams": [
                {"paper": "End Exam 2019", "section": "Section I", "marks": "2M"}
            ],
            "marks": "2M",
            "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
            "prompt": "What is NDVI (Normalized Difference Vegetation Index) and how is it used in natural resource accounting?",
            "key_answer_points": "<ul>\n<li><strong>Mathematical Formula:</strong>\n<div class=\"formula-box\">$$\\text{NDVI} = \\frac{\\text{NIR} - \\text{Red}}{\\text{NIR} + \\text{Red}}$$</div></li>\n<li><strong>Numerical Range & Interpretation:</strong> Values range from <strong>-1.0 to +1.0</strong>:\n<br>• Negative values ($-1.0$ to $0.0$): Water, snow, clouds.\n<br>• Near zero ($0.0$ to $0.2$): Bare rock, sand, concrete urban surfaces.\n<br>• Moderate positive ($0.2$ to $0.5$): Sparse grass, dry crops, shrubs.\n<br>• High positive ($0.6$ to $0.9$): Dense tropical rainforest, healthy mature crops.</li>\n<li><strong>Use in Natural Resource Accounting:</strong> Provides a standardized, objective spatial metric to quantify forest canopy degradation, track carbon sequestration stocks, and verify reforestation compliance for carbon credits.</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>Why Normalization Matters:</strong> Subtracting Red from NIR and dividing by their sum cancels out differences in solar illumination angles and atmospheric haze across seasons.</p>\n<p><em>Slide Reference: Class 18 Slides 10–11.</em></p>\n</div>"
        }
    ]

def get_class19_questions():
    return [
        {
            "id": "EQB-19-01",
            "class_id": 19,
            "class_name": "Environmental Ethics & Wetland Conservation",
            "topic": "Anthropocentrism vs Biocentrism vs Ecocentrism",
            "category": "Differentiate Between",
            "exams": [
                {"paper": "End Exam 2024", "section": "Section VI, Q3", "marks": "3M"},
                {"paper": "End Exam 2023", "section": "Section III, Q1", "marks": "3M"},
                {"paper": "End Exam 2022", "section": "Section X, Q(a)", "marks": "5M"},
                {"paper": "End Exam 2019", "section": "Section IX, Q5", "marks": "3M"},
                {"paper": "End Exam 2018", "section": "Part I, Q1", "marks": "6M"}
            ],
            "marks": "3M – 6M",
            "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
            "prompt": "Explain the basic difference between anthropocentrism, biocentrism and ecocentrism views on the environment?",
            "key_answer_points": "<ul>\n<li><strong>1. Anthropocentrism (Human-Centered Ethics):</strong>\n<br>• <em>Moral Standing:</em> Only humans possess moral standing and intrinsic worth.\n<br>• <em>Value of Nature:</em> Strictly <strong>instrumental value</strong> (nature exists merely to satisfy human economic needs, food, and recreation).\n<br>• <em>Conservation Justification:</em> Save forests so our grandchildren have clean water and timber (Gifford Pinchot, René Descartes).</li>\n<li><strong>2. Biocentrism (Life-Centered Ethics):</strong>\n<br>• <em>Moral Standing:</em> Extended to <strong>all individual living creatures</strong> (animals, birds, trees, microbes).\n<br>• <em>Value of Nature:</em> Every living organism has <strong>intrinsic value</strong> in its own right, independent of whether it is useful to humans.\n<br>• <em>Ethical Rule:</em> Harming a sentient animal or clearing a tree is morally wrong even if it benefits humans (Albert Schweitzer 'Reverence for Life', Paul Taylor).</li>\n<li><strong>3. Ecocentrism (Ecosystem-Centered / Holistic Ethics):</strong>\n<br>• <em>Moral Standing:</em> Extended to the <strong>entire ecological community as a whole</strong>, including non-living abiotic cycles (soils, watersheds, atmosphere, species populations).\n<br>• <em>Aldo Leopold's Land Ethic (1949):</em> <em>\"A thing is right when it tends to preserve the integrity, stability, and beauty of the biotic community. It is wrong when it tends otherwise.\"</em></li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>Expanding Moral Circles:</strong> Environmental ethics traces the historical expansion of who counts morally—from just humans, to all living organisms, to entire healthy watersheds.</p>\n<p><em>Slide Reference: Class 19 Slides 4–11.</em></p>\n</div>"
        },
        {
            "id": "EQB-19-02",
            "class_id": 19,
            "class_name": "Environmental Ethics & Wetland Conservation",
            "topic": "Deep Ecology vs Shallow Ecology (Arne Naess)",
            "category": "Differentiate Between",
            "exams": [
                {"paper": "End Exam 2023", "section": "Section II, Q13", "marks": "2M"}
            ],
            "marks": "2M",
            "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
            "prompt": "Differentiate between Deep ecology and Shallow ecology.",
            "key_answer_points": "<ul>\n<li><strong>Formulation:</strong> Introduced in 1973 by Norwegian philosopher <strong>Arne Naess</strong>.</li>\n<li><strong>Shallow Ecology:</strong>\n<br>• Fights pollution and resource depletion solely to protect the <strong>health and affluence of people in developed nations</strong>.\n<br>• Accepts modern technological capitalism, economic growth, and consumer lifestyles, seeking only technocratic band-aids (electric cars, catalytic converters, carbon offsets).</li>\n<li><strong>Deep Ecology:</strong>\n<br>• Demands a fundamental transformation in human spiritual and economic systems, recognizing <strong>biospherical egalitarianism</strong> (all species have an equal right to live and flourish).\n<br>• Rejects endless economic growth; argues that humans have no right to reduce rich biodiversity except to satisfy vital survival needs.</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>Reform vs Revolution:</strong> Shallow ecology asks 'how can we clean up pollution without hurting economic growth?', while Deep ecology asks 'how can we live in harmony with the planet without exceeding its carrying capacity?'.</p>\n<p><em>Slide Reference: Class 19 Slides 12–14.</em></p>\n</div>"
        },
        {
            "id": "EQB-19-03",
            "class_id": 19,
            "class_name": "Environmental Ethics & Wetland Conservation",
            "topic": "Libertarian Extension vs Ecological Extension",
            "category": "Differentiate Between",
            "exams": [
                {"paper": "End Exam 2024", "section": "Section IV(d)", "marks": "2M"},
                {"paper": "End Exam 2022", "section": "Section VII, Q(c)", "marks": "2M"}
            ],
            "marks": "2M",
            "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
            "prompt": "Differentiate between Libertarian and Ecological Extension.",
            "key_answer_points": "<ul>\n<li><strong>Libertarian Extension (Civil Rights Approach):</strong>\n<br>• Extends the traditional human philosophical framework of <strong>individual rights and civil liberties</strong> outward to non-human entities.\n<br>• Focuses on <em>individual organisms</em>: asserts that animals, birds, and trees have basic rights (right not to be tortured, right to life) just like human minorities (Peter Singer's Animal Liberation).</li>\n<li><strong>Ecological Extension (Relational Ecosystem Approach):</strong>\n<br>• Places emphasis not on individual legal rights, but on the <strong>fundamental ecological interdependence of all living and non-living things</strong> in biotic communities.\n<br>• Focuses on <em>the health of the whole system</em>: conserving nutrient loops, evolutionary diversity, and watershed stability (Aldo Leopold's Land Ethic).</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>Rights vs Systems:</strong> Libertarian extension looks at individual suffering; ecological extension looks at holistic ecosystem functioning.</p>\n<p><em>Slide Reference: Class 19 Slide 15.</em></p>\n</div>"
        },
        {
            "id": "EQB-19-04",
            "class_id": 19,
            "class_name": "Environmental Ethics & Wetland Conservation",
            "topic": "Article 51-A(g) Indian Constitution",
            "category": "Short Answer & Definitions",
            "exams": [
                {"paper": "End Exam 2024", "section": "Section II, Q(c)", "marks": "1M"},
                {"paper": "End Exam 2023", "section": "Section I, Q1(d)", "marks": "1M"}
            ],
            "marks": "1M",
            "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
            "prompt": "What is Art-51-A(g)? [one or two sentences]",
            "key_answer_points": "<ul>\n<li><strong>Constitutional Provision:</strong> Article 51-A(g) is a <strong>Fundamental Duty</strong> inserted into Part IV-A of the Constitution of India via the 42nd Amendment Act in 1976.</li>\n<li><strong>Verbatim Mandate:</strong> States that it shall be the duty of every citizen of India <em>\"to protect and improve the natural environment including forests, lakes, rivers and wildlife, and to have compassion for living creatures.\"</em></li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>Constitutional Green Duty:</strong> Pairs with Article 48-A (Directive Principles of State Policy) to give India one of the strongest constitutional frameworks for environmental protection in the world.</p>\n<p><em>Slide Reference: Class 19 Slide 18.</em></p>\n</div>"
        },
        {
            "id": "EQB-19-05",
            "class_id": 19,
            "class_name": "Environmental Ethics & Wetland Conservation",
            "topic": "Landmark Indian Environmental Legislation",
            "category": "Short Answer & Definitions",
            "exams": [
                {"paper": "End Exam 2019", "section": "Section IX, Q3", "marks": "2M"},
                {"paper": "End Exam 2018", "section": "Part I, Q2", "marks": "4M"}
            ],
            "marks": "2M – 4M",
            "importance": "HIGH (⭐⭐⭐⭐)",
            "prompt": "Give a brief account of Wild life Act and Air Act. (List any four environmental legislations).",
            "key_answer_points": "<ul>\n<li><strong>Wildlife (Protection) Act, 1972:</strong> Prohibits hunting of endangered species (Schedules I to VI), establishes National Parks and Wildlife Sanctuaries, and regulates trade in animal trophies and ivory.</li>\n<li><strong>Air (Prevention and Control of Pollution) Act, 1981:</strong> Enacted under Article 253 to implement the Stockholm Conference decisions; establishes Air Pollution Control Areas, sets ambient air quality standards, and empowers State Pollution Control Boards to monitor and penalize industrial smokestack emissions (amended in 1987 to include noise).</li>\n<li><strong>Other Key Acts:</strong> Water (Prevention and Control of Pollution) Act 1974, Environment (Protection) Act 1986, Biological Diversity Act 2002.</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>The Legislative Foundation:</strong> These laws form the statutory backbone of environmental regulation and judicial enforcement in India.</p>\n<p><em>Slide Reference: Class 19 Slides 19–21.</em></p>\n</div>"
        },
        {
            "id": "EQB-19-06",
            "class_id": 19,
            "class_name": "Environmental Ethics & Wetland Conservation",
            "topic": "Ramsar Convention Definition & Indian Sites Count",
            "category": "Short Answer & Definitions",
            "exams": [
                {"paper": "End Exam 2024", "section": "Section II, Q(b)", "marks": "1M"},
                {"paper": "End Exam 2023", "section": "Section I, Q1(f)", "marks": "1M"},
                {"paper": "End Exam 2022", "section": "Section III, Q2 & Section V(b)", "marks": "1M + 1M"},
                {"paper": "End Exam 2019", "section": "Section IX, Q4", "marks": "5M"},
                {"paper": "End Exam 2018", "section": "Part V, Q1", "marks": "1M"}
            ],
            "marks": "1M – 5M",
            "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
            "prompt": "What is Ramsar Convention? (Number of Ramsar sites in India as on Aug 2022?)",
            "key_answer_points": "<ul>\n<li><strong>Definition:</strong> The <strong>Ramsar Convention on Wetlands of International Importance</strong> is an intergovernmental environmental treaty adopted on 2nd February 1971 in Ramsar, Iran.</li>\n<li><strong>Core Philosophy:</strong> Provides the framework for national action and international cooperation for the conservation and <strong>'Wise Use'</strong> of wetlands and their resources.</li>\n<li><strong>Ramsar Sites in India:</strong> As of August 2022 (celebrating 75 years of Independence), India designated <strong>75 Ramsar sites</strong> (which expanded to 85 sites in 2024).</li>\n<li><strong>Examples of Indian Ramsar Sites:</strong> Chilika Lake (Odisha), Keoladeo National Park (Rajasthan), East Kolkata Wetlands (West Bengal), Loktak Lake (Manipur), Vembanad-Kol (Kerala), Wular Lake (J&K).</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>The Wise Use Doctrine:</strong> Unlike rigid exclusionist conservation, Ramsar recognizes that humans can sustainably harvest fish, reeds, and water as long as ecological character is preserved.</p>\n<p><em>Slide Reference: Class 19 Slides 22–26.</em></p>\n</div>"
        },
        {
            "id": "EQB-19-07",
            "class_id": 19,
            "class_name": "Environmental Ethics & Wetland Conservation",
            "topic": "Riparian Forest Buffers & Functions",
            "category": "Short Answer & Definitions",
            "exams": [
                {"paper": "End Exam 2023", "section": "Section II, Q18", "marks": "2M"},
                {"paper": "End Exam 2019", "section": "Section II, Q3", "marks": "0.5M"}
            ],
            "marks": "0.5M – 2M",
            "importance": "HIGH (⭐⭐⭐⭐)",
            "prompt": "What are riparian forest buffers and their functions?",
            "key_answer_points": "<ul>\n<li><strong>Definition:</strong> Strips of permanent trees, shrubs, and native grasses planted directly along the banks of rivers, streams, and lakes.</li>\n<li><strong>Function 1 (Filtration & Pollution Trap):</strong> Dense roots filter out up to <strong>80–90% of excess agricultural fertilizer (nitrates, phosphates) and pesticides</strong> from surface runoff before it reaches the river.</li>\n<li><strong>Function 2 (Riverbank Stabilization):</strong> Deep root networks physically bind bank soils, preventing bank collapse and reducing downstream reservoir siltation.</li>\n<li><strong>Function 3 (Aquatic Habitat & Thermal Shading):</strong> Overhanging tree canopies shade river waters, keeping water temperatures cool enough for sensitive cold-water fish and aquatic insects.</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>Nature's Buffer:</strong> Riparian zones act as the primary defense line protecting freshwater bodies from agricultural runoff.</p>\n<p><em>Slide Reference: Class 19 Slide 27 & Class 9 Slide 18.</em></p>\n</div>"
        },
        {
            "id": "EQB-19-08",
            "class_id": 19,
            "class_name": "Environmental Ethics & Wetland Conservation",
            "topic": "Ramsar Wetland Site Case Study (East Kolkata Wetlands)",
            "category": "Descriptive & Case Study",
            "exams": [
                {"paper": "End Exam 2019", "section": "Section IX, Q4", "marks": "5M"},
                {"paper": "End Exam 2018", "section": "Part V, Q3", "marks": "10M"}
            ],
            "marks": "5M – 10M",
            "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
            "prompt": "Describe any one Ramsar site with focus on: (a) Location and Any three criterion of convention to describe it as wetland (b) Ecological significance and Threats / Reasons for change (c) Restoration or conservation measurements.",
            "key_answer_points": "<ul>\n<li><strong>Site Choice: East Kolkata Wetlands (EKW), West Bengal, India</strong> (Designated Ramsar Site No. 1208 in 2002; area: ~12,500 hectares).</li>\n<li><strong>(a) Location & Three Ramsar Criteria:</strong>\n<br>• <em>Location:</em> Eastern fringes of Kolkata municipal corporation, West Bengal.\n<br>• <em>Criterion 1 (Unique Ecological Model):</em> World's largest organic sewage-fed wastewater resource recovery ecosystem.\n<br>• <em>Criterion 2 (Threatened Species Support):</em> Supports vulnerable marsh mongoose, fishing cats, and migratory waterfowl.\n<br>• <em>Criterion 3 (Biological Diversity):</em> Houses diverse plankton, algae, and over 100 species of waterfowl and commercial fish.</li>\n<li><strong>(b) Ecological Significance & Natural Water Treatment:</strong>\n<br>• Treats <strong>over 750 million liters of raw municipal sewage every day for free</strong> through natural sunlight, algal photosynthesis, and bacterial symbiosis without artificial chemical plants.\n<br>• Fishponds (<em>bheris</em>) harvest over 10,000 tonnes of fish annually, while agricultural beds supply 150 tonnes of fresh vegetables daily to Kolkata city.</li>\n<li><strong>(c) Major Threats & Conservation Measures:</strong>\n<br>• <em>Threats:</em> Rapid illegal real-estate encroachment, urban landfill dumping (Dhapa), industrial heavy metal effluent (tanneries), and water siltation.\n<br>• <em>Conservation Measures:</em> Judicial protection via Calcutta High Court landmark ruling (1992); establishment of the East Kolkata Wetlands Management Authority (EKWMA); strict enforcement against unauthorized land-use conversion.</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>A Living Ecological Miracle:</strong> The East Kolkata Wetlands save the municipal government hundreds of crores in sewage plant infrastructure while generating employment and food for local communities.</p>\n<p><em>Slide Reference: Class 19 Slides 24–26.</em></p>\n</div>"
        },
        {
            "id": "EQB-19-09",
            "class_id": 19,
            "class_name": "Environmental Ethics & Wetland Conservation",
            "topic": "Meaning of Endemic",
            "category": "MCQ & Objective",
            "exams": [
                {"paper": "End Exam 2022", "section": "Section II, Q1", "marks": "1M"}
            ],
            "marks": "1M",
            "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
            "prompt": "What is the meaning of the word \"endemic\"? [a] Rare and occur only in a few locations [b] Rare and occur everywhere [c] Abundant and seen everywhere [d] Abundant and only in few locations.",
            "key_answer_points": "<ul>\n<li><strong>Correct Option:</strong> <strong>[ a ] Rare and occur only in a few locations</strong> (or restricted to a specific geographic region).</li>\n<li><strong>Explanation:</strong> In ecology and biogeography, an endemic species is native and strictly confined to a defined geographic boundary (e.g. Lion-tailed Macaque in the Western Ghats).</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>Direct Exam Question:</strong> Appeared in End Exam 2022 Section II, Question 1.</p>\n<p><em>Slide Reference: Class 19 Slide 7 & Class 5 Slide 14.</em></p>\n</div>"
        },
        {
            "id": "EQB-19-10",
            "class_id": 19,
            "class_name": "Environmental Ethics & Wetland Conservation",
            "topic": "Year vs Environmental Act/Rule Match",
            "category": "Match the Following",
            "exams": [
                {"paper": "End Exam 2022", "section": "Section I(E)", "marks": "5M"}
            ],
            "marks": "5M",
            "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
            "prompt": "Section-I: Match the following: Year vs Act/Rule [5 Marks].",
            "key_answer_points": "<ul>\n<li><strong>Matching Solution:</strong>\n<br>1. <strong>1972</strong> $\\rightarrow$ <strong>The Wildlife Protection Act</strong>\n<br>2. <strong>1986</strong> $\\rightarrow$ <strong>The Environment Protection Act</strong>\n<br>3. <strong>1998</strong> $\\rightarrow$ <strong>The Biomedical waste Rules</strong>\n<br>4. <strong>2002</strong> $\\rightarrow$ <strong>The Biological Diversity Act</strong>\n<br>5. <strong>2010</strong> $\\rightarrow$ <strong>Wetland Rules (Wetlands Conservation & Management Rules)</strong></li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>Legal Chronology:</strong> Standard 5-mark match matrix tested in End Exam 2022 covering India's foundational environmental laws and statutory notifications.</p>\n<p><em>Slide Reference: Class 19 Slide 20.</em></p>\n</div>"
        }
    ]

if __name__ == "__main__":
    print(f"Class 18: {len(get_class18_questions())} Qs | Class 19: {len(get_class19_questions())} Qs.")
