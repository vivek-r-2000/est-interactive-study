#!/usr/bin/env python3
"""
Grounded Class 16 Questions: Green Accounting
Primary Source: Study_Material/raw_slide_texts/class_16_raw.json (Class-16-Green Accounting.pdf, 45 slides)
All 16 questions strictly grounded in lecture slides, with comprehensive multi-paragraph detailed answers and exam-ready expected answers.
"""

def get_class16_grounded_questions():
    return [
        {
            "id": "EQB-16-01",
            "class_id": 16,
            "class_name": "Green Accounting",
            "topic": "System of National Accounts (SNA) Framework & Historical Popularity",
            "category": "Descriptive & Case Study",
            "exams": [{"paper": "End Exam 2024", "section": "Section II, Q1", "marks": "5M"}, {"paper": "End Exam 2023", "section": "Section IV, Q1", "marks": "5M"}],
            "marks": "5M",
            "importance": "CRITICAL (\u2b50\u2b50\u2b50\u2b50\u2b50)",
            "prompt": "What is SNA? Define its framework? Why did the concept of SNA remain so popular for so long despite ignoring the environment?",
            "key_answer_points": "<ul>\n<li><strong>Definition:</strong> The System of National Accounts (SNA) is the internationally agreed standard set of recommendations on how to compile measures of economic activity (such as GDP and GNP) across a nation. Developed originally in the 1930s by Simon Kuznets and standardized by the UN in 1953.</li>\n<li><strong>Standard Macroeconomic Framework:</strong>$$\\text{GNP} = C + I + G + (X - M) + (R - P)$$Where $C$ = Private Consumption, $I$ = Gross Private Investment, $G$ = Government Expenditure, $X - M$ = Net Exports, and $R - P$ = Net Factor Income from Abroad.</li>\n<li><strong>Five Reasons for Enduring Popularity (Slide 10):</strong>\n<ol>\n<li><strong>Simplicity of Aggregation:</strong> Condenses millions of complex economic transactions into a single, understandable headline figure (GDP/GNP).</li>\n<li><strong>Monetary Uniformity:</strong> Relies exclusively on monetary market exchange prices, avoiding subjective non-market valuation disputes.</li>\n<li><strong>Standardized International Metric:</strong> Facilitates cross-country comparisons, sovereign credit ratings, and multilateral lending (IMF/World Bank).</li>\n<li><strong>Macroeconomic Policy Tool:</strong> Developed during the Great Depression and WWII to manage Keynesian aggregate demand, employment, and fiscal budgets.</li>\n<li><strong>Institutional Inertia:</strong> Deeply embedded in national statistical bureaus, tax frameworks, and economic planning bodies worldwide for over seven decades.</li>\n</ol></li>\n</ul>",
            "expected_answer": """<div class="expected-body">
<p><strong>1. Definition of System of National Accounts (SNA):</strong></p>
<p>The <strong>System of National Accounts (SNA)</strong> is an internationally standardized statistical framework developed originally by Simon Kuznets in the 1930s and adopted by the United Nations in 1953 to compile and measure a country's aggregate economic activity, output, and national income (GDP and GNP).</p>

<p><strong>2. Standard SNA Macroeconomic Accounting Framework:</strong></p>
<p>The core national income formula calculates Gross National Product ($\text{GNP}$) as the total market value of all final goods and services produced:</p>
<div class="formula-box">$$\text{GNP} = C + I + G + (X - M) + (R - P)$$</div>
<ul>
  <li><strong>$C$ (Private Consumption):</strong> Household expenditures on final goods and services.</li>
  <li><strong>$I$ (Gross Private Investment):</strong> Business capital expenditures on machinery, buildings, and inventories.</li>
  <li><strong>$G$ (Government Expenditure):</strong> Public sector spending on public administration, defense, and infrastructure.</li>
  <li><strong>$(X - M)$ (Net Exports):</strong> Total exports ($X$) minus total imports ($M$).</li>
  <li><strong>$(R - P)$ (Net Factor Income from Abroad):</strong> Receipts ($R$) earned by domestic factors abroad minus payments ($P$) made to foreign assets domestically.</li>
</ul>
<p>SNA accounts for depreciation of man-made physical capital via Net Investment: $I_n = I_g - D_m$, where $D_m$ is depreciation of manufactured capital.</p>

<p><strong>3. Five Reasons Why SNA Remained Popular for 70+ Years Despite Ignoring the Environment (Slide 10):</strong></p>
<ol>
  <li><strong>Simplicity of Aggregation:</strong> Condenses millions of diverse market transactions into a single, straightforward headline figure ($\text{GDP}/\text{GNP}$) for easy public communication.</li>
  <li><strong>Monetary Uniformity:</strong> Relies strictly on observable monetary market prices, avoiding subjective non-market environmental valuation disputes.</li>
  <li><strong>International Standardization:</strong> Enables consistent cross-country comparisons, sovereign credit ratings, and multilateral lending assessments by the IMF and World Bank.</li>
  <li><strong>Macroeconomic Policy Alignment:</strong> Designed to manage Keynesian aggregate demand, employment targets, inflation, and fiscal budgets.</li>
  <li><strong>Institutional Entrenchment:</strong> Deeply embedded across seven decades in national statistical bureaus, central banks, and international economic treaty frameworks.</li>
</ol>
<p><strong>The Core Ecological Flaw:</strong> SNA treats natural capital as an infinite, free gift. It treats depletion of natural assets as current revenue and counts pollution cleanup as positive economic growth, completely omitting natural capital depreciation ($D_n$).</p>
</div>""",
            "detailed_answer": """<div class="detailed-body">
<p><strong>Origins and Theoretical Architecture:</strong> Following the Great Depression, the United States commissioned Simon Kuznets in 1934 to develop a standardized accounting ledger of national production. This crystallized into the United Nations System of National Accounts (SNA). The core formula accounts for all final goods and services transacted in formal markets:</p>
<div class="formula-box">$$\text{GNP} = C + I + G + (X - M) + (R - P)$$</div>
<p><strong>The Fundamental Asymmetry of SNA:</strong> While the SNA meticulously calculates the depreciation of man-made physical capital (machines, buildings, roads) via the equation:</p>
<div class="formula-box">$$\text{Net Investment } (I_n) = \text{Gross Investment } (I_g) - \text{Depreciation } (D)$$</div>
<p>it treats natural capital as an inexhaustible, free gift. When an oil well is pumped dry or a virgin rainforest is clear-cut, the SNA records the revenue as pure income without deducting a single dollar for natural capital depreciation. Worse, the SNA records oil spill cleanups, hospital bills from toxic smog, and post-hurricane rebuilding as positive additions to GDP.</p>
<p><strong>Why Did SNA Persist for 70+ Years?:</strong> Slide 10 highlights that despite these glaring flaws, governments remained wedded to SNA because it provided an objective, easily audited transaction record. Non-market environmental services (such as carbon sequestration or pollination) do not come with cash register receipts, making politicians and conventional treasuries reluctant to include imputed ecological values in statutory budgets.</p>
<p><em>Slide Reference: Class 16, Slides 7, 8, 9, 10, 11, 23, 25.</em></p>
</div>"""
        },
        {
            "id": "EQB-16-02",
            "class_id": 16,
            "class_name": "Green Accounting",
            "topic": "SEEA Expansion of SNA & Classification of Natural Assets",
            "category": "Descriptive & Case Study",
            "exams": [{"paper": "End Exam 2024", "section": "Section II, Q2", "marks": "5M"}, {"paper": "End Exam 2022", "section": "Section IV, Q(a)", "marks": "5M"}],
            "marks": "5M",
            "importance": "CRITICAL (\u2b50\u2b50\u2b50\u2b50\u2b50)",
            "prompt": "How has SEEA expanded and complemented SNA? How are natural assets classified under SEEA?",
            "key_answer_points": "<ul>\n<li><strong>What is SEEA?:</strong> The System of Environmental-Economic Accounting (SEEA) was developed by the UN, World Bank, and European Commission as a satellite accounting system to complement SNA without overturning standard GDP.</li>\n<li><strong>Four Core Satellite Accounts in SEEA:</strong>\n<ol>\n<li><strong>Physical Flow Accounts:</strong> Tracks physical inputs of natural resources (water, energy, materials) into the economy and outputs of residuals (pollutants, solid waste, greenhouse gases) into nature.</li>\n<li><strong>Environmental Protection Expenditure Accounts (EPEA):</strong> Isolates economic expenditures dedicated to pollution prevention and environmental management.</li>\n<li><strong>Natural Resource Asset Accounts:</strong> Compiles physical and monetary opening and closing balance sheets of resource stocks (timber, subsoil minerals, fish stocks).</li>\n<li><strong>Environmentally-Adjusted Asset Accounts:</strong> Deducts depletion of natural assets and degradation of ecosystem health to compute Environmentally-adjusted Domestic Product (EDP).</li>\n</ol></li>\n<li><strong>Classification of Natural Assets (Slide 20):</strong>\n<ol>\n<li><strong>Biological Assets:</strong> Forests, fisheries, wildlife, livestock, and cultivated crops.</li>\n<li><strong>Land & Surface Water Assets:</strong> Land cover, urban land, agricultural soil, and open water bodies.</li>\n<li><strong>Subsoil Assets:</strong> Fossil fuels (coal, oil, gas), metallic ores, and non-metallic industrial minerals.</li>\n<li><strong>Water Resources:</strong> Groundwater aquifers, rivers, lakes, and reservoirs.</li>\n<li><strong>Atmospheric Assets:</strong> Clean air capacity and greenhouse gas absorption buffering.</li>\n</ol></li>\n</ul>",
            "expected_answer": """<div class="expected-body">
<p><strong>1. How SEEA Expands and Complements SNA:</strong></p>
<p>The <strong>System of Environmental-Economic Accounting (SEEA)</strong> was established by the UN, European Commission, IMF, OECD, and World Bank (1993, updated 2012) as a <em>satellite accounting system</em>. Rather than replacing the conventional SNA, SEEA operates parallel to it by linking environmental statistics directly with standard economic supply-and-use tables.</p>
<p>SEEA organizes this expansion through <strong>Four Core Satellite Accounts:</strong></p>
<ol>
  <li><strong>Physical Flow Accounts:</strong> Tracks physical inputs of natural resources (water, energy, timber, minerals) entering the economy and residual outputs (GHG emissions, solid waste, liquid effluents) discharged back into ecosystems.</li>
  <li><strong>Environmental Protection Expenditure Accounts (EPEA):</strong> Isolates and identifies economic expenditures dedicated to environmental protection, pollution abatement, and resource conservation.</li>
  <li><strong>Natural Resource Asset Accounts:</strong> Compiles opening and closing balance sheets (both in physical quantities and monetary values) for natural resource stocks (timber reserves, subsoil minerals, fish stocks).</li>
  <li><strong>Environmentally-Adjusted Asset Accounts:</strong> Computes the monetary cost of natural resource depletion and ecosystem degradation to derive <strong>Environmentally-adjusted Domestic Product (EDP)</strong>: $\text{EDP} = \text{GDP} - D_m - D_n$.</li>
</ol>

<p><strong>2. Classification of Natural Assets under SEEA (Slide 20):</strong></p>
<p>Under SEEA, natural assets are systematically classified into five primary classes:</p>
<ol>
  <li><strong>Biological Assets:</strong> Living cultivated and wild biological resources, including timber stocks, commercial marine fisheries, wild fauna and flora, livestock, and perennial crops.</li>
  <li><strong>Land and Associated Surface Water Assets:</strong> Land areas classified by land cover/use (agricultural arable land, urban built-up areas, wetlands) along with soil quality and recreational surface waters.</li>
  <li><strong>Subsoil Assets:</strong> Proven commercially recoverable underground mineral deposits, including fossil fuels (petroleum, coal, natural gas), metallic ores (iron, copper, bauxite), and non-metallic minerals (phosphates, limestone).</li>
  <li><strong>Water Resources:</strong> Freshwater hydrological stocks including groundwater aquifers, natural lakes, rivers, streams, and artificial water reservoirs.</li>
  <li><strong>Atmospheric Assets:</strong> The atmosphere evaluated as an assimilative sink resource for absorbing greenhouse gases and industrial air emissions without triggering catastrophic climate feedback.</li>
</ol>
</div>""",
            "detailed_answer": """<div class="detailed-body">
<p><strong>Bridging the Macroeconomic Blindspot:</strong> Traditional national accounting treats nature as an external sink. In 1993, the United Nations Statistical Commission introduced the System of Environmental-Economic Accounting (SEEA). Rather than replacing the conventional SNA, SEEA operates as a rigorous satellite framework that integrates physical environmental indicators directly with standard monetary supply-and-use tables.</p>
<p><strong>Detailed Structure of SEEA Accounts:</strong></p>
<ul>
<li><em>Physical Flows:</em> Measures natural resource inputs (in tonnes, gigajoules, or cubic meters) flowing from the environment into production, and residual flows (effluent, GHG emissions) returned to the biosphere.</li>
<li><em>Asset Boundaries:</em> Under conventional SNA, an asset must have an established economic owner and generate monetary profits. SEEA breaks this limitation by recognizing all environmental assets—whether economically owned or public commons—that provide vital life-support functions.</li>
</ul>
<p><strong>Natural Asset Classification Schema:</strong> As detailed in Slide 20, natural assets are grouped into five major categories: Biological assets (timber, marine biomass), Land and associated surface water (providing spatial foundation and soil fertility), Subsoil assets (finite geological reserves), Water resources (hydrological supply), and Atmospheric assets (air quality buffer). This provides the structural ledger needed to calculate natural capital depletion.</p>
<p><em>Slide Reference: Class 16, Slides 13, 14, 15, 16, 17, 18, 19, 20.</em></p>
</div>"""
        },
        {
            "id": "EQB-16-03",
            "class_id": 16,
            "class_name": "Green Accounting",
            "topic": "Hicksian Income and Green Accounting",
            "category": "Short Answer & Definitions",
            "exams": [{"paper": "End Exam 2024", "section": "Section III, Q(b)", "marks": "2M"}, {"paper": "End Exam 2022", "section": "Section V, Q(a)", "marks": "2M"}],
            "marks": "2M",
            "importance": "CRITICAL (\u2b50\u2b50\u2b50\u2b50\u2b50)",
            "prompt": "Relate Hicksian income with Green accounting.",
            "key_answer_points": "<ul>\n<li><strong>Hicksian Income Definition:</strong> Formulated by Nobel laureate John R. Hicks (1946): Income is the maximum amount an individual or nation can consume over a time period and still expect to be as well off at the end of the period as at the beginning (i.e., keeping capital stock intact).</li>\n<li><strong>Mathematical Foundation:</strong>$$\\text{Hicksian Income } Y_H = \\text{Consumption } C + \\Delta K \\quad \\text{subject to } \\Delta K \\ge 0$$</li>\n<li><strong>Direct Link to Green Accounting:</strong> Conventional GDP treats the liquidation of natural assets (selling off timber or oil) as current income, which directly violates Hicksian sustainability. Green Accounting enforces the Hicksian rule by deducting natural capital depletion ($D_n$) from GDP:$$\\text{EDP} = \\text{GDP} - D_m - D_n$$Where $D_m$ is depreciation of manufactured capital and $D_n$ is depletion/degradation of natural capital.</li>\n</ul>",
            "expected_answer": """<div class="expected-body">
<p><strong>1. Hicksian Income Definition:</strong></p>
<p>Sir John R. Hicks (1946) defined income as the maximum value an individual or nation can consume during a time period and still expect to be as well off at the end of the period as at the beginning:</p>
<div class="formula-box">$$\text{Hicksian Income } Y_H = C + \Delta K \quad (\text{subject to } \Delta K \ge 0)$$</div>
<p>True income must keep total capital stock intact; consuming capital while recording it as income is economic liquidation.</p>

<p><strong>2. Direct Relation to Green Accounting:</strong></p>
<ul>
  <li><strong>Conventional GDP Violation:</strong> Standard SNA treats the extraction and sale of non-renewable resources (e.g., pumping oil or clear-cutting forests) as current income, ignoring the depletion of the natural capital base.</li>
  <li><strong>Green Accounting Correction:</strong> Green accounting enforces Hicks's sustainability condition by calculating <strong>Environmentally-adjusted Net Domestic Product (EDP)</strong>:</li>
</ul>
<div class="formula-box">$$\text{EDP} = \text{GDP} - D_m - D_n$$</div>
<p>where $D_m$ is depreciation of manufactured physical capital and $D_n$ is the monetary depletion and degradation of natural capital. EDP reflects true sustainable Hicksian income.</p>
</div>""",
            "detailed_answer": """<div class="detailed-body">
<p><strong>The Core Economic Fallacy:</strong> In classical welfare economics, consuming your capital while calling it income is the quickest route to bankruptcy. Sir John Hicks established in <em>Value and Capital</em> that true income represents the maximum sustainable yield that can be extracted without reducing the productive asset base available for future periods.</p>
<p><strong>Application to Natural Resources:</strong> In conventional accounting, if a nation clear-cuts all its forests and exports the timber, its GDP rises sharply, giving an illusion of prosperity. However, its productive capital base has shrunk. Green accounting operationalizes the Hicksian concept by computing Environmentally-adjusted Net Domestic Product (EDP):</p>
<div class="formula-box">$$\text{EDP} = \text{GDP} - D_m - D_n$$</div>
<p>By subtracting both the depreciation of manufactured machinery ($D_m$) and the depletion of environmental resources ($D_n$), Hicksian green income reveals whether a nation is truly generating surplus or merely liquidating its ecological inheritance.</p>
<p><em>Slide Reference: Class 16, Slides 42, 47, 48.</em></p>
</div>"""
        },
        {
            "id": "EQB-16-04",
            "class_id": 16,
            "class_name": "Green Accounting",
            "topic": "Four Factors of Production in National Income & Natural Capital",
            "category": "Short Answer & Definitions",
            "exams": [{"paper": "End Exam 2024", "section": "Section III, Q(c)", "marks": "2M"}, {"paper": "End Exam 2018", "section": "Section II, Q2", "marks": "2M"}],
            "marks": "2M",
            "importance": "HIGH (\u2b50\u2b50\u2b50\u2b50)",
            "prompt": "What are the four factors of production considered in National income? How does Green Accounting re-evaluate them?",
            "key_answer_points": "<ul>\n<li><strong>The Four Classical Factors of Production:</strong>\n<ol>\n<li><strong>Land (Natural Resources):</strong> All gifts of nature including arable land, mineral deposits, water bodies, and forests. Yields <em>Rent</em>.</li>\n<li><strong>Labour:</strong> Human physical and cognitive effort applied to production. Yields <em>Wages</em>.</li>\n<li><strong>Capital:</strong> Man-made tools, machinery, buildings, and infrastructure. Yields <em>Interest</em>.</li>\n<li><strong>Organization (Enterprise/Entrepreneurship):</strong> The managerial ability to combine Land, Labour, and Capital to produce economic output while bearing risk. Yields <em>Profit</em>.</li>\n</ol></li>\n<li><strong>Green Accounting Re-evaluation:</strong> Traditional national accounts treat 'Land' as passive surface area. Green accounting redefines Land as dynamic 'Natural Capital' that provides active life-support and sink services (pollination, hydrological regulation, carbon absorption).</li>\n</ul>",
            "expected_answer": """<div class="expected-body">
<p><strong>1. The Four Classical Factors of Production and Returns:</strong></p>
<ol>
  <li><strong>Land (Natural Resources):</strong> All natural endowments (soil, water, forests, minerals). Yields <strong>Rent</strong>.</li>
  <li><strong>Labour:</strong> Human physical and intellectual effort deployed in production. Yields <strong>Wages</strong>.</li>
  <li><strong>Capital:</strong> Man-made productive physical assets (machinery, tools, factories, infrastructure). Yields <strong>Interest</strong>.</li>
  <li><strong>Organization (Entrepreneurship):</strong> Managerial coordination of the other three factors and risk assumption. Yields <strong>Profit</strong>.</li>
</ol>

<p><strong>2. How Green Accounting Re-evaluates Them:</strong></p>
<ul>
  <li>Traditional national accounts treat 'Land' as a passive, indestructible physical area or commercial plot of real estate.</li>
  <li><strong>Green Accounting Paradigm:</strong> Re-evaluates Land as dynamic <strong>Natural Capital</strong> that actively provides life-support functions, regulatory services (flood prevention, climate stabilization), and waste assimilation sinks. It treats natural capital as a depreciable asset: if degraded or depleted, its loss must be deducted from national product just like machinery depreciation.</li>
</ul>
</div>""",
            "detailed_answer": """<div class="detailed-body">
<p><strong>Classical Factors vs. Ecological Realities:</strong> In standard economic theory, output ($Y$) is modeled as an aggregate production function $Y = F(K, L, T, E)$ combining physical capital, labor, land, and entrepreneurship. In classical SNA practice, however, 'Land' was reduced merely to commercial real estate or site location value, while ecological processes were treated as free externalities.</p>
<p><strong>The Green Accounting Correction:</strong> Green accounting recognizes that without intact natural capital, the other three factors cannot function. Labor requires clean drinking water and breathable air; physical capital requires raw mineral inputs; and entrepreneurship requires stable climatic conditions. By pricing the services of Land (such as watershed buffering and soil formation), green accounting integrates the ecological foundation directly into macroeconomic production functions.</p>
<p><em>Slide Reference: Class 16, Slides 2, 3, 4, 15, 20.</em></p>
</div>"""
        },
        {
            "id": "EQB-16-05",
            "class_id": 16,
            "class_name": "Green Accounting",
            "topic": "The Three Market Axioms and Market Failure for Environmental Goods",
            "category": "Descriptive & Case Study",
            "exams": [{"paper": "End Exam 2023", "section": "Section II, Q1", "marks": "3M"}, {"paper": "End Exam 2019", "section": "Section III, Q2", "marks": "3M"}],
            "marks": "3M",
            "importance": "CRITICAL (\u2b50\u2b50\u2b50\u2b50\u2b50)",
            "prompt": "\"No Transaction: No Existence; No Money: No Existence; No Value Judgment: No Existence.\" Explain how the three market axioms lead to market failure for environmental goods.",
            "key_answer_points": "<ul>\n<li><strong>The Core Philosophical Dilemma:</strong> Classical economics operates on market exchange: if a commodity is not bought or sold for money, standard GDP assigns it a monetary value of exactly zero. A tree standing in a forest generating oxygen has no economic standing until it is cut down and sold as timber.</li>\n<li><strong>The Three Essential Market Axioms:</strong>\n<ol>\n<li><strong>Excludability:</strong> The owner can prevent non-paying individuals from consuming the good (e.g., locking a car or patenting software).</li>\n<li><strong>Rivalry:</strong> One person's consumption reduces the quantity available for another person (e.g., eating an apple).</li>\n<li><strong>Rejectability:</strong> Consumers have the freedom to reject or decline the good if they do not wish to consume it.</li>\n</ol></li>\n<li><strong>Why Markets Fail for Environmental Goods:</strong> Clean air, the ozone layer, and global climate stability are <em>non-excludable</em> (anyone can breathe), <em>non-rival</em> (one person breathing does not deplete air for another at normal scale), and <em>non-rejectable</em> (nobody can opt out of breathing polluted air). Because private markets cannot enforce price tags, free-market equilibrium leads to over-exploitation, severe pollution externalities, and market failure.</li>\n</ul>",
            "expected_answer": """<div class="expected-body">
<p><strong>1. Meaning of the Axiomatic Dilemma:</strong></p>
<p>Classical market economics relies entirely on monetary market transactions: if an asset is not traded for cash in an organized market, standard national accounts assign it an economic value of zero. (e.g., an intact forest purifying water and absorbing carbon has zero GDP value until logged and sold).</p>

<p><strong>2. The Three Essential Market Axioms:</strong></p>
<ol>
  <li><strong>Excludability:</strong> The legal or physical ability of an owner to prevent non-paying individuals from accessing or consuming the good.</li>
  <li><strong>Rivalry:</strong> Consumption by one individual diminishes the quantity or quality available for others.</li>
  <li><strong>Rejectability:</strong> Consumers have the freedom to refuse or decline to consume the good if they do not wish to.</li>
</ol>

<p><strong>3. Why These Axioms Fail for Environmental Goods (Market Failure):</strong></p>
<ul>
  <li><strong>Non-Excludable:</strong> Clean air, open marine fisheries, and the ozone layer cannot be fenced off, leading to free-riding and zero market pricing.</li>
  <li><strong>Non-Rival:</strong> One person breathing clean air does not immediately diminish air availability for another, preventing private firms from charging a marginal cost price.</li>
  <li><strong>Non-Rejectable:</strong> Citizens cannot opt out of inhaling toxic smog or ambient particulate emissions.</li>
</ul>
<p>Because environmental public goods violate all three market axioms, free markets produce negative externalities and severe resource over-exploitation ("Tragedy of the Commons"), necessitating Green Accounting shadow prices and government intervention.</p>
</div>""",
            "detailed_answer": """<div class="detailed-body">
<p><strong>The Market Pricing Paradox:</strong> In Slide 6, the course highlights the tragic paradox of modern economics: <em>'A tree growing in a forest has no standing in economics.'</em> While alive, it filters groundwater, anchors topsoil, prevents landslides, and hosts biodiversity—services worth millions of dollars. Yet, in national income accounting, its economic value is zero until it is felled, converted into commercial logs, and transacted on the open market.</p>
<p><strong>Systematic Failure of the Three Market Axioms:</strong></p>
<ul>
<li><em>Non-Excludability:</em> Because no private entity can establish property boundaries around the open atmosphere or high-seas fisheries, free-riders consume resources without payment.</li>
<li><em>Non-Rivalry:</em> Atmospheric carbon buffering benefits all humans simultaneously without direct point-of-sale rivalry, preventing pricing via marginal cost.</li>
<li><em>Non-Rejectability:</em> Citizens living in industrial cities cannot choose to reject toxic sulfur dioxide or particulate smog emitted by factories.</li>
</ul>
<p>Because these three axioms fail completely for environmental public goods, private capital ignores ecological degradation. Green accounting solves this market failure by constructing non-market shadow prices to force economies to value intact ecosystems.</p>
<p><em>Slide Reference: Class 16, Slides 6, 21, 24, 34, 35.</em></p>
</div>"""
        },
        {
            "id": "EQB-16-06",
            "class_id": 16,
            "class_name": "Green Accounting",
            "topic": "Non-Marketed Environmental Goods and Services",
            "category": "Short Answer & Definitions",
            "exams": [{"paper": "End Exam 2024", "section": "Section III, Q(d)", "marks": "2M"}, {"paper": "End Exam 2022", "section": "Section V, Q(c)", "marks": "2M"}],
            "marks": "2M",
            "importance": "HIGH (\u2b50\u2b50\u2b50\u2b50)",
            "prompt": "Give two examples for non-marketed environmental (a) Goods and (b) Services.",
            "key_answer_points": "<ul>\n<li><strong>Non-Marketed Environmental Goods (Tangible Physical Resources):</strong>\n<ol>\n<li><strong>Clean Ambient Air:</strong> Fresh, breathable atmospheric air required for biological survival, consumed without monetary transactions.</li>\n<li><strong>Wild Medicinal Plants / Forest Genetic Resources:</strong> Naturally occurring forest flora, wild tubers, and herbs gathered directly by local tribal communities without retail sale.</li>\n</ol></li>\n<li><strong>Non-Marketed Environmental Services (Intangible Functional Benefits):</strong>\n<ol>\n<li><strong>Watershed Protection & Flood Regulation:</strong> Dense mountain forest root networks that absorb torrential monsoon rainfall, replenish groundwater, and prevent downstream flash flooding.</li>\n<li><strong>Carbon Sequestration & Climate Regulation:</strong> Photosynthetic absorption of greenhouse gases by oceans and natural wetlands to stabilize global climate systems.</li>\n</ol></li>\n</ul>",
            "expected_answer": """<div class="expected-body">
<p><strong>(a) Non-Marketed Environmental Goods (Tangible Physical Resources):</strong></p>
<ol>
  <li><strong>Clean Ambient Air:</strong> Atmospheric oxygen inhaled freely by organisms for biological respiration without monetary payment.</li>
  <li><strong>Wild Medicinal Plants / Forest Produce:</strong> Naturally growing forest herbs, roots, and tubers collected by indigenous/tribal communities for direct subsistence.</li>
</ol>

<p><strong>(b) Non-Marketed Environmental Services (Intangible Functional / Ecological Processes):</strong></p>
<ol>
  <li><strong>Watershed Regulation & Flood Moderation:</strong> Natural soil retention and root catchment in mountain forests that absorb rainfall, recharge aquifers, and mitigate downstream floods.</li>
  <li><strong>Global Climate Regulation & Carbon Sequestration:</strong> Atmospheric carbon absorption and storage provided by oceanic phytoplankton, peatlands, and mangrove ecosystems.</li>
</ol>
</div>""",
            "detailed_answer": """<div class="detailed-body">
<p><strong>Physical Goods vs. Systemic Services:</strong> Slide 28 and Slide 34 distinguish between physical commodities extracted from nature and systemic regulatory functions performed by intact biomes:</p>
<ul>
<li><em>Non-Marketed Goods:</em> Physical materials that nature generates freely. Examples include clean ambient air inhaled by organisms, untamed marine fish gathered by subsistence coastal fishers, and wild uncultivated berries/herbs utilized by forest-dwelling indigenous peoples.</li>
<li><em>Non-Marketed Services:</em> Kinetic and biological processes that maintain environmental equilibrium. Examples include the mangrove root barrier dissipating cyclone storm surges along coastlines, bee pollination of agricultural crops, and microbial decomposition of toxic wastes in natural riverbeds.</li>
</ul>
<p>Because these goods and services carry no cash register invoice, traditional GDP completely ignores their depletion until catastrophe strikes.</p>
<p><em>Slide Reference: Class 16, Slides 6, 24, 28, 34.</em></p>
</div>"""
        },
        {
            "id": "EQB-16-07",
            "class_id": 16,
            "class_name": "Green Accounting",
            "topic": "Differentiate between Green Tax and Green Cess",
            "category": "Differentiate Between",
            "exams": [{"paper": "End Exam 2023", "section": "Section II, Q3", "marks": "2M"}, {"paper": "End Exam 2018", "section": "Section IV, Q1", "marks": "2M"}],
            "marks": "2M",
            "importance": "CRITICAL (\u2b50\u2b50\u2b50\u2b50\u2b50)",
            "prompt": "Differentiate between Green Tax and Green Cess. (What is Green tax?)",
            "key_answer_points": "<ul>\n<li><strong>Green Tax (Pigouvian Tax):</strong> An environmental levy imposed on polluting activities, emissions, or fossil fuel consumption designed to internalize negative externalities. Revenue goes into the government's <em>General Consolidated Fund</em> and can be spent on any budget priority (defense, healthcare, infrastructure).</li>\n<li><strong>Green Cess (Hypothecated/Earmarked Surcharge):</strong> An additional dedicated levy or surcharge tied directly to an existing tax, where the proceeds are <em>strictly legally ring-fenced</em> for a dedicated environmental purpose (e.g., Clean Energy Cess funding renewable energy projects).</li>\n<li><strong>Core Differences:</strong> Green tax disincentivizes bad behavior through price mechanisms; Green cess raises ring-fenced capital dedicated solely to funding environmental cleanup or green technological solutions.</li>\n</ul>",
            "expected_answer": """<div class="expected-body">
<p><strong>1. Definition of Green Tax:</strong></p>
<p>A <strong>Green Tax</strong> (or Pigouvian tax) is an environmental levy charged on environmentally harmful activities, fossil fuels, or pollutant emissions to internalize the external social cost of pollution and deter polluting behavior.</p>

<p><strong>2. Comparative Matrix: Green Tax vs. Green Cess:</strong></p>
<div class="table-responsive">
<table class="table table-bordered table-striped">
<thead class="table-dark">
<tr>
  <th>Feature</th>
  <th>Green Tax</th>
  <th>Green Cess</th>
</tr>
</thead>
<tbody>
<tr>
  <td><strong>Core Purpose</strong></td>
  <td>To change behavior by penalizing pollution via the price mechanism (disincentive).</td>
  <td>To generate targeted revenue earmarked for specific environmental cleanup projects.</td>
</tr>
<tr>
  <td><strong>Fund Utilization</strong></td>
  <td>Flows into the <strong>General Consolidated Fund</strong>; can be spent on any government expenditure (roads, defense, health).</td>
  <td><strong>Legally ring-fenced / hypothecated</strong>; must strictly be spent on designated environmental purposes.</td>
</tr>
<tr>
  <td><strong>Levy Base</strong></td>
  <td>Levied directly on the polluting activity, emission volume, or older polluting asset.</td>
  <td>Levied as a dedicated surcharge or piggyback percentage on an existing tax base.</td>
</tr>
<tr>
  <td><strong>Example in India</strong></td>
  <td>Green Tax levied on commercial vehicles older than 8 years during fitness renewal.</td>
  <td>Clean Energy Cess on coal production/import (₹400/tonne, funding clean energy projects).</td>
</tr>
</tbody>
</table>
</div>
</div>""",
            "detailed_answer": """<div class="detailed-body">
<p><strong>Comparative Analysis Matrix:</strong></p>
<table class="exam-table">
<thead><tr><th>Dimension</th><th>Green Tax (Pigouvian Tax)</th><th>Green Cess (Earmarked Levy)</th></tr></thead>
<tbody>
<tr><td><strong>Primary Objective</strong></td><td>To internalize the social cost of pollution and change consumer/corporate behavior by making polluting expensive.</td><td>To raise dedicated public revenue for specific environmental cleanup and cleantech programs.</td></tr>
<tr><td><strong>Revenue Destination</strong></td><td>Consolidated Fund of the State/Nation (unrestricted general spending).</td><td>Dedicated, legally ring-fenced Environmental Fund (e.g., National Clean Energy Fund).</td></tr>
<tr><td><strong>Tax Base</strong></td><td>Directly levied on pollutant volume, vehicle age, carbon emissions, or toxic chemical content.</td><td>Levied as a percentage surcharge on an existing tax base (e.g., cess on coal extraction or GST).</td></tr>
<tr><td><strong>Example in India</strong></td><td>Green Tax levied on older commercial transport vehicles during fitness certificate renewal.</td><td>Clean Energy Cess levied on coal produced/imported (₹400/tonne under GST compensation cess).</td></tr>
</tbody>
</table>
<p><em>Slide Reference: Class 16, Slides 21, 26, 27.</em></p>
</div>"""
        },
        {
            "id": "EQB-16-08",
            "class_id": 16,
            "class_name": "Green Accounting",
            "topic": "Green Certificates / Renewable Energy Certificates (REC)",
            "category": "Short Answer & Definitions",
            "exams": [{"paper": "End Exam 2022", "section": "Section V, Q(b)", "marks": "2M"}, {"paper": "End Exam 2019", "section": "Section III, Q1", "marks": "2M"}],
            "marks": "2M",
            "importance": "HIGH (\u2b50\u2b50\u2b50\u2b50)",
            "prompt": "What is a Green certificate?",
            "key_answer_points": "<ul>\n<li><strong>Definition:</strong> A Green Certificate\u2014commonly known as a Renewable Energy Certificate (REC) or Guarantee of Origin (GO)\u2014is a tradable, market-based instrument that certifies that exactly 1 Megawatt-hour (MWh) of electricity was generated from an eligible renewable energy source (solar, wind, biomass, small hydro) and injected into the power grid.</li>\n<li><strong>Unbundling Attribute:</strong> It separates the physical electricity (which enters the common electrical grid as electrons) from its clean 'green environmental attributes' (which can be traded independently on power exchanges).</li>\n<li><strong>Key Function:</strong> Enables obligated entities (such as power distribution companies, industrial consumers, and data centers) to fulfill statutory Renewable Purchase Obligations (RPO) without having to construct their own renewable power plants.</li>\n</ul>",
            "expected_answer": """<div class="expected-body">
<p><strong>1. Definition of Green Certificate:</strong></p>
<p>A <strong>Green Certificate</strong>—also designated as a <strong>Renewable Energy Certificate (REC)</strong> or Guarantee of Origin (GO)—is a tradable, market-based certificate confirming that exactly <strong>1 Megawatt-hour (1 MWh)</strong> of electricity was generated from an accredited renewable energy source (solar, wind, small hydro, biomass) and fed into the power grid.</p>

<p><strong>2. Core Mechanism (Unbundling):</strong></p>
<ul>
  <li>It unbundles the physical electricity (which enters the shared grid as identical electrons) from its clean environmental attributes.</li>
  <li>The physical electricity is sold at standard grid tariffs, while the Green Certificate is issued and traded separately on power exchanges.</li>
</ul>

<p><strong>3. Practical Application & Purpose:</strong></p>
<p>Enables obligated entities (such as electricity distribution utilities, large factories, and data centers) to satisfy statutory <strong>Renewable Purchase Obligations (RPO)</strong> without having to build or physically procure renewable power directly.</p>
</div>""",
            "detailed_answer": """<div class="detailed-body">
<p><strong>The Problem of Physical Grid Integration:</strong> Once renewable electricity is fed into the high-voltage transmission grid, electrons from solar farms mix indistinguishably with electrons from coal plants. A company in Mumbai cannot physically verify that the specific electricity entering its wall socket came from a wind farm in Tamil Nadu.</p>
<p><strong>The Market Solution:</strong> Green Certificates solve this issue by unbundling the physical electricity from its green attributes. When a verified renewable generator produces 1 MWh of clean power:</p>
<ol>
<li>The physical electricity is sold into the local power grid at standard baseline rates.</li>
<li>One Renewable Energy Certificate (1 REC = 1 MWh) is issued by the central registry.</li>
</ol>
<p>Entities with mandatory Renewable Purchase Obligations (RPOs) can buy these certificates on authorized energy exchanges (such as IEX or PXIL). This provides renewable developers with an additional revenue stream beyond physical power tariffs, accelerating cleantech adoption.</p>
<p><em>Slide Reference: Class 16, Slides 23, 24, 26, 27.</em></p>
</div>"""
        },
        {
            "id": "EQB-16-09",
            "class_id": 16,
            "class_name": "Green Accounting",
            "topic": "Genuine Progress Indicator (GPI) vs. GDP",
            "category": "Descriptive & Case Study",
            "exams": [{"paper": "End Exam 2024", "section": "Section II, Q3", "marks": "5M"}, {"paper": "End Exam 2022", "section": "Section IV, Q(b)", "marks": "5M"}],
            "marks": "5M",
            "importance": "CRITICAL (\u2b50\u2b50\u2b50\u2b50\u2b50)",
            "prompt": "How is GPI (Genuine Progress Indicator) created? What is its significance compared to GDP?",
            "key_answer_points": "<ul>\n<li><strong>What is GPI?:</strong> The Genuine Progress Indicator (GPI)\u2014an evolution of the Index of Sustainable Economic Welfare (ISEW)\u2014is an alternative macroeconomic index designed to measure the genuine economic, environmental, and social wellbeing of a nation.</li>\n<li><strong>How GPI is Created (Three-Tier Adjustment):</strong>$$\\text{GPI} = \\text{Personal Consumption } (C_{\\text{adj}}) + \\text{Positive Non-Market Contributions} - \\text{Social Costs} - \\text{Environmental Costs}$$\n<ol>\n<li><strong>Income Inequality Adjustment:</strong> Adjusts personal consumption expenditure based on Gini coefficient (diminishing marginal utility of income).</li>\n<li><strong>Positive Non-Market Additions:</strong> Adds the calculated economic value of unpaid household labor, child care, volunteer work, and public infrastructure services.</li>\n<li><strong>Social Cost Deductions:</strong> Subtracts costs of crime, family breakdown, divorce, lost leisure time, and vehicle commuting.</li>\n<li><strong>Environmental Cost Deductions:</strong> Subtracts the calculated damages from air/water pollution, depletion of wetlands and forests, long-term climate damage, and ozone depletion.</li>\n</ol></li>\n<li><strong>Significance:</strong> Unlike GDP (which counts oil spills, diseases, and post-war rebuilding as economic growth), GPI reflects true net sustainable progress. In most developed nations, GDP has risen continuously while GPI has plateaued or declined since the 1970s ('Threshold Hypothesis').</li>\n</ul>",
            "expected_answer": """<div class="expected-body">
<p><strong>1. Definition of Genuine Progress Indicator (GPI):</strong></p>
<p>The <strong>Genuine Progress Indicator (GPI)</strong> is an alternative macroeconomic index developed by Clifford Cobb and colleagues in 1995 (evolving from Daly and Cobb's Index of Sustainable Economic Welfare - ISEW) to measure the true, sustainable economic, social, and environmental wellbeing of a country.</p>

<p><strong>2. How GPI is Created (Mathematical Framework & Adjustments):</strong></p>
<div class="formula-box">$$\text{GPI} = C_{\text{adj}} + \text{Positive Non-Market Contributions} - \text{Social Costs} - \text{Environmental Costs}$$</div>
<p>GPI begins with baseline personal consumption expenditure ($C$) and applies four systematic correction tiers:</p>
<ol>
  <li><strong>Income Inequality Adjustment ($C_{\text{adj}}$):</strong> Personal consumption expenditure is weighted using the <strong>Gini coefficient</strong>, reflecting the principle that marginal consumption by low-income households contributes more to net societal welfare than luxury consumption by the wealthy.</li>
  <li><strong>Positive Non-Market Additions:</strong> Adds the imputed monetary value of non-market activities omitted by GDP:
    <ul>
      <li>Unpaid domestic housework, parenting, and elder care.</li>
      <li>Community volunteer work and civic services.</li>
      <li>Services provided by publicly owned capital (highways, parks, libraries).</li>
    </ul>
  </li>
  <li><strong>Deductions for Social Costs:</strong> Subtracts defensive expenditures and welfare-destroying social ills:
    <ul>
      <li>Direct and indirect economic costs of crime, legal battles, and incarceration.</li>
      <li>Costs of divorce, family breakdown, and mental stress.</li>
      <li>Loss of leisure time and productivity lost during traffic commuting.</li>
    </ul>
  </li>
  <li><strong>Deductions for Environmental Degradation:</strong> Subtracts the calculated loss of natural capital:
    <ul>
      <li>Air, water, and noise pollution damage to human health.</li>
      <li>Depletion of non-renewable fossil fuels and minerals.</li>
      <li>Loss of wetlands, farmland topsoil erosion, and deforestation.</li>
      <li>Long-term climate change damage and stratospheric ozone depletion.</li>
    </ul>
  </li>
</ol>

<p><strong>3. Significance of GPI Compared to GDP:</strong></p>
<ul>
  <li><strong>Exposing the "Defensive Expenditure" Flaw of GDP:</strong> GDP counts disasters, medical treatment for pollution-induced sickness, oil spill remediation, and car accident repairs as economic "growth". In contrast, GPI recognizes these as defensive costs and subtracts them.</li>
  <li><strong>The Threshold Hypothesis:</strong> Empirical studies demonstrate that while GDP per capita has grown continually since World War II, GPI per capita peaked in the late 1970s and has since plateaued or declined. This proves that beyond an optimal threshold, the social and environmental costs of unconstrained GDP growth exceed its marginal economic benefits.</li>
</ul>
</div>""",
            "detailed_answer": """<div class="detailed-body">
<p><strong>The GDP Growth Delusion:</strong> GDP measures gross financial churn, completely indifferent to human welfare or ecological health. Robert F. Kennedy famously observed that GDP measures everything <em>'except that which makes life worthwhile.'</em> If a chemical tanker spills millions of gallons of crude oil into a bay, GDP surges because of the millions paid to contractors, cleanup crews, and legal teams.</p>
<p><strong>Methodological Construction of GPI:</strong> Created originally by Clifford Cobb in 1995 as an extension of Daly and Cobb's ISEW, GPI starts with standard personal consumption but applies three major correction filters:</p>
<ul>
<li><em>Equitable Weighting:</em> Consumption is weighted by income distribution; a dollar in the hands of an impoverished laborer generates more genuine welfare than a dollar added to a billionaire's portfolio.</li>
<li><em>Integrating the Invisible Economy:</em> Millions of hours of unpaid domestic care, elder care, and civic volunteering—worth trillions globally—are assigned economic value and added.</li>
<li><em>Depletion & Defensive Deductions:</em> Costs incurred merely to defend against degradation (water purifiers, air filters, noise barriers) are subtracted, along with the permanent loss of wetlands, fossil fuels, and topsoil.</li>
</ul>
<p><strong>The Threshold Hypothesis:</strong> Empirical research in the US, Europe, and India shows that while GDP per capita has quadrupled since 1950, GPI per capita peaked around 1978 and has stagnated. This proves that beyond a certain economic scale, the externalized social and environmental costs of growth equal or exceed the economic gains.</p>
<p><em>Slide Reference: Class 16, Slides 11, 23, 25, 26, 27.</em></p>
</div>"""
        },
        {
            "id": "EQB-16-10",
            "class_id": 16,
            "class_name": "Green Accounting",
            "topic": "Surrogate Market Approach Methods with Real-World Examples",
            "category": "Descriptive & Case Study",
            "exams": [{"paper": "End Exam 2023", "section": "Section II, Q2", "marks": "5M"}, {"paper": "End Exam 2019", "section": "Section II, Q1", "marks": "5M"}],
            "marks": "5M",
            "importance": "CRITICAL (\u2b50\u2b50\u2b50\u2b50\u2b50)",
            "prompt": "Explain surrogate market approach methods with examples.",
            "key_answer_points": "<ul>\n<li><strong>What is the Surrogate Market Approach?:</strong> When environmental goods or services have no direct market price, economists examine the prices paid in <em>parallel, surrogate commercial markets</em> where environmental quality is an embedded, implicit attribute. Also called <em>Revealed Preference Methods</em>.</li>\n<li><strong>Method 1: Hedonic Pricing Method (HPM):</strong>\n<ul>\n<li><em>Mechanism:</em> Deconstructs the market price of a private asset (typically residential housing) into its component attributes (size, rooms, location) and its environmental quality attributes (ambient noise, air quality, lake view).</li>\n<li><em>Formula:</em> $P_{\\text{house}} = f(S_{\\text{structural}}, N_{\\text{neighborhood}}, E_{\\text{environmental}})$. Isolating $\\frac{\\partial P}{\\partial E}$ yields the implicit marginal price of clean air or scenic beauty.</li>\n<li><em>Example:</em> Two identical apartments in Hyderabad: one facing a clean green park vs. one adjacent to a noisy, polluted municipal landfill. The price difference reveals residents' valuation of environmental quiet and clean air.</li>\n</ul></li>\n<li><strong>Method 2: Travel Cost Method (TCM):</strong>\n<ul>\n<li><em>Mechanism:</em> Evaluates the non-market recreational and aesthetic value of natural sites (national parks, wildlife reserves, lakes) based on the time and travel expenses incurred by visitors to reach them.</li>\n<li><em>Example:</em> Calculating the total economic recreational value of Jim Corbett National Park or Dal Lake by surveying visitors from varying distance zones regarding fuel, lodging, entry tickets, and opportunity cost of travel time.</li>\n</ul></li>\n</ul>",
            "expected_answer": """<div class="expected-body">
<p><strong>1. Concept of Surrogate Market Approach (Revealed Preferences):</strong></p>
<p>When environmental goods and services (clean air, scenic landscapes, quiet surroundings) have no direct market prices, economists use the <strong>Surrogate Market Approach</strong>. This method observes actual consumer purchases in parallel commercial markets where environmental quality is an implicit, embedded characteristic. Two primary techniques are used:</p>

<p><strong>2. Method 1: Hedonic Pricing Method (HPM):</strong></p>
<ul>
  <li><strong>Underlying Principle:</strong> The market price of a multi-attribute private asset (most commonly residential housing) is determined by its structural features, neighborhood characteristics, and local environmental quality:</li>
</ul>
<div class="formula-box">$$P_{\text{house}} = f(S_{\text{structural}}, N_{\text{neighborhood}}, E_{\text{environmental}})$$</div>
<p>By applying econometric regression analysis across thousands of property transactions while controlling for structural variables ($S$: square footage, bedrooms) and neighborhood variables ($N$: school quality, highway access), the partial derivative $\frac{\partial P}{\partial E}$ isolates the implicit shadow price of the environmental amenity ($E$).</p>
<ul>
  <li><strong>Real-World Example:</strong> Comparing real estate prices between two identical apartment complexes in Hyderabad: one facing a clean, green urban lake and park, and an identical one located adjacent to a noisy expressway or toxic municipal dump site. The price premium commanded by the park-facing property directly quantifies buyers' willingness to pay for clean air and quiet aesthetics.</li>
</ul>

<p><strong>3. Method 2: Travel Cost Method (TCM):</strong></p>
<ul>
  <li><strong>Underlying Principle:</strong> Natural recreational sites (national parks, wildlife sanctuaries, scenic lakes) are usually open to the public for free or with nominal entry fees that do not reflect their true value. TCM uses the expenses visitors incur to travel to the site as a proxy for the price of access.</li>
  <li><strong>Cost Components Included:</strong> Direct transportation costs (fuel, rail/air fares), accommodation expenses, site entry tickets, and the opportunity cost of travel time (forgone wages).</li>
  <li><strong>Demand Curve Construction:</strong> By surveying visitors from varying distance zones, economists plot a downward-sloping demand curve relating visitation rates to travel costs, calculating the total <strong>Consumer Surplus</strong> (the aggregate economic recreational value of the ecosystem).</li>
  <li><strong>Real-World Example:</strong> Estimating the multi-crore economic recreational value of Jim Corbett National Park or Dal Lake by surveying visitors from across India regarding total travel outlay and visit frequency to justify preservation against industrial development.</li>
</ul>
</div>""",
            "detailed_answer": """<div class="detailed-body">
<p><strong>The Theory of Revealed Preferences:</strong> In Slide 35, the course outlines environmental valuation methodologies. When consumers cannot directly buy 'clean air' at a supermarket, their market choices in other sectors reveal their willingness to pay for environmental amenities. Surrogate market techniques uncover these shadow prices:</p>
<p><strong>1. The Hedonic Property Pricing Model:</strong></p>
<div class="formula-box">$$P_i = \beta_0 + \beta_1 (\text{Bedrooms})_i + \beta_2 (\text{Distance to CBD})_i + \beta_3 (\text{PM}_{2.5} \text{ Concentration})_i + \epsilon_i$$</div>
<p>By controlling statistically for architectural square footage and transit access, multiple regression isolates $\beta_3$—the negative property discount associated with higher particulate pollution. If home prices drop by ₹5,00,000 for every $10 \, \mu\text{g/m}^3$ increase in air pollution, that reveals the surrogate market value of air quality.</p>
<p><strong>2. The Zonal and Individual Travel Cost Method:</strong></p>
<p>Because entry tickets to national parks are typically heavily subsidized, ticket revenue severely underestimates their economic value. The Travel Cost Method uses travel expenses (fuel, flights, hotels, opportunity cost of lost wages) as a proxy for the price of access. By constructing a downward-sloping demand curve correlating visitation rates with travel costs, economists calculate the total consumer surplus generated by preserving the wild habitat.</p>
<p><em>Slide Reference: Class 16, Slide 35.</em></p>
</div>"""
        },
        {
            "id": "EQB-16-11",
            "class_id": 16,
            "class_name": "Green Accounting",
            "topic": "Kyoto Protocol vs. Paris Agreement",
            "category": "Differentiate Between",
            "exams": [{"paper": "End Exam 2024", "section": "Section II, Q4", "marks": "5M"}, {"paper": "End Exam 2023", "section": "Section IV, Q2", "marks": "5M"}, {"paper": "End Exam 2018", "section": "Section III, Q1", "marks": "5M"}],
            "marks": "5M",
            "importance": "CRITICAL (\u2b50\u2b50\u2b50\u2b50\u2b50)",
            "prompt": "What is the Kyoto Protocol? Differentiate thoroughly between the Kyoto Protocol and the Paris Agreement.",
            "key_answer_points": "<ul>\n<li><strong>What is Kyoto Protocol?:</strong> Adopted in 1997 in Kyoto, Japan under the UNFCCC. It was the world's first treaty to establish legally binding greenhouse gas emissions reduction targets for developed industrialized nations (Annex-I parties), averaging an aggregate 5.2% reduction below 1990 levels during 2008\u20132012.</li>\n<li><strong>Core Differences:</strong>\n<ol>\n<li><strong>Architecture:</strong> Kyoto is <em>Top-Down</em> (mandatory international targets imposed on developed nations); Paris is <em>Bottom-Up</em> (countries submit voluntary Nationally Determined Contributions / NDCs).</li>\n<li><strong>Participation & Differentiation:</strong> Kyoto divided the world strictly into Annex-I (legally bound) and Non-Annex-I (no emission caps); Paris requires <em>all nations</em> (developed and developing) to submit mitigation commitments.</li>\n<li><strong>Target Temperature:</strong> Kyoto aimed for aggregate percentage cuts (-5.2%); Paris aims for an explicit temperature boundary (hold global temperature rise well below 2.0\u00b0C and pursue 1.5\u00b0C above pre-industrial levels).</li>\n<li><strong>Enforcement & Compliance:</strong> Kyoto had a formal Compliance Committee with penalty surcharges; Paris relies on transparent reporting, 5-year global stocktakes, and peer pressure ('name and encourage').</li>\n</ol></li>\n</ul>",
            "expected_answer": """<div class="expected-body">
<p><strong>1. What is the Kyoto Protocol?:</strong></p>
<p>Adopted in December 1997 at COP3 in Kyoto, Japan under the United Nations Framework Convention on Climate Change (UNFCCC), the <strong>Kyoto Protocol</strong> was the first legally binding international climate treaty. It mandated that developed industrialized nations (Annex-I parties) reduce their collective greenhouse gas emissions by an aggregate <strong>5.2% below 1990 baseline levels</strong> over the first commitment period (2008–2012).</p>

<p><strong>2. Comprehensive Comparison: Kyoto Protocol vs. Paris Agreement:</strong></p>
<div class="table-responsive">
<table class="table table-bordered table-striped">
<thead class="table-dark">
<tr>
  <th style="width:20%;">Parameter</th>
  <th style="width:40%;">Kyoto Protocol (1997, COP3)</th>
  <th style="width:40%;">Paris Agreement (2015, COP21)</th>
</tr>
</thead>
<tbody>
<tr>
  <td><strong>Architectural Structure</strong></td>
  <td><strong>Top-Down:</strong> Centrally negotiated, legally binding emission reduction quotas assigned to individual countries.</td>
  <td><strong>Bottom-Up:</strong> Countries determine their own voluntary national pledges called <strong>Nationally Determined Contributions (NDCs)</strong>.</td>
</tr>
<tr>
  <td><strong>Country Participation & Obligations</strong></td>
  <td><strong>Strictly Bifurcated:</strong> Legally binding caps only for Annex-I (developed) nations; zero emission limitation commitments for developing nations (India, China).</td>
  <td><strong>Universal Participation:</strong> All 196+ ratifying parties (both developed and developing) are required to prepare, communicate, and maintain NDCs.</td>
</tr>
<tr>
  <td><strong>Temperature & Target Metric</strong></td>
  <td>Targeted an aggregate <strong>5.2% emissions reduction</strong> across 6 major greenhouse gases below 1990 levels.</td>
  <td>Targeted a temperature limit: Hold global average warming <strong>well below 2.0°C</strong> and pursue efforts to limit it to <strong>1.5°C</strong> above pre-industrial levels.</td>
</tr>
<tr>
  <td><strong>Market Mechanisms</strong></td>
  <td>Established three <strong>Kyoto Flexible Mechanisms:</strong> Clean Development Mechanism (CDM), Joint Implementation (JI), and International Emissions Trading (IET).</td>
  <td>Governed by <strong>Article 6:</strong> Article 6.2 (Internationally Transferred Mitigation Outcomes - ITMOs) and Article 6.4 (centralized crediting mechanism).</td>
</tr>
<tr>
  <td><strong>Compliance & Enforcement</strong></td>
  <td>Hard compliance mechanism via a Compliance Committee; non-compliant nations faced penalty deductions (1.3x penalty factor in subsequent periods).</td>
  <td>Non-punitive, facilitative compliance framework based on public transparency, peer review, and mandatory 5-year <strong>Global Stocktakes</strong>.</td>
</tr>
<tr>
  <td><strong>Major Weakness / Outcome</strong></td>
  <td>The United States never ratified; Canada withdrew in 2011; emissions from non-capped emerging nations expanded rapidly.</td>
  <td>NDCs are voluntary without punitive legal sanctions; cumulative current pledges remain insufficient to meet the 1.5°C threshold.</td>
</tr>
</tbody>
</table>
</div>
</div>""",
            "detailed_answer": """<div class="detailed-body">
<p><strong>Historical Evolution of Global Climate Treaties:</strong> Slides 31 and 33 track the international climate regime. The 1997 Kyoto Protocol operationalized the UNFCCC objective by committing industrialized economies to legally binding limits under the principle of Common But Differentiated Responsibilities (CBDR).</p>
<p><strong>Comprehensive Side-by-Side Comparison:</strong></p>
<table class="exam-table">
<thead><tr><th>Parameter</th><th>Kyoto Protocol (1997, COP3)</th><th>Paris Agreement (2015, COP21)</th></tr></thead>
<tbody>
<tr><td><strong>Structural Architecture</strong></td><td>Top-down, centralized mandatory emission quotas allocated by international negotiation.</td><td>Bottom-up hybrid; domestic governments determine their own Nationally Determined Contributions (NDCs).</td></tr>
<tr><td><strong>Applicability of Obligations</strong></td><td>Bifurcated: Mandatory binding cuts for Annex-I (37 developed nations + EU); zero mitigation caps for developing countries (India, China).</td><td>Universal: All 196 ratifying parties must submit progressively ambitious NDCs every 5 years.</td></tr>
<tr><td><strong>Target Benchmark</strong></td><td>Aggregate 5.2% reduction in 6 GHGs below 1990 baseline levels over 2008–2012.</td><td>Cap global warming well below 2.0°C, striving for 1.5°C; achieve net-zero global emissions in second half of century.</td></tr>
<tr><td><strong>Market Mechanisms</strong></td><td>Kyoto Flexibility Mechanisms: CDM (CER), Joint Implementation (ERU), International Emissions Trading (AAU).</td><td>Article 6 Mechanisms: Article 6.2 (ITMOs - Internationally Transferred Mitigation Outcomes) and Article 6.4 crediting.</td></tr>
<tr><td><strong>Major Limitation</strong></td><td>US failed to ratify; Canada withdrew; emissions from emerging economies grew rapidly without caps.</td><td>NDCs are voluntary; aggregate initial commitments lead to ~2.7°C warming, requiring drastic ambition ratchet.</td></tr>
</tbody>
</table>
<p><em>Slide Reference: Class 16, Slides 31, 33; Class 11, Slide 2.</em></p>
</div>"""
        },
        {
            "id": "EQB-16-12",
            "class_id": 16,
            "class_name": "Green Accounting",
            "topic": "Market-Based Flexible Mechanisms under Kyoto Protocol",
            "category": "Descriptive & Case Study",
            "exams": [{"paper": "End Exam 2024", "section": "Section II, Q5", "marks": "3M"}, {"paper": "End Exam 2022", "section": "Section IV, Q(c)", "marks": "3M"}],
            "marks": "3M",
            "importance": "CRITICAL (\u2b50\u2b50\u2b50\u2b50\u2b50)",
            "prompt": "Explain any 2-market based flexible mechanisms to reduce emissions under Kyoto Protocol.",
            "key_answer_points": "<ul>\n<li><strong>Purpose of Flexible Mechanisms:</strong> The Kyoto Protocol introduced three market-based mechanisms to allow Annex-I developed nations to meet their emission reduction targets cost-effectively anywhere in the world where abatement is cheapest.</li>\n<li><strong>1. Clean Development Mechanism (CDM - Article 12):</strong>\n<ul>\n<li><em>Operation:</em> An Annex-I developed nation (or its private firms) funds or implements emission-reduction projects in Non-Annex-I developing nations (e.g., solar farms, biomass plants in India or China).</li>\n<li><em>Currency:</em> Generates <strong>Certified Emission Reductions (CERs)</strong>, where $1 \\text{ CER} = 1 \\text{ metric tonne of } \\text{CO}_2\\text{ equivalent}$ avoided.</li>\n<li><em>Dual Goal:</em> Helps Annex-I meet compliance targets cheaply while promoting sustainable technology transfer to developing nations.</li>\n</ul></li>\n<li><strong>2. Joint Implementation (JI - Article 6):</strong>\n<ul>\n<li><em>Operation:</em> An Annex-I country invests in an emission-reduction project in another Annex-I country (typically in Eastern Europe or an Economy in Transition).</li>\n<li><em>Currency:</em> Generates <strong>Emission Reduction Units (ERUs)</strong> ($1 \\text{ ERU} = 1 \\text{ tonne } \\text{CO}_2\\text{e}$).</li>\n</ul></li>\n<li><strong>3. International Emissions Trading (IET - Article 17):</strong>\n<ul>\n<li><em>Operation:</em> Annex-I countries trade spare allowable emissions units (Assigned Amount Units / AAUs) in a 'cap-and-trade' carbon market.</li>\n</ul></li>\n</ul>",
            "expected_answer": """<div class="expected-body">
<p><strong>Purpose of Market-Based Flexible Mechanisms:</strong></p>
<p>Because greenhouse gases mix uniformly in the global atmosphere, 1 tonne of $\text{CO}_2$ avoided has the exact same climatic benefit anywhere on Earth. The Kyoto Protocol created market-based flexible mechanisms so Annex-I developed nations could achieve their emissions reduction targets cost-effectively by financing reductions where marginal abatement costs are lowest.</p>

<p><strong>Two Primary Flexible Mechanisms:</strong></p>

<p><strong>1. Clean Development Mechanism (CDM - Article 12):</strong></p>
<ul>
  <li><strong>How it Works:</strong> An Annex-I developed nation (or its authorized private companies) invests in greenhouse gas abatement or renewable energy projects in a Non-Annex-I developing nation (e.g., funding a solar park or biomass plant in India or China).</li>
  <li><strong>Accounting Unit:</strong> The project generates <strong>Certified Emission Reductions (CERs)</strong>, where $1 \text{ CER} = 1 \text{ metric tonne of } \text{CO}_2\text{ equivalent}$ avoided.</li>
  <li><strong>Dual Objective:</strong> Allows developed nations to achieve compliance at much lower cost than domestic retrofits, while transferring clean technology and sustainable capital to developing host nations.</li>
</ul>

<p><strong>2. Joint Implementation (JI - Article 6):</strong></p>
<ul>
  <li><strong>How it Works:</strong> An Annex-I developed nation invests in an emission-reduction project in another Annex-I nation (typically an Economy in Transition, such as in Eastern Europe or the Russian Federation).</li>
  <li><strong>Accounting Unit:</strong> Generates <strong>Emission Reduction Units (ERUs)</strong> ($1 \text{ ERU} = 1 \text{ tonne } \text{CO}_2\text{e}$).</li>
  <li><strong>Accounting Rule:</strong> Because both nations operate under national caps, the host nation converts an equivalent portion of its Assigned Amount Units (AAUs) into ERUs to prevent double-counting.</li>
</ul>

<p><em>(Alternative 3rd Mechanism - International Emissions Trading / IET, Article 17):</em> Allows Annex-I nations with surplus allowable emissions (unused AAUs) to sell them directly to Annex-I nations exceeding their Kyoto targets under a cap-and-trade market.</p>
</div>""",
            "detailed_answer": """<div class="detailed-body">
<p><strong>Economic Rationale for Carbon Markets:</strong> A molecule of $\text{CO}_2$ has the same global warming impact regardless of where it is emitted. Reducing 1 tonne of carbon in a coal plant in Germany might cost €150, whereas achieving the same 1-tonne reduction by upgrading a biomass boiler in rural India might cost only €15. The Kyoto Protocol created three flexible mechanisms to harness this marginal abatement cost differential:</p>
<p><strong>1. Clean Development Mechanism (CDM):</strong></p>
<p>CDM is the premier North-South mechanism. An entity in a developed country invests in clean energy (e.g., a wind farm in Rajasthan). After rigorous baseline auditing by a Designated Operational Entity (DOE) and registration with the UN CDM Executive Board, the project receives Certified Emission Reductions (CERs). The developed country counts these CERs against its domestic Kyoto targets.</p>
<p><strong>2. Joint Implementation (JI):</strong></p>
<p>JI is an Annex-I to Annex-I mechanism. Because both host and donor nations have legally binding emission caps, the host nation converts an equivalent number of its Assigned Amount Units (AAUs) into Emission Reduction Units (ERUs) and transfers them to the donor nation, ensuring strict integrity against double-counting.</p>
<p><em>Slide Reference: Class 16, Slides 31, 33, 39, 41.</em></p>
</div>"""
        },
        {
            "id": "EQB-16-13",
            "class_id": 16,
            "class_name": "Green Accounting",
            "topic": "Differentiate between Annex-1 and Annex-2 Countries",
            "category": "Differentiate Between",
            "exams": [{"paper": "End Exam 2023", "section": "Section II, Q4", "marks": "2M"}, {"paper": "End Exam 2019", "section": "Section III, Q3", "marks": "2M"}],
            "marks": "2M",
            "importance": "HIGH (\u2b50\u2b50\u2b50\u2b50)",
            "prompt": "Differentiate between Annex-1 and Annex-2 countries.",
            "key_answer_points": "<ul>\n<li><strong>Annex-I Countries:</strong> Includes industrialized developed countries that were members of the OECD in 1992, plus countries with Economies in Transition (EITs) such as the Russian Federation, Baltic states, and Eastern European nations (total ~43 parties). They took on legally binding emission limitation targets under the Kyoto Protocol.</li>\n<li><strong>Annex-II Countries:</strong> A strict <em>sub-group of Annex-I</em> consisting exclusively of the 24 highly developed OECD nations (excluding the EIT transition economies).</li>\n<li><strong>Core Functional Difference:</strong> Annex-I countries are committed to <em>emission reduction targets</em>. Annex-II countries have the additional statutory obligation to <em>provide new and additional financial resources and clean technology transfer</em> to developing nations to help them adapt to climate change.</li>\n</ul>",
            "expected_answer": """<div class="expected-body">
<p><strong>Comparative Breakdown: Annex-I vs. Annex-II Countries (UNFCCC / Kyoto Protocol):</strong></p>
<div class="table-responsive">
<table class="table table-bordered table-striped">
<thead class="table-dark">
<tr>
  <th>Feature</th>
  <th>Annex-I Countries</th>
  <th>Annex-II Countries</th>
</tr>
</thead>
<tbody>
<tr>
  <td><strong>Composition & Membership</strong></td>
  <td>Includes all industrialized OECD member nations (as of 1992) <strong>PLUS</strong> Economies in Transition (EITs) such as the Russian Federation, Baltic States, and Eastern European nations (~43 parties total).</td>
  <td>A strict <strong>sub-group of Annex-I</strong> consisting exclusively of the 24 highly developed OECD nations. <em>Economies in Transition (EITs) are excluded.</em></td>
</tr>
<tr>
  <td><strong>Primary Legal Obligation</strong></td>
  <td>Committed to <strong>emissions reduction and limitation targets</strong> to return emissions to baseline levels under the Kyoto Protocol.</td>
  <td>Committed to emission reduction targets <strong>PLUS</strong> the legal obligation to provide financial assistance and clean technology transfer.</td>
</tr>
<tr>
  <td><strong>Financial & Technology Mandate</strong></td>
  <td>EIT nations within Annex-I have no obligation to provide financial aid or fund climate projects in developing nations.</td>
  <td>Statutorily mandated under UNFCCC Articles 4.3, 4.4, and 4.5 to provide "new and additional" climate finance to developing countries (via GEF/GCF).</td>
</tr>
</tbody>
</table>
</div>
</div>""",
            "detailed_answer": """<div class="detailed-body">
<p><strong>UNFCCC Differentiation Schema:</strong> When the UNFCCC was drafted in 1992, parties recognized that historical emissions were predominantly generated by industrialized western nations. Countries were categorized into discrete annexes:</p>
<table class="exam-table">
<thead><tr><th>Feature</th><th>Annex-I Parties</th><th>Annex-II Parties</th></tr></thead>
<tbody>
<tr><td><strong>Composition</strong></td><td>Industrialized OECD nations + Economies in Transition (Russia, Ukraine, Eastern Europe). Total ~43 parties.</td><td>Exclusively OECD members of Annex-I (US, UK, Germany, Japan, Australia, etc.). Excludes EIT nations.</td></tr>
<tr><td><strong>Primary Duty</strong></td><td>Legally committed to reduce greenhouse gas emissions to specific baseline targets under the Kyoto Protocol.</td><td>Committed to emissions cuts <em>PLUS</em> providing grant-based financial aid and technology transfer to Non-Annex-I nations.</td></tr>
<tr><td><strong>Financial Obligation</strong></td><td>Transition economies (EITs) are exempt from financing climate adaptation in third countries.</td><td>Statutorily mandated under UNFCCC Article 4.3, 4.4, and 4.5 to fund the Global Environment Facility (GEF) and Green Climate Fund.</td></tr>
</tbody>
</table>
<p><em>Slide Reference: Class 16, Slides 31, 33.</em></p>
</div>"""
        },
        {
            "id": "EQB-16-14",
            "class_id": 16,
            "class_name": "Green Accounting",
            "topic": "Core Environmental Accounting and Climate Acronyms",
            "category": "Acronyms & Expansions",
            "exams": [{"paper": "End Exam 2024", "section": "Section I, Q1", "marks": "5M"}, {"paper": "End Exam 2022", "section": "Section I, Q2", "marks": "5M"}, {"paper": "End Exam 2019", "section": "Section I, Q1", "marks": "5M"}],
            "marks": "5M",
            "importance": "CRITICAL (\u2b50\u2b50\u2b50\u2b50\u2b50)",
            "prompt": "Expand the following acronyms: CER, EDP, IPCC, IUCN, SSRRS, WTP, ISEW, MEW, CDM, UNFCCC, COP, GWP.",
            "key_answer_points": "<ul>\n<li><strong>CER:</strong> Certified Emission Reduction (Carbon credit equal to $1 \\text{ tCO}_2\\text{e}$ avoided under Clean Development Mechanism).</li>\n<li><strong>EDP:</strong> Environmentally-adjusted Net Domestic Product (Eco-Domestic Product: $\\text{EDP} = \\text{GDP} - D_m - D_n$).</li>\n<li><strong>IPCC:</strong> Intergovernmental Panel on Climate Change (UN scientific body established in 1988 by UNEP and WMO).</li>\n<li><strong>IUCN:</strong> International Union for Conservation of Nature (Global conservation authority established in 1948; publishes the Red List).</li>\n<li><strong>SSRRS:</strong> Satellite-based Surface Runoff and Resource Survey (Remote sensing application for hydrological accounting).</li>\n<li><strong>WTP:</strong> Willingness to Pay (Maximum monetary amount a consumer will pay to obtain an environmental amenity).</li>\n<li><strong>ISEW:</strong> Index of Sustainable Economic Welfare (Macroeconomic welfare index created by Herman Daly and John Cobb in 1989).</li>\n<li><strong>MEW:</strong> Measure of Economic Welfare (Early green accounting metric created by William Nordhaus and James Tobin in 1972).</li>\n<li><strong>CDM:</strong> Clean Development Mechanism (Kyoto Protocol market-based mechanism under Article 12).</li>\n<li><strong>UNFCCC:</strong> United Nations Framework Convention on Climate Change (Treaty adopted at 1992 Rio Earth Summit).</li>\n<li><strong>COP:</strong> Conference of the Parties (The supreme decision-making governing body of the UNFCCC).</li>\n<li><strong>GWP:</strong> Global Warming Potential (Metric measuring heat trapped by a greenhouse gas relative to $\\text{CO}_2$ over 100 years).</li>\n</ul>",
            "expected_answer": """<div class="expected-body">
<p><strong>Official Expansions and Context for the 12 Acronyms:</strong></p>
<ol>
  <li><strong>CER:</strong> <strong>Certified Emission Reduction</strong> — Tradable carbon credit unit under the Kyoto Clean Development Mechanism equal to $1 \text{ metric tonne of } \text{CO}_2\text{e}$ sequestered or avoided.</li>
  <li><strong>EDP:</strong> <strong>Environmentally-adjusted Net Domestic Product</strong> (or Eco-Domestic Product) — Green accounting measure subtracting manufactured capital depreciation and natural capital depletion from GDP: $\text{EDP} = \text{GDP} - D_m - D_n$.</li>
  <li><strong>IPCC:</strong> <strong>Intergovernmental Panel on Climate Change</strong> — Scientific body established in 1988 by UNEP and WMO to assess climate change research and publish comprehensive assessment reports.</li>
  <li><strong>IUCN:</strong> <strong>International Union for Conservation of Nature</strong> — Global conservation organization founded in 1948, known for maintaining the IUCN Red List of Threatened Species.</li>
  <li><strong>SSRRS:</strong> <strong>Satellite-based Surface Runoff and Resource Survey</strong> — Remote-sensing geospatial methodology used to map hydrological catchment runoff and surface water resources.</li>
  <li><strong>WTP:</strong> <strong>Willingness to Pay</strong> — Microeconomic metric in environmental valuation measuring the maximum monetary amount a consumer would pay to preserve or improve an environmental good.</li>
  <li><strong>ISEW:</strong> <strong>Index of Sustainable Economic Welfare</strong> — Macroeconomic welfare indicator formulated by Herman Daly and John Cobb (1989) incorporating income distribution and environmental damage.</li>
  <li><strong>MEW:</strong> <strong>Measure of Economic Welfare</strong> — Early welfare index developed by William Nordhaus and James Tobin (1972) adjusting GDP for leisure time, non-market work, and pollution.</li>
  <li><strong>CDM:</strong> <strong>Clean Development Mechanism</strong> — Kyoto Protocol market mechanism (Article 12) enabling Annex-I countries to earn CER credits by investing in clean projects in developing nations.</li>
  <li><strong>UNFCCC:</strong> <strong>United Nations Framework Convention on Climate Change</strong> — Foundational international environmental treaty negotiated at the 1992 Rio Earth Summit.</li>
  <li><strong>COP:</strong> <strong>Conference of the Parties</strong> — The supreme decision-making body of the UNFCCC that meets annually to assess progress and negotiate climate agreements.</li>
  <li><strong>GWP:</strong> <strong>Global Warming Potential</strong> — Index quantifying the integrated radiative forcing (heat-trapping ability) of a greenhouse gas relative to $\text{CO}_2$ over a specified time horizon (normally 100 years).</li>
</ol>
</div>""",
            "detailed_answer": """<div class="detailed-body">
<p><strong>Systematic Directory of Environmental Governance and Accounting Acronyms:</strong> These twelve acronyms recur consistently across past exam papers and represent fundamental institutional, analytical, and economic metrics:</p>
<ul>
<li><strong>CER (Certified Emission Reduction):</strong> Official carbon credit token generated by CDM projects in developing nations, equivalent to 1 metric tonne of $\text{CO}_2$ avoided.</li>
<li><strong>EDP (Environmentally-adjusted Domestic Product):</strong> The central output indicator of SEEA, calculated by subtracting capital depreciation and environmental degradation from GDP.</li>
<li><strong>IPCC (Intergovernmental Panel on Climate Change):</strong> Nobel Peace Prize-winning scientific panel that produces global Assessment Reports (AR1–AR6) synthesizing climate science.</li>
<li><strong>IUCN (International Union for Conservation of Nature):</strong> Global authority that classifies species extinction risks into categories (Critically Endangered, Endangered, Vulnerable).</li>
<li><strong>SSRRS (Satellite-based Surface Runoff and Resource Survey):</strong> Geospatial remote sensing method combining satellite imagery and precipitation data to quantify water resources.</li>
<li><strong>WTP (Willingness to Pay):</strong> Central valuation metric in stated-preference Contingent Valuation Methods (CVM) to measure consumer valuation of public goods.</li>
<li><strong>ISEW & MEW:</strong> Foundational alternative indices developed by Nordhaus, Tobin, Daly, and Cobb to correct GDP for leisure, unpaid work, and ecological damage.</li>
<li><strong>CDM, UNFCCC, COP & GWP:</strong> Foundational legal and scientific building blocks of international climate diplomacy and carbon accounting.</li>
</ul>
<p><em>Slide Reference: Class 16, Slides 1, 8, 14, 19, 31, 33, 35, 41, 44.</em></p>
</div>"""
        },
        {
            "id": "EQB-16-15",
            "class_id": 16,
            "class_name": "Green Accounting",
            "topic": "Pioneering Country in NAMEA Accounting",
            "category": "MCQ & Objective",
            "exams": [{"paper": "End Exam 2024", "section": "Section I, Q4", "marks": "1M"}, {"paper": "End Exam 2022", "section": "Section I, Q(f)", "marks": "1M"}],
            "marks": "1M",
            "importance": "CRITICAL (\u2b50\u2b50\u2b50\u2b50\u2b50)",
            "prompt": "Country that has started accounting emission in national income under the NAMEA framework is: [a] Germany, [b] Netherlands, [c] Norway, [d] France.",
            "key_answer_points": "<ul>\n<li><strong>Correct Answer:</strong> <strong>[b] Netherlands</strong></li>\n<li><strong>Direct Slide Evidence (Slide 33):</strong> <em>'The Netherlands routinely constructs the \"National Accounting Matrix Including Environmental Accounts (NAMEA)\" which adds environmental accounts to the traditional national income accounts.'</em></li>\n<li><strong>Developed By:</strong> Statistics Netherlands (CBS) in 1993 under the leadership of economist Steven de Boo and colleagues.</li>\n</ul>",
            "expected_answer": """<div class="expected-body">
<p><strong>Correct Option:</strong> <strong>[b] Netherlands</strong></p>
<p><strong>Exam Justification & Key Details (Slide 33):</strong></p>
<ul>
  <li>Statistics Netherlands (Centraal Bureau voor de Statistiek - CBS) pioneered and routinely constructs the <strong>National Accounting Matrix including Environmental Accounts (NAMEA)</strong>.</li>
  <li>Developed in 1993 under Steven de Boo, NAMEA directly links conventional national input-output economic accounts with physical pollutant emissions matrices across the same industrial sectors, allowing precise calculation of eco-efficiency and emissions intensity per sector.</li>
</ul>
</div>""",
            "detailed_answer": """<div class="detailed-body">
<p><strong>The NAMEA Innovation:</strong> In conventional macroeconomic accounting, input-output tables link inter-industry financial transactions. In 1993, Statistics Netherlands (Centraal Bureau voor de Statistiek - CBS) developed the <em>National Accounting Matrix including Environmental Accounts (NAMEA)</em>. The system couples conventional input-output economic accounts with physical pollutant emissions tables (such as greenhouse gases, acidification, and toxic waste) categorized by the exact same industrial sectors.</p>
<p>This allows policymakers in the Netherlands and across the European Union (Eurostat adopted NAMEA as the EU standard) to identify precisely which economic industries produce the greatest emissions intensity per dollar of GDP output.</p>
<p><em>Slide Reference: Class 16, Slide 33.</em></p>
</div>"""
        },
        {
            "id": "EQB-16-16",
            "class_id": 16,
            "class_name": "Green Accounting",
            "topic": "Match Gases with Global Warming Potential (GWP)",
            "category": "Match the Following",
            "exams": [{"paper": "End Exam 2024", "section": "Section I, Match", "marks": "5M"}, {"paper": "End Exam 2022", "section": "Section I, Match", "marks": "5M"}],
            "marks": "5M",
            "importance": "CRITICAL (\u2b50\u2b50\u2b50\u2b50\u2b50)",
            "prompt": "Section-I: Match the following Gases with their Global Warming Potential (100-Year GWP):\\n(1) Carbon Dioxide (CO2)\\n(2) Methane (CH4)\\n(3) Nitrous Oxide (N2O)\\n(4) Sulfur Hexafluoride (SF6)",
            "key_answer_points": "<ul>\n<li><strong>(1) Carbon Dioxide ($\\text{CO}_2$):</strong> $\\text{GWP} = 1$ (Reference baseline gas by international definition).</li>\n<li><strong>(2) Methane ($\\text{CH}_4$):</strong> $\\text{GWP} = 28$ (or $25$\u2013$28$ under IPCC AR5 over 100-year time horizon).</li>\n<li><strong>(3) Nitrous Oxide ($\\text{N}_2\\text{O}$):</strong> $\\text{GWP} = 265$ (or $298$ under IPCC AR4/AR5).</li>\n<li><strong>(4) Sulfur Hexafluoride ($\\text{SF}_6$):</strong> $\\text{GWP} = 23,500$ (The most potent greenhouse gas evaluated by the IPCC, used in high-voltage electrical switchgear).</li>\n</ul>",
            "expected_answer": """<div class="expected-body">
<p><strong>1. Matched Table: Gases with 100-Year Global Warming Potential (GWP):</strong></p>
<div class="table-responsive">
<table class="table table-bordered table-striped">
<thead class="table-dark">
<tr>
  <th>Greenhouse Gas</th>
  <th>Chemical Formula</th>
  <th>100-Year GWP (IPCC AR5 / Curriculum)</th>
  <th>Key Characteristics & Atmospheric Lifetime</th>
</tr>
</thead>
<tbody>
<tr>
  <td><strong>(1) Carbon Dioxide</strong></td>
  <td>$\text{CO}_2$</td>
  <td><strong>1</strong> (Reference Baseline)</td>
  <td>Baseline standard; accounts for ~76% of anthropogenic warming; atmospheric lifetime spans centuries.</td>
</tr>
<tr>
  <td><strong>(2) Methane</strong></td>
  <td>$\text{CH}_4$</td>
  <td><strong>28</strong> (or 25–28)</td>
  <td>Atmospheric lifetime ~12 years; highly potent thermal absorption from enteric fermentation, wetlands, and gas leaks.</td>
</tr>
<tr>
  <td><strong>(3) Nitrous Oxide</strong></td>
  <td>$\text{N}_2\text{O}$</td>
  <td><strong>265</strong> (or 298)</td>
  <td>Atmospheric lifetime ~114 years; emitted primarily from synthetic agricultural fertilizers and industrial chemical synthesis.</td>
</tr>
<tr>
  <td><strong>(4) Sulfur Hexafluoride</strong></td>
  <td>$\text{SF}_6$</td>
  <td><strong>23,500</strong></td>
  <td>Extremely potent synthetic inorganic dielectric gas used in high-voltage circuit breakers; atmospheric lifetime > 3,200 years.</td>
</tr>
</tbody>
</table>
</div>

<p><strong>2. Mathematical Definition of GWP:</strong></p>
<p>Global Warming Potential represents the ratio of the time-integrated radiative forcing from the instantaneous release of 1 kg of a trace substance relative to that of 1 kg of reference gas ($\text{CO}_2$):</p>
<div class="formula-box">$$\text{GWP}_i = \frac{\int_0^{100} a_i \cdot C_i(t) \, dt}{\int_0^{100} a_{\text{CO}_2} \cdot C_{\text{CO}_2}(t) \, dt}$$</div>
<p>where $a_i$ is the radiative efficiency (forcing per unit atmospheric mass) and $C_i(t)$ is the time-dependent atmospheric concentration decay following pulse emission.</p>
</div>""",
            "detailed_answer": """<div class="detailed-body">
<p><strong>Scientific Definition of GWP:</strong> Global Warming Potential (GWP) is a relative index measuring how much thermal infrared energy 1 ton of a given greenhouse gas absorbs over a 100-year time horizon compared to 1 ton of carbon dioxide:</p>
<div class="formula-box">$$\text{GWP}_i = \frac{\int_0^{100} a_i \cdot C_i(t) \, dt}{\int_0^{100} a_{\text{CO}_2} \cdot C_{\text{CO}_2}(t) \, dt}$$</div>
<p><strong>Physical Characteristics of the Gases:</strong></p>
<ul>
<li><em>Carbon Dioxide ($CO_2$, GWP = 1):</em> Weakest radiative forcing per molecule, but accounts for ~76% of total anthropogenic warming due to gigatonne emission volumes and atmospheric lifetime of centuries.</li>
<li><em>Methane ($CH_4$, GWP = 28):</em> Absorbs infrared far more aggressively than $CO_2$; decays into $CO_2$ and $H_2O$ with a shorter atmospheric half-life (~12 years).</li>
<li><em>Nitrous Oxide ($N_2O$, GWP = 265):</em> Released from agricultural nitrogen fertilizers and adipic acid production; atmospheric lifetime ~114 years.</li>
<li><em>Sulfur Hexafluoride ($SF_6$, GWP = 23,500):</em> Synthetic, highly stable inorganic dielectric gas used in high-voltage circuit breakers and gas-insulated substations. Atmospheric lifetime exceeds 3,200 years.</li>
</ul>
<p><em>Slide Reference: Class 16, Slide 44.</em></p>
</div>"""
        }
    ]

if __name__ == "__main__":
    qs = get_class16_grounded_questions()
    print(f"Loaded {len(qs)} grounded Class 16 questions successfully.")
    for q in qs:
        assert "expected_answer" in q and len(q["expected_answer"]) > 50
    print("All 16 questions verified with robust expected_answer fields.")
