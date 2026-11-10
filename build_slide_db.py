import json
import re
import os
import fitz

with open("Study_Material/lectures_metadata.json", "r", encoding="utf-8") as f:
    meta_list = json.load(f)

# Specific topic contexts per lecture to enrich explanations
LECTURE_CONTEXTS = {
    "01": "Course overview, sustainable development, environmental ads, global ecological awareness, and Dr. Kalam's 'Letter from 2070' highlighting extreme water scarcity and climate breakdown.",
    "02": "Earth spheres (Atmosphere, Hydrosphere, Lithosphere, Biosphere), Garrett Hardin's Tragedy of the Commons (1968), IPAT identity (I = P x A x T), Easter Island collapse, Baltic Sea algal blooms, Sacred Groves, Kolleru Lake degradation, ecological footprint, biocapacity, Earth Overshoot Day, and Human Development Index (HDI).",
    "03": "Aquatic and terrestrial environmental issues: cultural eutrophication, ocean dead zones, Gulf of Mexico oil spill (Deepwater Horizon), Niger delta pollution, thermal pollution (Chaohu Lake), acid rain, desertification, Kubuqi greening model, shifting cultivation (Jhum), landfill leachate, biomagnification vs bioaccumulation, and Antarctic ozone depletion.",
    "04": "Remote sensing principles: electromagnetic spectrum (EMS), spectral reflectance curves of vegetation (NIR plateau, red absorption), satellite sensors (Landsat MSS/TM/OLI, IRS LISS III, Sentinel-2), mangrove mapping, 1976-1999 change detection, Katchal island tsunami impact, water quality in Kollam, AHP landslide susceptibility mapping in Nilambur, and Urban Heat Island (LST) mitigation in Hyderabad (GHMC).",
    "05": "Landmark environmental events and crises: persistent organic pollutants (POPs), Global Distillation (Grasshopper effect), Arctic Paradox in Inuit communities, Global Dimming vs Warming (Wild et al. 2005), Azolla event (49 Ma), Three Gorges Dam geophysics and Earth rotation lengthening (0.06 microseconds), groundwater depletion pole shift, Tambora 1815 and Waterloo weather, Toba supervolcano, and nuclear winter theory (Carl Sagan / TTAPS).",
    "06": "Earth system components: internal layers, plate tectonics, James Lovelock's GAIA hypothesis, Daisyworld homeostatic temperature regulation model, biome classification, oligotrophic vs eutrophic lakes, Eltonian trophic pyramids, Lindeman's 10% ecological efficiency law, and global biogeochemical cycles (Carbon, Nitrogen, Phosphorus, Hydrological).",
    "07": "Climate change impacts: radiative forcing, positive ice-albedo feedback, cloud feedbacks, Stern Review economics of climate action, paleovegetation migration (Lenoir et al. 2008 upslope shift of 29m/decade), sea level rise physics (steric expansion vs ice melt), Sundarbans mangrove vulnerability and Royal Bengal Tiger extinction risk, and estuarine salinity intrusion affecting the Sundari tree (Heritiera fomes).",
    "08": "Unexpected climate changes and tipping points: Arctic sea ice melt, West Antarctic ice sheet disintegration, Amazon rainforest dieback, Nassim Taleb's Black Swan theory, Eric Drexler's molecular nanotechnology risks (Grey Goo), Bulletin of the Atomic Scientists Doomsday Clock (90 seconds to midnight), Global Terrestrial Stilling, Hypercanes (50 deg C ocean SST), ocean darkening, Chinchorro mummy decay, and athletic wet-bulb heat safety rules.",
    "09": "Carbon sequestration in terrestrial sinks: Muir Glacier retreat evidence (1941 vs 2004), atmospheric CO2 trend (419 ppm), global carbon budget partitioning (40% atm, 30% ocean, 30% land), forest biomass carbon accounting (dry wood = 50% carbon), FAO global forest statistics (4.06B ha), soil organic carbon (SOC) reservoir down to 1m depth, agroforestry practices (windbreaks, riparian buffers, silvopasture), and forest age vs carbon productivity curves.",
    "10": "Clean Development Mechanism (CDM) & ocean sequestration: UNFCCC CBDR principle, Kyoto Protocol flexible mechanisms, 6 Kyoto greenhouse gases, Certified Emission Reductions (CERs), additionality principle, Powerguda village (India's first rural carbon credit sale), biological Azolla carbon capture, geological CCS in Illinois Basin (IBDP), John Martin's ocean iron hypothesis, toxic algae risks (Pseudo-nitzschia / domoic acid), ocean acidification carbonate equilibrium, and coal-bed methane displacement hazards.",
    "11": "Climate technology solutions & clean tech: negative emissions technologies (NETs), biochar pyrolysis (4.8 Gt/yr potential), blue carbon restoration, enhanced silicate rock weathering (olivine reaction), Direct Air Capture (Climeworks solid sorbent, Carbon Engineering liquid KOH), synthetic air-to-fuels, Net Zero Teesside, ruminant enteric methane reduction via seaweed (Asparagopsis taxiformis), alternative insect protein, marine cloud brightening, low-PUE green datacenters, floating solar (FPV), blockchain commodity tracking, and vertical aeroponic farming.",
    "12": "Environmental Impact Assessment (EIA): definition and objectives, dynamic baseline environmental characterization, project activity decomposition into actions, direct vs indirect impacts, Phase 1 Screening (Category A/B/C) and Scoping (Terms of Reference), Preliminary Environmental Assessment (PEA), Phase 2 Full EIA study, public hearing protocols, the mitigation hierarchy (Avoid, Minimize, Rehabilitate, Offset), Environmental Management Plan (EMP), Indian EIA notifications (1994, 2006), Schedule-1 mandatory clearance lists, and strict 7 km to 25 km wetland buffer siting rules.",
    "13": "Environmental movements and grassroots ecology: Bishnoi community conservation ethics in Rajasthan (protection of sacred Khejri trees / Prosopis cineraria, Amrita Devi martyrdom in 1730), the Chipko movement in Uttarakhand (Sunderlal Bahuguna, Gaura Devi, Chandi Prasad Bhatt - hugging forest trees to prevent commercial sports goods logging), Appiko movement in Uttara Kannada (Western Ghats - 5Fs: Food, Fodder, Fuel, Fertilizer, Fiber), Silent Valley agitation in Kerala (saving the evergreen rainforest and lion-tailed macaque from the KSEB Kunthipuzha hydro project), Kali Bachao Andolan, and Narmada Bachao Andolan (Medha Patkar, Baba Amte - opposing large dams and displacement on the Narmada river).",
    "14": "Green computing and sustainable ICT: environmental lifecycle of computer hardware, conflict mineral extraction (coltan, neodymium, tantalum) causing rainforest degradation, manufacturing footprint (an average 24-kg desktop requires 240 kg fossil fuels, 22 kg chemicals, and 1.5 tons of water - 10:1 materials ratio), Moore's Law vs Wirth's Law, Energy Star certification (EPA 1992), virtualization reducing server count, algorithm computational efficiency, Blackle display energy savings, thin vs thick clients (cost and energy comparison), dynamic voltage scaling (DVFS), sleep modes, and global electronic waste (e-waste) hazards (lead, cadmium, mercury, brominated flame retardants) and the Basel Convention.",
    "15": "Green engineering principles and industrial ecology: definition of green engineering, Paul Anastas & Julie Zimmerman's 12 Principles of Green Engineering (inherently non-hazardous, waste prevention, separation and purification operations, design for maximum mass and energy efficiency, output-pulled rather than input-pushed, embedded entropy and complexity reduction, targeted durability rather than immortal persistence, eliminate capacity over-sizing, minimize material diversity, integrate energy and material flows, design for afterlife, and renewable feedstocks), life cycle assessment (LCA) methodology, industrial symbiosis (Kalundborg eco-industrial park), and cradle-to-cradle material circularity."
}

def clean_text(t):
    if not t:
        return ""
    # remove non-ascii weird control characters but keep standard punctuation
    t = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\x9f]', ' ', t)
    t = re.sub(r'\s+', ' ', t).strip()
    return t

def generate_deep_explanation(lec_id, slide_num, title, bullets, full_text):
    text_combined = (title + " " + " ".join(bullets) + " " + full_text).lower()
    lec_ctx = LECTURE_CONTEXTS.get(lec_id, "")

    # Specialized slide explanations based on known high-yield topics
    if "bishnoi" in text_combined:
        return "This slide examines the historic Bishnoi community of Rajasthan, renowned as India's first ecological stewards. Founded by Guru Jambheshwar in the 15th century with 29 rules (including strict prohibitions against cutting green trees and harming wild animals), the Bishnois sacrificed 363 lives in 1730 led by Amrita Devi to protect sacred Khejri (Prosopis cineraria) trees from the Maharaja of Jodhpur's axemen, establishing the historical antecedent for modern forest conservation."
    elif "chipko" in text_combined or "bahuguna" in text_combined:
        return "This slide covers the landmark Chipko Movement initiated in the 1970s in the Garhwal Himalayas of Uttarakhand (Reni village). When the state forest department allotted ash trees to a commercial sports goods manufacturer while denying local agricultural access, rural women led by Gaura Devi and environmentalists Sunderlal Bahuguna and Chandi Prasad Bhatt physically clung to trees ('Chipko' = to hug/cling). The movement forced a 15-year commercial logging moratorium across Himalayan catchment forests."
    elif "appiko" in text_combined:
        return "This slide details the Appiko Movement, the southern counterpart to Chipko launched in September 1983 in Salkani forest, Uttara Kannada (Karnataka). Villagers embraced trees to halt clear-cutting in the Western Ghats biodiversity hotspot. Appiko articulated three operational objectives encapsulated as 'Ubbesu' (save/protect), 'Belessu' (grow/plant), and 'Balesu' (rational use), focusing on the 5 Fs of rural subsistence: Food, Fodder, Fuel, Fertilizer, and Fiber."
    elif "silent valley" in text_combined or "kunthipuzha" in text_combined:
        return "This slide analyzes the Save Silent Valley Movement (1970s–1980s) in Palakkad, Kerala. The Kerala State Electricity Board (KSEB) proposed a 120 MW hydroelectric dam across the Kunthipuzha River that would submerge 8.3 sq km of pristine tropical evergreen rainforest. Led by the Kerala Sastra Sahitya Parishad (KSSP) and poet-activist Sugathakumari, the struggle successfully mobilized public opinion and scientific surveys of the endangered Lion-tailed Macaque, culminating in the cancellation of the dam and declaration of Silent Valley National Park in 1984."
    elif "narmada" in text_combined or "medha patkar" in text_combined:
        return "This slide focuses on the Narmada Bachao Andolan (NBA), founded in 1985 by Medha Patkar and Baba Amte to oppose massive multi-purpose dam projects (particularly the Sardar Sarovar Dam in Gujarat and Narmada Sagar in MP). The movement challenged conventional developmental models by highlighting the involuntary displacement of over 250,000 predominantly tribal people without adequate rehabilitation, environmental submergence of fertile agricultural valleys, and questionable cost-benefit accounting."
    elif "24-kg computer" in text_combined or "fossil fuel" in text_combined and "monitor" in text_combined:
        return "This slide highlights the severe ecological footprint of electronics manufacturing. Constructing a typical 24-kg desktop computer and CRT/LCD monitor requires an astonishing 240 kg of fossil fuels, 22 kg of toxic specialty chemicals, and 1,500 kg (1.5 tons) of clean water. Unlike conventional heavy machinery where the product mass exceeds the raw manufacturing inputs, semiconductors and IT hardware exhibit an inverted 10:1 material footprint ratio, proving that embodied manufacturing impacts far surpass the device's operational electricity consumption."
    elif "moore" in text_combined and "law" in text_combined:
        return "This slide contrasts Moore's Law (Gordon Moore's 1965 empirical observation that transistor density on integrated circuits doubles approximately every 18-24 months) with environmental sustainability. Rapid hardware obsolescence driven by Moore's Law accelerates computer turnover cycles from a decade down to 2-3 years, overwhelming municipal waste streams with millions of tons of hazardous electronics and exacerbating global conflict mineral depletion."
    elif "e-waste" in text_combined or "electronic waste" in text_combined:
        return "This slide defines Electronic Waste (e-Waste)—discarded electrical and electronic equipment that is obsolete, broken, or end-of-life. E-waste represents the fastest-growing solid waste stream globally (over 50 million metric tons annually). Crucially, e-waste contains hazardous toxins including lead (in solder and CRT glass), cadmium (in rechargeable batteries and contacts), mercury (in backlights and switches), and brominated flame retardants (BFRs in plastics), necessitating strict adherence to the Basel Convention on hazardous waste trade."
    elif "thin client" in text_combined or "thick" in text_combined:
        return "This slide evaluates the architectural comparison between Traditional Thick Clients (individual desktop PCs with local CPUs, hard drives, and 250W power supplies) and Thin Clients (compact, solid-state terminal appliances that offload computation to centralized server clusters). Thin clients consume only 10-20% of the electrical energy, lack moving parts (longer lifespan of 6-8 years vs 3-4 years for PCs), cost £210 vs £400 per workstation, and drastically curtail physical e-waste generation."
    elif "anastas" in text_combined or "12 principles" in text_combined or "green engineering" in text_combined:
        return "This slide presents the core doctrine of Green Engineering codified by Paul Anastas and Julie Zimmerman. The 12 Principles provide a comprehensive systems engineering framework: 1. Inherent rather than circumstantial non-toxicity, 2. Prevention over remediation, 3. Design for separation, 4. Maximize mass/energy/space efficiency, 5. Output-pulled production, 6. Conserve complexity, 7. Targeted durability, 8. Minimize excess capacity, 9. Minimize material diversity, 10. Integrate local energy and material streams, 11. Design for commercial afterlife, and 12. Renewable and recyclable inputs."
    elif "year 2070" in text_combined or "letter written" in text_combined:
        return "This slide is part of the evocative narrative 'Letter Written in the Year 2070', highlighting the catastrophic social and physiological realities of unchecked environmental degradation. In this projected future, severe ozone depletion, complete aquifer exhaustion, and air taxation ($137\\,\\text{m}^3\\text{/day}$) force humanity into daily survival struggles, illustrating the paramount importance of intergenerational equity and preemptive decarbonization."
    elif "opat" in text_combined or "ipat" in text_combined or "garrett hardin" in text_combined or "tragedy of the commons" in text_combined:
        return "This slide establishes the foundational socioeconomic mechanics of environmental degradation: Garrett Hardin's 1968 'Tragedy of the Commons' (unregulated open-access resources inevitably suffer overexploitation because individual gain exceeds fractional shared cost) and the IPAT formulation ($I = P \\times A \\times T$), formalizing how population, per-capita affluence, and technology drive planetary impact."
    elif "remote sensing" in text_combined or "reflectance" in text_combined or "landsat" in text_combined or "ndvi" in text_combined:
        return "This slide explores satellite remote sensing principles in environmental monitoring. By analyzing multi-spectral radiance values across visible, Near-Infrared (NIR), Shortwave-Infrared (SWIR), and Thermal bands, geospatial algorithms compute vegetation vigor indices (NDVI) and detect multi-decadal land use land cover (LULC) changes with high spatial fidelity."
    elif "carbon" in text_combined and "sequestration" in text_combined or "biomass" in text_combined:
        return "This slide formalizes carbon sink dynamics and terrestrial/marine carbon capture. Dry forest biomass stores approximately 50% elemental carbon ($C = 0.5 \\times \\text{Biomass}$), which converts to $CO_2$ equivalents via stoichiometric factor 44/12 (3.67). It highlights how afforestation, agroforestry, and soil organic carbon preservation provide crucial negative emissions."
    elif "eia" in text_combined or "screening" in text_combined or "scoping" in text_combined:
        return "This slide details the Environmental Impact Assessment (EIA) protocol, the mandatory statutory framework under India's Environment Protection Act 1986. It maps out Phase 1 Screening (categorizing projects into Category A central vs Category B state levels) and Scoping to establish Terms of Reference (ToR) and baseline environmental studies before project clearance."

    # General synthesis using slide bullets and lecture context
    bullet_summary = "; ".join(bullets[:3]) if bullets else clean_text(full_text[:120])
    if len(bullet_summary) > 20:
        return f"This slide presents essential concepts in Lecture {lec_id}: {title}. Specifically, it examines {bullet_summary}. In the broader context of {lec_ctx}, mastering this material is critical for analyzing ecological tradeoffs, regulatory frameworks, and exam questions on environmental system dynamics."
    else:
        return f"This visual slide in Lecture {lec_id} illustrates core structural mechanisms and empirical data for {title}. It provides essential visual context within the curriculum of {lec_ctx}, directly connecting theoretical principles with real-world environmental technology observations."

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
        
        # Clean title
        if s_title.lower().startswith("slide ") and len(s_text) > 5:
            # extract first meaningful line from text
            first_line = clean_text(s_text.split(". ")[0].split("\n")[0])
            if len(first_line) > 3:
                s_title = first_line[:65]
        
        # Bullets
        bullets = []
        if s_text:
            lines = [clean_text(l) for l in s_text.split("\n") if len(clean_text(l)) > 3]
            bullets = [l for l in lines if not l.lower().startswith("http") and not l.isdigit()][:6]
        
        deep_exp = generate_deep_explanation(lec_id, s_num, s_title, bullets, s_text)
        
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
    print(f"Processed Lec {lec_id}: {len(slides_info)} slides with deep explanations.")

with open("Study_Material/full_slide_database.json", "w", encoding="utf-8") as f:
    json.dump(full_database, f, indent=2)

print("\nSaved Study_Material/full_slide_database.json with all 15 classes!")
