import os
import json
import re
import fitz # PyMuPDF

LECTURE_MAPPING = [
    {
        "id": "01",
        "title": "Course Overview & Planetary Vision (Year 2070)",
        "slug": "01_course_overview_vision_2070",
        "files": ["Class-1 Overview.pdf", "Class-1-Year_2070 - Compatibility Mode.pdf"]
    },
    {
        "id": "02",
        "title": "Comprehending Our Environment: Earth Spheres & Thermodynamics",
        "slug": "02_comprehending_environment_spheres",
        "files": ["Class-2-Comprehend our Environment-Part-1.pdf", "Class-2-Comprehend our environment-Part-2.pdf", "Class-2-Comprehend our Environment-Part-3.pdf"]
    },
    {
        "id": "03",
        "title": "Environmental Issues, Anthropogenic Pressures & Pollution",
        "slug": "03_environmental_issues_anthropogenic_pressures",
        "files": ["Class-3 Enviromental issues-Part-1.pdf", "Class-3 Enviromental issues-Part-2.pdf"]
    },
    {
        "id": "04",
        "title": "Remote Sensing & GIS in Environmental Technology",
        "slug": "04_remote_sensing_gis_monitoring",
        "files": ["Class-4-RS-EVS-upload.pdf"]
    },
    {
        "id": "05",
        "title": "Landmark Environmental Events, Crises & Disasters",
        "slug": "05_environmental_events_crises_disasters",
        "files": ["Class-5 -Environmental Events.pdf"]
    },
    {
        "id": "06",
        "title": "Earth Components, Biogeochemical Cycles & Ecological Systems",
        "slug": "06_earth_components_biogeochemical_cycles",
        "files": ["Class-6 Earth components-part-1.pdf", "Class-6 Earth components-Part-2.pdf"]
    },
    {
        "id": "07",
        "title": "Climate Change Impacts, Global Warming & Vulnerability",
        "slug": "07_climate_change_impacts_vulnerability",
        "files": ["Class-7 Climate Change impacts.pdf"]
    },
    {
        "id": "08",
        "title": "Unexpected Climate Changes, Non-Linear Tipping Points & Feedback Loops",
        "slug": "08_unexpected_climate_changes_tipping_points",
        "files": ["Class-8 Unexpected climate changes.pdf"]
    },
    {
        "id": "09",
        "title": "Carbon Sequestration & Terrestrial Sinks",
        "slug": "09_carbon_sequestration_terrestrial_sinks",
        "files": ["Class-9- Carbon sequestration.pdf"]
    },
    {
        "id": "10",
        "title": "Clean Development Mechanism (CDM) & Ocean Sequestration",
        "slug": "10_cdm_carbon_markets_ocean_sequestration",
        "files": ["Class-10- CDM.pdf", "Class-10b-Ocean Sequestration.pdf"]
    },
    {
        "id": "11",
        "title": "Climate Change Technology Solutions & Clean Tech Innovations",
        "slug": "11_climate_technology_solutions_cleantech",
        "files": ["Class-11-Climate Change-Technology Solutions.pdf"]
    },
    {
        "id": "12",
        "title": "Environmental Impact Assessment (EIA): Framework & Protocols",
        "slug": "12_eia_framework_methodology_protocols",
        "files": ["Class-12 EIA.pdf"]
    }
]

catalog_path = "Study_Material/extracted_diagrams_catalog.json"
catalog = {}
if os.path.exists(catalog_path):
    with open(catalog_path, "r", encoding="utf-8") as f:
        catalog = json.load(f)

result = {}

for lec in LECTURE_MAPPING:
    lec_id = lec["id"]
    lec_slides = []
    slide_num = 0
    lec_diags = catalog.get(lec_id, [])
    
    for fname in lec["files"]:
        pdf_path = os.path.join("Lecture_Slides", fname)
        if not os.path.exists(pdf_path):
            continue
        doc = fitz.open(pdf_path)
        for page_idx in range(len(doc)):
            slide_num += 1
            page = doc[page_idx]
            text = page.get_text("text").strip()
            
            # Split lines
            raw_lines = [l.strip() for l in text.split("\n") if l.strip()]
            
            # Title
            if raw_lines:
                title = raw_lines[0]
                if len(title) > 70:
                    title = title[:67] + "..."
                bullets = raw_lines[1:] if len(raw_lines) > 1 else []
            else:
                title = f"Slide {slide_num}"
                bullets = []
                
            # Filter redundant bullets or clean them
            clean_bullets = []
            for b in bullets:
                # Remove trivial slide numbers or URLs
                if b.startswith("http") or len(b) <= 2 or re.match(r'^\d+$', b):
                    continue
                clean_bullets.append(b)
                
            # Slide image path
            img_path = f"assets/slides/lec_{lec_id}/slide_{slide_num:02d}.jpg"
            
            # Check if any diagram in catalog belongs to this page or near it
            matched_diags = [d for d in lec_diags if d.get("page_num") == page_idx + 1]
            
            lec_slides.append({
                "slide_num": slide_num,
                "source_file": fname,
                "page_in_file": page_idx + 1,
                "title": title,
                "bullets": clean_bullets[:8], # up to 8 key bullet lines
                "image": img_path,
                "has_diagram": len(matched_diags) > 0,
                "diagrams": [d["rel_path"] for d in matched_diags[:2]]
            })
            
        doc.close()
        
    result[lec_id] = {
        "title": lec["title"],
        "slug": lec["slug"],
        "total_slides": slide_num,
        "slides": lec_slides
    }
    print(f"Lec {lec_id}: Extracted {slide_num} slides.")

with open("Study_Material/full_slide_database.json", "w", encoding="utf-8") as f:
    json.dump(result, f, indent=2)

print("Saved Study_Material/full_slide_database.json successfully!")
