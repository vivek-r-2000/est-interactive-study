import json

def get_class16_questions():
    return [
        {
            "id": "EQB-16-01",
            "class_id": 16,
            "class_name": "Green Accounting & Natural Capital",
            "topic": "SNA Framework & Popularity Rationale",
            "category": "Descriptive & Case Study",
            "exams": [
                {"paper": "End Exam 2024", "section": "Section VI, Q5", "marks": "5M"},
                {"paper": "End Exam 2023", "section": "Section IV, Q2", "marks": "4M"},
                {"paper": "End Exam 2022", "section": "Section XI", "marks": "10M"},
                {"paper": "End Exam 2019", "section": "Section VIII, Q1", "marks": "10M"},
                {"paper": "End Exam 2018", "section": "Part IV, Q7", "marks": "10M"}
            ],
            "marks": "4M – 10M",
            "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
            "prompt": "What is SNA? Define its framework? Why did the concept of SNA remain so popular for longer time (only list the factors)?",
            "key_answer_points": "<ul>\n<li><strong>Definition:</strong> <strong>System of National Accounts (SNA)</strong> is the standard international macroeconomic framework developed by the United Nations for measuring national economic activity, Gross Domestic Product (GDP), and economic growth.</li>\n<li><strong>Mathematical Framework:</strong>\n<br>• Gross National Product: \\(\\text{GNP} = C + I + G + (X - M) + (R - P)\\)\n<br>• Net National Product: \\(\\text{NNP} = \\text{GNP} - D\\) (where $D$ = physical capital depreciation)\n<br>• Gross Domestic Product: \\(\\text{GDP} = C + I + G + (X - M)\\)\n<br><em>Where:</em> $C$ = Consumption, $I$ = Investment, $G$ = Government spending, $X$ = Exports, $M$ = Imports, $R$ = Receipts from abroad, $P$ = Payments abroad.</li>\n<li><strong>Why SNA Remained Popular for Decades (The 5 Historical Factors):</strong>\n<br>1. <em>Post-War Focus on Economic Growth:</em> Rebuilding economies after the Great Depression and World War II prioritized factory output and jobs above all else.\n<br>2. <em>Nobody Thought About the Environment:</em> Natural resources (clean water, clean air, timber) were viewed as infinite, self-renewing, and cost-free.\n<br>3. <em>Dominance of the Market Price System:</em> SNA only tracks items bought and sold for monetary prices in organized markets.\n<br>4. <em>Difficulty of Accounting for Nature:</em> Valuing a forest's flood protection or biodiversity in dollars was deemed too subjective.\n<br>5. <em>Institutional Inertia:</em> Governments were reluctant to adopt complex satellite accounts that could lower their official published GDP numbers.</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>The Asymmetry of Traditional GDP:</strong> Under SNA, a standing forest that cleans air and prevents floods has a recorded economic value of zero. But if the forest is clear-cut and sold for timber, GDP records the logging as positive national income, ignoring the lost natural capital stock.</p>\n<p><em>Slide Reference: Class 16 Slides 4–9.</em></p>\n</div>"
        },
        {
            "id": "EQB-16-02",
            "class_id": 16,
            "class_name": "Green Accounting & Natural Capital",
            "topic": "SEEA Expansion of SNA & Asset Classification",
            "category": "Descriptive & Case Study",
            "exams": [
                {"paper": "End Exam 2024", "section": "Section V, Q1", "marks": "2M"},
                {"paper": "End Exam 2023", "section": "Section II, Q4", "marks": "2M"},
                {"paper": "End Exam 2022", "section": "Section XI (OR)", "marks": "10M"},
                {"paper": "End Exam 2019", "section": "Section VIII, Q1", "marks": "10M"},
                {"paper": "End Exam 2018", "section": "Part IV, Q7", "marks": "10M"}
            ],
            "marks": "2M – 10M",
            "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
            "prompt": "How SEEA has expanded and complemented SNA? How natural assets are classified in SNA and SEEA?",
            "key_answer_points": "<ul>\n<li><strong>How SEEA Expands SNA:</strong>\n<br>• Adopted by the UN in 1993, the <strong>System of Environmental-Economic Accounting (SEEA)</strong> integrates physical and monetary accounts of natural resource depletion and environmental degradation alongside conventional GDP.\n<br>• Enables calculation of <strong>Environmentally-Adjusted GDP (Green GDP)</strong>: \\(\\text{Green GDP} = \\text{GDP} - \\text{Natural Capital Depletion} - \\text{Environmental Degradation Costs}\\).</li>\n<li><strong>Asset Classification Comparison (SNA vs SEEA):</strong>\n<br>• <em>Cultivated Biological & Sub-soil Assets:</em> Both systems count commercial timber plantations, livestock, and mineral/petroleum reserves.\n<br>• <em>Atmosphere / Air:</em> <strong>Included strictly in SEEA</strong> as a sink asset for emissions; completely omitted in SNA.\n<br>• <em>Land & Water Surfaces:</em> SNA land includes water surfaces (lakes, rivers) only if commercially owned; SEEA separates water into distinct aquatic ecosystem and river flow accounts.\n<br>• <em>Ecosystems & Biodiversity:</em> Completely excluded from SNA; SEEA explicitly classifies wild forests, wetlands, and biomes under spatial ecosystem accounts.</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>Satellite Accounting:</strong> Rather than throwing away 70 years of historical GDP data, SEEA acts as satellite accounts linked directly to the national balance sheet.</p>\n<p><em>Slide Reference: Class 16 Slides 10–16.</em></p>\n</div>"
        },
        {
            "id": "EQB-16-03",
            "class_id": 16,
            "class_name": "Green Accounting & Natural Capital",
            "topic": "Hicksian Income & Green Accounting",
            "category": "Short Answer & Definitions",
            "exams": [
                {"paper": "End Exam 2024", "section": "Section V, Q5", "marks": "2M"},
                {"paper": "End Exam 2022", "section": "Section IX, Q(d)", "marks": "2M"},
                {"paper": "End Exam 2018", "section": "Part IV, Q4", "marks": "4M"}
            ],
            "marks": "2M – 4M",
            "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
            "prompt": "Relate Hicksian income with Green accounting.",
            "key_answer_points": "<ul>\n<li><strong>Hicksian Income Definition (Sir John Hicks, 1946):</strong> Income is the maximum amount of consumption an individual or nation can enjoy during a period and still expect to be just as well off at the end of the period (<strong>consuming only the fruit, not cutting down the tree</strong>).</li>\n<li><strong>Relation to Green Accounting:</strong> Traditional GDP violates Hicks' rule because it treats the liquidation of non-renewable natural capital (mining minerals, draining aquifers) as current production income.\n<br>• Green Accounting restores Hicksian income by deducting natural capital depletion: \\(\\text{True Sustainable Income} = \\text{GDP} - \\text{Depreciation of Man-made Capital} - \\text{Depletion of Natural Capital}\\).</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>True Income:</strong> If a business sells off its factory buildings to pay for dinner, it is going bankrupt, not generating income. Green accounting forces nations to apply the same basic rule to natural capital.</p>\n<p><em>Slide Reference: Class 16 Slide 7.</em></p>\n</div>"
        },
        {
            "id": "EQB-16-04",
            "class_id": 16,
            "class_name": "Green Accounting & Natural Capital",
            "topic": "Four Factors of Production in National Income",
            "category": "Short Answer & Definitions",
            "exams": [
                {"paper": "End Exam 2024", "section": "Section V, Q2", "marks": "2M"},
                {"paper": "End Exam 2023", "section": "Section II, Q10", "marks": "2M"}
            ],
            "marks": "2M",
            "importance": "HIGH (⭐⭐⭐⭐)",
            "prompt": "What are the four factors of production considered in National income?",
            "key_answer_points": "<ul>\n<li><strong>1. Land (Natural Resources):</strong> Physical ground, minerals, forests, and water bodies $\\rightarrow$ Earns <strong>Rent</strong>.</li>\n<li><strong>2. Labor (Human Effort):</strong> Physical and intellectual workforce input $\\rightarrow$ Earns <strong>Wages / Salaries</strong>.</li>\n<li><strong>3. Capital (Man-Made Assets):</strong> Machinery, factories, computers, tools, and infrastructure $\\rightarrow$ Earns <strong>Interest</strong>.</li>\n<li><strong>4. Enterprise / Entrepreneurship:</strong> Innovation, risk-taking, and business organization $\\rightarrow$ Earns <strong>Profit</strong>.</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>Factor Incomes:</strong> In classical economics, total national income is the sum of Rent + Wages + Interest + Profit ($Y = R + W + I + P$).</p>\n<p><em>Slide Reference: Class 16 Slide 8.</em></p>\n</div>"
        },
        {
            "id": "EQB-16-05",
            "class_id": 16,
            "class_name": "Green Accounting & Natural Capital",
            "topic": "Market Axioms in Traditional Economics",
            "category": "Short Answer & Definitions",
            "exams": [
                {"paper": "End Exam 2024", "section": "Section III, Q(b)", "marks": "1M"},
                {"paper": "End Exam 2023", "section": "Section II, Q14", "marks": "2M"},
                {"paper": "End Exam 2022", "section": "Section VI, Q(b)", "marks": "1M"},
                {"paper": "End Exam 2018", "section": "Part IV, Q6", "marks": "6M"}
            ],
            "marks": "1M – 6M",
            "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
            "prompt": "\"No Transaction: No Existence; No Money: No Existence; No Value Judgments\" – support each statement with an example in view of traditional economics.",
            "key_answer_points": "<ul>\n<li><strong>1. 'No Transaction: No Existence':</strong> An activity or asset is invisible in national accounts unless an explicit market trade occurs. <em>Example:</em> Millions of hectares of wild primary forest performing watershed protection have zero GDP value because no financial invoice is written.</li>\n<li><strong>2. 'No Money: No Existence':</strong> Unpaid labor or non-monetized services are excluded from GDP. <em>Example:</em> Grandparent childcare, household care work, and indigenous subsistence fishing/farming are valued at $0 in GDP.</li>\n<li><strong>3. 'No Value Judgments':</strong> Traditional economics treats all expenditures equally, whether productive or destructive. <em>Example:</em> The 2010 Deepwater Horizon oil spill added billions of positive dollars to US GDP through cleanup contracts, boat rentals, and emergency spending.</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>The Core Critique:</strong> These three axioms explain why traditional GDP can show robust economic 'growth' even while a country's ecology and social fabric are deteriorating.</p>\n<p><em>Slide Reference: Class 16 Slide 9.</em></p>\n</div>"
        },
        {
            "id": "EQB-16-06",
            "class_id": 16,
            "class_name": "Green Accounting & Natural Capital",
            "topic": "Non-Marketed Environmental Goods and Services",
            "category": "Short Answer & Definitions",
            "exams": [
                {"paper": "End Exam 2024", "section": "Section III, Q(e)", "marks": "1M"},
                {"paper": "End Exam 2023", "section": "Section II, Q8", "marks": "2M"},
                {"paper": "End Exam 2022", "section": "Section VI, Q(e)", "marks": "1M"},
                {"paper": "End Exam 2018", "section": "Part IV, Q2", "marks": "2M"}
            ],
            "marks": "1M – 2M",
            "importance": "HIGH (⭐⭐⭐⭐)",
            "prompt": "Give two examples for non-marketed environmental (a) Goods (b) Services.",
            "key_answer_points": "<ul>\n<li><strong>(a) Non-Marketed Environmental Goods:</strong>\n<br>1. <strong>Wild Fuelwood & Forest Fodder:</strong> Gathered directly from community forests for rural household cooking.\n<br>2. <strong>Wild Medicinal Herbs & Wild Berries:</strong> Foraged for local family consumption without financial sale.</li>\n<li><strong>(b) Non-Marketed Environmental Services:</strong>\n<br>1. <strong>Natural Insect Pollination:</strong> Bees and bats pollinating agricultural crops without human cost.\n<br>2. <strong>Wetland Water Filtration & Flood Buffering:</strong> Natural marshes purifying runoff and soaking up storm surges for free.</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>Ecosystem Services:</strong> These non-marketed benefits are vital for human survival, yet traditional economic models ignore them because they lack a price tag.</p>\n<p><em>Slide Reference: Class 16 Slide 18.</em></p>\n</div>"
        },
        {
            "id": "EQB-16-07",
            "class_id": 16,
            "class_name": "Green Accounting & Natural Capital",
            "topic": "Green Tax vs Green Cess",
            "category": "Differentiate Between",
            "exams": [
                {"paper": "End Exam 2024", "section": "Section IV(c)", "marks": "2M"},
                {"paper": "End Exam 2023", "section": "Section I, Q1(b)", "marks": "1M"},
                {"paper": "End Exam 2022", "section": "Section V, Q(a)", "marks": "1M"},
                {"paper": "End Exam 2019", "section": "Section IX, Q2", "marks": "1M"}
            ],
            "marks": "1M – 2M",
            "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
            "prompt": "Differentiate between Green Tax and Green Cess. (What is Green tax?)",
            "key_answer_points": "<ul>\n<li><strong>Green Tax (Pigouvian Tax):</strong>\n<br>• <em>Definition:</em> A tax levied on environmentally harmful goods, activities, or emissions (e.g. carbon tax, tax on older polluting motor vehicles) to internalize environmental damage costs.\n<br>• <em>Revenue Destination:</em> Flows into the <strong>General Government Treasury</strong> and can be used for any public expenditure (roads, education, debt reduction).</li>\n<li><strong>Green Cess:</strong>\n<br>• <em>Definition:</em> A specialized supplementary surcharge levied on specific polluting products (e.g. Clean Energy Cess on coal in India).\n<br>• <em>Revenue Destination:</em> Legally <strong>earmarked and ring-fenced strictly for dedicated environmental funds</strong> (such as the National Clean Energy Fund) to finance renewable solar, wind, and river rejuvenation projects.</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>Economic Instruments:</strong> Green taxes discourage pollution through price signals, while green cesses directly raise dedicated funds to finance clean alternatives.</p>\n<p><em>Slide Reference: Class 16 Slide 24.</em></p>\n</div>"
        },
        {
            "id": "EQB-16-08",
            "class_id": 16,
            "class_name": "Green Accounting & Natural Capital",
            "topic": "Green Certificate",
            "category": "Short Answer & Definitions",
            "exams": [
                {"paper": "End Exam 2022", "section": "Section V, Q(d)", "marks": "1M"}
            ],
            "marks": "1M",
            "importance": "HIGH (⭐⭐⭐⭐)",
            "prompt": "What is a Green certificate?",
            "key_answer_points": "<ul>\n<li><strong>Definition:</strong> A tradable official environmental asset (also known as a <strong>Renewable Energy Certificate - REC</strong>) that certifies that 1 Megawatt-hour (MWh) of electricity has been generated and injected into the grid from certified renewable energy sources (solar, wind, small hydro).</li>\n<li><strong>Function:</strong> Allows power distribution utilities and heavy industries to meet their Renewable Purchase Obligations (RPO) by purchasing certificates without having to build their own solar farms.</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>Market Mechanisms:</strong> Green certificates separate the environmental attribute of green power from the physical electrons, allowing clean energy generators to earn extra revenue.</p>\n<p><em>Slide Reference: Class 16 Slide 25.</em></p>\n</div>"
        },
        {
            "id": "EQB-16-09",
            "class_id": 16,
            "class_name": "Green Accounting & Natural Capital",
            "topic": "Genuine Progress Indicator (GPI)",
            "category": "Short Answer & Definitions",
            "exams": [
                {"paper": "End Exam 2023", "section": "Section II, Q6", "marks": "2M"}
            ],
            "marks": "2M",
            "importance": "HIGH (⭐⭐⭐⭐)",
            "prompt": "How GPI-genuine progress indicator is created? What is its significance in green accounting?",
            "key_answer_points": "<ul>\n<li><strong>How GPI is Created:</strong> Starts with baseline personal consumption expenditure from GDP, then:\n<br>• <strong>Adds</strong> non-market social and environmental benefits (household work, parenting, volunteering, higher education benefits).\n<br>• <strong>Subtracts</strong> environmental repair and social costs (cost of water/air pollution, loss of wetlands, carbon emissions, crime costs, income inequality).\n<br>• Formula: \\(\\text{GPI} = \\text{Consumption} + \\text{Unpaid Positive Contributions} - \\text{Environmental Degradation} - \\text{Social Costs}\\).</li>\n<li><strong>Significance in Green Accounting:</strong> Proves the <em>Threshold Hypothesis</em> (Max-Neef): while GDP continues climbing upward, true genuine economic well-being peaks and then plateaus once growth creates more pollution and inequality than real progress.</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>Measuring Real Progress:</strong> Developed from the earlier Index of Sustainable Economic Welfare (ISEW), GPI provides a realistic dashboard of national health.</p>\n<p><em>Slide Reference: Class 16 Slide 22.</em></p>\n</div>"
        },
        {
            "id": "EQB-16-10",
            "class_id": 16,
            "class_name": "Green Accounting & Natural Capital",
            "topic": "Surrogate Market Valuation (Hedonic & Travel Cost)",
            "category": "Descriptive & Case Study",
            "exams": [
                {"paper": "End Exam 2019", "section": "Section VIII, Q2", "marks": "3M"},
                {"paper": "End Exam 2018", "section": "Part IV, Q5", "marks": "4M"}
            ],
            "marks": "3M – 4M",
            "importance": "HIGH (⭐⭐⭐⭐)",
            "prompt": "Explain surrogate market approach methods with examples.",
            "key_answer_points": "<ul>\n<li><strong>Concept:</strong> When an environmental asset has no direct market price, economists examine prices in related real-world commercial markets to infer people's willingness to pay (Revealed Preference).</li>\n<li><strong>Method 1: Hedonic Property Pricing:</strong>\n<br>• <em>Principle:</em> Compares sales prices of identical homes located in clean vs polluted areas.\n<br>• <em>Example:</em> A 3-bedroom house next to a quiet public lake costs $50,000 more than an identical house next to a noisy, odorous highway. That $50,000 price difference reflects the market value of clean air and quiet green space.</li>\n<li><strong>Method 2: Travel Cost Method (TCM):</strong>\n<br>• <em>Principle:</em> Uses the time and travel expenses people spend visiting a national park or beach as a proxy price for recreation value.\n<br>• <em>Example:</em> Surveying 5,000 tourists visiting Kanha Tiger Reserve (fuel, hotels, flight tickets) to construct a demand curve and calculate the total economic recreational value of protecting tigers.</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>Revealed Preferences:</strong> Surrogate valuation looks at actual money spent by households rather than hypothetical survey answers.</p>\n<p><em>Slide Reference: Class 16 Slides 19–21.</em></p>\n</div>"
        },
        {
            "id": "EQB-16-11",
            "class_id": 16,
            "class_name": "Green Accounting & Natural Capital",
            "topic": "Kyoto Protocol vs Paris Agreement",
            "category": "Differentiate Between",
            "exams": [
                {"paper": "End Exam 2023", "section": "Section II, Q5", "marks": "2M"},
                {"paper": "End Exam 2022", "section": "Section VII, Q(b)", "marks": "2M"}
            ],
            "marks": "2M",
            "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
            "prompt": "What is Kyoto Protocol? Differentiate between Kyoto protocol and Paris agreement.",
            "key_answer_points": "<ul>\n<li><strong>Kyoto Protocol (1997 / 2005):</strong> An international treaty that set legally binding greenhouse gas reduction targets (average 5.2% below 1990 levels) <strong>exclusively for developed nations (Annex-I)</strong>, while developing nations (China, India) had zero mandatory reduction targets.</li>\n<li><strong>Key Differences with Paris Agreement (2015):</strong>\n<br>• <em>Governance Structure:</em> Kyoto used a <strong>top-down</strong> legally binding mandate; Paris uses a <strong>bottom-up</strong> model of Nationally Determined Contributions (NDCs).\n<br>• <em>Participation & Scope:</em> Kyoto applied only to Annex-I developed nations; Paris includes <strong>all 195 nations</strong> (both developed and developing).\n<br>• <em>Overarching Goal:</em> Kyoto aimed at narrow percentage emission cuts; Paris aims to limit global temperature rise to <strong>well below \\(2^\\circ\\text{C}\\)</strong> (pursuing \\(1.5^\\circ\\text{C}\\)) and reach net-zero by mid-century.</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>The Geopolitical Shift:</strong> Because Kyoto exempted emerging economic powerhouses like China and India, the US withdrew. Paris corrected this by involving every country in voluntary national climate pledges.</p>\n<p><em>Slide Reference: Class 16 Slides 27–31.</em></p>\n</div>"
        },
        {
            "id": "EQB-16-12",
            "class_id": 16,
            "class_name": "Green Accounting & Natural Capital",
            "topic": "Kyoto Protocol Flexible Market Mechanisms",
            "category": "Short Answer & Definitions",
            "exams": [
                {"paper": "End Exam 2023", "section": "Section IV, Q6", "marks": "4M"},
                {"paper": "End Exam 2022", "section": "Section VII, Q(e)", "marks": "2M"},
                {"paper": "End Exam 2019", "section": "Section III, Q2", "marks": "3M"}
            ],
            "marks": "2M – 4M",
            "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
            "prompt": "Explain any 2-market based flexible mechanisms to reduce emissions under Kyoto protocol.",
            "key_answer_points": "<ul>\n<li><strong>1. International Emissions Trading (IET - Carbon Market):</strong> Annex-I developed countries that cut emissions below their targets can sell their surplus Assigned Amount Units (AAUs) to other Annex-I nations struggling to meet their targets (cap-and-trade).</li>\n<li><strong>2. Clean Development Mechanism (CDM):</strong> An Annex-I developed nation invests in clean emission-reduction projects in a non-Annex-I developing nation (e.g. building a solar park in India). The investor earns <strong>Certified Emission Reductions (CERs)</strong> to offset emissions back home while helping the developing country leapfrog to clean tech.</li>\n<li><strong>3. Joint Implementation (JI):</strong> An Annex-I country invests in an emission-reduction project in another Annex-I industrialized country (typically in Eastern Europe), earning Emission Reduction Units (ERUs).</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>Economic Efficiency:</strong> Greenhouse gases mix globally. By allowing investments where cutting a tonne of \\(\\text{CO}_2\\) is cheapest, Kyoto sought to achieve emissions reductions at the lowest global economic cost.</p>\n<p><em>Slide Reference: Class 16 Slides 28–30.</em></p>\n</div>"
        },
        {
            "id": "EQB-16-13",
            "class_id": 16,
            "class_name": "Green Accounting & Natural Capital",
            "topic": "Annex-I vs Annex-II Countries Under UNFCCC",
            "category": "Differentiate Between",
            "exams": [
                {"paper": "End Exam 2023", "section": "Section II, Q7", "marks": "2M"}
            ],
            "marks": "2M",
            "importance": "HIGH (⭐⭐⭐⭐)",
            "prompt": "Differentiate between Annex-1 and Annex-2 countries.",
            "key_answer_points": "<ul>\n<li><strong>Annex-I Countries:</strong> Industrialized OECD countries plus Economies in Transition (EIT - former Soviet bloc countries like Russia, Poland). They committed to emissions reduction targets under Kyoto.</li>\n<li><strong>Annex-II Countries:</strong> A wealthy sub-group of Annex-I comprising strictly the developed OECD nations (e.g. USA, UK, Germany, Japan) excluding former Soviet transition economies. <strong>They bear a special mandatory obligation to provide financial grants and clean technology transfer</strong> to developing countries to assist climate mitigation and adaptation.</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>Common But Differentiated Responsibilities:</strong> Annex-II nations carry the historical financial duty because their early industrial development caused the majority of historical carbon emissions.</p>\n<p><em>Slide Reference: Class 16 Slide 32.</em></p>\n</div>"
        },
        {
            "id": "EQB-16-14",
            "class_id": 16,
            "class_name": "Green Accounting & Natural Capital",
            "topic": "Economic & Climate Acronym Expansions",
            "category": "Acronyms & Expansions",
            "exams": [
                {"paper": "End Exam 2022", "section": "Section IV", "marks": "5M"},
                {"paper": "End Exam 2019", "section": "Section III, Q1", "marks": "3M"},
                {"paper": "End Exam 2018", "section": "Part IV, Q1", "marks": "4M"}
            ],
            "marks": "1M – 5M",
            "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
            "prompt": "Expand the following acronyms: CER, EDP, IPCC, IUCN, SSRRS, WTP, ISEW, MEW, CDM, UNFCCC, COP, GWP.",
            "key_answer_points": "<ul>\n<li><strong>CER:</strong> Certified Emission Reductions</li>\n<li><strong>EDP:</strong> Eco Domestic Product (or Environmentally Adjusted Domestic Product)</li>\n<li><strong>IPCC:</strong> Intergovernmental Panel on Climate Change</li>\n<li><strong>IUCN:</strong> International Union for Conservation of Nature</li>\n<li><strong>SSRRS:</strong> Soil Suction Radon Reduction System</li>\n<li><strong>WTP:</strong> Willingness To Pay</li>\n<li><strong>ISEW:</strong> Index of Sustainable Economic Welfare</li>\n<li><strong>MEW:</strong> Measure of Economic Welfare</li>\n<li><strong>CDM:</strong> Clean Development Mechanism</li>\n<li><strong>UNFCCC:</strong> United Nations Framework Convention on Climate Change</li>\n<li><strong>COP:</strong> Conference of the Parties</li>\n<li><strong>GWP:</strong> Global Warming Potential</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>High-Yield Exam Keys:</strong> Memorize these exact full forms as they appear repeatedly across multiple end-semester exams for rapid points.</p>\n<p><em>Slide Reference: Class 16 Slide 3 & Class 14 Slide 29.</em></p>\n</div>"
        },
        {
            "id": "EQB-16-15",
            "class_id": 16,
            "class_name": "Green Accounting & Natural Capital",
            "topic": "NAMEA Framework Country",
            "category": "MCQ & Objective",
            "exams": [
                {"paper": "End Exam 2022", "section": "Section II, Q10", "marks": "1M"}
            ],
            "marks": "1M",
            "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
            "prompt": "Country that has started accounting emission in nation income under the name of National Accounting Matrix Including Environmental Accounts is: [a] The Netherlands [b] Namibia [c] Indonesia [d] Norway.",
            "key_answer_points": "<ul>\n<li><strong>Correct Option:</strong> <strong>[ a ] The Netherlands</strong></li>\n<li><strong>Key Innovation:</strong> In 1991, Statistics Netherlands pioneered NAMEA, which pairs standard economic national accounting supply-and-use tables side-by-side with physical pollutant emission tables (in kg/tonnes) for each industrial sector without using artificial shadow pricing.</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>Physical Accounting:</strong> NAMEA avoids controversial monetary valuations by recording environmental pressures in physical units alongside standard GDP money flows.</p>\n<p><em>Slide Reference: Class 16 Slide 23.</em></p>\n</div>"
        },
        {
            "id": "EQB-16-16",
            "class_id": 16,
            "class_name": "Green Accounting & Natural Capital",
            "topic": "Greenhouse Gases vs 100-Year GWP",
            "category": "Match the Following",
            "exams": [
                {"paper": "End Exam 2022", "section": "Section I(C)", "marks": "5M"}
            ],
            "marks": "5M",
            "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
            "prompt": "Section-I: Match the following Gases with their Global Warming Potential (GWP) [5 Marks].",
            "key_answer_points": "<ul>\n<li><strong>Matching Solution:</strong>\n<br>1. <strong>Methane (\\(\\text{CH}_4\\))</strong> $\\rightarrow$ <strong>21</strong> (or 28 in recent IPCC reports)\n<br>2. <strong>Nitrous Oxide (\\(\\text{N}_2\\text{O}\\))</strong> $\\rightarrow$ <strong>310</strong> (or 273 in AR6)\n<br>3. <strong>Perfluorocarbons (PFCs)</strong> $\\rightarrow$ <strong>9,200</strong>\n<br>4. <strong>Hydrofluorocarbons (HFCs)</strong> $\\rightarrow$ <strong>11,700</strong>\n<br>5. <strong>Sulfur Hexafluoride (\\(\\text{SF}_6\\))</strong> $\\rightarrow$ <strong>23,900</strong></li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>Technical Rationale:</strong> Tested in 2022. \\(\\text{SF}_6\\) used in electrical switchgear has the highest warming potential of any gas known, persisting in the air for over 3,200 years.</p>\n<p><em>Slide Reference: Class 16 Slide 26 & Class 7 Slide 12.</em></p>\n</div>"
        }
    ]

def get_class17_questions():
    return [
        {
            "id": "EQB-17-01",
            "class_id": 17,
            "class_name": "Sustainable Development Goals (SDGs)",
            "topic": "Brundtland Definition of Sustainable Development",
            "category": "Short Answer & Definitions",
            "exams": [
                {"paper": "End Exam 2022", "section": "Section IX, Q(d)", "marks": "1M"},
                {"paper": "End Exam 2019", "section": "Section VIII, Q3", "marks": "1M"}
            ],
            "marks": "1M",
            "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
            "prompt": "What is Sustainable development defined by WCED (1987)?",
            "key_answer_points": "<ul>\n<li><strong>Official Definition (Our Common Future):</strong> <em>\"Sustainable development is development that meets the needs of the present without compromising the ability of future generations to meet their own needs.\"</em></li>\n<li><strong>Two Fundamental Concepts:</strong>\n<br>1. The concept of <strong>'needs'</strong>, in particular the essential needs of the world's poor, to which overriding priority should be given.\n<br>2. The idea of <strong>limitations</strong> imposed by the state of technology and social organization on the environment's ability to meet present and future needs.</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>The Universal Baseline:</strong> Established by the UN World Commission on Environment and Development (chaired by Gro Harlem Brundtland), this remains the cornerstone definition of international environmental policy.</p>\n<p><em>Slide Reference: Class 17 Slide 4.</em></p>\n</div>"
        },
        {
            "id": "EQB-17-02",
            "class_id": 17,
            "class_name": "Sustainable Development Goals (SDGs)",
            "topic": "Strong vs Weak Sustainability",
            "category": "Differentiate Between",
            "exams": [
                {"paper": "End Exam 2024", "section": "Section IV(b)", "marks": "2M"},
                {"paper": "End Exam 2023", "section": "Section II, Q15", "marks": "2M"},
                {"paper": "End Exam 2022", "section": "Section IX, Q(d)", "marks": "2M"},
                {"paper": "End Exam 2019", "section": "Section VIII, Q3", "marks": "3M"}
            ],
            "marks": "2M – 3M",
            "importance": "CRITICAL (⭐⭐⭐⭐⭐)",
            "prompt": "What is the difference between strong and weak sustainability? Under which category do you place Green Accounting, and why?",
            "key_answer_points": "<ul>\n<li><strong>Weak Sustainability (Hartwick-Solow Paradigm):</strong> Assumes that manufactured capital (machines, roads, technology) and natural capital (forests, clean air) are <strong>interchangeable and substitutable</strong>. As long as total capital stock (\\(K_m + K_n\\)) does not decline, destroying a wetland is acceptable if the land is replaced with a profitable shopping mall.</li>\n<li><strong>Strong Sustainability (Ecological Economics Paradigm):</strong> Rejects full substitution. Natural capital provides unique, non-substitutable life-support services (clean air, stable climate, ozone layer) for which no machine can substitute (Critical Natural Capital). Natural capital must be preserved independently in physical units.</li>\n<li><strong>Placement of Green Accounting:</strong> Green Accounting conforms to <strong>Weak Sustainability</strong> because it translates physical natural resources into monetary dollar values, assuming financial investments can offset depleted environmental capital.</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>Core Debate:</strong> Can technology replace nature? Weak sustainability says yes through money and innovation; strong sustainability says no because thermodynamics and ecological thresholds cannot be engineered away.</p>\n<p><em>Slide Reference: Class 17 Slides 8–11.</em></p>\n</div>"
        },
        {
            "id": "EQB-17-03",
            "class_id": 17,
            "class_name": "Sustainable Development Goals (SDGs)",
            "topic": "Sustainable Development Objectives",
            "category": "MCQ & Objective",
            "exams": [
                {"paper": "End Exam 2022", "section": "Section II, Q7", "marks": "1M"}
            ],
            "marks": "1M",
            "importance": "HIGH (⭐⭐⭐⭐)",
            "prompt": "Sustainable development will not aim at: [a] Social economic development optimizing benefits without spoiling future [b] Reasonable and equally distributed well-being [c] Meeting present needs without compromising future generations [d] Maximizing present-day benefits through increased resource consumption.",
            "key_answer_points": "<ul>\n<li><strong>Correct Option:</strong> <strong>[ d ] Maximizing the present-day benefits through increased resource consumption.</strong></li>\n<li><strong>Explanation:</strong> Maximizing short-term consumption at the expense of ecological balance is the antithesis of sustainable development.</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>Exam Question:</strong> Tested in 2022 Section II. Options (a), (b), and (c) are all foundational principles of Brundtland sustainability.</p>\n<p><em>Slide Reference: Class 17 Slide 6.</em></p>\n</div>"
        },
        {
            "id": "EQB-17-04",
            "class_id": 17,
            "class_name": "Sustainable Development Goals (SDGs)",
            "topic": "ISEW GDP Adjustment",
            "category": "MCQ & Objective",
            "exams": [
                {"paper": "End Exam 2022", "section": "Section II, Q5", "marks": "1M"}
            ],
            "marks": "1M",
            "importance": "HIGH (⭐⭐⭐⭐)",
            "prompt": "Which of the following adjustments would be made to any increase in GDP in order to derive an 'Index of Sustainable Economic Welfare'? [a] Subtract monetary value of non-defensive public expenditures [b] Subtract monetary value of personal consumption [c] Subtract monetary value of capital formation [d] Subtract the costs of environmental degradation.",
            "key_answer_points": "<ul>\n<li><strong>Correct Option:</strong> <strong>[ d ] Subtract the costs of environmental degradation.</strong></li>\n<li><strong>Explanation:</strong> The Index of Sustainable Economic Welfare (ISEW) deducts external costs of air/water pollution, resource depletion, and habitat loss from standard GDP.</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>Direct Exam Question:</strong> Appeared in End Exam 2022. ISEW corrects the flaw where GDP counts environmental destruction and subsequent cleanup as positive growth.</p>\n<p><em>Slide Reference: Class 17 Slide 14.</em></p>\n</div>"
        },
        {
            "id": "EQB-17-05",
            "class_id": 17,
            "class_name": "Sustainable Development Goals (SDGs)",
            "topic": "Cartoon Interpretation: Overconsumption & Resource Inequality",
            "category": "Descriptive & Case Study",
            "exams": [
                {"paper": "End Exam 2018", "section": "Part VI, Q1", "marks": "2M"}
            ],
            "marks": "2M",
            "importance": "MEDIUM (⭐⭐⭐)",
            "prompt": "Give a critical comment on the relationship between overconsumption and resource inequality (The Industrialist on Steamer and Island Fisherman cartoon).",
            "key_answer_points": "<ul>\n<li><strong>Visual Symbolism:</strong> A wealthy industrialist on a smoke-belching luxury ship takes the very last fish from an indigenous islander standing on a tiny eroding rock with one palm tree.</li>\n<li><strong>Ecological Inequality (IPAT Imbalance):</strong> Shows that the top 20% of the world consumes over 80% of global resources, while the vulnerable global poor bear the immediate brunt of environmental collapse and rising sea levels.</li>\n<li><strong>Environmental Justice Message:</strong> Technology-driven commercial greed treats the finite commons as a private profit machine, leaving developing communities stripped of basic food security.</li>\n</ul>",
            "detailed_answer": "<div class=\"detailed-body\">\n<p><strong>Visual Exam Analysis:</strong> Shows the stark contrast between consumption luxury and climate vulnerability, directly tying into SDG 10 (Reduced Inequalities) and SDG 12 (Responsible Consumption).</p>\n<p><em>Slide Reference: Class 17 Slide 18 & Class 3 Slide 15.</em></p>\n</div>"
        }
    ]

if __name__ == "__main__":
    print(f"Class 16: {len(get_class16_questions())} Qs | Class 17: {len(get_class17_questions())} Qs.")
