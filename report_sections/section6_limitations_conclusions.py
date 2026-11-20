"""
section6_limitations_conclusions.py - Section 6: Limitations & Future Scope; Section 7: Conclusions;
Acknowledgements, and Declarations. (~1,000–1,200 words total)
"""

LIMITATIONS_PARAGRAPHS = [
    (
        "While this study delivers an end-to-end, reproducible assessment of late-Quaternary forest dynamics, several methodological and taphonomic constraints warrant careful consideration. "
        "First, standard light-microscopy palynology resolves plant taxa primarily to the genus or family level, obscuring species-level ecological differentiation (Birks 2019; Dawson et al. 2016). "
        "In our dataset, Quercus aggregates over 20 eastern oak species with widely varying moisture and temperature niches (such as mesic Quercus rubra versus xeric Quercus velutina). "
        "Similarly, Picea blends cold-adapted boreal black spruce (Picea mariana) with upland white spruce (Picea glauca) and temperate red spruce (Picea rubens). "
        "Consequently, observed genus-level lags represent aggregate population turnover rather than individual species range dynamics. "
        "Future investigations should pair sediment palynology with sedimentary ancient DNA (sedaDNA) to resolve cryptic species-level identities and detect low-density founder populations centuries before local pollen reaches the 1% palynological detection threshold (Parducci et al. 2017)."
    ),
    (
        "Second, temporal regularization into 500-year time bins—necessary to harmonize cores with disparate sedimentation rates across 15,000 years—inherently attenuates high-frequency, sub-century ecological pulses (Mottl et al. 2021). "
        "While our 250-year sensitivity test (Table 5) confirmed that our three-tier lag hierarchy remains consistent under finer binning, 500-year windows cannot capture rapid decadal responses to multi-year mega-droughts or transient fire episodes. "
        "Applying our analytical pipeline to annually laminated (varved) lake sediments, speleothem records, and sub-fossil tree-ring chronologies will be vital for quantifying decade-scale climate–vegetation lags."
    ),
    (
        "Third, the spatial resolution of the TraCE-21ka paleoclimate simulation (~3.75° spectral atmospheric grid, ~300 km) smooths out fine-scale, topographically mediated microclimates (Liu et al. 2009; He 2011). "
        "In rugged terrain like the Appalachian Mountains, steep north-facing ravines and riparian corridors maintained localized thermal buffers that allowed temperate hardwoods to persist throughout glacial maxima in microrefugia (Gavin et al. 2014). "
        "Coarse general circulation models cannot capture these microclimatic pockets, potentially overestimating the distance trees were forced to migrate. "
        "Coupling high-resolution regional climate models (RCMs) or dynamical downscaling with local digital elevation models represents an essential frontier for late-Quaternary spatial modeling."
    ),
    (
        "Finally, although our 2D planar arrival regression isolated coherent regional migration wavefronts, thin-plate splines interpolate across intervening landscapes that may have contained unobserved physical barriers. "
        "Integrating sedimentary charcoal fire histories, Sporormiella dung fungal spore indices of megafaunal herbivore density across all 69 cores (Gill et al. 2009), and mechanistic spatio-temporal forest simulators (such as TreeMig or SORTIE) will allow researchers to model the coupled interactions of climate, fire, seed dispersal, and competition under future climate scenarios."
    )
]

CONCLUSIONS_PARAGRAPHS = [
    (
        "This study synthesised 15,000 years of sedimentary fossil pollen records from 69 Eastern North American lakes alongside independent TraCE-21ka paleoclimate simulations to provide an empirical assessment of postglacial forest dynamics. "
        "By applying REVEALS Relative Pollen Productivity calibrations, LegacyAge 1.0 Bayesian chronologies, stationary first-differencing, 1,000 Ebisuzaki surrogate tests, and two-dimensional equal-area planar migration models, we resolve three major ecological questions:"
    ),
    (
        "1. Forests do not respond as unified biome units. Tree taxa operate on distinct biological clocks structured into three ecological speed tiers (Kruskal–Wallis H = 30.54, p = 0.0023): pioneer conifer Larix adjusted in 750 yr, nine canopy reorganization taxa clustered at 1,500 yr, and shade-tolerant climax dominants (Fagus, Tsuga) lagged by 2,500 yr. Response polarity separated abrupt boreal retreat (Picea, 94.9% negative, mean r = -0.637) from gradual temperate hardwood expansion (Quercus, 79.1% positive)."
    ),
    (
        "2. No-analogue forest communities were a transient phenomenon that peaked at 79.0% at 14.5 ka BP during early deglacial warming before declining to an 8.0% pre-colonial floor at 500 BP under TRSH-only filtering. Additive Squared Chord Distance decomposition proved that novelty was driven by anomalous mixtures of Quercus, Alnus, Betula, Populus, and Picea, sustained by extreme orbital seasonal contrast (32.6 °C winter-summer range) and early-deglacial hydroclimatic decoupling."
    ),
    (
        "3. Postglacial tree migration followed distinct two-dimensional geomorphic corridors—such as Carya along the Ohio and Mississippi river valleys (azimuth 65.0° ENE) and Fagus along the Appalachian spine (azimuth 344.4° NNW)—with empirical population front speeds hitting a ceiling between 116.9 and 277.0 m/yr (median 169.6 m/yr). Empirical tree migration fell roughly 9.3 times slower than contemporary 21st-century climate-zone velocity (1,573.8 m/yr under 1.9 °C/century warming)."
    ),
    (
        "These empirical speed limits demonstrate that unassisted natural tree migration will fail to keep pace with contemporary anthropogenic warming across today's highly fragmented landscapes. "
        "Safeguarding future forest ecosystems requires transitioning from passive preservation to proactive, climate-informed management, including assisted population migration and the strategic conservation of continuous, topographically buffered migration corridors."
    )
]

ACKNOWLEDGEMENTS_TEXT = (
    "The authors acknowledge the Neotoma Paleoecology Database and the global community of palynologists and data contributors whose open-science archiving made this synthesis possible. "
    "We thank the creators and maintainers of the LegacyAge 1.0 dataset (Alfred Wegener Institute and PANGAEA) for providing harmonized Bayesian age-depth models, and the National Center for Atmospheric Research (NCAR) for providing the open-access TraCE-21ka transient paleoclimate model simulation archives via the Climate Data Gateway (GDEX dataset d651050). "
    "The open-source scientific Python community (NumPy, SciPy, Pandas, Matplotlib, Seaborn, python-docx, and Project Jupyter) is sincerely recognized for facilitating reproducible computational analyses."
)

DECLARATIONS = {
    "CRediT author statement": (
        "Vivek R: Conceptualization, Methodology, Software, Formal Analysis, Data Curation, Writing – Original Draft, Visualization, Project Administration. "
        "Nandan Rajesh Kamat: Methodology, Validation, Investigation, Formal Analysis, Writing – Review & Editing. "
        "Shaurya Gupta: Investigation, Resources, Data Curation, Validation, Writing – Review & Editing, Supervision."
    ),
    "Funding": "This research received no specific grant from funding agencies in the public, commercial, or not-for-profit sectors.",
    "Data Availability": "All fossil pollen datasets and modern surface analogue records are openly accessible via the Neotoma Paleoecology Database (https://www.neotomadb.org). The LegacyAge 1.0 chronological models are available via PANGAEA (https://doi.pangaea.de/10.1594/PANGAEA.931819). The TraCE-21ka paleoclimate model outputs are available from NCAR GDEX (https://doi.org/10.5065/CXB5-TV56). Processed data and Python analysis scripts generated during this study are archived in the project repository.",
    "Conflict of Interest": "The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper."
}
