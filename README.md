# 🌿 Environmental Science & Technology (ES1.101) — Interactive Study Suite

[![Live Hub](https://img.shields.io/badge/Study%20Suite-Live%20Portal-10b981?style=for-the-badge&logo=safari)](https://vivek-r-2000.github.io/est-interactive-study/)
[![Course](https://img.shields.io/badge/Course-ES1.101%20EST-14b8a6?style=for-the-badge)](https://courses.iiit.ac.in/course/view.php?id=5826)
[![Slides](https://img.shields.io/badge/Primary%20Slides-444%20Rendered-f59e0b?style=for-the-badge)](./Lecture_Slides/)
[![Visuals](https://img.shields.io/badge/Extracted%20Visuals-770%2B%20Diagrams-06b6d4?style=for-the-badge)](./Study_Material/assets/diagrams/)
[![Institution](https://img.shields.io/badge/Institution-IIIT%20Hyderabad-blue?style=for-the-badge)](https://www.iiit.ac.in)

A production-grade, zero-dependency educational web application and interactive study suite for **Environmental Science & Technology (ES1.101 / Monsoon 2026)** at IIIT Hyderabad, taught by **Prof. Ramachandra Prasad P**.

---

## 🌟 Key Features

1. **Direct Slide Figures & Visualizations:** Over 770 extracted high-resolution diagrams, flowcharts, spectral curves, and disaster maps directly embedded into concept screens.
2. **Dedicated Lecture Modules (1 to 12):** Separate interactive HTML modules with working Pomodoro timers, progress trackers, active recall 3D flip cards, and multiple-choice quizzes.
3. **Complete Slide Reference Galleries:** Every lecture module ends with an interactive gallery of all slide pages from the original presentations with one-click full-screen lightbox zoom.
4. **Playable Video Masterclasses:** Embedded responsive video players for all YouTube lectures and documentary references found in the slide decks.
5. **Interactive Physics & Environmental Simulators:**
   - ⚡ *Planetary Decarbonization 2070 Pathway Simulator*
   - 🌐 *Earth Radiation Budget & Greenhouse Equilibrium Calculator*
   - 🏭 *Air Quality Index (AQI) & Plume Dispersion Calculator*
   - 🛰️ *Multispectral Remote Sensing & NDVI Visualizer*
   - ⚠️ *Toxic Chemical Exposure & Gaussian Plume Model (Bhopal Scenario)*
   - 🔄 *Biogeochemical Nutrient Flux Model*
   - 🌡️ *Sea Level Rise & Thermal Expansion Model*
   - ⚡ *AMOC Tipping Element Hysteresis Explorer*
   - 🌲 *Terrestrial Carbon Sink & Biochar Calculator*
   - 🌊 *Clean Development Mechanism (CDM) Additionality & Ocean Chemistry*
   - ⚡ *Direct Air Capture (DAC) Energy Efficacy Evaluator*
   - 📋 *EIA Leopold Matrix & Significance Evaluator*
6. **Eco-Tech Visual Design System:** Dark biosphere theme with Emerald (`#10b981`), Forest Green, Earth Amber, and Ocean Cyan palette.

---

## 📚 Curriculum Breakdown

| Module | Title | Primary Slide Decks | Key Interactive Features |
| :---: | :--- | :--- | :--- |
| **01** | [Course Overview & Vision 2070](./Study_Material/01_course_overview_vision_2070.html) | `Class-1 Overview`, `Class-1-Year_2070` (54 slides) | Decarbonization pathway simulator, Panchamrit targets |
| **02** | [Earth Spheres & Thermodynamics](./Study_Material/02_comprehending_environment_spheres.html) | `Class-2-Part-1, 2, 3` (57 slides) | Radiation balance model, Stefan-Boltzmann calculator |
| **03** | [Pollution & Anthropogenic Pressures](./Study_Material/03_environmental_issues_anthropogenic_pressures.html) | `Class-3-Part-1, 2` (34 slides) | AQI calculator, Streeter-Phelps oxygen sag curve |
| **04** | [Remote Sensing & GIS](./Study_Material/04_remote_sensing_gis_monitoring.html) | `Class-4-RS-EVS-upload` (18 slides) | Spectral reflectance curve, NDVI live classifier |
| **05** | [Landmark Environmental Disasters](./Study_Material/05_environmental_events_crises_disasters.html) | `Class-5 -Environmental Events` (30 slides) | Bhopal MIC runaway kinetics, Gaussian plume tool |
| **06** | [Biogeochemical Cycles](./Study_Material/06_earth_components_biogeochemical_cycles.html) | `Class-6 Earth components-Part-1, 2` (41 slides) | Nitrogen & carbon flux perturbator, Redfield ratio |
| **07** | [Climate Change Impacts](./Study_Material/07_climate_change_impacts_vulnerability.html) | `Class-7 Climate Change impacts` (31 slides) | Radiative forcing formula, Sea level rise model |
| **08** | [Unexpected Climate Tipping Points](./Study_Material/08_unexpected_climate_changes_tipping_points.html) | `Class-8 Unexpected climate changes` (30 slides) | AMOC Stommel bifurcation & hysteresis explorer |
| **09** | [Carbon Sequestration & Sinks](./Study_Material/09_carbon_sequestration_terrestrial_sinks.html) | `Class-9- Carbon sequestration` (34 slides) | Geological CCS trapping stages, biochar calculator |
| **10** | [CDM & Ocean Sequestration](./Study_Material/10_cdm_carbon_markets_ocean_sequestration.html) | `Class-10- CDM`, `Class-10b-Ocean` (54 slides) | Additionality proof, ocean acidification model |
| **11** | [Climate Technology Solutions](./Study_Material/11_climate_technology_solutions_cleantech.html) | `Class-11-Climate Change-Technology` (29 slides) | Direct Air Capture thermodynamics, Green hydrogen |
| **12** | [EIA Framework & Protocols](./Study_Material/12_eia_framework_methodology_protocols.html) | `Class-12 EIA` (32 slides) | Leopold matrix calculator, 8-stage EIA lifecycle |

---

## 🚀 How to Run Locally

Because the study suite uses zero external build dependencies (pure HTML5, CSS3, and Vanilla JavaScript with CDN Tailwind and KaTeX), it runs directly:

```powershell
# Option 1: Open index.html directly in browser
start index.html

# Option 2: Run local lightweight Python server
python -m http.server 8000
# Then open http://localhost:8000
```

---

## 🌐 Deploy to GitHub Pages

To publish this website live to GitHub Pages:
```powershell
./DEPLOY_GITHUB_PAGES.bat
```
