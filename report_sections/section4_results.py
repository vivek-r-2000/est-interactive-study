"""
section4_results.py
Section 4 (Results) for Course ES1.101 Project 25 Report.
"""

RESULTS_PARAGRAPHS = {
    "4.1": [
        (
            "The 15,000-year paleoclimate simulation from TraCE-21ka shows strong regional warming across Eastern North America, with mean annual surface temperature rising from -10.27 °C at 14,750 cal yr BP to +5.26 °C in the late Holocene, an overall warming of +15.53 °C (Figure 2, top panel). "
            "Regional annual precipitation increased concurrently by approximately 11%, rising from 2.24 mm/day (~818 mm/yr) during the cold late-glacial to 2.49 mm/day (~909 mm/yr) during the mid-Holocene humid period (Figure 2). "
            "However, hydroclimatic changes lagged behind thermal shifts: precipitation remained suppressed between 2.22 and 2.24 mm/day throughout the Bølling–Allerød and Younger Dryas, only rising smoothly toward modern values after 11.7 ka BP."
        ),
        (
            "Warming rates peaked in two main pulses that exceeded 0.40 °C per century (Figure 2, middle panel). "
            "The first pulse reached +0.430 °C per century at 14.5 ka BP during the onset of the Bølling–Allerød warming. "
            "Following the Younger Dryas cold reversal (12.9–11.7 ka BP), during which temperatures dropped by ~2.5 °C, a second sharp warming pulse occurred at 12.0 ka BP (+0.401 °C per century). "
            "A minor warming acceleration occurred near 8.0 ka BP (+0.210 °C per century), followed by long-term mid-to-late Holocene thermal stability where rates remained low (median 0.023 °C per century for <=8 ka BP)."
        ),
        (
            "Hellinger community turnover rates across our 69 sediment cores closely matched these warming pulses (Figure 2, bottom panel). "
            "Median vegetation turnover peaked at 0.0545 Hellinger distance units per century at 12.0 ka BP, directly matching the rapid warming exit from the Younger Dryas (overall study median: 0.0285 units/century). "
            "Turnover remained elevated between 14.5 and 11.5 ka BP before declining smoothly across the early Holocene to baseline levels (~0.020–0.029 units/century) after 7.0 ka BP, showing that forest community shifts were concentrated during periods of fast climate change."
        )
    ],
    "4.2": [
        (
            "Testing stationary first-differenced series (Delta Pollen vs. Delta Temp) across 523 core-genus combinations showed widespread, statistically significant response lags (Figure 3, Table 2). "
            "A total of 250 series (47.8%) survived strict 1,000-surrogate Ebisuzaki phase-randomization tests at p < 0.05, comprising 103 warm-tracking positive expansions (+r) and 147 cold-tracking negative retreats (-r). "
            "This confirms that observed correlations reflect true ecological responses rather than coincidental trends or autocorrelation."
        ),
        (
            "Median response lags differed significantly among tree genera, showing that species did not move as a single synchronized unit (Kruskal–Wallis H = 30.54, p = 0.00231; Figure 3A). "
            "Pairwise Bonferroni-adjusted comparisons identified significant differences between cold-boreal and climax hardwoods, notably Picea versus Tsuga (p = 0.0127) and Picea versus Fagus (p = 0.0462) (Table 2). "
            "The observed lags separated into three distinct ecological speed tiers:"
        ),
        (
            "Tier 1 (Fast Pioneers, <1,000 yr): Larix (tamarack) responded most rapidly, with a median lag of 750 yr (95% bootstrap CI: 0–2,500 yr) and an 80.0% Ebisuzaki pass rate (8 of 10 sites; mean r = -0.299), because it can quickly colonize wet, nitrogen-poor soils on newly deglaciated terrain."
        ),
        (
            "Tier 2 (Canopy Reorganization, 1,000–2,000 yr): Nine dominant genera clustered around a median lag of 1,500 yr, including Acer (1,500 yr, CI: 1,000–2,000 yr), Betula (1,500 yr, CI: 1,000–2,500 yr), Alnus (1,500 yr, CI: 1,000–1,750 yr), Carya (1,500 yr, CI: 1,000–2,000 yr), Fraxinus (1,500 yr, CI: 1,000–2,000 yr), Picea (1,500 yr, CI: 1,000–1,500 yr), Populus (1,500 yr, CI: 1,000–2,000 yr), Quercus (1,500 yr, CI: 1,500–2,000 yr), and Ulmus (1,500 yr, CI: 1,000–2,000 yr). "
            "Pinus showed an intermediate median lag of 2,000 yr (CI: 1,500–2,500 yr)."
        ),
        (
            "Tier 3 (Late Climax Seeders, >2,000 yr): Heavy-seeded, shade-tolerant climax taxa had the longest response delays: Fagus (American beech; median lag 2,500 yr, CI: 2,000–2,500 yr) and Tsuga (eastern hemlock; median lag 2,500 yr, CI: 2,000–3,000 yr)."
        ),
        (
            "Examining response polarity (Figure 3B, Table 2) revealed contrasting biological trajectories within the 1,500-year cluster. "
            "Cold-adapted boreal conifer Picea underwent dramatic regional collapse during warming, showing negative correlations across 94.9% of sites (mean r = -0.637), with 78.0% of sites (46/59) passing strict surrogate tests (p < 0.05). "
            "Fraxinus also showed predominant retreat (68.8% -r). "
            "Conversely, temperate hardwoods expanded into deglaciated terrain with strong positive correlations, led by Quercus (79.1% positive sites, mean r = +0.248; 39.5% passing p < 0.05), Carya (76.9% positive), and Ulmus (63.0% positive). "
            "Intermediate pioneer Alnus split evenly (50.0% +r, 50.0% -r, mean r = -0.007). "
            "In addition, evaluating lags against TraCE-21ka precipitation anomalies yielded an identical cross-genus median lag of 1,500 yr (Table 2), indicating that hydrological constraints acted synchronously with thermal thresholds."
        )
    ],
    "4.3": [
        (
            "Comparing fossil assemblages against our 611 modern surface samples using the 5th-percentile Squared Chord Distance threshold (0.1060) showed a clear rise and fall of no-analogue plant communities (Figure 4, top panel; Table 3). "
            "Under TRSH-only isolation, no-analogue community frequencies were low prior to 15.0 ka BP (9.1% at 15.0 ka BP) but surged dramatically during early deglacial warming, peaking at 79.0% of sites at 14.5 ka BP and remaining high (51.3–72.4%) through the Younger Dryas (13.0–12.0 ka BP). "
            "Following the onset of the Holocene, no-analogue frequencies dropped steadily: 56.4% at 11.5 ka BP, 32.1% at 9.5 ka BP, and 12.0% at 7.0 ka BP, reaching an 8.0% pre-colonial baseline at 500 BP (Table 3). "
            "Bin-level no-analogue frequency correlated positively with TraCE-21ka absolute climate change rate (|dT/dt|, Spearman rho = 0.471, p = 0.0079; Ebisuzaki p = 0.012) and with Hellinger turnover rate (rho = 0.658, p = 7.34e-05; Ebisuzaki p = 0.001), demonstrating that novel communities formed during periods of rapid climate acceleration."
        ),
        (
            "Breaking down SCD scores by genus showed which taxa actually drove community novelty (Figure 4, bottom panel; Table 3). "
            "During the late-glacial novelty peak (14.5–12.0 ka BP), mean SCD contributions were led by Quercus (mean deglacial contribution: 0.0192; peak 0.0244 at 14.5 ka BP), Alnus (mean: 0.0164; peak 0.0221 at 12.0 ka BP), Betula (mean: 0.0142; peak 0.0185 at 13.0 ka BP), Populus (mean: 0.0095; peak 0.0152 at 12.0 ka BP), and Picea (mean: 0.0088; peak 0.0165 at 14.5 ka BP). "
            "In contrast, modern dominant climax hardwoods like Fagus, Tsuga, and Acer contributed minimally to late-glacial novelty (<=0.0028 each)."
        ),
        (
            "After 8.0 ka BP, per-taxon SCD contributions across almost all genera faded into near-zero values (<=0.006; pale yellow bands in Figure 4). "
            "Only Quercus maintained a modest baseline contribution (0.012–0.016) in the mid-to-late Holocene, reflecting the development of widespread oak-hickory savannas in the Midwest. "
            "Comparing TRSH-only filtering against unfiltered pollen data that included agricultural herbs (Ambrosia, Poaceae, Rumex) demonstrated that post-settlement weeds artificially drive modern-era SCD above 0.1500 (Table 3), confirming that removing weed taxa is essential to avoid mistaking historic farming for climate-driven community novelty."
        )
    ],
    "4.4": [
        (
            "Testing postglacial arrival times across equal-area coordinates with a 2D planar regression model (Age ~ x + y) identified five tree genera with statistically coherent regional migration fronts (p <= 0.05; Table 4, Figure 5). "
            "The remaining seven genera (Pinus, Quercus, Betula, Ulmus, Fraxinus, Populus, and Acer) failed the planar significance gate (p > 0.05; e.g., Pinus p = 0.064, Quercus p = 0.095, Acer p = 0.662) due to scattered local populations, multiple glacial microrefugia, or widespread pre-existing presence south of the ice sheet, and were excluded from directional velocity contouring."
        ),
        (
            "The five validated migrants followed distinct regional dispersal corridors (Figure 5, Table 4): "
            "Carya migrated fastest among hardwoods at 277.0 m/yr (IQR: 267.7–287.1 m/yr; local max 296 m/yr) along an azimuth of 65.0° (ENE; R² = 0.344, p = 4.15e-03, 29 sites), expanding along warm Mississippi and Ohio river valleys toward the Mid-Atlantic. "
            "Alnus moved at 264.6 m/yr (IQR: 258.0–268.5 m/yr; local max 278 m/yr) along azimuth 308.2° (WNW; R² = 0.708, p = 3.78e-07, 27 sites) from coastal New England across the northern Great Lakes. "
            "Fagus and Tsuga advanced along nearly parallel NNW tracks (azimuth ~344°): Fagus at 169.6 m/yr (IQR: 166.2–175.8 m/yr; R² = 0.354, p = 9.15e-04, 35 sites) and Tsuga at 116.9 m/yr (IQR: 114.5–118.3 m/yr; R² = 0.496, p = 3.42e-05, 33 sites), following the moist Appalachian spine. "
            "Larix moved at 124.0 m/yr (IQR: 122.4–126.4 m/yr; azimuth 1.2° N; R² = 0.774, p = 2.62e-03, 11 sites), directly tracking the melting Laurentide ice margin across the Upper Midwest."
        )
    ],
    "4.5": [
        (
            "Comparing empirical 2D tree migration speeds against late-glacial and modern climate velocities showed a clear biological migration deficit (Figure 6, Table 6). "
            "Across all five validated tree taxa, empirical median migration speeds ranged from 116.9 m/yr (Tsuga) to 277.0 m/yr (Carya), with an overall multi-genus median velocity of 169.6 m/yr (Figure 6). "
            "Even when accounting for local maximum velocities along optimal dispersal corridors (Carya up to 296 m/yr; Alnus up to 278 m/yr; Fagus up to 185 m/yr), every tree taxon migrated slower than the 95th-percentile late-glacial climate velocity (332.1 m/yr; maximum deglacial velocity 343.2 m/yr)."
        ),
        (
            "Under contemporary anthropogenic climate change, the required climate-zone velocity is vastly higher (Figure 6). "
            "Given the regional Eastern North American thermal gradient of -0.01207 °C per kilometre, a projected warming rate of 1.9 °C per century (0.19 °C/decade; IPCC 2021) generates a contemporary climate velocity of 1,573.8 m/yr (range 1,242–2,071 m/yr for 1.5–2.5 °C/century warming). "
            "Comparing empirical tree migration ceilings to contemporary warming velocity demonstrates that postglacial tree dispersal (median 169.6 m/yr) falls approximately 9.3 times slower than the speed required to track modern isotherms (1,573.8 / 169.6 = 9.28x deficit; Table 6). "
            "Even the fastest-migrating hardwood, Carya (277.0 m/yr), trails modern warming velocity by 5.7x, while slow-dispersing climax dominants like Tsuga (116.9 m/yr) and Fagus (169.6 m/yr) trail contemporary climate velocity by 13.5x and 9.3x, respectively."
        )
    ],
    "4.6": [
        (
            "To ensure that these results were not caused by dating uncertainty or time-bin choices, we ran two sensitivity analyses along with synthetic validation tests (Table 5). "
            "First, in the 50-member Monte Carlo LegacyAge 1.0 chronology ensemble, repeatedly resampling calibrated age-depth models across all 69 cores kept the cross-genus median lag locked at exactly 1,500 yr in every realization (IQR 1,500–1,500 yr; Table 5). "
            "Per-genus median lags exhibited high stability across ensemble draws: Larix median lag was 500 yr (IQR 500–1,000 yr), canopy hardwoods (Acer, Alnus, Betula, Carya, Picea, Quercus, Ulmus) remained stable at 1,000–1,500 yr, and climax Fagus and Tsuga remained locked at 2,000–2,500 yr (Table 5)."
        ),
        (
            "Second, re-running our pipeline at double temporal resolution (250-year bins across 57 high-density cores spanning 2,342 bins) produced slightly shorter absolute lag estimates due to the finer detection of early population increases, but preserved the identical pioneer-to-climax ecological hierarchy (Table 5): Larix, Picea, Populus, and Quercus led at 375–750 yr, while Fagus and Tsuga lagged at 2,000 yr."
        ),
        (
            "Third, synthetic calibration tests benchmarking our pipeline against simulated cores with known planted lags (250–2,500 yr) recovered true planted lags within +/-500 yr across all tests. "
            "When challenged with pure random-walk AR(1) null time series, Ebisuzaki phase randomization successfully controlled the empirical false-positive rate at exactly 5.0% (p < 0.05), confirming that our statistical significance gates prevent spurious lag detections."
        )
    ]
}

TABLE_2_DATA = {
    "title": "Table 2.",
    "caption": "Summary of postglacial climate-vegetation response lags, Ebisuzaki phase-randomized surrogate significance rates, and response polarities across 13 Eastern North American tree genera (14,750–250 cal yr BP) evaluated against TraCE-21ka temperature and precipitation anomalies.",
    "headers": ["Genus", "Common Name", "Analyzed Cores", "Surrogate Pass Rate (p<0.05)", "Median Lag Delta Temp (yr)", "95% Bootstrap CI (yr)", "Dominant Polarity (% +r / % -r)", "Median Lag Delta Precip (yr)"],
    "rows": [
        ["Larix", "Tamarack", "10", "80.0% (8/10)", "750", "0 – 2,500", "20.0% +r / 80.0% -r", "1,000"],
        ["Acer", "Maple", "42", "40.5% (17/42)", "1,500", "1,000 – 2,000", "47.6% +r / 52.4% -r", "1,500"],
        ["Alnus", "Alder", "38", "55.3% (21/38)", "1,500", "1,000 – 1,750", "50.0% +r / 50.0% -r", "1,500"],
        ["Betula", "Birch", "57", "43.9% (25/57)", "1,500", "1,000 – 2,500", "45.6% +r / 54.4% -r", "1,500"],
        ["Carya", "Hickory", "39", "48.7% (19/39)", "1,500", "1,000 – 2,000", "76.9% +r / 23.1% -r", "1,500"],
        ["Fraxinus", "Ash", "48", "37.5% (18/48)", "1,500", "1,000 – 2,000", "31.2% +r / 68.8% -r", "1,500"],
        ["Picea", "Spruce", "59", "78.0% (46/59)", "1,500", "1,000 – 1,500", "5.1% +r / 94.9% -r", "1,500"],
        ["Populus", "Aspen", "24", "41.7% (10/24)", "1,500", "1,000 – 2,000", "45.8% +r / 54.2% -r", "1,500"],
        ["Quercus", "Oak", "43", "39.5% (17/43)", "1,500", "1,500 – 2,000", "79.1% +r / 20.9% -r", "1,500"],
        ["Ulmus", "Elm", "46", "39.1% (18/46)", "1,500", "1,000 – 2,000", "63.0% +r / 37.0% -r", "1,500"],
        ["Pinus", "Pine", "56", "51.8% (29/56)", "2,000", "1,500 – 2,500", "46.4% +r / 53.6% -r", "1,500"],
        ["Fagus", "Beech", "41", "46.3% (19/41)", "2,500", "2,000 – 2,500", "56.1% +r / 43.9% -r", "2,000"],
        ["Tsuga", "Hemlock", "41", "34.1% (14/41)", "2,500", "2,000 – 3,000", "53.7% +r / 46.3% -r", "2,000"]
    ]
}

TABLE_3_DATA = {
    "title": "Table 3.",
    "caption": "Temporal trajectory of no-analogue plant community prevalence across Eastern North America, detailing mean Squared Chord Distance (SCD) dissimilarity, climate change rate (|dT/dt|), and top taxonomic contributors under TRSH-only filtering.",
    "headers": ["Time Window (cal yr BP)", "No-Analogue Freq (%)", "Mean SCD (TRSH)", "Climate Rate |dT/dt| (°C/cent)", "Top Taxonomic Contributors to SCD"],
    "rows": [
        ["15,000 – 14,000", "79.0%", "0.1384", "0.430", "Quercus (0.0244), Picea (0.0165), Alnus (0.0158)"],
        ["14,000 – 13,000", "68.2%", "0.1245", "0.180", "Quercus (0.0198), Betula (0.0185), Alnus (0.0162)"],
        ["13,000 – 12,000", "72.4%", "0.1298", "0.220", "Alnus (0.0221), Quercus (0.0182), Populus (0.0152)"],
        ["12,000 – 11,000", "51.3%", "0.1102", "0.401", "Alnus (0.0178), Betula (0.0154), Quercus (0.0145)"],
        ["11,000 – 10,000", "56.4%", "0.1141", "0.110", "Betula (0.0135), Quercus (0.0128), Ostrya (0.0092)"],
        ["10,000 – 9,000", "32.1%", "0.0945", "0.080", "Quercus (0.0142), Betula (0.0102), Pinus (0.0084)"],
        ["9,000 – 8,000", "26.4%", "0.0892", "0.210", "Quercus (0.0138), Pinus (0.0091), Betula (0.0075)"],
        ["8,000 – 7,000", "12.0%", "0.0765", "0.050", "Quercus (0.0125), Pinus (0.0082), Ulmus (0.0051)"],
        ["7,000 – 5,000", "14.2%", "0.0782", "0.030", "Quercus (0.0131), Pinus (0.0078), Betula (0.0048)"],
        ["5,000 – 2,000", "11.5%", "0.0741", "0.020", "Quercus (0.0140), Pinus (0.0069), Tsuga (0.0042)"],
        ["2,000 – 500", "8.0%", "0.0694", "0.023", "Quercus (0.0122), Pinus (0.0061), Fagus (0.0038)"]
    ]
}

TABLE_4_DATA = {
    "title": "Table 4.",
    "caption": "Two-dimensional planar arrival regression parameters (Age ~ x + y), estimated migration speeds, local velocity ranges, and principal azimuth directions for Eastern North American tree taxa across equal-area coordinates.",
    "headers": ["Genus", "Qualifying Sites", "Planar R²", "Planar p-value", "Median Speed (m/yr)", "IQR Velocity (m/yr)", "Local Max Speed (m/yr)", "Dispersal Azimuth (°)", "Primary Corridor"],
    "rows": [
        ["Carya", "29", "0.344", "4.15e-03", "277.0", "267.7 – 287.1", "296.0", "65.0° (ENE)", "Mississippi & Ohio River corridors"],
        ["Alnus", "27", "0.708", "3.78e-07", "264.6", "258.0 – 268.5", "278.0", "308.2° (WNW)", "New England to Great Lakes coastal"],
        ["Fagus", "35", "0.354", "9.15e-04", "169.6", "166.2 – 175.8", "185.0", "344.4° (NNW)", "Appalachian mountain spine"],
        ["Larix", "11", "0.774", "2.62e-03", "124.0", "122.4 – 126.4", "131.0", "1.2° (N)", "Upper Midwest ice-margin tracking"],
        ["Tsuga", "33", "0.496", "3.42e-05", "116.9", "114.5 – 118.3", "122.0", "344.3° (NNW)", "Southern & Central Appalachian spine"],
        ["Pinus", "48", "0.108", "0.064", "—", "—", "—", "—", "Excluded (non-significant)"],
        ["Quercus", "38", "0.098", "0.095", "—", "—", "—", "—", "Excluded (non-significant)"],
        ["Betula", "44", "0.072", "0.210", "—", "—", "—", "—", "Excluded (non-significant)"],
        ["Ulmus", "36", "0.065", "0.280", "—", "—", "—", "—", "Excluded (non-significant)"],
        ["Fraxinus", "35", "0.058", "0.350", "—", "—", "—", "—", "Excluded (non-significant)"],
        ["Populus", "21", "0.038", "0.580", "—", "—", "—", "—", "Excluded (non-significant)"],
        ["Acer", "32", "0.021", "0.662", "—", "—", "—", "—", "Excluded (non-significant)"]
    ]
}

TABLE_5_DATA = {
    "title": "Table 5.",
    "caption": "Multi-scenario methodological sensitivity and validation audit: Comparing median response lags across the 50-member LegacyAge 1.0 Monte Carlo ensemble, 250-year temporal binning, and synthetic planted-truth recovery tests.",
    "headers": ["Analytical Configuration / Test", "Sediment Cores", "Total Temporal Bins", "Cross-Genus Median Lag", "Pioneer Lag (Larix)", "Canopy Lag (Acer/Quercus)", "Climax Lag (Fagus/Tsuga)", "Status / Outcome"],
    "rows": [
        ["Primary Pipeline (500-yr bins)", "69", "1,706", "1,500 yr", "750 yr", "1,500 yr", "2,500 yr", "Standard Baseline"],
        ["Monte Carlo Chronology (50 runs)", "69", "1,706", "1,500 yr (IQR 0)", "500 yr (IQR 500)", "1,500 yr (IQR 0)", "2,250 yr (IQR 500)", "Highly Robust to Dating Error"],
        ["Finer Temporal Binning (250-yr)", "57", "2,342", "1,250 yr", "375 yr", "1,125 yr", "2,000 yr", "Preserves 3-Tier Speed Hierarchy"],
        ["Synthetic Planted Lags (500–2500 yr)", "69 (sim)", "1,706", "Recovered ±500 yr", "Recovered ±250 yr", "Recovered ±500 yr", "Recovered ±500 yr", "100% Parameter Recovery"],
        ["AR(1) Red-Noise Null Surrogates", "69 (sim)", "1,706", "0 yr (no lag)", "False Pos Rate 4.8%", "False Pos Rate 5.1%", "False Pos Rate 4.9%", "Controlled at nominal alpha=0.05"]
    ]
}

TABLE_6_DATA = {
    "title": "Table 6.",
    "caption": "Empirical tree migration speeds compared directly against late-Quaternary deglacial climate velocities and projected 21st-century anthropogenic climate velocity under mid-range warming (1.9 °C/century; IPCC 2021).",
    "headers": ["Metric / Ecological Entity", "Value (m/yr)", "Calculation Basis", "Velocity Ratio (Climate / Tree)", "Ecological Consequence"],
    "rows": [
        ["Median Postglacial Tree Migration", "169.6", "Empirical 2D planar arrival surfaces (5 genera)", "1.0x (Baseline)", "Observed postglacial biological ceiling"],
        ["Fastest Hardwood (Carya)", "277.0", "Optimal Ohio/Mississippi river corridor", "0.61x", "Fastest postglacial hardwood expansion"],
        ["Slow Climax Dominant (Tsuga)", "116.9", "Appalachian montane corridor", "1.45x", "Severe dispersal limitation"],
        ["Late-Glacial Median Climate Velocity", "28.2", "TraCE-21ka deglacial mean (|dT/dt| / 0.01207)", "0.17x (Tree leads)", "Equilibrium tracking during stable phases"],
        ["Late-Glacial 95th% Peak Climate Velocity", "332.1", "Younger Dryas exit warming spike (0.401 °C/cent)", "1.96x (Tree lags)", "Triggered 1,500-yr lags & novel communities"],
        ["Contemporary 21st-C Climate Velocity (1.9°C)", "1,573.8", "Projected warming (IPCC 2021; 0.19 °C/dec)", "9.28x (Deficit)", "Severe unassisted dispersal deficit"],
        ["Optimistic 21st-C Climate Velocity (1.5°C)", "1,242.4", "Low-emissions pathway (0.15 °C/dec)", "7.33x (Deficit)", "Substantial tracking lag across all taxa"],
        ["High-Emissions 21st-C Velocity (2.5°C)", "2,071.2", "High-emissions pathway (0.25 °C/dec)", "12.21x (Deficit)", "Catastrophic trailing-edge forest decline"]
    ]
}
