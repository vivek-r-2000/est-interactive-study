"""
section6_limitations_conclusions.py
Section 6 (Limitations and Future Directions) and Section 7 (Conclusions) plus Acknowledgements & Declarations
for Course ES1.101 Project 25 Report.
"""

LIMITATIONS_PARAGRAPHS = [
    (
        "While this study provides a comprehensive look at late-Quaternary forest changes, several methodological and taphonomic constraints should be recognized. "
        "First, standard light-microscopy pollen analysis identifies plant taxa primarily to the genus or family level, which masks ecological differences among individual species (Birks 2019; Dawson et al. 2016). "
        "In our dataset, Quercus includes more than 20 eastern oak species with widely varying moisture and temperature preferences (such as drought-tolerant Quercus velutina versus upland Quercus rubra). "
        "Similarly, Picea combines cold-adapted boreal black spruce (Picea mariana) with white spruce (Picea glauca) and temperate red spruce (Picea rubens). "
        "As a result, observed genus-level lags represent the combined response of several species rather than individual species shifts. "
        "Future research should pair traditional pollen analysis with sedimentary ancient DNA (sedaDNA) to identify exact species and detect small founder populations centuries before local pollen reaches the 1% detection threshold (Parducci et al. 2017)."
    ),
    (
        "Second, grouping records into 500-year time bins (which was necessary to harmonize cores with different sedimentation rates over 15,000 years) naturally smooths out rapid, sub-century environmental pulses (Mottl et al. 2021). "
        "While our 250-year sensitivity test (Table 5) confirmed that our three-tier lag pattern holds under finer binning, 500-year windows cannot capture decade-scale responses to multi-year droughts or sudden fire episodes. "
        "Testing our analytical pipeline on annually layered (varved) lake sediments, speleothems, or sub-fossil tree-ring records will be valuable for measuring decade-scale forest lags."
    ),
    (
        "Third, the spatial resolution of the TraCE-21ka climate model (~3.75° atmospheric grid, ~300 km) smooths out fine-scale, topographically sheltered microclimates (Liu et al. 2009; He 2011). "
        "In complex terrain like the Appalachian Mountains, steep north-facing ravines and sheltered river valleys provided local microclimates that allowed temperate trees to survive glacial cold in microrefugia (Gavin et al. 2014). "
        "Coarse global climate models cannot capture these small pockets, which may slightly overestimate how far trees had to migrate. "
        "Linking high-resolution regional climate models (RCMs) or downscaling methods with local elevation models will be an important next step for late-Quaternary spatial modeling."
    ),
    (
        "Finally, although our 2D planar arrival regression successfully isolated broad regional migration fronts, thin-plate splines interpolate across landscapes that may have contained unrecorded physical barriers. "
        "Combining sedimentary charcoal records of fire history, Sporormiella fungal spore counts of herbivore abundance across all 69 cores (Gill et al. 2009), and individual-based forest simulators (such as TreeMig or SORTIE) will help researchers model how climate, wildfire, seed dispersal, and competition interact under future warming scenarios."
    )
]

CONCLUSIONS_PARAGRAPHS = [
    (
        "In this study, we synthesized 15,000 years of fossil pollen records from 69 Eastern North American sediment cores alongside independent TraCE-21ka paleoclimate simulations to evaluate postglacial forest dynamics. "
        "By using REVEALS pollen productivity corrections, LegacyAge 1.0 Bayesian chronologies, stationary first-differencing, 1,000 Ebisuzaki surrogate tests, and two-dimensional planar migration models, we answered three key ecological questions:"
    ),
    (
        "1. Forests did not respond as single, unified biome units. Different tree genera responded on distinct biological schedules structured into three clear speed tiers (Kruskal–Wallis H = 30.54, p = 0.0023): pioneer tamarack (Larix) adjusted in 750 yr, nine canopy reorganization genera clustered around 1,500 yr, and heavy-seeded climax dominants (Fagus, Tsuga) lagged by 2,500 yr. Response direction separated rapid boreal dieback (Picea, 94.9% negative, mean r = -0.637) from gradual temperate hardwood expansion (Quercus, 79.1% positive)."
    ),
    (
        "2. No-analogue forest communities were a temporary phenomenon that peaked at 79.0% at 14.5 ka BP during early deglacial warming before falling to an 8.0% pre-colonial baseline by 500 BP under TRSH-only filtering. Decomposing Squared Chord Distance scores proved that community novelty was driven by unusual co-occurrences of Quercus, Alnus, Betula, Populus, and Picea, supported by extreme late-Pleistocene seasonal contrast (32.6 °C winter-summer range) and early-deglacial moisture decoupling."
    ),
    (
        "3. Postglacial tree migration followed distinct two-dimensional terrain corridors, such as Carya moving along the Ohio and Mississippi river valleys (azimuth 65.0° ENE) and Fagus following the Appalachian mountain spine (azimuth 344.4° NNW). Empirical migration speeds reached an upper limit between 116.9 and 277.0 m/yr (median 169.6 m/yr). This historical tree migration speed is roughly 9.3 times slower than projected 21st-century climate velocity (1,573.8 m/yr under 1.9 °C/century warming)."
    ),
    (
        "These empirical speed limits show that natural seed dispersal alone cannot keep pace with modern human-driven warming across today's heavily fragmented landscapes. Protecting future forests will require moving beyond passive conservation toward active, climate-informed management, including assisted population migration and the protection of continuous, topographically buffered migration pathways."
    )
]

ACKNOWLEDGEMENTS_TEXT = (
    "We thank the course instructors and teaching assistants of ES1.101 (Introduction to Environmental Sciences, Monsoon 2026) at IIIT Hyderabad for project guidance and technical feedback. "
    "We gratefully acknowledge the data contributors and database maintainers of the Neotoma Paleoecology Database and the developers of the NCAR TraCE-21ka climate simulation project. "
    "Computational analyses, Bayesian age-depth modeling, and spatial interpolations were executed using open-source Python scientific computing environments (NumPy, SciPy, Pandas, Scikit-learn, and Geopandas)."
)

DECLARATIONS = {
    "CRediT author statement": (
        "Vivek R: Conceptualization, Methodology, Software, Formal Analysis, Writing - Original Draft, Visualization. "
        "Nandan Rajesh Kamat: Data Curation, Validation, Investigation, Writing - Review & Editing. "
        "Shaurya Gupta: Software, Data Curation, Formal Analysis, Writing - Review & Editing."
    ),
    "Funding": (
        "This project was completed as part of the academic curriculum for Course ES1.101 at the International Institute of Information Technology, Hyderabad. No external funding was received."
    ),
    "Data Availability": (
        "All raw palynological count datasets are openly available from the Neotoma Paleoecology Database (https://www.neotomadb.org). "
        "TraCE-21ka climate simulation outputs are archived at the NCAR Climate Data Gateway (https://www.earthsystemgrid.org). "
        "Standardized Bayesian chronologies are accessible via the LegacyAge 1.0 PANGAEA repository (https://doi.org/10.1594/PANGAEA.933132). "
        "All analytical Python scripts, data processing workflows, and figure generation code are archived in the project repository."
    ),
    "Conflict of Interest": (
        "The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper."
    )
}
