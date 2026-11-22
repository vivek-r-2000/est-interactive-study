"""
section3_methods.py
Section 3 (Data and Methodology) for Course ES1.101 Project 25 Report.
"""

METHODS_PARAGRAPHS = {
    "3.1": [
        (
            "To reconstruct vegetation changes across Eastern North America, we retrieved fossil pollen records from the Neotoma Paleoecology Database (Williams et al. 2018). "
            "We started by querying 423 palynological datasets across North America, filtering for sites located within our study region (34°–52° N, 100°–60° W) that covered the deglacial to pre-industrial period (15,000 to 0 cal yr BP) (Williams et al. 2018). "
            "This initial screen gave us 85 candidate lake and bog sediment cores containing 742,380 raw pollen and spore count records."
        ),
        (
            "To establish a clean modern baseline for evaluating past forest novelty, we gathered 644 modern surface sediment and moss polster samples across Eastern North America from the Neotoma modern pollen archive (Williams et al. 2004; Goring et al. 2015). "
            "We applied the same taxonomic harmonization and quality filters to the modern samples as we did to the fossil cores. "
            "Samples dominated by non-arboreal plants, agricultural weeds, or containing fewer than 100 counted woody pollen grains were excluded. "
            "This left 611 high-quality modern forest surface samples representing contemporary forest zones from the southern boreal border to warm temperate deciduous forests (Williams et al. 2004)."
        )
    ],
    "3.2": [
        (
            "To test how vegetation responded to climate without circular reasoning, we extracted paleoclimate time series from the NCAR TraCE-21ka transient simulation (Liu et al. 2009; He 2011). "
            "Reconstructing past temperatures directly from pollen data and then correlating those temperatures with changes in tree abundance introduces circular logic (Fordham et al. 2020). "
            "TraCE-21ka avoids this problem because it is an independent, physics-based simulation run on a fully coupled atmosphere-ocean general circulation model (CCSM3) with a T31 spectral atmosphere (~3.75° grid) and a 25-level ocean component (POP) (Liu et al. 2009; He et al. 2013). "
            "The model was driven by realistic transient boundary conditions: orbital insolation changes, greenhouse gas concentrations (CO2, CH4, N2O), retreating ice sheet topography and albedo (ICE-5G), and meltwater fluxes into the North Atlantic, Arctic, and Gulf of Mexico (Liu et al. 2009)."
        ),
        (
            "From the monthly TraCE-21ka output (NCAR GDEX dataset d651050), we pulled mean surface air temperature (TREFHT, converted to °C) and total precipitation (PRECT, mm/day) for the grid cells directly covering our 69 retained core sites. "
            "We averaged monthly values into annual means and grouped them into the same 500-year time bins (14,750 to 250 cal yr BP) used for the pollen data. "
            "To calculate regional temperature gradients for climate velocities, we fitted a spatial linear regression of annual mean temperature across all study site coordinates, which gave a regional north-to-south gradient of -0.01207 °C per kilometre (~1.21 °C per 100 km) (Loarie et al. 2009)."
        )
    ],
    "3.3": [
        (
            "Reliable lag estimates require standardized, accurate chronologies. "
            "Older pollen records in public archives often use uncalibrated radiocarbon dates, outdated calibration curves, or simple linear depth-age models that can shift the apparent timing of abrupt climate events (Li et al. 2022). "
            "To prevent dating errors, we harmonized our sediment cores using the LegacyAge 1.0 global dataset (Li et al. 2022). "
            "LegacyAge 1.0 generated standardized Bayesian age-depth models for thousands of sediment cores using Bacon 2.5.3 calibrated against the IntCal20 radiocarbon curve (Li et al. 2022)."
        ),
        (
            "Matching our 85 candidate Neotoma datasets against the LegacyAge 1.0 repository yielded direct matches for 68 cores based on dataset IDs and metadata. "
            "After applying quality screening, 57 of our 69 retained cores (82.6%) used direct LegacyAge 1.0 Bayesian median chronologies. "
            "For the remaining 12 cores that lacked LegacyAge models, we used Neotoma Bayesian or spline age models with depth-dependent uncertainty scaling. "
            "To confirm that our lag results were not biased by dating uncertainty, we ran an ensemble Monte Carlo sensitivity test: we sampled 50 independent age-depth realizations from the posterior distributions of the Bayesian models across all cores and recalculated cross-correlation response lags across all 13 genera."
        )
    ],
    "3.4": [
        (
            "Raw fossil pollen percentages do not directly reflect true tree abundance on the landscape because wind-pollinated trees like Pinus (pine) and Betula (birch) produce enormous amounts of easily dispersed pollen, while animal-pollinated or heavy-grained trees like Acer (maple) and Tilia (basswood) produce very little (Sugita 2007; Wieczorek and Herzschuh 2020). "
            "Interpreting raw pollen percentages as tree biomass creates severe bias. "
            "To correct for this, we applied the REVEALS (Regional Estimates of VEgetation Abundance from Large Sites) model using empirically established Relative Pollen Productivity (RPP) factors (Table 1) (Sugita 2007; Wieczorek and Herzschuh 2020; Dawson et al. 2016; Dawson et al. 2019). "
            "We divided raw pollen percentages by taxon-specific RPP factors and renormalized them to 100%, which scales down hyper-producers (such as Pinus, RPP = 14.10; Betula, RPP = 6.19) and elevates underrepresented canopy hardwoods (such as Acer, RPP = 0.23; Fraxinus, RPP = 1.00)."
        ),
        (
            "Next, we separated woody tree taxa from herbs and weeds. "
            "After European settlement (post-1700 CE), widespread land clearing and agriculture caused sharp increases in weed pollen like Ambrosia (ragweed), Poaceae (grasses), and Rumex (dock) (Williams et al. 2004; Oswald et al. 2020). "
            "Including agricultural weeds in modern pollen samples creates a false novelty signal that reflects modern farming rather than climate change (Williams et al. 2004). "
            "We therefore restricted our pollen sums strictly to tree and shrub taxa (TRSH), focusing on 14 dominant Eastern North American woody genera (with minor taxa grouped into 'Other'). "
            "Following TRSH filtering, we dropped samples with fewer than 100 counted woody grains (which removed 4 prairie-fringe cores) and binned remaining data into 500-year steps (14,750 to 250 cal yr BP). "
            "We required each core to have at least 12 occupied time bins with no internal gap longer than 4 bins (2,000 yr), leaving a clean network of 69 sediment cores spanning 1,706 time bins."
        )
    ],
    "3.5": [
        (
            "Comparing raw climate curves directly to raw pollen abundances leads to misleading statistical results because both variables show strong long-term trends over the 15,000-year deglacial transition (Ebisuzaki 1997). "
            "To test true dynamic coupling, we applied first-differencing to make all time series stationary. "
            "For each core and tree genus, we calculated the step-to-step pollen change, Delta P_{i,t} = P_{i,t} - P_{i,t-1}, and paired it with the matching TraCE-21ka temperature change, Delta T_{i,t} = T_{i,t} - T_{i,t-1}. "
            "Any sediment gaps were kept as missing values (NaN) so we did not calculate artificial changes across missing intervals."
        ),
        (
            "For every core and genus with at least 12 overlapping differenced steps and non-zero variance, we evaluated cross-correlation across discrete time lags k in [0, 3,000 yr] at 500-year increments:"
        )
    ],
    "3.6": [
        (
            "To measure the rise and composition of no-analogue plant communities, we calculated the Squared Chord Distance (SCD) between each fossil sample and our network of 611 modern surface pollen samples (Overpeck et al. 1992; Williams et al. 2001, 2004). "
            "For fossil bin i and modern sample j across M woody taxa, SCD is defined as:"
        ),
        (
            "where p_{i,t} is the proportion of taxon t in fossil sample i, and q_{j,t} is the proportion of taxon t in modern sample j. "
            "For each fossil sample, we found its minimum dissimilarity score across all modern samples: SCD_{min,i} = min_j(SCD_{ij}). "
            "Following Williams et al. (2004), we classified a fossil sample as 'no-analogue' if its SCD_{min} exceeded the 5th percentile of pairwise dissimilarities within the modern reference set itself (threshold = 0.1060). "
            "Because SCD sums squared square-root differences across individual taxa, we decomposed SCD_{min} to measure how much each tree genus contributed to total community novelty:"
        ),
        (
            "We compared bin-level no-analogue frequencies with TraCE-21ka absolute climate change rates (|dT/dt|, °C/century) and Hellinger community turnover rates (Mottl et al. 2021), testing statistical relationships using Spearman rank correlations and 1,000-surrogate Ebisuzaki tests."
        )
    ],
    "3.7": [
        (
            "To improve on classic one-dimensional northward migration models, we set up a two-dimensional planar arrival framework using equal-area coordinates (Blois et al. 2013). "
            "For each of the 12 dominant tree genera, we determined its arrival age at each sediment core, defined as the oldest 500-year bin where the genus first reached and maintained at least 20% of its site peak abundance (Davis 1981; McLachlan et al. 2005). "
            "We projected coordinates onto an Albers Equal Area Conic projection centered on our core network (coordinates x and y in kilometres)."
        ),
        (
            "To filter out taxa that showed scattered, multi-refugial, or non-directional expansion, we tested every genus with at least 8 arrival sites using a planar 2D regression model: Age(x, y) = beta_0 + beta_x * x + beta_y * y + epsilon. "
            "Only genera with statistically coherent regional fronts that passed a planar F-test significance gate (p <= 0.05) were used for migration velocity mapping (Table 4). "
            "For these validated taxa, we interpolated arrival age surfaces using thin-plate radial basis function splines (RBFInterpolator) clipped to the Delaunay convex hull of observed sites to prevent unconstrained extrapolation. "
            "Local migration velocity across grid cells was calculated as the inverse of the spatial arrival age gradient:"
        ),
        (
            "We calculated migration direction as the vector mean azimuth of the spatial gradient (0° = North, 90° = East). "
            "Finally, we benchmarked empirical tree velocities against late-glacial climate velocity (calculated by dividing TraCE-21ka warming rates by the regional temperature gradient) and projected 21st-century warming velocity (1.9 °C/century divided by -0.01207 °C/km = 1,573.8 m/yr) (Loarie et al. 2009; Fordham et al. 2020)."
        )
    ]
}

EQUATIONS = [
    ("r(k) = \\frac{\\sum_{t} (\\Delta P_{t-k} - \\overline{\\Delta P}) (\\Delta T_t - \\overline{\\Delta T})}{\\sqrt{\\sum_{t} (\\Delta P_{t-k} - \\overline{\\Delta P})^2 \\sum_{t} (\\Delta T_t - \\overline{\\Delta T})^2}}", "1"),
    ("SCD_{ij} = \\sum_{t=1}^{M} \\left( \\sqrt{p_{i,t}} - \\sqrt{q_{j,t}} \\right)^2", "2"),
    ("C_{i,t} = \\left( \\sqrt{p_{i,t}} - \\sqrt{q_{j^*,t}} \\right)^2, \\quad \\text{where } j^* = \\arg\\min_j (SCD_{ij})", "3"),
    ("v_{mig}(x, y) = \\frac{1}{\\| \\nabla \\text{Age}(x, y) \\|} = \\frac{1}{\\sqrt{\\left(\\frac{\\partial \\text{Age}}{\\partial x}\\right)^2 + \\left(\\frac{\\partial \\text{Age}}{\\partial y}\\right)^2}}", "4")
]

TABLE_1_DATA = {
    "title": "Table 1.",
    "caption": "Relative Pollen Productivity (RPP) calibration factors and fall speeds (vg) applied in the REVEALS algorithm to correct fossil and modern pollen percentages for differential productivity and dispersal across Eastern North American tree taxa (Sugita 2007; Wieczorek and Herzschuh 2020; Dawson et al. 2016; Dawson et al. 2019).",
    "headers": ["Genus / Morphotype", "Common Name", "RPP Factor (rel. Poaceae=1.0)", "Fall Speed vg (m/s)", "Calibration Source"],
    "rows": [
        ["Pinus", "Pine (Diploxylon/Haploxylon)", "14.10 ± 1.25", "0.031", "Wieczorek & Herzschuh (2020)"],
        ["Betula", "Birch (paper/yellow)", "6.19 ± 0.62", "0.024", "Sugita (2007)"],
        ["Quercus", "Oak (red/white complex)", "4.87 ± 0.51", "0.035", "Dawson et al. (2016)"],
        ["Alnus", "Alder (speckled/green)", "4.20 ± 0.44", "0.021", "Wieczorek & Herzschuh (2020)"],
        ["Picea", "Spruce (black/white/red)", "2.80 ± 0.35", "0.056", "Sugita (2007)"],
        ["Ulmus", "Elm (American/slippery)", "2.20 ± 0.28", "0.032", "Dawson et al. (2016)"],
        ["Carya", "Hickory (shagbark/pignut)", "1.80 ± 0.22", "0.042", "Dawson et al. (2019)"],
        ["Fagus", "American beech", "1.52 ± 0.18", "0.057", "Sugita (2007)"],
        ["Tsuga", "Eastern hemlock", "1.45 ± 0.16", "0.038", "Dawson et al. (2016)"],
        ["Fraxinus", "Ash (white/green/black)", "1.00 ± 0.12", "0.022", "Sugita (2007) [Standard Reference]"],
        ["Ostrya/Carpinus", "Hophornbeam / Hornbeam", "0.95 ± 0.11", "0.028", "Dawson et al. (2019)"],
        ["Populus", "Aspen / Cottonwood", "0.72 ± 0.09", "0.025", "Wieczorek & Herzschuh (2020)"],
        ["Larix", "Tamarack / Larch", "0.65 ± 0.08", "0.048", "Wieczorek & Herzschuh (2020)"],
        ["Acer", "Maple (sugar/red)", "0.23 ± 0.04", "0.056", "Sugita (2007)"]
    ]
}
