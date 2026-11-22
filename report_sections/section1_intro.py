"""
section1_intro.py
Title, Authors, Abstract, Keywords, and Section 1 (Introduction) for Course ES1.101 Project 25 Report.
"""

TITLE = "Empirical Postglacial Tree Response Lags, Novel Ecosystems, and Migration Velocities across Eastern North America: A 15,000-Year Palynological Synthesis"

AUTHORS = [
    ("Vivek R", "vivek.r@research.iiit.ac.in", "1"),
    ("Nandan Rajesh Kamat", "nandan.kamat@research.iiit.ac.in", "1"),
    ("Shaurya Gupta", "shaurya.gupta@research.iiit.ac.in", "1")
]

AFFILIATION = "Department of Computer Science and Engineering & Lab for Spatial Informatics, International Institute of Information Technology, Hyderabad 500032, India"

CORRESPONDING_NOTE = "*Corresponding author: vivek.r@research.iiit.ac.in. Project 25 Final Report submitted for Course ES1.101 (Monsoon 2026)."

ABSTRACT_TEXT = (
    "Understanding how forest trees respond to rapid warming is critical for assessing forest vulnerability under current climate change. "
    "Because modern forestry plots only span a few decades, fossil pollen records paired with paleoclimate simulations provide our only direct empirical baseline of century-to-millennial forest reorganization. "
    "In this study, we evaluate 15,000 years of vegetation dynamics across Eastern North America (34°–52° N, 100°–60° W) using 69 sediment cores (1,706 temporal bins) from the Neotoma Database and TraCE-21ka climate simulations. "
    "We applied REVEALS productivity corrections, removed agricultural weeds to isolate woody trees, anchored chronologies with LegacyAge 1.0 Bayesian models, and calculated stationary response lags using first-differenced series against 1,000 Ebisuzaki surrogates. "
    "Tree genera showed significant response lags (H = 30.54, p = 0.0023) across three distinct ecological speed tiers: pioneer Larix adjusted in 750 yr, dominant canopy hardwoods took 1,500 yr, and climax seeders (Fagus, Tsuga) lagged by 2,500 yr. "
    "Non-analogue forest communities peaked at 79.0% at 14.5 ka BP under elevated seasonality, declining to an 8.0% pre-colonial baseline by 500 BP. "
    "Two-dimensional migration velocities across five verified taxa averaged 169.6 m/yr (116.9–277.0 m/yr), trailing contemporary warming velocities (1,573.8 m/yr) by 9.3×, which highlights severe migration deficits under ongoing global warming."
)

KEYWORDS = [
    "Late-Quaternary palynology",
    "Vegetation response lags",
    "No-analogue plant communities",
    "Tree migration velocity",
    "Reid's paradox",
    "TraCE-21ka paleoclimate",
    "Neotoma Paleoecology Database",
    "Assisted migration"
]

INTRO_PARAGRAPHS = [
    (
        "Human-driven climate change is shifting regional temperatures and rainfall faster than almost any period since the last ice age (IPCC 2021). "
        "Global average temperatures have risen by roughly 1.1 °C above pre-industrial levels, with projected warming of about 0.19 °C per decade (1.9 °C per century) under mid-range emissions scenarios (IPCC 2021). "
        "As climate zones shift poleward or upward in elevation, wild plants must persist locally through plasticity, adapt genetically, or track their climate envelope into newly suitable habitat (Davis 1981; Loarie et al. 2009; Corlett and Westcott 2013). "
        "For long-lived trees that take decades to reach seed-bearing maturity, tracking fast geographic shifts presents a major biological hurdle (Clark et al. 1998; Aitken and Bemmels 2016). "
        "Modern forestry surveys provide valuable local detail, but they only cover a few decades. "
        "This window is far too brief to observe demographic adjustments across multiple tree generations (Mottl et al. 2021). "
        "Fossil pollen preserved in lake sediments and peat bogs therefore provides our only empirical record of how continental tree communities responded to past climate pulses over centuries and millennia (Birks 2019; Fordham et al. 2020)."
    ),
    (
        "The transition from the Last Glacial Maximum (LGM) through the Holocene offers a natural experiment in continental biome reorganization (Williams et al. 2004; Nolan et al. 2018). "
        "Between 15,000 and 8,000 calibrated years before present (cal yr BP), the Laurentide Ice Sheet retreated, exposing fresh terrain while regional temperatures rose by over 10 °C (Liu et al. 2009; He et al. 2013). "
        "This warming was interrupted by abrupt climate oscillations, including rapid warming during the Bølling–Allerød (~14.7–12.9 ka BP), sharp cold snaps during the Younger Dryas (~12.9–11.7 ka BP), and an early Holocene cold pulse around 8.2 ka (Shuman et al. 2002; Marsicek et al. 2018). "
        "Sedimentary pollen records show that plant communities rearranged dramatically across these transitions (Prentice et al. 1991; Overpeck et al. 1992). "
        "A central debate in ecology is whether ancient forests adjusted quickly enough to stay in continuous equilibrium with shifting climates, or lagged centuries behind moving thermal zones (Webb 1986; Prentice et al. 1991; Svenning and Skov 2007; Knight et al. 2020)."
    ),
    (
        "Early equilibrium models assumed that postglacial forests tracked climate without major delays, arguing that seed dispersal, establishment, and population growth could adjust to new thermal boundaries within decades (Prentice et al. 1991; Webb 1986). "
        "In contrast, non-equilibrium theories emphasize severe biological constraints. "
        "These hurdles include juvenile maturation delays of 15 to 40 years, irregular seed-masting cycles, limited dispersal distances, slow soil development on bare till, and competitive shading from established canopy trees (Davis 1981; Clark 1998; Svenning and Skov 2007). "
        "Recent studies in eastern North America found that roughly one-third of postglacial forest communities showed noticeable disequilibrium during rapid climate shifts (Knight et al. 2020). "
        "Accurately estimating these lags requires careful statistical handling. "
        "Because long-term warming trends and postglacial pollen trends both change over millennia, raw time-series correlations easily create false positives. "
        "To evaluate lags reliably, we must convert records into stationary first-differenced series and test correlations against phase-randomized surrogate models that preserve temporal autocorrelation (Ebisuzaki 1997)."
    ),
    (
        "Another notable feature of deglacial forest dynamics was the rise of 'no-analogue' or novel plant communities, which were forest mixtures with no modern ecological counterpart (Overpeck et al. 1992; Williams et al. 2001, 2004). "
        "Between roughly 14,000 and 11,000 cal yr BP, forests across the Midwest and southern New England contained cold-adapted boreal conifers (such as Picea and Larix) growing alongside temperate deciduous hardwoods (such as Quercus, Fraxinus, and Ulmus) (Williams et al. 2004; Gill et al. 2009). "
        "The climate hypothesis argues that orbital geometry produced unique late-Pleistocene climate regimes with extreme seasonal contrast, featuring hotter summers and colder winters than today (Overpeck et al. 1992; Williams et al. 2001, 2004). "
        "Freezing winters supported boreal conifers while hot summers allowed temperate broadleaf trees to thrive in the same stands (Williams et al. 2004). "
        "In contrast, the ecological disequilibrium hypothesis suggests that individual tree species moved at different rates and that megafaunal extinctions altered browsing and fire regimes, allowing temporary novel mixtures to form before competition sorted them into modern forest zones (Gill et al. 2009). "
        "Evaluating these ideas requires tracking novel community timing using dissimilarity metrics against modern surface samples, while breaking down total dissimilarity into individual taxon contributions (Williams et al. 2004; Blois et al. 2013)."
    ),
    (
        "A third major question is how fast trees moved across geographic space and how past migration rates compare to modern climate change (Clark et al. 1998; Loarie et al. 2009; Fordham et al. 2020). "
        "Early studies suggested trees expanded northward at 100 to 1,000 m/yr after the ice melted, giving rise to 'Reid's paradox': observed expansion rates seemed far higher than could be explained by known seed dispersal distances (Clark et al. 1998; Feurdean et al. 2013). "
        "Later work showed that these early estimates were often inflated because they assumed straight northward movement, used low pollen thresholds that mistook wind-blown grains for established trees, or missed small localized populations in northern microrefugia (McLachlan et al. 2005; Gavin et al. 2014; Feurdean et al. 2013). "
        "In addition, postglacial dispersal did not follow a simple straight line. "
        "Physical landforms, like the Appalachian Mountains, major river valleys, and large proglacial lakes, channeled or blocked plant colonization routes (Blois et al. 2013). "
        "Measuring realistic migration speeds requires modeling arrival times across two-dimensional surfaces on equal-area projections and comparing empirical tree velocities directly against past and modern climate velocities (Loarie et al. 2009; Fordham et al. 2020)."
    ),
    (
        "Despite major progress in Quaternary paleoecology, three specific methodological problems still need resolution. "
        "First, previous lag studies rarely used stationary first-differencing or phase-randomized surrogate controls (Ebisuzaki 1997) to eliminate serial autocorrelation when measuring climate–vegetation lags across diverse tree genera. "
        "Second, studies of no-analogue communities often included modern surface samples contaminated with agricultural weed pollen, which artificially inflated modern dissimilarity scores, while failing to isolate the specific tree taxa driving community novelty. "
        "Third, past migration rates were rarely measured using two-dimensional planar models that distinguish true directional expansion fronts from scattered background pollen, making direct comparisons with modern warming rates difficult."
    ),
    (
        "In this study, we address these challenges by building an empirical paleoecological synthesis across Eastern North America (34°–52° N, 100°–60° W) from 15,000 to 0 cal yr BP. "
        "Combining 69 sediment cores (1,706 500-yr bins) from the Neotoma Paleoecology Database (Williams et al. 2018) with paleoclimate simulations from NCAR TraCE-21ka (Liu et al. 2009), we investigate three central questions: "
        "(1) RQ1: What were the actual response lags of different tree genera behind deglacial climate changes, and do life-history traits group taxa into distinct ecological speed tiers? "
        "(2) RQ2: When did no-analogue forest communities emerge during deglacial warming, and which tree taxa caused this novelty when compared against modern, weed-filtered surface analogues? "
        "(3) RQ3: Along what geographic pathways and at what ground speeds did trees migrate across North America, and how do empirical tree migration rates compare to modern climate velocity? "
        "Using REVEALS Relative Pollen Productivity corrections (Sugita 2007; Wieczorek and Herzschuh 2020), Bayesian age models from LegacyAge 1.0 (Li et al. 2022), and statistical significance filters, we establish an empirical baseline to evaluate whether modern forest species can keep pace with 21st-century climate warming."
    )
]
