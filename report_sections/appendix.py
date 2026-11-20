"""
appendix.py - Supplementary Material / Appendix
Supplementary Tables S1–S4 and Supplementary Figures S1–S3.
"""

SUPPLEMENTARY_TABLES = {
    "S1": {
        "title": "Supplementary Table S1.",
        "caption": "Regional summary and chronological characteristics of the 69 retained fossil pollen cores across Eastern North America.",
        "headers": ["Region / Sub-basin", "Cores (n)", "Lat Range (°N)", "Lon Range (°W)", "LegacyAge 1.0 Direct", "Neotoma Fallback", "Mean Time Span (cal yr BP)"],
        "rows": [
            ["Midwest & Ohio Valley", "24", "36.2–44.8", "90.4–81.2", "20", "4", "14,750–250"],
            ["Great Lakes & St. Lawrence", "20", "41.8–48.1", "94.2–76.5", "17", "3", "14,500–250"],
            ["New England & Maritime", "15", "41.2–47.2", "73.8–64.5", "13", "2", "14,250–250"],
            ["Appalachian & Southeast", "10", "34.2–38.5", "86.8–78.0", "7", "3", "14,750–250"],
            ["Total Corridor", "69", "34.2–48.1", "94.2–64.5", "57 (82.6%)", "12 (17.4%)", "14,580–250"]
        ]
    },
    "S2": {
        "title": "Supplementary Table S2.",
        "caption": "Cross-correlation response lags against precipitation anomalies (Delta Precip) compared with thermal forcing (Delta Temp).",
        "headers": ["Genus", "Temp Median Lag (yr)", "Temp Sig Pass (%)", "Precip Median Lag (yr)", "Precip Sig Pass (%)", "Thermal vs Precip Pacemaker"],
        "rows": [
            ["Larix", "750", "80.0", "1,500", "40.0", "Thermally paced (early response)"],
            ["Acer", "1,500", "31.2", "1,500", "34.4", "Thermally & hydrologically coupled"],
            ["Alnus", "1,500", "62.5", "1,500", "46.9", "Thermally paced"],
            ["Betula", "1,500", "51.3", "1,500", "38.5", "Thermally paced"],
            ["Carya", "1,500", "17.6", "2,000", "23.5", "Thermally paced"],
            ["Fraxinus", "1,500", "68.8", "1,500", "43.8", "Thermally paced"],
            ["Picea", "1,500", "78.0", "1,500", "42.4", "Thermally paced (abrupt collapse)"],
            ["Populus", "1,500", "63.3", "1,000", "36.7", "Thermally paced"],
            ["Quercus", "1,500", "41.8", "1,500", "38.8", "Thermally paced"],
            ["Ulmus", "1,500", "60.6", "1,500", "42.4", "Thermally paced"],
            ["Pinus", "2,000", "49.1", "2,000", "36.4", "Thermally paced"],
            ["Fagus", "2,500", "15.6", "2,500", "28.1", "Slow dispersal limited"],
            ["Tsuga", "2,500", "23.5", "2,000", "35.3", "Slow dispersal & moisture coupled"]
        ]
    },
    "S3": {
        "title": "Supplementary Table S3.",
        "caption": "Pairwise post-hoc Bonferroni-corrected Dunn tests of lag differences among ecological speed tiers.",
        "headers": ["Comparison Pair (Taxon A vs Taxon B)", "Raw p-value", "Bonferroni-adjusted p-value", "Significance Level", "Ecological Interpretation"],
        "rows": [
            ["Picea vs Tsuga", "0.00016", "0.0127", "p < 0.05*", "Boreal collapse significantly earlier than climax hemlock expansion"],
            ["Picea vs Fagus", "0.00059", "0.0462", "p < 0.05*", "Boreal collapse significantly earlier than climax beech expansion"],
            ["Acer vs Tsuga", "0.00079", "0.0617", "Trend (p < 0.10)", "Canopy maple response earlier than climax hemlock"],
            ["Acer vs Fagus", "0.00226", "0.1764", "Not significant", "Broadleaf canopy reorganization vs climax hardwood"],
            ["Alnus vs Tsuga", "0.00309", "0.2413", "Not significant", "Pioneer alder vs climax hemlock"],
            ["Fraxinus vs Tsuga", "0.00403", "0.3144", "Not significant", "Canopy ash vs climax hemlock"],
            ["Larix vs Tsuga", "0.02081", "1.0000", "Not significant (small n)", "Pioneer larch vs climax hemlock (power constrained by n=10)"]
        ]
    },
    "S4": {
        "title": "Supplementary Table S4.",
        "caption": "Synthetic planted-truth model calibration benchmarks: recovery of stepped lags, AR(1) false positive rates, and 2D wavefront recovery.",
        "headers": ["Planted Truth Parameter", "Planted Benchmark", "Recovered Value", "Error / Deviation", "Validation Status"],
        "rows": [
            ["Short Lag Step (Pioneer)", "250 yr", "250 ± 125 yr", "0 yr (exact bin)", "Passed (within ±500 yr)"],
            ["Medium Lag Step (Canopy)", "1,250 yr", "1,250 ± 250 yr", "0 yr (exact bin)", "Passed (within ±500 yr)"],
            ["Long Lag Step (Climax)", "2,500 yr", "2,500 ± 250 yr", "0 yr (exact bin)", "Passed (within ±500 yr)"],
            ["Random-Walk Null (AR1 phi=0.7)", "r_true = 0.00", "r_obs = 0.02 ± 0.11", "False Pos: 5.0%", "Passed (clean 5% alpha)"],
            ["2D Wavefront Velocity", "200.0 m/yr", "198.4 m/yr", "-1.6 m/yr (-0.8%)", "Passed (accurate recovery)"],
            ["2D Dispersal Azimuth", "45.0° (NE)", "44.6°", "-0.4°", "Passed (accurate vector heading)"]
        ]
    }
}

SUPPLEMENTARY_FIGURES = [
    {
        "file": "fig_geographic_corridors.png",
        "title": "Supplementary Figure S1.",
        "caption": "Topographic steering and two-dimensional migration vectors for five validated tree genera across Eastern North America. Arrows indicate vector mean migration headings along major geomorphic corridors: Carya along the Mississippi and Ohio river valleys (azimuth 65.0° ENE), Alnus across the northern Great Lakes (azimuth 308.2° WNW), Fagus and Tsuga along the Appalachian mountain spine (azimuth 344.4° and 344.3° NNW), and Larix due North along the retreating glacial ice margin (azimuth 1.2° N)."
    },
    {
        "file": "fig_pollen_morphology.png",
        "title": "Supplementary Figure S2.",
        "caption": "Pollen grain morphology and Relative Pollen Productivity (RPP) adjustment factors under the REVEALS modeling framework. High pollen-producing, wind-dispersed taxa with high dispersal capacity (such as bisaccate Pinus, RPP 14.10, and triporate Betula, RPP 6.19) are scaled down, whereas insect-pollinated, low-producing hardwoods (such as tricolpate Acer, RPP 0.23) are adjusted upward to accurately reflect true canopy biomass."
    },
    {
        "file": "fig_seed_dispersal_tradeoff.png",
        "title": "Supplementary Figure S3.",
        "caption": "Ecological trade-off between reproductive maturation interval (years to first seed production) and ballistic seed dispersal distance (metres from parent stem) among Eastern North American tree taxa. Pioneer conifers (Larix) combine early maturity with light winged seeds, whereas climax hardwoods (Fagus, Quercus, Carya) require decades to mature and produce heavy nuts restricted to short drop shadows (<30 m), generating substantial century-to-millennial population response lags."
    }
]
