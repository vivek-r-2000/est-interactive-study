"""
section3_methods.py - Section 3: Data and Methodology (1,450–1,550 words)
Fossil pollen, TraCE-21ka, LegacyAge 1.0, REVEALS RPP, TRSH filtering, first-differenced lags,
Ebisuzaki phase-randomization, Squared Chord Distance decomposition, 2D planar arrival velocity.
"""

METHODS_PARAGRAPHS = {
    "3.1": [
        (
            "To reconstruct continental-scale vegetation dynamics across Eastern North America, we extracted sedimentary fossil pollen records from the community-curated Neotoma Paleoecology Database (Williams et al. 2018). "
            "We initially queried 423 candidate palynological datasets spanning North America, filtering for coordinates within our defined regional study corridor (34°–52° N, 100°–60° W) and temporal boundaries covering the deglacial to pre-industrial period (15,000 to 0 cal yr BP) (Williams et al. 2018). "
            "This spatial screening yielded 85 candidate lake sediment and bog cores comprising 742,380 raw palynological count observations across identified pollen and spore morphotypes."
        ),
        (
            "To establish a reliable modern compositional yardstick for evaluating past forest novelty, we compiled 644 modern surface sediment and moss polster samples across Eastern North America from the Neotoma modern pollen archive (Williams et al. 2004; Goring et al. 2015). "
            "Modern samples were subjected to identical taxonomic harmonization and quality screening criteria as the fossil datasets. "
            "Samples dominated by open non-arboreal vegetation, agricultural weeds, or containing fewer than 100 counted woody pollen grains were discarded, retaining 611 modern forest surface assemblages that represent contemporary vegetation zones from the southern boreal ecotone to warm temperate deciduous forests (Williams et al. 2004)."
        )
    ],
    "3.2": [
        (
            "To evaluate vegetation responses against climate forcing without introducing circular reasoning, we extracted paleoclimatic time series from the NCAR TraCE-21ka transient climate simulation (Liu et al. 2009; He 2011). "
            "Palaeoecological studies that reconstruct paleotemperature directly from fossil pollen assemblages and subsequently correlate those temperatures with changes in tree abundance suffer from circular logic (Fordham et al. 2020). "
            "TraCE-21ka circumvents this artifact by employing a fully coupled, synchronously integrated atmosphere-ocean general circulation model (CCSM3) run at T31 spectral resolution (~3.75° grid) with a 25-level ocean component (POP) (Liu et al. 2009; He et al. 2013). "
            "The model was forced transiently by realistic boundary conditions: orbital insolation variations, greenhouse gas concentrations (CO2, CH4, N2O), retreating ice sheet topography and albedo (ICE-5G), and meltwater discharge fluxes into the North Atlantic, Arctic, and Gulf of Mexico (Liu et al. 2009)."
        ),
        (
            "From the monthly TraCE-21ka archives (NCAR GDEX dataset d651050), we extracted mean surface air temperature (TREFHT, converted to °C) and total precipitation (PRECT, mm/day) directly for grid cells overlying each of the 69 retained fossil sediment cores. "
            "Monthly values were aggregated into annual means and binned into the identical 500-year temporal windows (14,750 to 250 cal yr BP) used for palynological data. "
            "To measure the regional spatial temperature gradient necessary for computing climate velocities, we fitted a spatial linear regression of annual mean temperature across the coordinates of all study sites, yielding a regional meridional lapse rate of -0.01207 °C per kilometre southward (~1.21 °C per 100 km) across the corridor (Loarie et al. 2009)."
        )
    ],
    "3.3": [
        (
            "Accurate determination of ecological response lags depends on reliable, standardized chronology. "
            "Historical palynological records stored in public repositories often rely on uncalibrated radiocarbon determinations, disparate calibration curves, or linear depth-age interpolations that distort the timing of abrupt climatic events (Li et al. 2022). "
            "To eliminate chronological artifacts, we harmonized our sediment cores using the LegacyAge 1.0 global dataset (Li et al. 2022). "
            "LegacyAge 1.0 constructed standardized Bayesian age-depth models for thousands of pollen cores using the Bacon 2.5.3 software package calibrated against the IntCal20 atmospheric radiocarbon calibration curve (Li et al. 2022)."
        ),
        (
            "Direct cross-referencing between our 85 candidate Neotoma datasets and the LegacyAge 1.0 PANGAEA database matched 68 cores directly based on dataset identifiers and site metadata. "
            "Following sample quality filtering, 57 of the final 69 retained cores (82.6%) possessed direct LegacyAge 1.0 Bayesian median chronologies. "
            "For the remaining 12 cores lacking LegacyAge entries, we employed default Neotoma Bayesian or spline age models with empirical depth-dependent uncertainty scaling. "
            "To confirm that derived response lags were not driven by chronological uncertainty, we implemented an ensemble Monte Carlo sensitivity protocol. "
            "We drew 50 independent age-depth realizations from the posterior uncertainty distributions of the Bayesian age models across all cores and re-evaluated cross-correlation response lags across all 50 realizations."
        )
    ],
    "3.4": [
        (
            "Raw fossil pollen percentages systematically distort true forest biomass because wind-pollinated anemophilous taxa (such as Pinus and Betula) release orders of magnitude more pollen per tree than insect-pollinated entomophilous species (such as Acer and Tilia) (Sugita 2007; Wieczorek and Herzschuh 2020). "
            "To correct this taxonomic bias, we applied the REVEALS modeling framework (Sugita 2007). "
            "Raw pollen counts were adjusted prior to calculating proportions by dividing each taxon's grain count by its empirical Relative Pollen Productivity (RPP) divisor, drawn from Northern Hemisphere syntheses (Wieczorek and Herzschuh 2020) and upper Midwestern historical forest calibration studies (Dawson et al. 2016; Dawson et al. 2019). "
            "The specific RPP divisors applied were: Pinus (14.10), Abies (6.88), Betula (6.19), Picea (2.80), Alnus (2.70), Fraxinus (2.42), Fagus (2.35), Ulmus (2.24), Quercus (2.08), Tsuga (1.60), Larix (1.24), Carya (1.00), Populus (0.67), and Acer (0.23) (Table 1). "
            "Taxa lacking specific empirical RPP values were normalized to the arboreal baseline (1.00)."
        ),
        (
            "A second preprocessing step involved isolating woody arboreal taxa. "
            "Following European colonization (post-1700 CE), extensive agricultural deforestation across eastern North America triggered widespread soil disturbance and massive blooms of upland herbaceous pollen (UPHE), primarily ragweed (Ambrosia), grasses (Poaceae), and sorrel (Rumex) (Williams et al. 2004; Oswald et al. 2020). "
            "Including herbaceous pollen in dissimilarity comparisons against pre-industrial sediments creates an artificial novelty signal that reflects modern farming rather than climatic forcing (Williams et al. 2004). "
            "We therefore restricted our pollen sum strictly to tree and shrub taxa (TRSH), evaluating 14 dominant Eastern North American woody genera (plus minor woody taxa aggregated into 'Other'). "
            "Following TRSH filtering, samples with fewer than 100 counted woody grains were removed (discarding 4 prairie-fringe cores), and remaining records were regularized into 500-year bins (14,750 to 250 cal yr BP). "
            "Cores were required to possess at least 12 occupied time bins with no internal hiatus exceeding 4 consecutive bins (2,000 yr), yielding a continuous network of 69 sediment cores spanning 1,706 time bins."
        )
    ],
    "3.5": [
        (
            "Correlating raw paleoclimate time series against raw vegetation abundances produces spurious statistical significance because both variables exhibit non-stationary, millennial-scale trends over the 15,000-year deglacial transition (Ebisuzaki 1997). "
            "To isolate genuine dynamic coupling, we applied stationary first-differencing to all time series. "
            "For each regularized sediment core and tree genus, we computed bin-to-bin compositional change, Delta P_{i,t} = P_{i,t} - P_{i,t-1}, and paired it with the corresponding bin-to-bin TraCE-21ka temperature change, Delta T_{i,t} = T_{i,t} - T_{i,t-1}. "
            "Internal chronological gaps were preserved strictly as missing values (NaN) to prevent false step-change calculations across sediment hiatuses."
        ),
        (
            "For each core and genus with at least 12 overlapping differenced steps and non-zero variance, we evaluated cross-correlation across discrete time lags k in [0, 3,000 yr] at 500-year increments:"
        )
    ],
    "3.6": [
        (
            "To quantify the emergence and composition of no-analogue plant communities, we computed the Squared Chord Distance (SCD) between each fossil pollen assemblage and our reference network of 611 modern surface pollen samples (Overpeck et al. 1992; Williams et al. 2001, 2004). "
            "For fossil bin i and modern surface sample j across M woody taxa, SCD is defined as:"
        ),
        (
            "where p_{i,t} is the proportion of taxon t in fossil sample i, and q_{j,t} is the proportion of taxon t in modern sample j. "
            "For each fossil sample, we identified its minimum dissimilarity score across all modern samples: SCD_{min,i} = min_j(SCD_{ij}). "
            "Following Williams et al. (2004), a fossil sample was categorized as 'no-analogue' if its SCD_{min} exceeded the 5th percentile of pairwise dissimilarity scores measured within the modern reference dataset itself (threshold = 0.1060). "
            "Because SCD sums squared square-root differences additively across individual taxa, we directly decomposed SCD_{min} to calculate the numerical contribution of each tree genus to total community novelty:"
        ),
        (
            "We paired bin-level no-analogue frequencies with TraCE-21ka absolute climate change rates (|dT/dt|, °C/century) and Hellinger community turnover rates (Mottl et al. 2021), evaluating statistical associations using Spearman rank correlation and 1,000-surrogate Ebisuzaki tests."
        )
    ],
    "3.7": [
        (
            "To overcome the limitations of classical one-dimensional northward migration models, we developed a two-dimensional planar arrival framework on equal-area projected coordinates (Blois et al. 2013). "
            "For each of the 12 dominant tree genera, we identified the empirical arrival age at each sediment core, defined as the oldest 500-year bin where the taxon first achieved and sustained at least 20% of its site peak abundance (Davis 1981; McLachlan et al. 2005). "
            "Geographic coordinates were transformed onto an Albers Equal Area Conic projection centered on the centroid of the core network (coordinates x and y in kilometres)."
        ),
        (
            "To eliminate taxa exhibiting diffuse, non-directional, or multi-refugial expansion patterns, every genus with at least 8 qualifying arrival sites was evaluated using a planar 2D regression model: Age(x, y) = beta_0 + beta_x * x + beta_y * y + epsilon. "
            "Only genera demonstrating statistically coherent regional expansion fronts passing a planar F-test significance gate (p_2d <= 0.05) advanced to spatial velocity mapping (Table 4). "
            "For validated taxa, arrival age surfaces were interpolated using thin-plate radial basis function splines (RBFInterpolator) clipped strictly to the Delaunay convex hull of observed sites to prevent unconstrained boundary extrapolation. "
            "Local migration velocity was calculated across grid cells as the inverse of the spatial arrival age gradient:"
        ),
        (
            "Dispersal direction was computed as the vector mean azimuth of the spatial gradient (0° = North, 90° = East). "
            "Finally, empirical tree velocities were benchmarked against late-glacial climate velocity (computed by dividing TraCE-21ka temporal warming rates by the regional temperature gradient) and projected 21st-century warming velocity (1.9 °C/century divided by -0.01207 °C/km = 1,573.8 m/yr) (Loarie et al. 2009; Fordham et al. 2020)."
        )
    ]
}

EQUATIONS = [
    ("r(k) = \\frac{\\sum_{t} (\\Delta P_{t-k} - \\overline{\\Delta P}) (\\Delta T_t - \\overline{\\Delta T})}{\\sqrt{\\sum_{t} (\\Delta P_{t-k} - \\overline{\\Delta P})^2 \\sum_{t} (\\Delta T_t - \\overline{\\Delta T})^2}}", "1"),
    ("SCD_{ij} = \\sum_{t=1}^{M} \\left( \\sqrt{p_{i,t}} - \\sqrt{q_{j,t}} \\right)^2", "2"),
    ("C_{i,t} = \\left( \\sqrt{p_{i,t}} - \\sqrt{q_{j^*,t}} \\right)^2, \\quad \\text{where } j^* = \\arg\\min_j(SCD_{ij})", "3"),
    ("v_{mig}(x, y) = \\frac{1}{\\| \\nabla \\text{Age}(x, y) \\|} = \\frac{1}{\\sqrt{\\left(\\frac{\\partial \\text{Age}}{\\partial x}\\right)^2 + \\left(\\frac{\\partial \\text{Age}}{\\partial y}\\right)^2}}", "4")
]

TABLE_1_DATA = {
    "title": "Table 1.",
    "caption": "Summary of experimental design parameters, REVEALS relative pollen productivity calibration weights, and statistical significance controls.",
    "headers": ["Category", "Experimental Setting", "Rationale & Empirical Basis"],
    "rows": [
        ["Spatial & Temporal Domain", "34°–52° N, 100°–60° W; 15,000–0 cal yr BP; 500-yr bins", "Encompasses eastern deglacial corridor across 69 continuous sediment cores and 1,706 time bins (min 12 occupied bins, max 4-bin gap)."],
        ["Modern Analogue Scope", "611 quality-filtered modern surface samples", "Provides contemporary vegetation baseline; samples with <100 woody grains or agricultural weeds excluded."],
        ["Taxonomic Filtering", "TRSH woody arboreal taxa only (>=100 grains/sample)", "Eliminates post-settlement agricultural weed spikes (Ambrosia, Poaceae) that distort pre-industrial forest comparisons."],
        ["REVEALS RPP Multipliers", "Pinus 14.10, Abies 6.88, Betula 6.19, Picea 2.80, Alnus 2.70, Fraxinus 2.42, Fagus 2.35, Ulmus 2.24, Quercus 2.08, Tsuga 1.60, Larix 1.24, Carya 1.00, Populus 0.67, Acer 0.23", "Normalizes unequal pollen productivity and dispersal biases based on empirical Northern Hemisphere consensus (Wieczorek & Herzschuh 2020; Dawson et al. 2016)."],
        ["Chronological Harmonization", "LegacyAge 1.0 (57 direct, 12 fallback) + N=50 ensemble", "Standardized Bayesian Bacon/IntCal20 depth-age models (Li et al. 2022) with Monte Carlo uncertainty propagation."],
        ["Paleoclimate Simulation", "NCAR TraCE-21ka synchronously coupled AOGCM (TREFHT & PRECT)", "Independent physical climate model driven by orbital forcing, greenhouse gases, and ice retreat, preventing circular proxy logic."],
        ["Statistical Significance Gates", "First-differencing, 1,000 Ebisuzaki surrogates, 2D planar p_2d <= 0.05", "Controls for millennial non-stationarity, red-noise autocorrelation, and isolates coherent directional migration fronts."]
    ]
}
