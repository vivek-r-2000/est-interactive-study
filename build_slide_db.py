import json
import re
import os
import fitz

with open("Study_Material/lectures_metadata.json", "r", encoding="utf-8") as f:
    meta_list = json.load(f)

def clean_text(t):
    if not t:
        return ""
    t = t.replace('\ufffd', '').replace('', '')
    t = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\x9f]', ' ', t)
    t = re.sub(r'\s+', ' ', t).strip()
    return t

# Specific slide title overrides where PDF has blank text or generic "Slide X"
SLIDE_TITLES_OVERRIDE = {
    ("01", 14): "Emergency Response to Climate Breakdown (WWF)",
    ("01", 15): "Commercial Deforestation and Paper Consumption (WWF)",
    ("01", 16): "Evolutionary Adaptation and Climate Disruption (WWF)",
    ("01", 17): "Ocean Plastic Pollution and Marine Debris (WWF)",
    ("01", 18): "Habitat Destruction and Forest Fragmentation (Robin Wood)",
    ("01", 19): "Global Biodiversity Loss and Extinction Rates (Bund)",
    ("01", 20): "Endangered Wildlife Protection Campaign (WWF)",
    ("01", 21): "Earth Hour and Urban Energy Conservation",
    ("01", 22): "Desertification and Arid Soil Degradation (WWF)",
    ("01", 23): "Global Afforestation and Reforestation (Plant-for-the-Planet)",
    ("01", 24): "Letter from Year 2070: Premise & Context",
    ("01", 25): "Letter from 2070: Water Depletion & Health Crisis",
    ("01", 26): "Letter from 2070: Atmosphere & UV Radiation Hazards",
    ("01", 27): "Letter from 2070: Oxygen Rationing & Air Scarcity",
    ("01", 28): "Letter from 2070: Societal Collapse & Resource Wars",
    ("01", 29): "Letter from 2070: Intergenerational Warning & Action",
    ("02", 10): "Global Income and Resource Consumption Disparity",
    ("02", 16): "Easter Island Ecological Overshoot Case Study",
    ("02", 19): "Ecosystem Collapse in the Baltic Sea",
    ("02", 20): "Baltic Sea Dead Zones and Hypoxia",
    ("02", 21): "Sacred Groves: Community-Based Forest Conservation",
    ("02", 23): "Kolleru Lake Wetland Encroachment and Degradation",
    ("02", 24): "Kolleru Lake Aquaculture Expansion Satellite Evidence",
    ("02", 25): "Kolleru Lake Water Quality Degradation",
    ("02", 29): "Global Biocapacity Deficit and Ecological Debt",
    ("02", 34): "Earth Overshoot Day Trends (1970–Present)",
    ("02", 38): "Human Development Index vs Ecological Footprint",
    ("02", 42): "National Ecological Deficits vs Reserves Matrix",
    ("02", 44): "Global Biocapacity Distribution by Continent",
    ("02", 45): "Per Capita Carbon Footprint Across Major Economies",
    ("02", 46): "Global Sustainability Framework and Tradeoffs",
    ("03", 2): "Anthropogenic Pressures on Planetary Boundaries",
    ("03", 9): "Cultural Eutrophication in Coastal Waters",
    ("03", 15): "Deepwater Horizon Oil Spill Impact and Chemical Dispersants",
    ("03", 21): "Kubuqi Model: Ecosystem Restoration in the Kubuqi Desert",
    ("03", 27): "Biomagnification of Persistent Organic Pollutants (POPs)",
    ("04", 6): "Electromagnetic Spectrum: Atmospheric Transmission Windows",
    ("04", 8): "Spectral Reflectance Signatures of Healthy Vegetation, Water, and Soil",
    ("04", 12): "Satellite Sensor Comparison: Landsat, IRS LISS-III, and Sentinel-2",
    ("04", 16): "Urban Heat Island Mitigation and Land Surface Temperature in GHMC",
    ("05", 1): "Environmental Crises and Landmark Planetary Events",
    ("05", 2): "Global Media Coverage of Major Ecological Disasters",
    ("05", 8): "Persistent Organic Pollutants (POPs) and the Stockholm Convention",
    ("05", 14): "Global Distillation (Grasshopper Effect) in Arctic Food Chains",
    ("05", 19): "Global Dimming vs Global Warming: Solar Radiation Trends",
    ("05", 25): "Azolla Event: Eocene CO2 Drawdown and Paleoclimate Cooling",
    ("06", 1): "Earth System Spheres and Biogeochemical Interactions",
    ("06", 7): "Internal Structure of Earth: Core, Mantle, and Tectonic Crust",
    ("06", 14): "Lovelock's Gaia Hypothesis and Daisyworld Homeostasis Model",
    ("06", 22): "Eltonian Trophic Pyramids and Lindeman's 10% Efficiency Law",
    ("06", 30): "Global Carbon Cycle Reservoirs and Anthropogenic Fluxes",
    ("06", 36): "Nitrogen Cycle: Biological Fixation, Nitrification, and Anammox",
    ("07", 1): "Climate System Dynamics and Global Vulnerability",
    ("07", 8): "Radiative Forcing and Greenhouse Gas Absorption Spectra",
    ("07", 15): "Steric Sea Level Rise vs Continental Glacier Melt Physics",
    ("07", 22): "Sundarbans Mangrove Vulnerability and Sea Level Rise Threats",
    ("08", 1): "Tipping Points and Abrupt Nonlinear Climate Change",
    ("08", 7): "Atlantic Meridional Overturning Circulation (AMOC) Collapse Risk",
    ("08", 14): "Eric Drexler's Nanotechnology Risk and the Molecular Assembler Debate",
    ("08", 20): "Wet-Bulb Temperature Thresholds and Human Heat Survival Limits",
    ("09", 1): "Terrestrial Carbon Sequestration and Forest Biomass",
    ("09", 2): "Muir Glacier Photographic Evidence of Retreat (1941 vs 2004)",
    ("09", 8): "Global Forest Carbon Stocks and FAO Biomass Accounting",
    ("09", 18): "Soil Organic Carbon (SOC) Reservoirs and Depth Profiles",
    ("10", 1): "Clean Development Mechanism (CDM) and Ocean Sequestration",
    ("10", 8): "UNFCCC Kyoto Protocol Flexible Market Mechanisms and CERs",
    ("10", 18): "Deep Ocean CO2 Injection Thermodynamics and Hydrate Lakes",
    ("10", 28): "Ocean Iron Fertilization (Martin Hypothesis) and Toxic Diatoms",
    ("11", 1): "Clean Technology Solutions and Negative Emissions",
    ("11", 6): "Biochar Thermochemical Pyrolysis Chemistry and Soil Stability",
    ("11", 14): "Enhanced Silicate Rock Weathering (Olivine Carbonate Cycle)",
    ("11", 22): "Direct Air Capture (DAC) Sorbent Thermodynamics and Costs",
    ("12", 1): "Environmental Impact Assessment (EIA) Principles and Framework",
    ("12", 2): "Statutory EIA Process Workflow Under Indian Notification 2006",
    ("12", 8): "Baseline Environmental Characterization and Prediction Trajectories",
    ("13", 1): "Grassroots Environmental Movements in India",
    ("13", 3): "Historical Chronology of Community Ecological Struggles",
    ("14", 1): "Green Computing and Sustainable ICT Architecture",
    ("14", 3): "Semiconductor Supply Chain and Conflict Mineral Extraction",
    ("15", 1): "Green Engineering Principles and Industrial Ecology",
    ("15", 2): "Anastas and Zimmerman's 12 Principles of Green Engineering",
    ("15", 8): "Kalundborg Industrial Symbiosis Closed-Loop Material Exchange"
}

def generate_compact_explanation(lec_id, slide_num, title, bullets, full_text):
    text_combined = (title + " " + " ".join(bullets) + " " + full_text).lower()
    
    # 1. Specialized high-yield scientific topics with word boundaries
    if re.search(r'\bbishnoi\b', text_combined):
        return "The Bishnoi community of Rajasthan sacrificed 363 lives in 1730 led by Amrita Devi to protect sacred Khejri (Prosopis cineraria) trees from the Maharaja of Jodhpur's axemen. Founded by Guru Jambheshwar in the 15th century with 29 rules protecting green trees and wildlife, the Bishnois established India's first recorded grassroots conservation movement."
    elif re.search(r'\bchipko\b|\bbahuguna\b|\bgaura\s+devi\b', text_combined):
        return "The Chipko Movement started in the 1970s in the Garhwal Himalayas of Uttarakhand (Reni village). When the state forest department allotted ash trees to a commercial sports goods manufacturer while banning local agricultural use, rural women led by Gaura Devi, Sunderlal Bahuguna, and Chandi Prasad Bhatt hugged trees to halt commercial felling. The struggle forced a 15-year logging ban across Himalayan catchment forests."
    elif re.search(r'\bappiko\b', text_combined):
        return "The Appiko Movement began in September 1983 in Salkani, Uttara Kannada (Karnataka) as the southern counterpart to Chipko. Villagers hugged trees to stop commercial clear-cutting of moist tropical forests in the Western Ghats. Appiko organized around three principles: Ubbesu (save), Belessu (grow), and Balesu (rational use), focusing on the 5 Fs of subsistence: food, fodder, fuel, fertilizer, and fiber."
    elif re.search(r'\bsilent\s+valley\b|\bkunthipuzha\b', text_combined):
        return "The Save Silent Valley struggle (1970s–1980s) in Palakkad, Kerala stopped a 120 MW hydroelectric dam across the Kunthipuzha River that would have submerged 8.3 sq km of undisturbed tropical evergreen rainforest. Scientific surveys demonstrating that the valley was a critical refuge for the endangered Lion-tailed Macaque led the central government to scrap the dam and designate Silent Valley National Park in 1984."
    elif re.search(r'\bnarmada\b|\bmedha\s+patkar\b|\bbaba\s+amte\b', text_combined):
        return "The Narmada Bachao Andolan (NBA), founded in 1985 by Medha Patkar and Baba Amte, opposed large dams along the Narmada river, focusing on the Sardar Sarovar Project. The campaign challenged large-scale river engineering by documenting the displacement of over 250,000 predominantly tribal residents without adequate rehabilitation, fertile valley submergence, and flawed cost-benefit estimates."
    elif "24-kg" in text_combined or (re.search(r'\bfossil\s+fuels?\b', text_combined) and re.search(r'\bmonitor\b', text_combined)):
        return "Manufacturing a typical 24-kg desktop computer and CRT monitor consumes 240 kg of fossil fuels, 22 kg of chemicals, and 1,500 kg of water. Unlike conventional heavy machinery where the product weight exceeds the manufacturing inputs, semiconductors and computer hardware have an inverted 10:1 material footprint ratio. Over 80% of an electronic device's lifecycle energy is embodied in manufacturing rather than operational use."
    elif re.search(r'\bmoore(?:\'s)?\s+law\b', text_combined):
        return "Moore's Law observed that transistor density on integrated circuits doubles approximately every 18 to 24 months. While this drove exponential gains in compute speed, it shortened hardware replacement cycles to 2–3 years. Rapid obsolescence accelerates conflict mineral extraction and generates millions of tons of hazardous electronic waste annually."
    elif re.search(r'\be-?waste\b|\belectronic\s+waste\b', text_combined):
        return "Electronic waste (e-waste) covers obsolete, broken, or end-of-life electrical equipment. E-waste is the fastest-growing solid waste stream globally, exceeding 50 million metric tons annually. It concentrates hazardous substances including lead in CRT glass, cadmium in contacts, mercury in backlights, and brominated flame retardants in plastics, which are regulated internationally under the Basel Convention."
    elif re.search(r'\bthin\s+clients?\b|\bthick\s+clients?\b', text_combined):
        return "Traditional thick clients run local CPUs and storage with 150–250W power draws. Thin clients use compact solid-state hardware drawing only 10–20W, offloading computation to centralized servers. Thin clients last 6–8 years compared to 3–4 years for desktop PCs, cut workstation acquisition costs by roughly 50%, and reduce physical e-waste volume."
    elif re.search(r'\banastas\b|\b12\s+principles\b', text_combined) or (lec_id == "15" and re.search(r'\bprinciples?\b', text_combined)):
        return "Paul Anastas and Julie Zimmerman codified the 12 Principles of Green Engineering to guide sustainable product and process design. Key principles include making processes inherently non-hazardous, prioritizing waste prevention over remediation, designing for separation, minimizing material diversity, integrating energy and mass flows, and designing for commercial end-of-life recycling."
    elif re.search(r'\byear\s+2070\b|\bletter\s+written\b', text_combined):
        return "The 'Letter Written in the Year 2070' narrative dramatizes the consequences of severe ecological overshoot. It portrays an arid future where groundwater depletion, extreme UV radiation from ozone destruction, and air taxation force extreme survival measures, emphasizing the need for precautionary resource stewardship and intergenerational equity."
    elif re.search(r'\bgarrett\s+hardin\b|\btragedy\s+of\s+the\s+commons\b|\bipat\b', text_combined):
        return "Garrett Hardin's 1968 paper 'Tragedy of the Commons' demonstrates that open-access common resources suffer inevitable depletion when individuals capture full private benefits of extraction while sharing ecological costs across society. The IPAT equation ($I = P \\times A \\times T$) links environmental impact ($I$) to population ($P$), per-capita affluence ($A$), and technological intensity ($T$)."
    elif re.search(r'\bremote\s+sensing\b|\bspectral\s+reflectance\b|\blandsat\b|\bndvi\b', text_combined):
        return "Satellite remote sensing measures reflected and emitted electromagnetic radiation across visible, near-infrared (NIR), and shortwave-infrared (SWIR) bands. Healthy green vegetation absorbs red light for photosynthesis and strongly scatters NIR light at the spongy mesophyll layer, allowing multispectral indices like NDVI to quantify plant vigor and track regional land cover change over decades."
    elif re.search(r'\bcarbon\s+sequestration\b|\bcarbon\s+sink\b', text_combined):
        return "Terrestrial carbon sequestration stores atmospheric $CO_2$ in plant biomass and soil organic matter. Dry forest biomass contains approximately 50% elemental carbon, converting to $CO_2$ equivalents through the molecular mass ratio $44/12 \\approx 3.67$. Protecting old-growth forest soils and restoring degraded land maintains active terrestrial carbon sinks without industrial energy penalties."
    elif re.search(r'\beia\b|\bterms\s+of\s+reference\b|\bpublic\s+hearing\b', text_combined) and lec_id == "12":
        return "Environmental Impact Assessment (EIA) evaluates the environmental consequences of a proposed development before statutory approval. Under India's EIA Notification 2006, projects undergo Screening to classify them into Category A (central clearance) or Category B (state clearance), followed by Scoping to define formal Terms of Reference (ToR) and baseline monitoring criteria."
    elif re.search(r'\bbhopal\b|\bmethyl\s+isocyanate\b', text_combined):
        return "The Bhopal disaster occurred on December 2–3, 1984, when water entered storage tank 610 at the Union Carbide pesticide plant, triggering an exothermic runaway reaction that released 42 tons of toxic methyl isocyanate (MIC) gas across the city. The disaster caused thousands of acute fatalities and led directly to the enactment of India's Environment (Protection) Act 1986."
    elif re.search(r'\bchernobyl\b', text_combined):
        return "The Chernobyl disaster on April 26, 1986, destroyed reactor 4 of the Chernobyl Nuclear Power Plant in Ukraine during an unauthorized low-power turbine test. A severe steam explosion and graphite fire released 12 exabecquerels of radioactivity (notably Iodine-131 and Cesium-137), forcing the evacuation of 350,000 residents and creating the 2,600 sq km Chernobyl Exclusion Zone."
    elif re.search(r'\bminamata\b', text_combined):
        return "Minamata disease is severe neurological poisoning caused by methylmercury bioaccumulation. The Chisso Corporation discharged industrial wastewater containing methylmercury into Minamata Bay, Japan from 1932 to 1968. Marine organisms bioaccumulated the organic mercury, causing severe sensory loss, ataxia, paralysis, and congenital defects in fishing families, prompting the global Minamata Convention on Mercury."
    elif re.search(r'\beutrophication\b|\balgal\s+blooms?\b', text_combined):
        return "Cultural eutrophication occurs when excess agricultural nitrogen and phosphorus run off into lakes and estuaries. Nutrient enrichment triggers explosive algae blooms that block sunlight and deplete dissolved oxygen (DO) as dead biomass decays, creating anoxic dead zones with DO levels below 2 mg/L that suffocate fish and benthic organisms."
    elif re.search(r'\bozone\s+deplet|\bstratospheric\s+ozone\b|\bcfcs?\b', text_combined):
        return "Stratospheric ozone ($O_3$) absorbs harmful solar ultraviolet-B radiation (280–315 nm). Chlorofluorocarbons (CFCs) release reactive chlorine radicals under UV radiation, with each free chlorine radical catalytically destroying up to 100,000 ozone molecules. The 1987 Montreal Protocol phased out ozone-depleting substances, setting the ozone layer on a gradual recovery path."
    elif re.search(r'\bamoc\b|\bmeridional\s+overturning\b', text_combined):
        return "The Atlantic Meridional Overturning Circulation (AMOC) transports warm, saline tropical surface water to the North Atlantic, where it cools, sinks, and returns south as deep water. Freshwater influx from accelerating Greenland ice melt lowers seawater density, weakening the sinking mechanism and risking a regional climate tipping point."

    # 2. Derive concise pedagogical explanation from slide bullets and text
    clean_bullets = [b for b in bullets if len(b) > 10 and not b.lower().startswith("http")]
    if clean_bullets:
        bullet_text = ". ".join(clean_bullets[:3])
        # Ensure it ends with a period
        if not bullet_text.endswith("."):
            bullet_text += "."
        # Combine into a clean 2-sentence summary
        return f"{title}: {bullet_text} This material establishes quantitative limits, operational trade-offs, and core exam principles for Lecture {lec_id}."
    
    # 3. Visual slide fallback with specific descriptive language
    clean_title = title if not title.lower().startswith("slide ") else f"Lecture {lec_id} figure {slide_num}"
    return f"{clean_title} illustrates key empirical observations and visual relationships in Lecture {lec_id}. It provides field data, case evidence, or system diagrams that support the quantitative and regulatory concepts taught in this topic."

full_database = {}

for lec in meta_list:
    lec_id = lec["id"]
    lec_title = lec["title"]
    lec_slug = lec["slug"]
    slides_info = []
    
    for s in lec["slides"]:
        s_num = s["slide_num"]
        s_title = s.get("title", f"Slide {s_num}").strip()
        s_text = s.get("text_snippet", "").strip()
        
        # Override generic titles
        if (lec_id, s_num) in SLIDE_TITLES_OVERRIDE:
            s_title = SLIDE_TITLES_OVERRIDE[(lec_id, s_num)]
        elif s_title.lower().startswith("slide ") and len(s_text) > 5:
            first_line = clean_text(s_text.split(". ")[0].split("\n")[0])
            if len(first_line) > 3 and not first_line.lower().startswith("http"):
                s_title = first_line[:65]
        
        # Clean bullets
        bullets = []
        if s_text:
            lines = [clean_text(l) for l in s_text.split("\n") if len(clean_text(l)) > 3]
            bullets = [l for l in lines if not l.lower().startswith("http") and not l.isdigit() and not l.startswith("$$")][:6]
        
        # Clean dollar signs in title and bullets to prevent KaTeX issues
        s_title = s_title.replace("$$", "funds")
        bullets = [b.replace("$$", "funds") for b in bullets]
        
        deep_exp = generate_compact_explanation(lec_id, s_num, s_title, bullets, s_text)
        deep_exp = deep_exp.replace("$$", "funds")
        
        slides_info.append({
            "slide_num": s_num,
            "source_file": s["source_file"],
            "page_in_file": s["page_in_file"],
            "title": s_title,
            "bullets": bullets,
            "image": s["image"],
            "deep_explanation": deep_exp
        })
        
    full_database[lec_id] = {
        "title": lec_title,
        "slug": lec_slug,
        "total_slides": len(slides_info),
        "slides": slides_info
    }
    print(f"Processed Lec {lec_id}: {len(slides_info)} slides with unslopped compact explanations.")

with open("Study_Material/full_slide_database.json", "w", encoding="utf-8") as f:
    json.dump(full_database, f, indent=2)

print("\nSaved Study_Material/full_slide_database.json with unslopped writing!")
