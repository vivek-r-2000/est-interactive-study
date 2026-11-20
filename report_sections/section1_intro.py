"""
section1_intro.py - Introduction (1,000–1,200 words)
Focus of the work, motivation/rationale, literature review context, and research objectives.
"""

TITLE = "Late-Quaternary Climate–Vegetation Lags, No-Analogue Communities, and 2D Spatial Tree Migration in Eastern North America"

AUTHORS = [
    ("Vivek R", "vivek.r@research.iiit.ac.in", "1*"),
    ("Nandan Rajesh Kamat", "nandan.kamat@research.iiit.ac.in", "1"),
    ("Shaurya Gupta", "shaurya.gupta@research.iiit.ac.in", "1")
]

AFFILIATION = "Department of Computer Science and Engineering & Lab for Spatial Informatics, International Institute of Information Technology - Hyderabad, Gachibowli, Hyderabad, Telangana, 500032, India."

CORRESPONDING_NOTE = "*Corresponding Author: Vivek R; Department of Computer Science and Engineering, International Institute of Information Technology - Hyderabad, Prof. C.R. Rao Road, Gachibowli, Hyderabad, Telangana, 500032, India. Tel: +91-40-6653-1000; Email: vivek.r@research.iiit.ac.in; vivek.r@ihub-data.iiit.ac.in"

ABSTRACT_TEXT = (
    "Understanding how tree populations adjust to climate warming is central to assessing forest vulnerability under anthropogenic change. "
    "Because contemporary forestry surveys cover decades, sedimentary fossil pollen records paired with independent paleoclimate simulations provide the only empirical baseline of century-to-millennial forest reorganizations. "
    "Here, we quantify 15,000 years of vegetation dynamics across Eastern North America (34°–52° N, 100°–60° W) using 69 sediment cores (1,706 temporal bins) from the Neotoma Database and TraCE-21ka climate simulations. "
    "We applied REVEALS calibrations, restricted analysis to woody taxa to remove weed contamination, anchored chronologies to LegacyAge 1.0 Bayesian models, and evaluated stationary lags using first-differenced cross-correlations against 1,000 Ebisuzaki surrogates. "
    "Tree taxa exhibited significant response lags (H = 30.54, p = 0.0023) structured into three ecological speed tiers: pioneer Larix adjusted in 750 yr, broadleaf canopy dominants in 1,500 yr, and climax seeders (Fagus, Tsuga) in 2,500 yr. "
    "Non-analogue communities peaked at 79.0% at 14.5 ka BP under elevated seasonality before declining to an 8.0% pre-colonial floor at 500 BP. "
    "Empirical two-dimensional migration velocities across five validated taxa averaged 169.6 m/yr (116.9–277.0 m/yr), lagging late-glacial climate velocity (332.1 m/yr) and trailing contemporary warming velocities (1,573.8 m/yr) by 9.3×, indicating severe unassisted dispersal deficits under ongoing climate change."
)

KEYWORDS = [
    "Fossil pollen",
    "Vegetation phenology and lags",
    "No-analogue communities",
    "Two-dimensional tree migration",
    "TraCE-21ka simulation",
    "Eastern North America"
]

INTRO_PARAGRAPHS = [
    (
        "Anthropogenic climate change is shifting thermal and hydrological regimes at rates exceeding most postglacial warming episodes (IPCC 2021). "
        "Global surface air temperatures have increased by approximately 1.1 °C since pre-industrial times and are projected to warm at roughly 0.19 °C per decade (1.9 °C per century) under mid-range emissions scenarios (IPCC 2021). "
        "In response to shifting thermal zones, sessile organisms must persist through physiological plasticity, adapt genetically, or shift their geographic distributions poleward and upward in elevation (Davis 1981; Loarie et al. 2009; Corlett and Westcott 2013). "
        "For canopy trees requiring decades to reach reproductive maturity, tracking fast geographic shifts poses severe biological challenges (Clark et al. 1998; Aitken and Bemmels 2016). "
        "Contemporary ecological monitoring networks and forestry surveys, though rich in spatial resolution, span only several decades. "
        "They remain too brief to observe multi-generational population adjustments or demographic equilibria (Mottl et al. 2021). "
        "Consequently, sedimentary fossil pollen archives preserved in natural lakes and peatlands provide the sole empirical foundation for observing how continental-scale tree communities respond to major warming and cooling events across centuries and millennia (Birks 2019; Fordham et al. 2020)."
    ),
    (
        "The late-Quaternary transition from the Last Glacial Maximum (LGM) provides a natural experiment in biome reorganization (Williams et al. 2004; Nolan et al. 2018). "
        "Between 15,000 and 8,000 calibrated years before present (cal yr BP), the Laurentide Ice Sheet retreated across North America, exposing mineral substrate while regional mean temperatures rose by over 10 °C (Liu et al. 2009; He et al. 2013). "
        "This deglacial warming was punctuated by abrupt climatic pulses, including the rapid Bølling–Allerød warming (~14.7–12.9 ka BP), the Younger Dryas cold oscillation (~12.9–11.7 ka BP), and the early Holocene 8.2 ka cooling event (Shuman et al. 2002; Marsicek et al. 2018). "
        "Palaeoecological records demonstrate that past plant communities underwent profound structural transformations during these transitions (Prentice et al. 1991; Overpeck et al. 1992). "
        "However, whether these ancient forest reorganizations maintained continuous equilibrium with prevailing climates or lagged behind shifting isotherms by centuries has generated extensive scientific debate (Webb 1986; Prentice et al. 1991; Svenning and Skov 2007; Knight et al. 2020)."
    ),
    (
        "Classical equilibrium theory posited that postglacial vegetation tracked climatic shifts with negligible delays, assuming that seed dispersal, establishment, and population growth adjusted within decades to shifting thermal boundaries (Prentice et al. 1991; Webb 1986). "
        "In contrast, non-equilibrium perspectives argue that biological constraints—including juvenile maturation intervals of 15 to 40 years, intermittent masting cycles, limited physical seed shadows, slow postglacial soil development, and competitive canopy inertia—imposed multi-century lags on tree population expansions (Davis 1981; Clark 1998; Svenning and Skov 2007). "
        "Recent continental syntheses in eastern North America revealed that nearly one-third of postglacial plant assemblages exhibited substantial climatic disequilibrium during rapid transitions (Knight et al. 2020). "
        "Yet, rigorously quantifying these lags has been hindered by methodological artefacts. "
        "Correlating non-stationary, trending time series induces inflated significance and false-positive correlations unless series are stationary-transformed and evaluated against red-noise surrogate models that account for temporal autocorrelation (Ebisuzaki 1997)."
    ),
    (
        "A second defining feature of late-glacial forest dynamics was the emergence of 'no-analogue' or novel plant communities—assemblages possessing taxonomic compositions with no counterpart in modern vegetation (Overpeck et al. 1992; Williams et al. 2001, 2004). "
        "Between approximately 14,000 and 11,000 cal yr BP, extensive forests across the Midwestern United States and southern New England contained simultaneous co-occurrences of cold-adapted boreal conifers (such as Picea and Larix) alongside temperate deciduous hardwoods (such as Quercus, Fraxinus, and Ulmus) (Williams et al. 2004; Gill et al. 2009). "
        "The climatic hypothesis posits that unique orbital configurations produced non-analogue climate regimes characterised by elevated insolation seasonality, resulting in colder winters and warmer summers than occur today (Overpeck et al. 1992; Williams et al. 2001, 2004). "
        "Under this regime, extreme winter cold favored boreal conifers while high summer warmth enabled temperate broadleaf trees to thrive within the same regional stands (Williams et al. 2004). "
        "Conversely, the ecological disequilibrium hypothesis suggests that differential response rates and the abrupt extinction of Late-Pleistocene megaherbivores released plant species from historic browsing pressure and altered fire regimes, permitting transient, novel community recombinations before competitive exclusion restored typical forest zonation (Gill et al. 2009). "
        "Disentangling these drivers requires tracking the temporal trajectory of no-analogue assemblages using dissimilarity metrics against modern surface sample baselines, decomposed directly into individual taxon contributions (Williams et al. 2004; Blois et al. 2013)."
    ),
    (
        "A third critical issue concerns the spatial velocity of postglacial tree migration and its relation to modern climate change (Clark et al. 1998; Loarie et al. 2009; Fordham et al. 2020). "
        "Earlier palynological studies estimated that tree taxa migrated northward at rates between 100 and 1,000 m/yr following deglaciation, giving rise to 'Reid's paradox' of rapid plant migration: observed speeds appeared vastly higher than predicted by classical diffusion models based on measured seed shadows (Clark et al. 1998; Feurdean et al. 2013). "
        "Subsequent investigations revealed that earlier estimates were often inflated by one-dimensional northward assumptions, low pollen detection thresholds, and unrecognised northern microrefugia (McLachlan et al. 2005; Gavin et al. 2014; Feurdean et al. 2013). "
        "Furthermore, postglacial dispersal did not proceed along straight meridional lines. "
        "Geomorphic features—such as the Appalachian mountain spine, major river drainage networks, and proglacial lake systems—funneled, deflected, or blocked plant colonisation routes (Blois et al. 2013). "
        "Accurately determining past migration velocities requires estimating two-dimensional arrival surfaces on equal-area projections and benchmarking empirical tree velocities against past and contemporary climate velocity (Loarie et al. 2009; Fordham et al. 2020)."
    ),
    (
        "Despite substantial advances in Quaternary palynology, three major research gaps remain. "
        "First, previous lag studies rarely deployed stationary first-differencing or phase-randomized surrogate controls (Ebisuzaki 1997) to eliminate serial autocorrelation when measuring climate–vegetation lags across diverse tree genera. "
        "Second, assessments of no-analogue communities often suffered from modern agricultural pollen contamination that falsely elevated modern dissimilarity, while failing to isolate the specific taxa responsible for ancient community novelty. "
        "Third, tree migration speeds have seldom been evaluated using rigorous two-dimensional planar regression models that isolate coherent directional dispersal fronts from diffuse distributions while explicitly comparing empirical migration ceilings against contemporary anthropogenic climate velocities."
    ),
    (
        "To address these challenges, this study designs and executes a unified, reproducible palaeoecological synthesis across Eastern North America (34°–52° N, 100°–60° W) covering the period from 15,000 to 0 cal yr BP. "
        "By integrating 69 high-density sediment cores (1,706 500-yr bins) from the Neotoma Paleoecology Database (Williams et al. 2018) with the synchronously coupled NCAR TraCE-21ka transient paleoclimate simulation (Liu et al. 2009), we answer three core research questions: "
        "(1) RQ1: Do different tree genera exhibit unequal response lags behind deglacial temperature and precipitation changes, and do life-history traits structure taxa into distinct ecological speed tiers? "
        "(2) RQ2: Did rapid deglacial climate transitions induce transient no-analogue forest communities, and which specific taxa drove community novelty when evaluated against modern, weed-filtered surface analogues? "
        "(3) RQ3: What were the actual two-dimensional geographic corridors and ground velocities of postglacial tree migration, and how do empirical tree migration ceilings compare with contemporary anthropogenic climate velocity? "
        "By combining REVEALS Relative Pollen Productivity calibrations (Sugita 2007; Wieczorek and Herzschuh 2020), Bayesian age-depth models from LegacyAge 1.0 (Li et al. 2022), and rigorous statistical significance gating, this research provides an empirical baseline for understanding forest capacity to track 21st-century global climate change."
    )
]
