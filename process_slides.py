import os
import glob
import re
import json
import fitz # PyMuPDF
from PIL import Image
import io

LECTURE_MAPPING = [
    {
        "id": "01",
        "title": "Course Overview & Planetary Vision (Year 2070)",
        "slug": "01_course_overview_vision_2070",
        "short_title": "Overview & Vision 2070",
        "description": "Environmental science fundamentals, global sustainability vision, IPCC scenarios, decarbonization roadmap to Year 2070, and planetary boundaries.",
        "files": ["Class-1 Overview.pdf", "Class-1-Year_2070 - Compatibility Mode.pdf"],
        "icon": "🌍",
        "difficulty": "Beginner",
        "duration": "40 mins"
    },
    {
        "id": "02",
        "title": "Comprehending Our Environment: Earth Spheres & Thermodynamics",
        "slug": "02_comprehending_environment_spheres",
        "short_title": "Earth Spheres & Dynamics",
        "description": "Atmosphere, Hydrosphere, Lithosphere, Biosphere interactions; solar radiation budget, thermodynamic equilibrium, greenhouse effect, and biotic-abiotic couplings.",
        "files": ["Class-2-Comprehend our Environment-Part-1.pdf", "Class-2-Comprehend our environment-Part-2.pdf", "Class-2-Comprehend our Environment-Part-3.pdf"],
        "icon": "🌐",
        "difficulty": "Intermediate",
        "duration": "55 mins"
    },
    {
        "id": "03",
        "title": "Environmental Issues, Anthropogenic Pressures & Pollution",
        "slug": "03_environmental_issues_anthropogenic_pressures",
        "short_title": "Issues & Anthropogenic Impact",
        "description": "Air and water pollution, soil degradation, industrial effluents, particulate matter ($PM_{2.5}, PM_{10}$), eutrophication, acid rain, and ecological footprint.",
        "files": ["Class-3 Enviromental issues-Part-1.pdf", "Class-3 Enviromental issues-Part-2.pdf"],
        "icon": "🏭",
        "difficulty": "Intermediate",
        "duration": "45 mins"
    },
    {
        "id": "04",
        "title": "Remote Sensing & GIS in Environmental Technology",
        "slug": "04_remote_sensing_gis_monitoring",
        "short_title": "Remote Sensing & GIS",
        "description": "Electromagnetic spectrum, multispectral satellite sensors (Landsat, Sentinel, MODIS), false color composites (FCC), NDVI vegetation indices, spatial resolution, and GIS mapping.",
        "files": ["Class-4-RS-EVS-upload.pdf"],
        "icon": "🛰️",
        "difficulty": "Advanced",
        "duration": "60 mins"
    },
    {
        "id": "05",
        "title": "Landmark Environmental Events, Crises & Disasters",
        "slug": "05_environmental_events_crises_disasters",
        "short_title": "Landmark Crises & Disasters",
        "description": "Bhopal Gas Tragedy (MIC), Chernobyl nuclear disaster, Minamata disease (Mercury bioaccumulation), London Smog 1952, Exxon Valdez, Deepwater Horizon, and policy impacts.",
        "files": ["Class-5 -Environmental Events.pdf"],
        "icon": "⚠️",
        "difficulty": "Intermediate",
        "duration": "45 mins"
    },
    {
        "id": "06",
        "title": "Earth Components, Biogeochemical Cycles & Ecological Systems",
        "slug": "06_earth_components_biogeochemical_cycles",
        "short_title": "Biogeochemical Cycles",
        "description": "Carbon, Nitrogen, Phosphorus, and Hydrological cycles; ecological succession, energy pyramids, trophic levels, homeostasis, and ecosystem resilience.",
        "files": ["Class-6 Earth components-part-1.pdf", "Class-6 Earth components-Part-2.pdf"],
        "icon": "🔄",
        "difficulty": "Intermediate",
        "duration": "50 mins"
    },
    {
        "id": "07",
        "title": "Climate Change Impacts, Global Warming & Vulnerability",
        "slug": "07_climate_change_impacts_vulnerability",
        "short_title": "Climate Change Impacts",
        "description": "Radiative forcing, global temperature anomalies, cryosphere melt (Greenland, Antarctica), sea-level rise modeling, extreme weather events, and socioeconomic vulnerability.",
        "files": ["Class-7 Climate Change impacts.pdf"],
        "icon": "🌡️",
        "difficulty": "Intermediate",
        "duration": "50 mins"
    },
    {
        "id": "08",
        "title": "Unexpected Climate Changes, Non-Linear Tipping Points & Feedback Loops",
        "slug": "08_unexpected_climate_changes_tipping_points",
        "short_title": "Tipping Points & Feedbacks",
        "description": "AMOC collapse risk, permafrost thaw and methane feedback, albedo degradation, runaway greenhouse dynamics, hysteresis loops, and catastrophic shifts.",
        "files": ["Class-8 Unexpected climate changes.pdf"],
        "icon": "⚡",
        "difficulty": "Advanced",
        "duration": "55 mins"
    },
    {
        "id": "09",
        "title": "Carbon Sequestration & Terrestrial Sinks",
        "slug": "09_carbon_sequestration_terrestrial_sinks",
        "short_title": "Carbon Sequestration & Sinks",
        "description": "Biological carbon pumps, afforestation/reforestation, soil organic carbon (SOC), biochar, geological carbon capture & storage (CCS), enhanced weathering, and capacity math.",
        "files": ["Class-9- Carbon sequestration.pdf"],
        "icon": "🌲",
        "difficulty": "Intermediate",
        "duration": "45 mins"
    },
    {
        "id": "10",
        "title": "Clean Development Mechanism (CDM) & Ocean Sequestration",
        "slug": "10_cdm_carbon_markets_ocean_sequestration",
        "short_title": "CDM & Ocean Sequestration",
        "description": "Kyoto Protocol Article 12, Certified Emission Reductions (CERs), additionality criteria, carbon trading markets; deep ocean $CO_2$ injection, iron fertilization, and ocean acidification risks.",
        "files": ["Class-10- CDM.pdf", "Class-10b-Ocean Sequestration.pdf"],
        "icon": "🌊",
        "difficulty": "Advanced",
        "duration": "50 mins"
    },
    {
        "id": "11",
        "title": "Climate Change Technology Solutions & Clean Tech Innovations",
        "slug": "11_climate_technology_solutions_cleantech",
        "short_title": "Tech Solutions & Clean Tech",
        "description": "Direct Air Capture (DAC), solar radiation management (SRM), green hydrogen, renewable grids, energy storage thermodynamics, circular bio-economy, and decarbonization metrics.",
        "files": ["Class-11-Climate Change-Technology Solutions.pdf"],
        "icon": "⚡",
        "difficulty": "Intermediate",
        "duration": "45 mins"
    },
    {
        "id": "12",
        "title": "Environmental Impact Assessment (EIA): Framework & Protocols",
        "slug": "12_eia_framework_methodology_protocols",
        "short_title": "EIA Framework & Practice",
        "description": "Screening, Scoping, Baseline data collection, Impact Prediction, Environmental Management Plan (EMP), public consultation, Leopold matrix, Batelle environmental evaluation, and post-project monitoring.",
        "files": ["Class-12 EIA.pdf"],
        "icon": "📋",
        "difficulty": "Advanced",
        "duration": "50 mins"
    }
]

def process_lectures(workspace_dir):
    slides_root = os.path.join(workspace_dir, "Lecture_Slides")
    assets_dir = os.path.join(workspace_dir, "Study_Material", "assets")
    slides_out_dir = os.path.join(assets_dir, "slides")
    diagrams_out_dir = os.path.join(assets_dir, "diagrams")
    os.makedirs(slides_out_dir, exist_ok=True)
    os.makedirs(diagrams_out_dir, exist_ok=True)

    summary_data = []

    for lec in LECTURE_MAPPING:
        lec_id = lec["id"]
        lec_slug = lec["slug"]
        lec_slides_dir = os.path.join(slides_out_dir, f"lec_{lec_id}")
        lec_diagrams_dir = os.path.join(diagrams_out_dir, f"lec_{lec_id}")
        os.makedirs(lec_slides_dir, exist_ok=True)
        os.makedirs(lec_diagrams_dir, exist_ok=True)

        print(f"\n==========================================")
        print(f"Processing Lecture {lec_id}: {lec['title']}")
        print(f"Files: {lec['files']}")
        print(f"==========================================")

        lec_slides_info = []
        video_links = []
        slide_counter = 0
        diagram_counter = 0

        for fname in lec["files"]:
            pdf_path = os.path.join(slides_root, fname)
            if not os.path.exists(pdf_path):
                print(f"  [!] Missing file: {pdf_path}")
                continue

            doc = fitz.open(pdf_path)
            print(f"  Loaded {fname}: {len(doc)} pages")

            for page_num in range(len(doc)):
                page = doc[page_num]
                slide_counter += 1
                text = page.get_text("text").strip()

                # Search for video URLs or web references
                found_urls = re.findall(r'(https?://[^\s)"]+)', text)
                for u in found_urls:
                    if any(v in u.lower() for v in ["youtube", "youtu.be", "vimeo", "ted.com", "video", ".mp4", "webcast"]):
                        if u not in video_links:
                            video_links.append(u)

                # Check links in page annotations
                for link in page.get_links():
                    uri = link.get("uri")
                    if uri and any(v in uri.lower() for v in ["youtube", "youtu.be", "vimeo", "ted.com", "video", ".mp4"]):
                        if uri not in video_links:
                            video_links.append(uri)

                # Render slide to high-quality image (scale=1.5 for crisp 1080p/720p display)
                mat = fitz.Matrix(1.5, 1.5)
                pix = page.get_pixmap(matrix=mat, alpha=False)
                slide_img_rel = f"assets/slides/lec_{lec_id}/slide_{slide_counter:02d}.jpg"
                slide_img_abs = os.path.join(lec_slides_dir, f"slide_{slide_counter:02d}.jpg")
                pix.save(slide_img_abs, "jpeg")

                # Extract embedded images / diagrams from this slide
                img_list = page.get_images(full=True)
                extracted_diagrams = []
                for img_info in img_list:
                    xref = img_info[0]
                    base_image = doc.extract_image(xref)
                    image_bytes = base_image["image"]
                    image_ext = base_image["ext"]
                    # Filter out tiny icons / bullet markers (< 15KB or dimensions < 120px)
                    if len(image_bytes) > 15000:
                        try:
                            im = Image.open(io.BytesIO(image_bytes))
                            w, h = im.size
                            if w >= 150 and h >= 150:
                                diagram_counter += 1
                                diag_rel = f"assets/diagrams/lec_{lec_id}/diag_{diagram_counter:02d}.{image_ext}"
                                diag_abs = os.path.join(diagrams_out_dir, f"diag_{diagram_counter:02d}.{image_ext}")
                                with open(diag_abs, "wb") as f_img:
                                    f_img.write(image_bytes)
                                extracted_diagrams.append({
                                    "rel_path": diag_rel,
                                    "width": w,
                                    "height": h,
                                    "size_kb": round(len(image_bytes) / 1024, 1)
                                })
                        except Exception as e:
                            pass

                # Derive clean slide title from text lines
                lines = [l.strip() for l in text.split("\n") if l.strip() and len(l.strip()) > 2]
                slide_title = lines[0] if lines else f"Slide {slide_counter}"
                if len(slide_title) > 65:
                    slide_title = slide_title[:62] + "..."

                lec_slides_info.append({
                    "slide_num": slide_counter,
                    "source_file": fname,
                    "page_in_file": page_num + 1,
                    "title": slide_title,
                    "image": slide_img_rel,
                    "text_snippet": " ".join(lines[:4]) if lines else "",
                    "diagrams": extracted_diagrams
                })

            doc.close()

        print(f"  [+] Lecture {lec_id}: Rendered {slide_counter} slides, extracted {diagram_counter} diagrams, found {len(video_links)} videos")
        lec["slide_count"] = slide_counter
        lec["diagram_count"] = diagram_counter
        lec["slides"] = lec_slides_info
        lec["videos"] = video_links
        summary_data.append(lec)

    # Save summary metadata JSON
    out_meta = os.path.join(workspace_dir, "Study_Material", "lectures_metadata.json")
    with open(out_meta, "w", encoding="utf-8") as f:
        json.dump(summary_data, f, indent=2)
    print(f"\n[+] Saved complete lecture metadata to {out_meta}")
    return summary_data

if __name__ == "__main__":
    process_lectures(r"C:\Users\vivek\EST")
